# 题材 12：沙雕反套路脑洞

适用子类：沙雕逆袭、反套路系统流、穿书炮灰自救、拟人脑洞（动物/植物/物品成精）。
红线：整活不能碰低俗擦边、恶心猎奇、地域/性别/职业歧视；梗不得影射敏感事件。

**技能池**
- 强制：`sd-qc-engine`、`frame-consistency-checker`、`shot-continuity-inspector`、`subtitle-timing-checker`、`audio-sync-checker`
- 补强：`short-drama-review`（笑点铺垫、梗密度、人设稳定）、`novel-worldbuilding-validator`（设定不自推翻）、`costume-consistency-checker`（拟人形象一致性）
- 校验器清理：清单内原缺失项已按 H3 可执行口径替换（对照见 SKILL.md「校验器可用性」），无需安装。

## 质检清单 V1

| 模块 | 序 | 检查项 | 合格标准 | 等级 | 强制 | 补强 |
|---|---|---|---|---|---|---|
| 脚本·喜剧 | 1 | 笑点铺垫 | 每个梗有起手铺垫，不硬抖 | 🔴 | sd-qc-engine | short-drama-review |
| 脚本·喜剧 | 2 | 梗不重复 | 同集同类梗不三连用，不重复同一包袱 | 🟡 | sd-qc-engine | short-drama-review |
| 脚本·喜剧 | 3 | 设定不自我推翻 | 前面立的荒诞规则后面仍遵守 | 🔴 | sd-qc-engine | novel-worldbuilding-validator |
| 脚本·喜剧 | 4 | 人设稳定 | 沙雕但不 OOC，性格行为一致 | 🔴 | sd-qc-engine | short-drama-review |
| 脚本·喜剧 | 5 | 节奏与反转 | 反转有伏笔，不靠旁白解释笑点 | 🟡 | sd-qc-engine | short-drama-review |
| 资产 | 6 | 拟人形象 | 拟人角色造型、配饰、表情体系跨镜一致 | 🔴 | sd-qc-engine | costume-consistency-checker |
| 资产 | 7 | 夸张道具 | 变身道具、系统面板造型统一 | 🟡 | sd-qc-engine | frame-consistency-checker |
| 分镜 | 8 | 表情节奏 | 夸张表情与台词同拍，不过度演 | 🟡 | sd-qc-engine | frame-consistency-checker |
| 分镜 | 9 | 空间与机位 | 沙雕场面不穿帮，方向不跳 | 🟡 | sd-qc-engine | shot-continuity-inspector |
| 画面 | 10 | 画风统一 | 整活不跳画风，夸张程度统一 | 🔴 | sd-qc-engine | frame-consistency-checker |
| 画面 | 11 | 人体与变形 | 夸张变形有设计感，不崩成畸形 | 🔴 | sd-qc-engine | frame-consistency-checker |
| 音频 | 12 | 台词节奏 | 抖包袱处留气口，配音不赶 | 🔴 | sd-qc-engine | audio-sync-checker |
| 音频 | 13 | 音效整活 | 音效与动作同拍，不靠音量硬搞笑 | 🟡 | sd-qc-engine | audio-sync-checker |
| 字幕 | 14 | 台词字幕 | 逐字一致，谐音梗标注不乱 | 🔴 | sd-qc-engine | subtitle-timing-checker |
| 字幕 | 15 | 字幕不遮挡 | 不挡夸张表情与关键道具 | 🟡 | sd-qc-engine | subtitle-timing-checker |
| 合规 | 16 | 整活红线 | 无低俗擦边、恶心猎奇、歧视性表达 | 🔴 | sd-qc-engine | 人工复核位 |
| 交付 | 17 | 物料归档 | 剧本、梗表、分镜、审计齐全 | 🟡 | sd-qc-engine | — |

## 加载文本

```text
【沙雕反套路质检基线V1】
1.笑点铺垫：有起手不硬抖；阻断；sd-qc-engine；short-drama-review
2.梗不重复：同类梗不三连；一般；sd-qc-engine；short-drama-review
3.设定不自我推翻：荒诞规则仍遵守；阻断；sd-qc-engine；novel-worldbuilding-validator
4.人设稳定：沙雕不OOC；阻断；sd-qc-engine；short-drama-review
5.节奏与反转：有伏笔不靠旁白解释；一般；sd-qc-engine；short-drama-review
6.拟人形象：造型表情体系一致；阻断；sd-qc-engine；costume-consistency-checker
7.夸张道具：变身道具面板统一；一般；sd-qc-engine；frame-consistency-checker
8.表情节奏：与台词同拍不过度；一般；sd-qc-engine；frame-consistency-checker
9.空间与机位：不穿帮方向不跳；一般；sd-qc-engine；shot-continuity-inspector
10.画风统一：夸张程度统一；阻断；sd-qc-engine；frame-consistency-checker
11.人体与变形：有设计不崩畸形；阻断；sd-qc-engine；frame-consistency-checker
12.台词节奏：留气口不赶；阻断；sd-qc-engine；audio-sync-checker
13.音效整活：同拍不硬搞笑；一般；sd-qc-engine；audio-sync-checker
14.台词字幕：逐字一致谐音不乱；阻断；sd-qc-engine；subtitle-timing-checker
15.字幕不遮挡：不挡表情道具；一般；sd-qc-engine；subtitle-timing-checker
16.整活红线：无低俗猎奇歧视；阻断；sd-qc-engine；人工复核位
17.物料归档：四件齐全；一般；sd-qc-engine；无
```

## 口令

- **初始化**：`sd-qc-engine，加载《沙雕反套路质检清单V1》+绑定表，冻结为基线；笑点相关条款以项目梗表为口径。`
- **单集终审**：`sd-qc-engine，加载沙雕基线，逐段逐句逐镜过 17 条；笑点与设定矛盾走 short-drama-review、novel-worldbuilding-validator；出报告+审计栏。`
- **剧本前置**：`sd-qc-engine，仅跑脚本·喜剧 5 条，调 short-drama-review、novel-worldbuilding-validator。`
- **单点抽检**：`subtitle-timing-checker，单点抽检谐音梗字幕，仅内部参考。`
