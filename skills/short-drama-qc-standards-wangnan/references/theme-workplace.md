# 题材 4：现实职场（含 4 子类）

适用子类：精英商战、基层写实、医疗职场、律政法庭。
红线：不得出现错误的急救/法律程序/财务常识；不得污名化职业群体。

**技能池**
- 强制：`sd-qc-engine`、`frame-consistency-checker`、`costume-consistency-checker`（工装制服）、`shot-continuity-inspector`、`subtitle-timing-checker`、`audio-sync-checker`
- 补强：`short-drama-review`（职场话术、层级关系）、`novel-worldbuilding-validator`（案件/项目因果）
- 校验器清理：清单内原缺失项已按 H3 可执行口径替换（对照见 SKILL.md「校验器可用性」），无需安装。

## 质检清单 V1（基底 18 条）

| 模块 | 序 | 检查项 | 合格标准 | 等级 | 强制 | 补强 |
|---|---|---|---|---|---|---|
| 脚本 | 1 | 职级与权限 | 汇报线、审批权限、跨部门关系成立 | 🔴 | sd-qc-engine | short-drama-review |
| 脚本 | 2 | 专业流程 | 手术/庭审/尽调/审计的步骤不失真 | 🔴 | sd-qc-engine | 人工复核位 |
| 脚本 | 3 | 专业文本 | 病历、合同、报表、判决书字段与用语正确 | 🔴 | sd-qc-engine | 人工复核位 |
| 脚本 | 4 | 术语与话术 | 行业黑话使用场景正确，不悬浮 | 🔴 | sd-qc-engine | short-drama-review |
| 脚本 | 5 | 项目/案件因果 | 冲突源头与解决路径成立 | 🟡 | sd-qc-engine | novel-worldbuilding-validator |
| 资产 | 6 | 工装与制服 | 白大褂、律师袍、正装同场次一致，牌徽位置固定 | 🔴 | sd-qc-engine | costume-consistency-checker |
| 资产 | 7 | 证件与工牌 | 姓名、头像、职位跨镜一致 | 🟡 | sd-qc-engine | frame-consistency-checker |
| 资产 | 8 | 办公/诊疗道具 | 器械、文件、屏幕内容与场景匹配 | 🟡 | sd-qc-engine | frame-consistency-checker |
| 分镜 | 9 | 办公室/诊室空间 | 房间布局、座位关系前后一致 | 🟡 | sd-qc-engine | shot-continuity-inspector |
| 分镜 | 10 | 多人桌面戏 | 站位与视线不乱，文件传递方向可读 | 🟡 | sd-qc-engine | shot-continuity-inspector |
| 分镜 | 11 | 手部操作 | 打字、签字、手术、翻阅动作成立 | 🔴 | sd-qc-engine | frame-consistency-checker |
| 画面 | 12 | 画风统一 | 全程写实质感 | 🔴 | sd-qc-engine | frame-consistency-checker |
| 画面 | 13 | 人体结构 | 无畸形、穿模、多指 | 🔴 | sd-qc-engine | frame-consistency-checker |
| 音频 | 14 | 台词与语速 | 专业长句语速自然，不同步失帧 | 🔴 | sd-qc-engine | audio-sync-checker |
| 音频 | 15 | 环境音 | 键盘、走廊、器械音效匹配场景 | 🟡 | sd-qc-engine | audio-sync-checker |
| 字幕 | 16 | 专业名词字幕 | 术语、数值、日期、金额逐字正确 | 🔴 | sd-qc-engine | subtitle-timing-checker |
| 字幕 | 17 | 字幕不遮挡 | 不挡关键文本与器械操作 | 🟡 | sd-qc-engine | subtitle-timing-checker |
| 合规 | 18 | 职业形象导向 | 不污名化职业群体，不教违规操作 | 🔴 | sd-qc-engine | 人工复核位 |

## 加载文本

```text
【现实职场质检基线V1】
1.职级权限：汇报审批关系成立；阻断；sd-qc-engine；short-drama-review
2.专业流程：手术庭审尽调步骤不失真；阻断；sd-qc-engine；人工复核位
3.专业文本：病历合同报表字段用语正确；阻断；sd-qc-engine；人工复核位
4.术语话术：黑话场景正确；阻断；sd-qc-engine；short-drama-review
5.项目案件因果：源头与解决路径成立；一般；sd-qc-engine；novel-worldbuilding-validator
6.工装制服：同场次一致牌徽固定；阻断；sd-qc-engine；costume-consistency-checker
7.证件工牌：姓名头像职位一致；一般；sd-qc-engine；frame-consistency-checker
8.办公诊疗道具：与场景匹配；一般；sd-qc-engine；frame-consistency-checker
9.空间布局：房间座位一致；一般；sd-qc-engine；shot-continuity-inspector
10.多人桌面戏：站位视线文件方向可读；一般；sd-qc-engine；shot-continuity-inspector
11.手部操作：打字签字手术动作成立；阻断；sd-qc-engine；frame-consistency-checker
12.画风统一：写实质感；阻断；sd-qc-engine；frame-consistency-checker
13.人体结构：无畸形穿模多指；阻断；sd-qc-engine；frame-consistency-checker
14.台词语速：长句自然不失帧；阻断；sd-qc-engine；audio-sync-checker
15.环境音：键盘走廊器械匹配；一般；sd-qc-engine；audio-sync-checker
16.专业名词字幕：逐字正确；阻断；sd-qc-engine；subtitle-timing-checker
17.字幕不遮挡：不挡关键文本器械；一般；sd-qc-engine；subtitle-timing-checker
18.职业形象导向：不污名不教违规；阻断；sd-qc-engine；人工复核位
```

## 口令

- **初始化**：`sd-qc-engine，加载《现实职场质检清单V1》+绑定表，注明子类，冻结为基线；前置盘点只确认清单内校验器可执行，缺失项已替换为人工复核位。`
- **单集终审**：`sd-qc-engine，加载职场基线，逐段逐句逐镜过 18 条；专业流程与文本两条标【人工复核·未自动校验】+人工复核签字；出报告+审计栏。`
- **剧本前置**：`sd-qc-engine，仅跑脚本 5 条，调 short-drama-review、novel-worldbuilding-validator；专业条列人工复核。`
- **单点抽检**：`costume-consistency-checker，单点抽检工装制服与牌徽，仅内部参考。`
