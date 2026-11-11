# 题材 14：国风神话志怪

适用子类：洪荒上古神明、民间传说改编、聊斋志怪、山海异兽。
红线：不得把神话写成现实迷信引导（不许出现"照做能消灾治病"等）；不贬损真实民族信仰；不魔改公认经典人物成反面。

**技能池**
- 强制：`sd-qc-engine`、`frame-consistency-checker`、`costume-consistency-checker`（神像/道袍/妖装）、`shot-continuity-inspector`、`subtitle-timing-checker`、`audio-sync-checker`
- 补强：`fx-logic-checker`（神光、幻境、妖气）、`novel-worldbuilding-validator`（神谱与典故自洽）、`giant-scale-scene`（法相与神域尺度）
- 校验器清理：清单内原缺失项已按 H3 可执行口径替换（对照见 SKILL.md「校验器可用性」），无需安装。

## 质检清单 V1

| 模块 | 序 | 检查项 | 合格标准 | 等级 | 强制 | 补强 |
|---|---|---|---|---|---|---|
| 脚本·设定 | 1 | 神谱层级 | 神、仙、妖、鬼的位阶与从属清楚，不越级 | 🔴 | sd-qc-engine | novel-worldbuilding-validator |
| 脚本·设定 | 2 | 典故与出处 | 引用的传说、法宝、神职有据，不随意改写公认情节 | 🔴 | sd-qc-engine | 人工复核位 |
| 脚本·设定 | 3 | 法器等阶 | 法宝威能与持有者匹配，不随便下发 | 🔴 | sd-qc-engine | novel-worldbuilding-validator |
| 脚本·设定 | 4 | 妖异规则 | 妖怪原形、弱点、禁忌前后一致 | 🔴 | sd-qc-engine | novel-worldbuilding-validator |
| 脚本·设定 | 5 | 人神关系动机 | 供奉、降妖、报应的因果成立 | 🟡 | sd-qc-engine | short-drama-review |
| 资产 | 6 | 神像与法相 | 造型、手印、法器持拿位置跨镜一致 | 🔴 | sd-qc-engine | costume-consistency-checker |
| 资产 | 7 | 服饰与符箓 | 道袍、经文、符箓样式统一，不混搭 | 🔴 | sd-qc-engine | costume-consistency-checker |
| 资产 | 8 | 妖物原形 | 同一妖物化形前后特征可追溯 | 🟡 | sd-qc-engine | frame-consistency-checker |
| 分镜·特效 | 9 | 神光与妖气 | 光从法器或本体发出，有来源与衰减 | 🔴 | sd-qc-engine | fx-logic-checker |
| 分镜·特效 | 10 | 幻境与结界 | 结界边界清楚，景物不透穿 | 🟡 | sd-qc-engine | fx-logic-checker |
| 分镜·特效 | 11 | 法相尺度 | 巨身法相有人物与建筑参照 | 🟡 | sd-qc-engine | giant-scale-scene |
| 分镜·空间 | 12 | 庙宇与神域空间 | 殿内方位、供桌关系自洽 | 🟡 | sd-qc-engine | shot-continuity-inspector |
| 画面 | 13 | 画风统一 | 国风质感统一，不跳现代 | 🔴 | sd-qc-engine | frame-consistency-checker |
| 画面 | 14 | 人体结构 | 无畸形、穿模 | 🔴 | sd-qc-engine | frame-consistency-checker |
| 音频 | 15 | 诵经与台词 | 诵经、咒语与画面时序对齐 | 🔴 | sd-qc-engine | audio-sync-checker |
| 音频 | 16 | 钟磬与氛围音 | 法器音、风声匹配场景 | 🟡 | sd-qc-engine | audio-sync-checker |
| 字幕 | 17 | 经文与神名字幕 | 逐字正确，神名、经文写法无错 | 🔴 | sd-qc-engine | subtitle-timing-checker |
| 字幕 | 18 | 字幕不遮挡 | 不挡手印、符箓、法器关键处 | 🟡 | sd-qc-engine | subtitle-timing-checker |
| 合规 | 19 | 迷信红线 | 无现实迷信引导、无民族信仰贬损 | 🔴 | sd-qc-engine | 人工复核位（必过） |
| 交付 | 20 | 物料归档 | 剧本、神谱设定、分镜、审计齐全 | 🟡 | sd-qc-engine | — |

## 加载文本

```text
【国风神话志怪质检基线V1】
1.神谱层级：位阶从属清楚不越级；阻断；sd-qc-engine；novel-worldbuilding-validator
2.典故与出处：引用有据不改公认情节；阻断；sd-qc-engine；人工复核位
3.法器等阶：威能与持有者匹配；阻断；sd-qc-engine；novel-worldbuilding-validator
4.妖异规则：原形弱点禁忌一致；阻断；sd-qc-engine；novel-worldbuilding-validator
5.人神关系动机：供奉降妖报应成立；一般；sd-qc-engine；short-drama-review
6.神像与法相：造型手印法器一致；阻断；sd-qc-engine；costume-consistency-checker
7.服饰与符箓：样式统一不混搭；阻断；sd-qc-engine；costume-consistency-checker
8.妖物原形：化形前后特征可追溯；一般；sd-qc-engine；frame-consistency-checker
9.神光与妖气：有来源与衰减；阻断；sd-qc-engine；fx-logic-checker
10.幻境与结界：边界清楚不透穿；一般；sd-qc-engine；fx-logic-checker
11.法相尺度：有人物建筑参照；一般；sd-qc-engine；giant-scale-scene
12.庙宇神域空间：殿内方位自洽；一般；sd-qc-engine；shot-continuity-inspector
13.画风统一：国风质感；阻断；sd-qc-engine；frame-consistency-checker
14.人体结构：无畸形穿模；阻断；sd-qc-engine；frame-consistency-checker
15.诵经与台词：时序对齐；阻断；sd-qc-engine；audio-sync-checker
16.钟磬氛围音：匹配场景；一般；sd-qc-engine；audio-sync-checker
17.经文神名字幕：逐字正确；阻断；sd-qc-engine；subtitle-timing-checker
18.字幕不遮挡：不挡手印符箓法器；一般；sd-qc-engine；subtitle-timing-checker
19.迷信红线：无现实迷信引导与贬损；阻断；sd-qc-engine；人工复核位
20.物料归档：四件齐全；一般；sd-qc-engine；无
```

## 口令

- **初始化**：`sd-qc-engine，加载《国风神话志怪质检清单V1》+绑定表，锁定本作神谱设定，冻结为基线；清单内校验器均为本机可执行项。`
- **单集终审**：`sd-qc-engine，加载神话基线，逐段逐句逐镜过 20 条；神光妖气走 fx-logic-checker；法相走 giant-scale-scene；迷信红线必须人工复核；出报告+审计栏。`
- **设定前置**：`sd-qc-engine，仅跑脚本·设定 5 条，调 novel-worldbuilding-validator、short-drama-review。`
- **单点抽检**：`fx-logic-checker，单点抽检本集神光与结界，仅内部参考。`
