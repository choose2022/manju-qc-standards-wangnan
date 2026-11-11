# 漫剧全题材质检标准合集（wangnan 版）

一套可直接照做的漫剧 / 短剧质检标尺：**第 0 套全链路通用基线（10 阶段）** + **14 套题材专项清单**，每套自带「检查项 + 合格标准 + 缺陷等级 + 强制/补强校验器 + 加载文本 + 口令」。既可作为 Agent Skill 直接调用，也可整份复制给协作方当验收标准。

作者：wangnan

---

## 目录结构

```
.
├── README.md
├── skills/
│   └── short-drama-qc-standards-wangnan/     ← Agent Skill（拷进 .user_skills 即可用）
│       ├── SKILL.md                          调用入口：题材必选 + 流程 + 判定口径
│       ├── references/
│       │   ├── pipeline-10stage.md            第 0 套·常驻层（55 条 + 5 张专项复检表）
│       │   ├── theme-*.md                     14 套题材专项清单
│       │   ├── stage-gate-map.md              附录 A·10 阶段卡点流转表
│       │   ├── report-template.md             附录 D·报告结构
│       │   ├── automation.md                  附录 E·脚本与状态台账
│       │   └── model-compat-matrix.md         附录 F·模型分轨矩阵（8 条失效条款）
│       └── scripts/
│           ├── qc_state.py                    项目状态 / 风险台账（题材必选）
│           ├── build_report.py                出报告骨架（八节 + 审计栏 + 待办四表）
│           └── qc_lint.py                     四道自检（skill / checklists / validators / report）
└── docs/
    ├── 漫剧全题材质检标准合集V1.md            表格版合集，可直接复制给人
    ├── 漫剧全题材质检标准合集V1-手机版.md     手机阅读版（表格已拆成单条）
    └── 漫剧全题材质检标准合集V1-H5.html       单文件 H5，打开先选题材才能看
```

---

## 硬约束：先选题材，不选不许用

第 0 套是常驻层，会随任一题材自动叠加；一次只锁一套专项题材。

| 编号 | 题材 | 编号 | 题材 |
|---|---|---|---|
| 0 | 全链路通用（常驻） | 8 | 年代重生 |
| 1 | 修仙玄幻 | 9 | 悬疑刑侦谍战 |
| 2 | 写实军事 | 10 | 科幻未来 |
| 3 | 现实情感 | 11 | 校园青春 |
| 4 | 现实职场 | 12 | 沙雕反套路脑洞 |
| 5 | 末世废土 | 13 | 游戏穿越系统流 |
| 6 | 无限流规则怪谈 | 14 | 国风神话志怪 |
| 7 | 古装古风 | — | — |

- 不许用「上次用过的那套」顶替，不许按稿件内容反推，不许默认常驻单跑。
- 脚本层同样强制：`qc_state.py init` 不给 `--genre` 直接退出码 2 并回显这 15 项。

---

## 给 Agent 用（装 Skill）

把 `skills/short-drama-qc-standards-wangnan/` 整个目录放进 Agent 的用户技能目录，通常是：

```
<workspace>/.user_skills/short-drama-qc-standards-wangnan/
```

- `SKILL.md` 的 frontmatter `name` 必须与目录名一致，改名会导致触发不到。
- `references/` 里的相对路径不能拆散，`scripts/` 只用 Python 标准库，无需装依赖。

装好后先跑一次自检：

```bash
python scripts/qc_lint.py skill      --skill <skill目录>
python scripts/qc_lint.py checklists --dir  <skill目录>/references
python scripts/qc_lint.py validators --skill <skill目录> --roots <.skills> --roots <.user_skills>
```

`--roots` 每次只放一个目录，多个就重复写多次（写成 `"a;b"` 会被当成一个不存在的路径）。

---

## 给人用（没有 Agent）

- **要能复制**：用 `docs/漫剧全题材质检标准合集V1.md`。
- **手机上翻**：用手机版 md，或用 `docs/漫剧全题材质检标准合集V1-H5.html`（支持搜索、按等级筛选，打开先选题材）。
- 对方开工第一句：把 15 项列给他单选，选完再加载「第 0 套 + 所选题材」。

---

## 跑一份质检（最小流程）

```bash
# 0) 把 15 项给使用人单选；没选就停在这里
python scripts/qc_state.py --project <项目目录> genres

# 1) 建状态（缺 --genre 会退出码 2）
python scripts/qc_state.py --project <项目目录> init --genre 古装古风 --episode 3 --model h3

# 2) 出报告骨架（八节 + 签字列 + 待办四表）
python scripts/build_report.py --project <项目目录> --episode 3

# 3) 逐条填结论：一段一段、一句一句、一镜一镜，不许整批盲跑

# 4) 报告自检；不通过不得交付、不得放行
python scripts/qc_lint.py report --file <报告.md>
```

风险台账 `todo-add / todo-done / todo-list` 见 `references/automation.md`。

---

## 校验器口径（重要）

- 清单的「强制 / 补强校验器」列只保留**本机可执行、目标模型可调用**的名字；原先把不存在的校验器换成可执行项或**人工复核位**。
- 换机器只以实测为准：`qc_lint.py validators`。真缺时：提示安装 → 该条标 `【人工复核·未自动校验】` → 结论只能写「未完成」，**不许写「通过」**。
- 缺技能只提示安装，不追查安装来源、不给安装路径、不因缺技能停掉整份报告。

## 等级与报告口径

- 🔴 阻断：不修不能流转；🟡 一般：交付前应修；🟢 优化：不阻断。
- 等级由清单定，校验器只报现象、不判级。
- 待办四表只要有一行不是「无」，结论只能是**不可放行**。

## 换模型

先锁模型 → 只换投喂层与执行层、校验层全保留 → 逐条查 `references/model-compat-matrix.md` 的 8 条跨模型失效条款：

H3 六段式台词块｜H3 段长 4–15 秒硬区间｜15 秒分段硬脚本｜`[SFX:]` 音效标记开关｜H3 声音分层禁台词｜H3 不出画面内字幕条｜字数与图数平台上限｜素材形态 M0/M1/M2

---

## 许可

本仓库**原创部分**（README、`docs/` 三份成品、`skills/short-drama-qc-standards-wangnan/` 全部内容）
按 **CC BY-NC-SA 4.0** 授权：署名（wangnan + 本仓库链接）、非商业使用、相同方式共享。全文见 [LICENSE](LICENSE)。

商业授权请与作者联系。

## 第三方内容

本仓库**不包含**任何第三方 skill 的正文副本。清单与矩阵中出现的 `sd-qc-engine`、`sd-feed-engine`、
`short-drama-director` 等名称属于「调用关系声明」；`references/model-compat-matrix.md` 第三节的
8 条跨模型失效条款是对这些 skill 原文的**压缩转述 + 出处标注**（章节号 / 文件名 / 行号）。

版权归各自作者（套装部分为 **漫剧老李AIGC · V7.4.26**），本仓库不对其再授权。逐条归属见
[THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md)。

如果你是其中某个 skill 的作者且认为引用方式不妥，开 Issue 即可，我会调整或移除。
