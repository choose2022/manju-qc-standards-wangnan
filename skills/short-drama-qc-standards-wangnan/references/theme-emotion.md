# 题材 3：现实情感（含 4 子类）

适用子类：甜宠恋爱（17 条基底 + 加甜宠补充）、虐恋破镜重圆、家庭伦理、现实治愈。
红线：不得美化控制欲、PUA、家暴；亲密戏不越线；不物化人物。

**技能池**
- 强制：`sd-qc-engine`、`frame-consistency-checker`、`costume-consistency-checker`、`shot-continuity-inspector`、`subtitle-timing-checker`、`audio-sync-checker`
- 补强：`short-drama-review`（人设 OOC、台词、情绪）、`novel-worldbuilding-validator`（动机因果）
- 子类追加：甜宠加 `frame-consistency-checker`（妆造甜度统一）；虐恋加 `audio-sync-checker`（哭腔与气息）；家庭伦理加 `shot-continuity-inspector`（家庭空间动线）；治愈加 `frame-consistency-checker`（光影统一）
- 校验器清理：清单内原缺失项已按 H3 可执行口径替换（对照见 SKILL.md「校验器可用性」），无需安装。

## 质检清单 V1（基底 18 条）

| 模块 | 序 | 检查项 | 合格标准 | 等级 | 强制 | 补强 |
|---|---|---|---|---|---|---|
| 脚本 | 1 | 人物小传与动机 | 主要人物动机能在剧本里找到因果 | 🔴 | sd-qc-engine | short-drama-review |
| 脚本 | 2 | 情感推进层次 | 好感/误会/破裂/复合有梯度，不一步到位 | 🔴 | sd-qc-engine | short-drama-review |
| 脚本 | 3 | 台词人设一致 | 口吻符合年龄与身份，不 OOC | 🔴 | sd-qc-engine | short-drama-review |
| 脚本 | 4 | 冲突合理性 | 争吵、误会、分手有可理解触发点，不强行降智 | 🔴 | sd-qc-engine | novel-worldbuilding-validator |
| 脚本 | 5 | 时间线 | 相遇、相处、分离的时长与季节自洽 | 🟡 | sd-qc-engine | novel-worldbuilding-validator |
| 脚本 | 6 | 价值观导向 | 不美化控制、PUA、家暴、炫富 | 🔴 | sd-qc-engine | 人工复核位 |
| 资产 | 7 | 面部一致性 | 男女主不换脸，特写与中景同一张脸 | 🔴 | sd-qc-engine | frame-consistency-checker |
| 资产 | 8 | 妆造一致 | 同场次发型、妆容、服装不漂移 | 🔴 | sd-qc-engine | costume-consistency-checker |
| 资产 | 9 | 道具信物 | 戒指、手机、信件、礼物跨镜一致 | 🔴 | sd-qc-engine | frame-consistency-checker |
| 分镜 | 10 | 双人戏机位 | 正反打轴线不断，身高差与视线合理 | 🔴 | sd-qc-engine | shot-continuity-inspector |
| 分镜 | 11 | 情绪特写 | 表情强度与情节匹配，不过度演 | 🟡 | sd-qc-engine | short-drama-review |
| 分镜 | 12 | 空间动线 | 客厅、卧室、餐厅布局前后一致 | 🟡 | sd-qc-engine | shot-continuity-inspector |
| 画面 | 13 | 画风统一 | 全片同一写实质感 | 🔴 | sd-qc-engine | frame-consistency-checker |
| 画面 | 14 | 光照氛围 | 同场次色温稳定，夜戏不忽明忽暗 | 🟡 | sd-qc-engine | frame-consistency-checker |
| 音频 | 15 | 台词与气息 | 哭腔、哽咽、气声与画面同步 | 🔴 | sd-qc-engine | audio-sync-checker |
| 音频 | 16 | BGM 与响度 | BGM 情绪匹配，不压人声，不爆音 | 🟡 | sd-qc-engine | audio-sync-checker |
| 字幕 | 17 | 台词字幕 | 逐字一致，称呼与昵称统一 | 🔴 | sd-qc-engine | subtitle-timing-checker |
| 字幕 | 18 | 字幕不遮挡 | 不挡面部表情与关键信物 | 🟡 | sd-qc-engine | subtitle-timing-checker |

**子类追加条**
- 甜宠：+脸红/心跳/靠近镜头的身体距离不跳；+同框甜度一致。
- 虐恋：+哭戏妆不花得假；+雨中/夜戏情绪光影统一。
- 家庭伦理：+多人餐桌戏座位关系固定；+长辈与晚辈称谓不乱。
- 治愈：+日常空镜节奏统一；+暖色光调不突跳冷调。

## 加载文本

```text
【现实情感质检基线V1】
1.人物动机：动机有剧本因果；阻断；sd-qc-engine；short-drama-review
2.情感推进层次：有梯度；阻断；sd-qc-engine；short-drama-review
3.台词人设一致：不OOC；阻断；sd-qc-engine；short-drama-review
4.冲突合理性：有可理解触发点；阻断；sd-qc-engine；novel-worldbuilding-validator
5.时间线：时长季节自洽；一般；sd-qc-engine；novel-worldbuilding-validator
6.价值观导向：不美化控制暴力；阻断；sd-qc-engine；人工复核位
7.面部一致性：不换脸；阻断；sd-qc-engine；frame-consistency-checker
8.妆造一致：同场次不漂移；阻断；sd-qc-engine；costume-consistency-checker
9.道具信物：跨镜一致；阻断；sd-qc-engine；frame-consistency-checker
10.双人戏机位：轴线不断身高视线合理；阻断；sd-qc-engine；shot-continuity-inspector
11.情绪特写：强度匹配不过度演；一般；sd-qc-engine；short-drama-review
12.空间动线：布局前后一致；一般；sd-qc-engine；shot-continuity-inspector
13.画风统一：同质感；阻断；sd-qc-engine；frame-consistency-checker
14.光照氛围：色温稳定；一般；sd-qc-engine；frame-consistency-checker
15.台词与气息：哭腔气声同步；阻断；sd-qc-engine；audio-sync-checker
16.BGM与响度：情绪匹配不压人声；一般；sd-qc-engine；audio-sync-checker
17.台词字幕：逐字一致称呼统一；阻断；sd-qc-engine；subtitle-timing-checker
18.字幕不遮挡：不挡表情信物；一般；sd-qc-engine；subtitle-timing-checker
```

## 口令

- **初始化**：`sd-qc-engine，加载《现实情感质检清单V1》+绑定表，注明子类（甜宠/虐恋/家庭伦理/治愈），冻结为基线；解绑修仙与军事校验器。`
- **单集终审**：`sd-qc-engine，加载情感基线+子类追加条，逐段逐句逐镜校验；双人戏重点走 shot-continuity-inspector；情绪条走 short-drama-review；出报告+审计栏。`
- **剧本前置**：`sd-qc-engine，仅跑脚本 6 条，调 short-drama-review、novel-worldbuilding-validator；价值观条列人工复核位。`
- **单点抽检**：`frame-consistency-checker，单点抽检男女主面部与妆造，仅内部参考。`
