# 题材 13：游戏穿越 / 系统流

适用子类：网游电竞、游戏世界穿越、系统任务流、乙女攻略、生存副本游戏。
红线：不得出现真实游戏抄袭式复刻；数值不能随时改；不宣扬沉迷与代练代打。

**技能池**
- 强制：`sd-qc-engine`、`frame-consistency-checker`、`subtitle-timing-checker`、`shot-continuity-inspector`、`audio-sync-checker`
- 补强：`novel-worldbuilding-validator`（数值/规则/任务因果）、`short-drama-review`（玩家行为与 NPC 反应）、`costume-consistency-checker`（装备外观）
- 校验器清理：清单内原缺失项已按 H3 可执行口径替换（对照见 SKILL.md「校验器可用性」），无需安装。

## 质检清单 V1

| 模块 | 序 | 检查项 | 合格标准 | 等级 | 强制 | 补强 |
|---|---|---|---|---|---|---|
| 脚本·规则 | 1 | 数值与面板 | 等级、血量、经验、金币在同集内增减可算平 | 🔴 | sd-qc-engine | novel-worldbuilding-validator |
| 脚本·规则 | 2 | 技能描述 | 技能效果、冷却、消耗与表现一致 | 🔴 | sd-qc-engine | novel-worldbuilding-validator |
| 脚本·规则 | 3 | 装备属性 | 装备加成与战果对得上，不无理由开挂 | 🔴 | sd-qc-engine | novel-worldbuilding-validator |
| 脚本·规则 | 4 | 任务条件 | 接取、完成、奖励条件写死且自洽 | 🟡 | sd-qc-engine | novel-worldbuilding-validator |
| 脚本·规则 | 5 | NPC 反应逻辑 | NPC 依规则响应，不随机示好或暴走 | 🔴 | sd-qc-engine | short-drama-review |
| 资产 | 6 | 装备与武器外观 | 换装后外观稳定，品阶视觉可区分 | 🔴 | sd-qc-engine | costume-consistency-checker |
| 资产 | 7 | 面板 UI | 同系统面板版式、字体、配色统一 | 🔴 | sd-qc-engine | frame-consistency-checker |
| 分镜 | 8 | 战斗与操作 | 操作有输入反馈，不凭结果倒推画面 | 🟡 | sd-qc-engine | shot-continuity-inspector |
| 分镜 | 9 | 场景空间 | 副本地图与镜头方位能对上 | 🟡 | sd-qc-engine | shot-continuity-inspector |
| 画面 | 10 | 画风统一 | 游戏世界与实景切换规则清楚，不混跳 | 🔴 | sd-qc-engine | frame-consistency-checker |
| 画面 | 11 | 人体结构 | 无畸形、穿模 | 🔴 | sd-qc-engine | frame-consistency-checker |
| 音频 | 12 | 台词与提示音 | 系统提示音与画面同拍，不抢台词 | 🔴 | sd-qc-engine | audio-sync-checker |
| 音频 | 13 | 环境与战斗音 | 匹配场景，响度分层清楚 | 🟡 | sd-qc-engine | audio-sync-checker |
| 字幕 | 14 | 面板与系统字幕 | 数值、技能名、任务名逐字正确 | 🔴 | sd-qc-engine | subtitle-timing-checker |
| 字幕 | 15 | 字幕不遮挡 | 不挡面板数值与技能图标 | 🟡 | sd-qc-engine | subtitle-timing-checker |
| 合规 | 16 | 内容与导向 | 不复刻真实游戏素材，不宣扬沉迷 | 🔴 | sd-qc-engine | 人工复核位 |
| 交付 | 17 | 物料归档 | 剧本、数值表、面板规范、审计齐全 | 🟡 | sd-qc-engine | — |

## 加载文本

```text
【游戏穿越系统流质检基线V1】
1.数值与面板：增减可算平；阻断；sd-qc-engine；novel-worldbuilding-validator
2.技能描述：效果冷却消耗与表现一致；阻断；sd-qc-engine；novel-worldbuilding-validator
3.装备属性：加成与战果对得上；阻断；sd-qc-engine；novel-worldbuilding-validator
4.任务条件：接取完成奖励自洽；一般；sd-qc-engine；novel-worldbuilding-validator
5.NPC反应逻辑：依规则响应；阻断；sd-qc-engine；short-drama-review
6.装备武器外观：稳定且品阶可辨；阻断；sd-qc-engine；costume-consistency-checker
7.面板UI：版式字体配色统一；阻断；sd-qc-engine；frame-consistency-checker
8.战斗与操作：有输入反馈；一般；sd-qc-engine；shot-continuity-inspector
9.场景空间：地图与方位对上；一般；sd-qc-engine；shot-continuity-inspector
10.画风统一：世界切换规则清楚；阻断；sd-qc-engine；frame-consistency-checker
11.人体结构：无畸形穿模；阻断；sd-qc-engine；frame-consistency-checker
12.台词与提示音：同拍不抢台词；阻断；sd-qc-engine；audio-sync-checker
13.环境与战斗音：分层清楚；一般；sd-qc-engine；audio-sync-checker
14.面板系统字幕：数值技能任务名正确；阻断；sd-qc-engine；subtitle-timing-checker
15.字幕不遮挡：不挡数值图标；一般；sd-qc-engine；subtitle-timing-checker
16.内容与导向：不复刻素材不宣扬沉迷；阻断；sd-qc-engine；人工复核位
17.物料归档：四件齐全；一般；sd-qc-engine；无
```

## 口令

- **初始化**：`sd-qc-engine，加载《游戏穿越系统流质检清单V1》+绑定表，锁定本作数值表与面板规范，冻结为基线。`
- **单集终审**：`sd-qc-engine，加载游戏基线，逐段逐句逐镜过 17 条；数值与技能走 novel-worldbuilding-validator 对表；面板 UI 走 frame-consistency-checker；出报告+审计栏。`
- **数值前置**：`sd-qc-engine，仅跑脚本·规则 5 条，逐条对数值表核算。`
- **单点抽检**：`subtitle-timing-checker，单点抽检面板与数值字幕，仅内部参考。`
