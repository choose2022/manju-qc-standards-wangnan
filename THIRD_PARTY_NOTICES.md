# 第三方内容声明（THIRD PARTY NOTICES）

本仓库**不包含**任何第三方 skill 的正文副本。以下内容仅为**名称引用、条款提要转述与出处标注**，
版权归各自作者所有，本仓库不对其再授权。

**我是哪一种？** —— 属于「引用 + 派生提要」：没有整篇搬运，但第 2 节表格里的 8 条失效条款是对他人
skill 正文的**压缩改写**，并标注了原文位置（章节号 / 文件名 / 行号）。改动处已在下表写明。

---

## 一、被引用的 skill 名称（仅名称，不涉正文）

| skill | 归属 | 本仓库怎么用它 |
|---|---|---|
| `sd-qc-engine` | 漫剧老李AIGC 全流程 Skill · V7.4.26 套装 · 子技能 | 作为主质检引擎，清单只写「调用它」，不复制其正文 |
| `sd-feed-engine` / `sd-combat-engine` / `sd-decision-engine` / `sd-asset-engine` / `sd-script-engine` / `sd-overseas-engine` / `sd-jieshuo-engine` / `sd-recon-engine` / `sd-real-engine` / `sd-xuanhuan-engine` / `sd-storyboard-engine` | 同上（套装子技能） | 只在「换模型失效表」与「按模型分轨矩阵」里被点名归类 |
| `short-drama-director` | 漫剧老李AIGC（套装总控） | 仅作为套装总控被提及 |
| `short-drama-review` / `short-drama-edit` / `short-drama-produce` | 原作者未在其 SKILL.md 标注 | 仅作为校验/剪辑环节的调度对象被点名 |
| `frame-consistency-checker` / `costume-consistency-checker` / `shot-continuity-inspector` / `fx-logic-checker` / `audio-sync-checker` / `subtitle-timing-checker` / `novel-worldbuilding-validator` / `novel-cultivation-logic-checker` / `giant-scale-scene` / `script-to-manga` / `novel-storyboard` / `byted-mediakit-image` / `byted-mediakit-video` | 原作者未在其 SKILL.md 标注 | 清单的「强制 / 补强校验器」列只写名字与用途，不复制其判据正文 |
| `h3-prompt-writing` / `h3-video-prompting` / `minimax-h3` / `qwen3-tts` / `comfyui` | 原作者未在其 SKILL.md 标注 | 仅在「单模型专用」分类里被点名 |

> 说明：以上名称出现在 `SKILL.md` 的技能池、以及 `references/theme-*.md` 的「强制 / 补强」列。
> 属于**调用关系声明**，不是内容再分发。

---

## 二、派生与转述（需要特别标注的部分）

文件：`skills/short-drama-qc-standards-wangnan/references/model-compat-matrix.md` 第三节
《跨模型失效条款表》共 8 条。每条都是对下列原文的**压缩改写**（不是逐字摘录），并标注了原文位置：

| 条款 | 原文出处（作者 skill 内） | 本仓库的改动 |
|---|---|---|
| H3 六段式台词块 | `sd-feed-engine/SKILL.md` 契约 §2；`novel-storyboard/references/h3-prompt.md` | 压缩为一句判定 + 换模型后处置 |
| H3 段长 4–15 秒硬区间 | `sd-qc-engine/references/machine-check-manual.md` L24–L27 | 同上 |
| 15 秒分段硬脚本 | `sd-qc-engine/references/editing-transition-gate.md` L34–L36 | 同上 |
| `[SFX:]` 音效标记开关 | `sd-qc-engine/references/sound-design-template.md` L33 | 同上 |
| H3 声音分层禁台词 | 同上 L37 | 同上 |
| H3 不出画面内字幕条 | `subtitle-timing-checker/SKILL.md` L45 | 同上 |
| 字数与图数平台上限 | `sd-feed-engine` 闸门 3、闸门 5 | 同上 |
| 素材形态 M0/M1/M2 | `sd-feed-engine` 契约 §8 | 同上 |

这些条目的**原始表述与判定权仍归原作者**；本仓库的版本只服务于「换模型前自查」这一用途，
如需权威口径请直接读对应 skill 的正文。

---

## 三、未随仓库分发的内容

- 上述任何 skill 的 `SKILL.md`、`references/`、`scripts/` 正文，**均未复制进本仓库**。
- 本仓库 `skills/` 下只有 `short-drama-qc-standards-wangnan` 一个目录，是 wangnan 原创。

## 四、如需引用本仓库

按根目录 `LICENSE` 执行；引用时请保留 `README.md` 的作者署名与本文件。
若你是上表某个 skill 的作者，认为上述引用方式不妥，请开 Issue，我会在 48 小时内调整或移除。
