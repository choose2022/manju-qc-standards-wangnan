# 题材 6：无限流 / 规则怪谈

适用子类：无限流闯关副本、中式民俗规则怪谈、密室解谜逃脱。
红线：禁止宣扬封建迷信、真实民俗恶意贬损、过度恐怖血腥与惊吓堆砌。

**技能池**
- 强制：`sd-qc-engine`、`frame-consistency-checker`、`shot-continuity-inspector`、`subtitle-timing-checker`、`audio-sync-checker`
- 补强：`novel-worldbuilding-validator`（规则自洽与线索闭环）、`short-drama-review`（NPC 言行与悬念节奏）、`costume-consistency-checker`（随身信物）
- 校验器清理：清单内原缺失项已按 H3 可执行口径替换（对照见 SKILL.md「校验器可用性」），无需安装。

## 质检清单 V1

| 模块 | 序 | 检查项 | 合格标准 | 等级 | 强制 | 补强 |
|---|---|---|---|---|---|---|
| 脚本·规则 | 1 | 副本基础规则 | 规则条款前后自洽，不在后文推翻 | 🔴 | sd-qc-engine | novel-worldbuilding-validator |
| 脚本·规则 | 2 | 禁忌与惩罚 | 违反禁忌的后果与规则一致 | 🔴 | sd-qc-engine | novel-worldbuilding-validator |
| 脚本·规则 | 3 | 线索与解谜 | 线索能推回谜底，无天降答案 | 🔴 | sd-qc-engine | novel-worldbuilding-validator |
| 脚本·规则 | 4 | 任务面板文案 | 通关条件、失败条件、倒计时统一 | 🔴 | sd-qc-engine | 人工复核位（逐字核） |
| 脚本·规则 | 5 | NPC 行为逻辑 | 触发条件、反应、话术稳定不横跳 | 🔴 | sd-qc-engine | short-drama-review |
| 脚本·规则 | 6 | 时间线与轮回次数 | 第几轮、存活人数、剩余时间算得平 | 🔴 | sd-qc-engine | novel-worldbuilding-validator |
| 资产 | 7 | 随身信物与道具 | 手牌、钥匙、道具跨镜一致，增减须标 | 🔴 | sd-qc-engine | frame-consistency-checker |
| 资产 | 8 | 场景陈设与符号 | 房内标记、符纸、摆件位置稳定 | 🟡 | sd-qc-engine | frame-consistency-checker |
| 分镜·空间 | 9 | 密室空间结构 | 房间大小、门窗、通道关系不自相矛盾 | 🔴 | sd-qc-engine | shot-continuity-inspector |
| 分镜·空间 | 10 | 走廊与门位 | 进门出门方向和前一镜接得上 | 🔴 | sd-qc-engine | shot-continuity-inspector |
| 分镜·空间 | 11 | 视线与窥视关系 | 谁在看谁成立，躲藏位置空间正确 | 🟡 | sd-qc-engine | shot-continuity-inspector |
| 画面 | 12 | 画风与氛围统一 | 单副本色调光影一致 | 🔴 | sd-qc-engine | frame-consistency-checker |
| 画面 | 13 | 人体结构 | 无畸形崩坏，畸形怪物有设计 | 🔴 | sd-qc-engine | frame-consistency-checker |
| 音频 | 14 | 台词与异响 | 台词时序对齐，异响方向感正确 | 🔴 | sd-qc-engine | audio-sync-checker |
| 音频 | 15 | 氛围音与惊吓点 | 惊吓点与画面同拍，不靠音量硬炸 | 🟡 | sd-qc-engine | audio-sync-checker |
| 字幕 | 16 | 规则/面板/线索字幕 | 逐字与设定文档一致，编号不错乱 | 🔴 | sd-qc-engine | subtitle-timing-checker |
| 字幕 | 17 | 字幕不遮挡 | 不挡关键符号与线索特写 | 🟡 | sd-qc-engine | subtitle-timing-checker |
| 合规 | 18 | 迷信与恐怖红线 | 不宣扬迷信、不贬损真实民俗、不血腥猎奇 | 🔴 | sd-qc-engine | 人工复核位 |
| 交付 | 19 | 物料归档 | 剧本、规则文档、分镜、审计齐全 | 🟡 | sd-qc-engine | — |

## 加载文本

```text
【无限流规则怪谈质检基线V1】
1.副本基础规则：条款自洽不推翻；阻断；sd-qc-engine；novel-worldbuilding-validator
2.禁忌与惩罚：后果与规则一致；阻断；sd-qc-engine；novel-worldbuilding-validator
3.线索与解谜：可推回谜底；阻断；sd-qc-engine；novel-worldbuilding-validator
4.任务面板文案：条件倒计时统一；阻断；sd-qc-engine；人工复核位
5.NPC行为逻辑：触发与话术稳定；阻断；sd-qc-engine；short-drama-review
6.时间线与轮回次数：轮次人数时间算得平；阻断；sd-qc-engine；novel-worldbuilding-validator
7.随身信物道具：跨镜一致增减须标；阻断；sd-qc-engine；frame-consistency-checker
8.场景陈设符号：位置稳定；一般；sd-qc-engine；frame-consistency-checker
9.密室空间结构：房间门窗通道自洽；阻断；sd-qc-engine；shot-continuity-inspector
10.走廊与门位：进出方向接得上；阻断；sd-qc-engine；shot-continuity-inspector
11.视线与窥视关系：看与被看成立；一般；sd-qc-engine；shot-continuity-inspector
12.画风氛围统一：单副本一致；阻断；sd-qc-engine；frame-consistency-checker
13.人体结构：无畸形崩坏；阻断；sd-qc-engine；frame-consistency-checker
14.台词与异响：时序对齐方向感正确；阻断；sd-qc-engine；audio-sync-checker
15.氛围音与惊吓点：同拍不硬炸；一般；sd-qc-engine；audio-sync-checker
16.规则面板字幕：逐字一致编号不错；阻断；sd-qc-engine；subtitle-timing-checker
17.字幕不遮挡：不挡符号线索；一般；sd-qc-engine；subtitle-timing-checker
18.迷信恐怖红线：不宣扬迷信不血腥；阻断；sd-qc-engine；人工复核位
19.物料归档：四件齐全；一般；sd-qc-engine；无
```

## 口令

- **初始化**：`sd-qc-engine，加载《无限流规则怪谈质检清单V1》+绑定表，冻结为基线；规则与线索条款以项目设定文档为唯一口径；解绑其他题材。`
- **单集终审**：`sd-qc-engine，加载无限流基线，逐段逐句逐镜过 19 条；规则/线索/时间线走 novel-worldbuilding-validator；密室空间走 shot-continuity-inspector；出报告+审计栏。`
- **规则前置**：`sd-qc-engine，仅跑脚本·规则 6 条，调 novel-worldbuilding-validator、short-drama-review；面板文案列逐字人工复核。`
- **单点抽检**：`shot-continuity-inspector，单点抽检本副本密室动线，仅内部参考。`
