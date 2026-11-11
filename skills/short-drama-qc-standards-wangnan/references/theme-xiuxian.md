# 题材 1：修仙玄幻

适用子类：传统修仙（炼气→筑基→金丹→元婴→化神）、穿越逆袭、洪荒神话向、宗门权谋。
红线：战力表现不能与境界设定矛盾；不得出现设定外的功法与法宝。

**技能池**
- 强制：`sd-qc-engine`、`frame-consistency-checker`、`costume-consistency-checker`、`shot-continuity-inspector`、`subtitle-timing-checker`、`audio-sync-checker`
- 补强：`novel-cultivation-logic-checker`（境界功法法宝门派）、`fx-logic-checker`（斗法特效）、`sd-combat-engine`（打斗动作口径）、`giant-scale-scene`（巨物尺度）、`short-drama-review`（人设台词）
- 校验器清理：清单内原缺失项已按 H3 可执行口径替换（对照见 SKILL.md「校验器可用性」），无需安装。

## 质检清单 V1

| 模块 | 序 | 检查项 | 合格标准 | 等级 | 强制 | 补强 |
|---|---|---|---|---|---|---|
| 脚本·设定 | 1 | 境界层级 | 出场人物境界与战力匹配，不跳级、不越级压制 | 🔴 | sd-qc-engine | novel-cultivation-logic-checker |
| 脚本·设定 | 2 | 功法招式归属 | 招式归属本门功法，不出现未学过的招 | 🔴 | sd-qc-engine | novel-cultivation-logic-checker |
| 脚本·设定 | 3 | 法宝形制与用法 | 法宝外观、能力、使用条件前后一致 | 🔴 | sd-qc-engine | novel-cultivation-logic-checker |
| 脚本·设定 | 4 | 门派关系与称谓 | 掌门/长老/弟子称谓与门派关系不乱 | 🔴 | sd-qc-engine | novel-cultivation-logic-checker |
| 脚本·设定 | 5 | 剧情因果与时间线 | 修行时间、闭关时长、事件先后自洽 | 🔴 | sd-qc-engine | novel-worldbuilding-validator |
| 脚本·设定 | 6 | 台词人设 | 角色口吻符合修为与身份，不 OOC | 🔴 | sd-qc-engine | short-drama-review |
| 资产 | 7 | 道袍/常服一致性 | 同场次服装款式颜色不漂移 | 🔴 | sd-qc-engine | costume-consistency-checker |
| 资产 | 8 | 法器持拿位置 | 同一法器握持位置、佩戴位置不跳 | 🔴 | sd-qc-engine | costume-consistency-checker |
| 资产 | 9 | 面部与人体 | 不换脸、不崩坏、手指数正常 | 🔴 | sd-qc-engine | frame-consistency-checker |
| 分镜·打斗 | 10 | 斗法招式可读 | 招→挡→反的顺序看得懂，不糊成一团 | 🔴 | sd-qc-engine | sd-combat-engine、fx-logic-checker |
| 分镜·打斗 | 11 | 特效来源 | 剑气/法阵从武器或手印长出，不是凭空贴图 | 🔴 | sd-qc-engine | fx-logic-checker |
| 分镜·打斗 | 12 | 抽掉特效是否成立 | 去掉光效后动作仍能看懂 | 🟡 | sd-qc-engine | fx-logic-checker |
| 分镜·打斗 | 13 | 命中瞬间 | 中招有受力反馈，不是穿过对手 | 🔴 | sd-qc-engine | fx-logic-checker |
| 分镜·空间 | 14 | 机位与轴线 | 正反打轴线不断，视线对得上 | 🟡 | sd-qc-engine | shot-continuity-inspector |
| 分镜·空间 | 15 | 巨物尺度 | 仙山/法相/天劫有人物参照，不像小土坡 | 🟡 | sd-qc-engine | giant-scale-scene |
| 画面 | 16 | 画风统一 | 全片同一写实漫剧质感，不跳风格 | 🔴 | sd-qc-engine | frame-consistency-checker |
| 画面 | 17 | 光照色调 | 同场景光照方向与色温稳定 | 🟡 | sd-qc-engine | frame-consistency-checker |
| 音频 | 18 | 台词音画对齐 | 语音与口型、动作时序匹配 | 🔴 | sd-qc-engine | audio-sync-checker |
| 音频 | 19 | 响度与音效 | 斗法音效与招式同拍，不爆音不静音 | 🟡 | sd-qc-engine | audio-sync-checker |
| 字幕 | 20 | 台词字幕 | 与定稿剧本逐字一致，境界称号写法正确 | 🔴 | sd-qc-engine | subtitle-timing-checker |
| 字幕 | 21 | 字幕不遮挡 | 不挡法印手型、法宝关键处 | 🟡 | sd-qc-engine | subtitle-timing-checker |
| 合规 | 22 | 内容合规 | 无过度血腥、无迷信引导、无违规导向 | 🔴 | sd-qc-engine | 人工复核位 |
| 交付 | 23 | 物料归档 | 剧本、分镜、设定卡、报告、审计日志齐全 | 🟡 | sd-qc-engine | — |

## 加载文本

```text
【修仙玄幻质检基线V1】
1.境界层级：战力与境界匹配，不跳级；阻断；强制 sd-qc-engine；补强 novel-cultivation-logic-checker
2.功法招式归属：招式归属本门功法；阻断；强制 sd-qc-engine；补强 novel-cultivation-logic-checker
3.法宝形制用法：外观能力使用条件一致；阻断；强制 sd-qc-engine；补强 novel-cultivation-logic-checker
4.门派称谓关系：称谓与门第不乱；阻断；强制 sd-qc-engine；补强 novel-cultivation-logic-checker
5.剧情因果时间线：修行时长与事件顺序自洽；阻断；强制 sd-qc-engine；补强 novel-worldbuilding-validator
6.台词人设：口吻符合修为身份不OOC；阻断；强制 sd-qc-engine；补强 short-drama-review
7.道袍常服一致性：同场次服装不漂移；阻断；强制 sd-qc-engine；补强 costume-consistency-checker
8.法器持拿位置：握持佩戴位置不跳；阻断；强制 sd-qc-engine；补强 costume-consistency-checker
9.面部与人体：不换脸不崩坏；阻断；强制 sd-qc-engine；补强 frame-consistency-checker
10.斗法招式可读：招挡反顺序清楚；阻断；强制 sd-qc-engine；补强 sd-combat-engine、fx-logic-checker
11.特效来源：从武器或手印长出；阻断；强制 sd-qc-engine；补强 fx-logic-checker
12.抽掉特效仍成立：纯动作可读；一般；强制 sd-qc-engine；补强 fx-logic-checker
13.命中瞬间：有受力反馈；阻断；强制 sd-qc-engine；补强 fx-logic-checker
14.机位轴线：轴线不断视线对得上；一般；强制 sd-qc-engine；补强 shot-continuity-inspector
15.巨物尺度：有人物参照；一般；强制 sd-qc-engine；补强 giant-scale-scene
16.画风统一：全片同质感；阻断；强制 sd-qc-engine；补强 frame-consistency-checker
17.光照色调：同场景稳定；一般；强制 sd-qc-engine；补强 frame-consistency-checker
18.台词音画对齐：时序匹配；阻断；强制 sd-qc-engine；补强 audio-sync-checker
19.响度音效：同拍不爆音；一般；强制 sd-qc-engine；补强 audio-sync-checker
20.台词字幕：逐字一致；阻断；强制 sd-qc-engine；补强 subtitle-timing-checker
21.字幕不遮挡：不挡法印手型；一般；强制 sd-qc-engine；补强 subtitle-timing-checker
22.内容合规：无血腥迷信违规；阻断；强制 sd-qc-engine；补强 人工复核位
23.物料归档：五件齐全；一般；强制 sd-qc-engine；补强 无
```

## 口令

- **初始化**：`sd-qc-engine，加载《修仙玄幻质检清单V1》+绑定表，冻结为项目基线；开启前置盘点与后置审计；强制校验器不就绪即终止告警；解绑其他题材校验器。`
- **单集终审**：`sd-qc-engine，加载修仙基线，逐段逐句逐镜过 23 条，斗法段先调 sd-combat-engine 对动作口径、再调 fx-logic-checker；巨物镜头调 giant-scale-scene；出报告+审计栏，阻断项不可验收。`
- **脚本前置**：`sd-qc-engine，仅跑脚本·设定 6 条，调 novel-cultivation-logic-checker、novel-worldbuilding-validator、short-drama-review；出脚本专项报告+审计。`
- **单点抽检**：`fx-logic-checker，单点抽检本集斗法特效，仅内部参考。`
