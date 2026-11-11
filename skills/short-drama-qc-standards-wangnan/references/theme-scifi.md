# 题材 10：科幻未来

适用子类：星际与殖民、赛博朋克都市、系统科幻/都市异能。
红线：科技设定不得自相矛盾；不宣扬技术极权与违法实验；异能不做成修仙法术。

**技能池**
- 强制：`sd-qc-engine`、`frame-consistency-checker`、`costume-consistency-checker`（义体/舱服）、`shot-continuity-inspector`、`subtitle-timing-checker`、`audio-sync-checker`
- 补强：`fx-logic-checker`（能量、激光、全息、力场）、`novel-worldbuilding-validator`（科技规则统一）、`giant-scale-scene`（舰队/巨构尺度）
- 校验器清理：清单内原缺失项已按 H3 可执行口径替换（对照见 SKILL.md「校验器可用性」），无需安装。

## 质检清单 V1

| 模块 | 序 | 检查项 | 合格标准 | 等级 | 强制 | 补强 |
|---|---|---|---|---|---|---|
| 脚本·设定 | 1 | 科技树自洽 | 能量源、推进、通讯的能力边界前后统一 | 🔴 | sd-qc-engine | novel-worldbuilding-validator |
| 脚本·设定 | 2 | 异能规则 | 能力代价、冷却、触发条件写死，不随时变 | 🔴 | sd-qc-engine | novel-worldbuilding-validator |
| 脚本·设定 | 3 | 势力与世界观 | 公司、政府、殖民地关系清楚，不临时加设定 | 🟡 | sd-qc-engine | short-drama-review |
| 剧本·设定 | 4 | 术语一致 | 舰级、机型、协议名全文一套写法 | 🔴 | sd-qc-engine | subtitle-timing-checker（同步核） |
| 资产 | 5 | 舰船与巨构构型 | 同一舰/城外观结构跨镜不变形 | 🔴 | sd-qc-engine | frame-consistency-checker |
| 资产 | 6 | 义体与舱服 | 义体部位、接口、舱服配色同角色一致 | 🔴 | sd-qc-engine | costume-consistency-checker |
| 资产 | 7 | 设备与武器 | 枪械、终端、能量匣造型统一 | 🟡 | sd-qc-engine | frame-consistency-checker |
| 分镜 | 8 | 舱内空间 | 驾驶舱、走廊、气闸方向关系自洽 | 🟡 | sd-qc-engine | shot-continuity-inspector |
| 分镜 | 9 | 舰队与巨城场面 | 编队层级、尺度参照成立 | 🟡 | sd-qc-engine | 【替代校验】giant-scale-scene + 人工复核位 |
| 特效 | 10 | 能量与激光 | 光源从设备发出，有衰减与反射 | 🔴 | sd-qc-engine | fx-logic-checker |
| 特效 | 11 | 全息与 UI 面板 | 面板透视贴合空间，不贴片飘浮 | 🔴 | sd-qc-engine | fx-logic-checker |
| 特效 | 12 | 力场与失重 | 有物理反馈，物件不乱飘 | 🟡 | sd-qc-engine | fx-logic-checker |
| 画面 | 13 | 画风统一 | 全片同一科幻质感，不跳风格 | 🔴 | sd-qc-engine | frame-consistency-checker |
| 画面 | 14 | 人体结构 | 无畸形、义体接口穿模 | 🔴 | sd-qc-engine | frame-consistency-checker |
| 音频 | 15 | 台词与通讯音 | 电台、AI 语音与画面时序对齐 | 🔴 | sd-qc-engine | audio-sync-checker |
| 音频 | 16 | 机械与环境音 | 引擎、气闸、警报匹配场景 | 🟡 | sd-qc-engine | audio-sync-checker |
| 字幕 | 17 | 术语与面板字幕 | 逐字一致，编号与单位写法正确 | 🔴 | sd-qc-engine | subtitle-timing-checker |
| 字幕 | 18 | 字幕不遮挡 | 不挡关键 UI 与仪表 | 🟡 | sd-qc-engine | subtitle-timing-checker |
| 合规 | 19 | 科技与导向 | 不宣扬技术极权、违法实验、危险示范 | 🔴 | sd-qc-engine | 人工复核位 |
| 交付 | 20 | 物料归档 | 剧本、设定集、分镜、审计齐全 | 🟡 | sd-qc-engine | — |

## 加载文本

```text
【科幻未来质检基线V1】
1.科技树自洽：能力边界统一；阻断；sd-qc-engine；novel-worldbuilding-validator
2.异能规则：代价冷却触发写死；阻断；sd-qc-engine；novel-worldbuilding-validator
3.势力世界观：关系清楚不临时加设定；一般；sd-qc-engine；short-drama-review
4.术语一致：舰级机型协议一套写法；阻断；sd-qc-engine；subtitle-timing-checker
5.舰船巨构构型：跨镜不变形；阻断；sd-qc-engine；frame-consistency-checker
6.义体舱服：部位接口配色一致；阻断；sd-qc-engine；costume-consistency-checker
7.设备武器：造型统一；一般；sd-qc-engine；frame-consistency-checker
8.舱内空间：方向关系自洽；一般；sd-qc-engine；shot-continuity-inspector
9.舰队巨城场面：编队层级尺度成立；一般；sd-qc-engine；shot-continuity-inspector + 人工复核位
10.能量与激光：有衰减反射；阻断；sd-qc-engine；fx-logic-checker
11.全息与UI：透视贴合空间；阻断；sd-qc-engine；fx-logic-checker
12.力场与失重：有物理反馈；一般；sd-qc-engine；fx-logic-checker
13.画风统一：科幻质感；阻断；sd-qc-engine；frame-consistency-checker
14.人体结构：无畸形接口穿模；阻断；sd-qc-engine；frame-consistency-checker
15.台词通讯音：时序对齐；阻断；sd-qc-engine；audio-sync-checker
16.机械环境音：匹配场景；一般；sd-qc-engine；audio-sync-checker
17.术语面板字幕：逐字正确单位无误；阻断；sd-qc-engine；subtitle-timing-checker
18.字幕不遮挡：不挡UI仪表；一般；sd-qc-engine；subtitle-timing-checker
19.科技导向：不宣扬极权与危险示范；阻断；sd-qc-engine；人工复核位
20.物料归档：四件齐全；一般；sd-qc-engine；无
```

## 口令

- **初始化**：`sd-qc-engine，加载《科幻未来质检清单V1》+绑定表，冻结为基线；设定类条款以项目科技设定集为唯一口径；清单内校验器均为本机可执行项。`
- **单集终审**：`sd-qc-engine，加载科幻基线，逐段逐句逐镜过 20 条；能量/全息走 fx-logic-checker；巨构走 giant-scale-scene 并标缺口；出报告+审计栏。`
- **设定前置**：`sd-qc-engine，仅跑脚本·设定 4 条，调 novel-worldbuilding-validator、short-drama-review。`
- **单点抽检**：`fx-logic-checker，单点抽检本集能量与全息特效，仅内部参考。`
