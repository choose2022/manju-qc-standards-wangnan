# 题材 7：古装古风

适用子类：古言甜宠虐恋、宅斗嫡庶、权谋朝堂、江湖武侠。
红线：不魔改重大史实、不丑化正面历史人物、避免跨朝代大乱炖。

**技能池**
- 强制：`sd-qc-engine`、`frame-consistency-checker`、`costume-consistency-checker`、`shot-continuity-inspector`、`subtitle-timing-checker`、`audio-sync-checker`
- 补强：`fx-logic-checker`（剑气、内功、轻功光晕）、`short-drama-review`（称谓礼仪与权谋逻辑）
- 校验器清理：清单内原缺失项已按 H3 可执行口径替换（对照见 SKILL.md「校验器可用性」），无需安装。

## 质检清单 V1

| 模块 | 序 | 检查项 | 合格标准 | 等级 | 强制 | 补强 |
|---|---|---|---|---|---|---|
| 脚本·古风 | 1 | 称谓与身份 | 陛下/娘娘/臣/属下用法不乱，主仆不乱称 | 🔴 | sd-qc-engine | short-drama-review |
| 脚本·古风 | 2 | 礼节与仪轨 | 跪拜、拱手、行礼对象与场合正确 | 🔴 | sd-qc-engine | 人工复核位 |
| 脚本·古风 | 3 | 官制与品级 | 官职体系自洽，不混串联官 | 🔴 | sd-qc-engine | 人工复核位 |
| 脚本·古风 | 4 | 人物言行不 OOC | 皇子/夫人/江湖客口吻符合身份 | 🔴 | sd-qc-engine | short-drama-review |
| 脚本·古风 | 5 | 权谋与宅斗逻辑 | 计谋有前置铺垫，不靠降智推进 | 🟢 | sd-qc-engine | short-drama-review |
| 脚本·古风 | 6 | 武功兵器设定 | 招式、兵器、内力规则前后一致 | 🔴 | sd-qc-engine | novel-worldbuilding-validator |
| 资产 | 7 | 服饰形制与朝代 | 同剧一个朝代体系，形制不混搭 | 🔴 | sd-qc-engine | costume-consistency-checker + 人工复核位 |
| 资产 | 8 | 发饰与妆容 | 身份对应发型冠饰，同场次不漂移 | 🔴 | sd-qc-engine | costume-consistency-checker |
| 资产 | 9 | 器物与兵器 | 玉佩、茶具、书卷、刀剑跨镜不变形 | 🟡 | sd-qc-engine | frame-consistency-checker |
| 分镜·动作 | 10 | 武打招式成立 | 招式配合兵器，无畸形反常识姿势 | 🔴 | sd-qc-engine | sd-combat-engine、fx-logic-checker |
| 分镜·动作 | 11 | 轻功与身法 | 起落有借力点，不悬空滑行 | 🟡 | sd-qc-engine | fx-logic-checker |
| 分镜·场面 | 12 | 朝会与市集排布 | 队列、站位、朝拜方向符合礼制 | 🟡 | sd-qc-engine | 【替代校验】shot-continuity-inspector + 人工复核位 |
| 分镜·空间 | 13 | 府邸空间与轴线 | 厅堂、内院、门口方向关系自洽 | 🟡 | sd-qc-engine | shot-continuity-inspector |
| 画面 | 14 | 画风统一 | 全程古风质感，不跳现代或二次元 | 🔴 | sd-qc-engine | frame-consistency-checker |
| 画面 | 15 | 人体结构 | 无畸形、穿模、多指 | 🔴 | sd-qc-engine | frame-consistency-checker |
| 音频 | 16 | 对白与旁白 | 台词时序对齐，旁白不压戏 | 🔴 | sd-qc-engine | audio-sync-checker |
| 音频 | 17 | 古风氛围音 | 马蹄、更鼓、兵器碰撞匹配场景 | 🟡 | sd-qc-engine | audio-sync-checker |
| 字幕 | 18 | 台词与称谓字幕 | 逐字正确，官职、称谓、年号写法正确 | 🔴 | sd-qc-engine | subtitle-timing-checker |
| 字幕 | 19 | 字幕不遮挡 | 不挡面部、玉佩、兵器关键处 | 🟡 | sd-qc-engine | subtitle-timing-checker |
| 合规 | 20 | 史实与导向 | 不魔改重大史实、不丑化正面人物 | 🔴 | sd-qc-engine | 人工复核位 |
| 交付 | 21 | 物料归档 | 剧本、服饰参考卡、分镜、审计齐全 | 🟡 | sd-qc-engine | — |

## 加载文本

```text
【古装古风质检基线V1】
1.称谓与身份：称谓用法不乱；阻断；sd-qc-engine；short-drama-review
2.礼节与仪轨：行礼对象场合正确；阻断；sd-qc-engine；人工复核位
3.官制与品级：官职体系自洽；阻断；sd-qc-engine；人工复核位
4.人物言行不OOC：口吻符合身份；阻断；sd-qc-engine；short-drama-review
5.权谋宅斗逻辑：计谋有铺垫不降智；优化；sd-qc-engine；short-drama-review
6.武功兵器设定：招式兵器内力一致；阻断；sd-qc-engine；novel-worldbuilding-validator
7.服饰形制朝代：一剧一朝不混搭；阻断；sd-qc-engine；costume-consistency-checker+人工复核位
8.发饰与妆容：身份对应不漂移；阻断；sd-qc-engine；costume-consistency-checker
9.器物与兵器：跨镜不变形；一般；sd-qc-engine；frame-consistency-checker
10.武打招式成立：配合兵器无畸形；阻断；sd-qc-engine；sd-combat-engine、fx-logic-checker
11.轻功与身法：有借力点不悬空；一般；sd-qc-engine；fx-logic-checker
12.朝会市集排布：符合礼制；一般；sd-qc-engine；shot-continuity-inspector + 人工复核位
13.府邸空间轴线：厅堂内院门口自洽；一般；sd-qc-engine；shot-continuity-inspector
14.画风统一：古风质感；阻断；sd-qc-engine；frame-consistency-checker
15.人体结构：无畸形穿模；阻断；sd-qc-engine；frame-consistency-checker
16.对白与旁白：时序对齐；阻断；sd-qc-engine；audio-sync-checker
17.古风氛围音：匹配场景；一般；sd-qc-engine；audio-sync-checker
18.称谓字幕：逐字正确；阻断；sd-qc-engine；subtitle-timing-checker
19.字幕不遮挡：不挡面部器物；一般；sd-qc-engine；subtitle-timing-checker
20.史实与导向：不魔改不丑化；阻断；sd-qc-engine；人工复核位
21.物料归档：四件齐全；一般；sd-qc-engine；无
```

## 口令

- **初始化**：`sd-qc-engine，加载《古装古风质检清单V1》+绑定表，锁定本剧朝代与礼制口径，冻结为基线；清单内校验器均为本机可执行项；解绑其他题材。`
- **单集终审**：`sd-qc-engine，加载古风基线，逐段逐句逐镜过 21 条；形制与队形条标替代校验+人工复核；武打条先 sd-combat-engine 对动作再 fx-logic-checker；出报告+审计栏。`
- **剧本前置**：`sd-qc-engine，仅跑脚本·古风 6 条，调 short-drama-review、novel-worldbuilding-validator；礼节官制列人工复核。`
- **单点抽检**：`costume-consistency-checker，单点抽检本集服饰与法器，仅内部参考。`
