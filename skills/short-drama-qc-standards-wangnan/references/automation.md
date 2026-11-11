# 自动化与状态（脚本层）

三个脚本都是标准库实现，Windows / macOS / Linux 通用。它们负责**确定性部分**（状态、台账、结构自检），判断与写结论仍由 `sd-qc-engine` 做。

## 状态文件 `<项目目录>/.qc-state.json`

字段：`genre`（当前题材）、`genre_history`（最近 5 个，倒序）、`stage`（当前卡点阶段）、`episode`、`todos`（风险台账）、`updated`。

**题材必选规则**（不选不许用）：
1. 每次质检开始，先把 15 项（0 全链路通用（常驻）＋ 1～14 套专项）整表给使用人，由使用人**单选一项**；
2. 用户没选 → **不许用上次那套顶替、不许按稿子反推、不许默认常驻单跑**；`init` 缺 `--genre` 直接报错退出（退出码 2），只回显选项表；
3. `--genre` 传的名字必须是 15 项里的原样名字，传别的名字同样报错退出；
4. 换题材必须显式 `set-genre` 重选，并在报告首页写明切换原因。

切题材只换 `genre`，`stage`、台账不动（台账是项目级的，跨题材仍要销项）。

## qc_state.py —— 状态与台账

```bash
python scripts/qc_state.py --project <项目目录> genres            # 打印 15 项选项表
python scripts/qc_state.py --project <项目目录> init --genre 古装古风 --episode 3 --model h3
python scripts/qc_state.py --project <项目目录> set-genre 末世废土
python scripts/qc_state.py --project <项目目录> get
python scripts/qc_state.py --project <项目目录> resolve-genre      # 本项目已选则回显；未选则 genre_required 并列 15 项
python scripts/qc_state.py --project <项目目录> stage 3
python scripts/qc_state.py --project <项目目录> todo-add --item "第9条 队形" --level 阻断 --stage 3
python scripts/qc_state.py --project <项目目录> todo-done --id 1 --sign wangnan
python scripts/qc_state.py --project <项目目录> todo-list
```

`--model` 取 `h3 / 2.5 / 2.0 / seedream / other`，锁进状态文件；后续分支（段式、段长、机检码）按它走，不按各自默认。

- `todo-add` 的 `--level` 只接受 `阻断 / 一般 / 优化`，与清单等级一一对应。
- `todo-done` 必须带签字，不留空签字；销项后 `status=done`。
- 台账是终审的唯一放行依据：`status=open` 且 `level=阻断` 的条目不为 0，阶段 9 不许放行。

## build_report.py —— 生成报告骨架

```bash
python scripts/build_report.py --project <项目目录> --episode 3
python scripts/build_report.py --project <项目目录> --episode 3 --genre 末世废土 --mode 单点抽检
```

- 不带 `--genre` 时**直接报错退出，不生成文件**；会自动带出 `init` 时锁定的题材，且该题材必须属于 15 项之一。
- 骨架已内置：前置盘点、逐条明细（含签字列）、逐段小结、缺陷汇总、审计栏、缺口与人工复核位、待办四表（②表自动填入未销项台账）。
- 生成后由 agent 逐条填结论，不许删节。

## qc_lint.py —— 三道自检

```bash
python scripts/qc_lint.py skill --skill <skill目录>
python scripts/qc_lint.py checklists --dir <skill目录>/references
python scripts/qc_lint.py validators --skill <skill目录> --roots "<skills根1>" --roots "<skills根2>"
python scripts/qc_lint.py report --file <报告.md>
python scripts/qc_lint.py models --file <投喂稿.md> --model h3|2.5|2.0
```

| 检查 | 拦什么 | 不通过怎么办 |
|---|---|---|
| `skill` | frontmatter 缺字段/多字段、name 与目录名不一致、引用不存在的 references 文件、SKILL.md 超 500 行 | 修 skill 结构 |
| `checklists` | 某套题材缺清单表/加载文本/口令、缺技能池、清单行缺等级 | 补该题材文件 |
| `validators` | 清单里引用的校验器本机不存在 → 输出 `需安装: xxx` | 先按实测核对；缺失时提示安装并标 `【人工复核·未自动校验】` |
| `models` | 稿式与声明模型错配（H3 六段式混进 Seedance 稿、2.0 用了 `[SFX:]`） | 按 `model-compat-matrix.md` 失效表换适配器重写 |
| `report` | 报告缺审计栏、缺待办四表任一张、缺「未完成」口径、签字不足 | 补件后重出不通过的报告 |

**硬规则**：`qc_lint.py report` 不通过的报告，不得交付、不得作为放行依据。`validators` 报出的清单内校验器均为本机可执行项。

## 一次完整调用的顺序

```bash
# 0) 先让使用人选题材（15 项单选）；没选就停在这里，脚本也会拦
python scripts/qc_state.py --project . genres
# 1) 建状态（首次；缺 --genre 会退出码 2 并回显选项表）
python scripts/qc_state.py --project . init --genre 古装古风 --episode 3
# 2) 出报告骨架
python scripts/build_report.py --project . --episode 3
# 3) agent 逐条填结论（引用清单条款，逐段逐句逐镜检查）
# 4) 自检
python scripts/qc_lint.py report --file 质检报告_第3集.md
# 5) 有阻断/台账未销项 → 不可放行；改完重填再自检
```
