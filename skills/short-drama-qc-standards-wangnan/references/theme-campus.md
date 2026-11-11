# 题材 11：校园青春

适用子类：校园甜宠暗恋、学神成长逆袭、校园悬疑、校园现实向（霸凌/原生家庭）。
红线：未成年人不做任何性暗示与恋爱越界描写；霸凌、自伤等题材须正向收束；不美化升学焦虑与体罚。

**技能池**
- 强制：`sd-qc-engine`、`frame-consistency-checker`、`costume-consistency-checker`（校服年级）、`shot-continuity-inspector`、`subtitle-timing-checker`、`audio-sync-checker`
- 补强：`short-drama-review`（年龄感、台词、价值观）、`novel-worldbuilding-validator`（成长线因果）
- 校验器清理：清单内原缺失项已按 H3 可执行口径替换（对照见 SKILL.md「校验器可用性」），无需安装。

## 质检清单 V1

| 模块 | 序 | 检查项 | 合格标准 | 等级 | 强制 | 补强 |
|---|---|---|---|---|---|---|
| 脚本 | 1 | 年龄感与人设 | 台词、行为、心智与年级匹配，不幼儿化也不成人化 | 🔴 | sd-qc-engine | short-drama-review |
| 脚本 | 2 | 成长线因果 | 逆袭、转变有过程，不一夜开挂 | 🟡 | sd-qc-engine | novel-worldbuilding-validator |
| 脚本 | 3 | 校园关系网 | 班级、师生、家庭关系清楚不混乱 | 🟡 | sd-qc-engine | short-drama-review |
| 脚本 | 4 | 价值观导向 | 霸凌、早恋、自伤写正向收束，不美化 | 🔴 | sd-qc-engine | 人工复核位 |
| 脚本 | 5 | 未成年保护红线 | 无性暗示、无越界亲密、无暴力示范 | 🔴 | sd-qc-engine | 人工复核位（必过） |
| 资产 | 6 | 校服与年级标识 | 同校服制统一，年级/班级标识不乱 | 🔴 | sd-qc-engine | costume-consistency-checker |
| 资产 | 7 | 校园道具 | 书包、课本、试卷、黑板内容跨镜一致 | 🟡 | sd-qc-engine | frame-consistency-checker |
| 资产 | 8 | 面部与年龄感 | 同一角色不忽老忽幼、不换脸 | 🔴 | sd-qc-engine | frame-consistency-checker |
| 分镜 | 9 | 教室空间 | 座位表与镜头位置对应，不穿墙 | 🔴 | sd-qc-engine | shot-continuity-inspector |
| 分镜 | 10 | 走廊与操场动线 | 前后镜方向接得上 | 🟡 | sd-qc-engine | shot-continuity-inspector |
| 画面 | 11 | 画风统一 | 全片青春质感统一 | 🔴 | sd-qc-engine | frame-consistency-checker |
| 画面 | 12 | 人体结构 | 无畸形、穿模 | 🔴 | sd-qc-engine | frame-consistency-checker |
| 音频 | 13 | 台词与朗读 | 时序对齐，课堂朗读不抢戏 | 🔴 | sd-qc-engine | audio-sync-checker |
| 音频 | 14 | 校园环境音 | 铃声、操场、教室底噪匹配 | 🟡 | sd-qc-engine | audio-sync-checker |
| 字幕 | 15 | 台词与板书字幕 | 逐字一致，人名、科目名正确 | 🔴 | sd-qc-engine | subtitle-timing-checker |
| 字幕 | 16 | 字幕不遮挡 | 不挡表情与关键板书 | 🟡 | sd-qc-engine | subtitle-timing-checker |
| 合规 | 17 | 未成年与导向 | 无违规内容，导向正向 | 🔴 | sd-qc-engine | 人工复核位（必过） |
| 交付 | 18 | 物料归档 | 剧本、分镜、人物卡、审计齐全 | 🟡 | sd-qc-engine | — |

## 加载文本

```text
【校园青春质检基线V1】
1.年龄感人设：台词行为心智匹配年级；阻断；sd-qc-engine；short-drama-review
2.成长线因果：有过程不开挂；一般；sd-qc-engine；novel-worldbuilding-validator
3.校园关系网：班级师生家庭清楚；一般；sd-qc-engine；short-drama-review
4.价值观导向：敏感题材正向收束；阻断；sd-qc-engine；人工复核位
5.未成年保护红线：无性暗示越界暴力示范；阻断；sd-qc-engine；人工复核位
6.校服年级标识：同校统一不乱；阻断；sd-qc-engine；costume-consistency-checker
7.校园道具：书包试卷黑板一致；一般；sd-qc-engine；frame-consistency-checker
8.面部年龄感：忽老忽幼或换脸；阻断；sd-qc-engine；frame-consistency-checker
9.教室空间：座位与机位对应；阻断；sd-qc-engine；shot-continuity-inspector
10.走廊操场动线：方向接得上；一般；sd-qc-engine；shot-continuity-inspector
11.画风统一：青春质感；阻断；sd-qc-engine；frame-consistency-checker
12.人体结构：无畸形穿模；阻断；sd-qc-engine；frame-consistency-checker
13.台词朗读：时序对齐；阻断；sd-qc-engine；audio-sync-checker
14.校园环境音：匹配场景；一般；sd-qc-engine；audio-sync-checker
15.台词板书字幕：逐字一致；阻断；sd-qc-engine；subtitle-timing-checker
16.字幕不遮挡：不挡表情板书；一般；sd-qc-engine；subtitle-timing-checker
17.未成年与导向：无违规导向正向；阻断；sd-qc-engine；人工复核位
18.物料归档：四件齐全；一般；sd-qc-engine；无
```

## 口令

- **初始化**：`sd-qc-engine，加载《校园青春质检清单V1》+绑定表，冻结为基线；未成年保护两条设为必过阻断项。`
- **单集终审**：`sd-qc-engine，加载校园基线，逐段逐句逐镜过 18 条；教室空间走 shot-continuity-inspector；合规两条必须人工复核签字；出报告+审计栏。`
- **剧本前置**：`sd-qc-engine，仅跑脚本 5 条，调 short-drama-review、novel-worldbuilding-validator；红线两条人工复核。`
- **单点抽检**：`frame-consistency-checker，单点抽检学生面部年龄感，仅内部参考。`
