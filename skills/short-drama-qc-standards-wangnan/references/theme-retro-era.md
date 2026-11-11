# 题材 8：年代重生

适用子类：七零八零九零年代重生、知青下乡、年代经商（摆摊/开厂/外贸）、年代家庭伦理。
红线：时代道具不得超前（还没发明的东西不能出现）；不美化违法致富；年代苦难不做猎奇消费。

**技能池**
- 强制：`sd-qc-engine`、`frame-consistency-checker`、`costume-consistency-checker`、`shot-continuity-inspector`、`subtitle-timing-checker`、`audio-sync-checker`
- 补强：`short-drama-review`（年代话术与家庭关系）、`novel-worldbuilding-validator`（重生信息差逻辑）
- 校验器清理：清单内原缺失项已按 H3 可执行口径替换（对照见 SKILL.md「校验器可用性」），无需安装。

## 质检清单 V1

| 模块 | 序 | 检查项 | 合格标准 | 等级 | 强制 | 补强 |
|---|---|---|---|---|---|---|
| 脚本·年代 | 1 | 年代锚点 | 首集明确年份、地点、家庭成分，全剧不飘 | 🔴 | sd-qc-engine | short-drama-review |
| 脚本·年代 | 2 | 道具时代下限 | 家电、通讯、交通、服饰不超前于设定年份 | 🔴 | sd-qc-engine | 人工复核位 |
| 脚本·年代 | 3 | 物价与票据 | 工资、粮票、布票、价格符合当年水平 | 🔴 | sd-qc-engine | 人工复核位 |
| 脚本·年代 | 4 | 政策与机会 | 经商、招工、考学的时间窗口成立 | 🟡 | sd-qc-engine | novel-worldbuilding-validator |
| 脚本·年代 | 5 | 重生信息差 | 主角"预知"限于已亲历之事，不无限开挂 | 🔴 | sd-qc-engine | novel-worldbuilding-validator |
| 脚本·年代 | 6 | 称谓与话术 | 称呼、口头禅、标语符合年代，不带现代网络词 | 🔴 | sd-qc-engine | short-drama-review |
| 资产 | 7 | 服装与发型 | 的确良、军绿、喇叭裤等与年份匹配且跨镜稳定 | 🔴 | sd-qc-engine | costume-consistency-checker |
| 资产 | 8 | 家居陈设 | 老家具、挂历、搪瓷缸、缝纫机同屋不换样 | 🔴 | sd-qc-engine | frame-consistency-checker |
| 资产 | 9 | 交通工具 | 自行车、三轮、拖拉机型号与年代一致 | 🟡 | sd-qc-engine | frame-consistency-checker |
| 分镜 | 10 | 街景与院落空间 | 巷口、院门、屋内外方向关系自洽 | 🟡 | sd-qc-engine | shot-continuity-inspector |
| 分镜 | 11 | 劳动动作 | 挑担、插秧、踩缝纫机、摆摊动作成立 | 🟡 | sd-qc-engine | frame-consistency-checker |
| 画面 | 12 | 年代质感与画风 | 全片统一胶片/暖黄年代调，不跳现代高清感 | 🔴 | sd-qc-engine | frame-consistency-checker |
| 画面 | 13 | 人体结构 | 无畸形、穿模 | 🔴 | sd-qc-engine | frame-consistency-checker |
| 音频 | 14 | 台词口音与年代音 | 方言/口音统一，语音时序对齐 | 🔴 | sd-qc-engine | audio-sync-checker |
| 音频 | 15 | 年代环境音 | 广播、集市、厂区噪音匹配场景 | 🟡 | sd-qc-engine | audio-sync-checker |
| 字幕 | 16 | 年代名词字幕 | 票证、单位、工种名称写法正确 | 🔴 | sd-qc-engine | subtitle-timing-checker |
| 字幕 | 17 | 字幕不遮挡 | 不挡关键老物件与手部劳作 | 🟡 | sd-qc-engine | subtitle-timing-checker |
| 合规 | 18 | 年代与价值观 | 不美化违法致富、不猎奇消费苦难 | 🔴 | sd-qc-engine | 人工复核位 |
| 交付 | 19 | 物料归档 | 剧本、年代道具卡、分镜、审计齐全 | 🟡 | sd-qc-engine | — |

## 加载文本

```text
【年代重生质检基线V1】
1.年代锚点：年份地点成分明确不飘；阻断；sd-qc-engine；short-drama-review
2.道具时代下限：不超前于年份；阻断；sd-qc-engine；人工复核位
3.物价与票据：工资票证价格符合当年；阻断；sd-qc-engine；人工复核位
4.政策与机会：时间窗口成立；一般；sd-qc-engine；novel-worldbuilding-validator
5.重生信息差：预知限于亲历；阻断；sd-qc-engine；novel-worldbuilding-validator
6.称谓与话术：年代用语不带网络词；阻断；sd-qc-engine；short-drama-review
7.服装与发型：与年份匹配跨镜稳定；阻断；sd-qc-engine；costume-consistency-checker
8.家居陈设：老物件同屋不换样；阻断；sd-qc-engine；frame-consistency-checker
9.交通工具：型号与年代一致；一般；sd-qc-engine；frame-consistency-checker
10.街景院落空间：方向关系自洽；一般；sd-qc-engine；shot-continuity-inspector
11.劳动动作：挑担插秧摆摊成立；一般；sd-qc-engine；frame-consistency-checker
12.年代质感画风：统一不跳现代；阻断；sd-qc-engine；frame-consistency-checker
13.人体结构：无畸形穿模；阻断；sd-qc-engine；frame-consistency-checker
14.台词口音：统一且时序对齐；阻断；sd-qc-engine；audio-sync-checker
15.年代环境音：匹配场景；一般；sd-qc-engine；audio-sync-checker
16.年代名词字幕：票证单位工种正确；阻断；sd-qc-engine；subtitle-timing-checker
17.字幕不遮挡：不挡老物件劳作；一般；sd-qc-engine；subtitle-timing-checker
18.年代价值观：不美化违法不猎奇苦难；阻断；sd-qc-engine；人工复核位
19.物料归档：四件齐全；一般；sd-qc-engine；无
```

## 口令

- **初始化**：`sd-qc-engine，加载《年代重生质检清单V1》+绑定表，锁定设定年份与地域，冻结为基线；清单内校验器均为本机可执行项。`
- **单集终审**：`sd-qc-engine，加载年代基线，逐段逐句逐镜过 19 条；道具年代下限逐件核并标缺口；出报告+审计栏。`
- **剧本前置**：`sd-qc-engine，仅跑脚本·年代 6 条，调 short-drama-review、novel-worldbuilding-validator；物价票据列人工复核。`
- **单点抽检**：`frame-consistency-checker，单点抽检老物件与陈设一致性，仅内部参考。`
