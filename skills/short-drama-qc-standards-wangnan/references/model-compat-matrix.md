# 模型分轨矩阵（哪些 skill 只能 H3 用、哪些别的模型用、哪些都能用）

判据不看 skill 的自述，看它**正文里引用的字段、机检码、段长上限**锚在哪个模型上。

## 一、三个判据锚

| 锚 | 含义 | 换模型会怎样 |
|---|---|---|
| 成片现象 | 只看画面/声音/字幕出了什么问题，不碰提示词结构 | **完全不受影响**，换模型照跑 |
| 稿件结构 | 看投喂稿的段式、字段名、标记体系（如 H3 六段式 `<d>` 块、Seedance 七段式） | 换模型直接失效，必须换对应适配器 |
| 模型参数 | 段长上限、字数上限、图数上限、机检码（C1~C26 / H1~H12） | 参数按模型重设，脚本可能硬编码旧值 |

## 二、分类矩阵

### A 类：全模型通用（不绑模型，换模型不用改）

| 校验器 | 管什么 | 判据锚 | 换模型影响 |
|---|---|---|---|
| `shot-continuity-inspector` | 机位穿帮、轴线、景别重复、转场 | 成片现象 | 无 |
| `frame-consistency-checker` | 变脸、结构崩坏、画风、同场光照、NPC 复制 | 成片现象 | 无 |
| `costume-consistency-checker` | 服装、法器、饰品一致性 | 成片现象 | 无 |
| `fx-logic-checker` | 特效来源、力的回执、抽特效后动作是否成立 | 成片现象 | 无 |
| `audio-sync-checker` | 口型、响度分层、音效同拍、爆音静音 | 成片现象 | 无 |
| `subtitle-timing-checker` | 逐字一致、时轴、样式、遮挡 | 成片现象 | 无（仅一处口径差，见失效表「H3 不出画面内字幕条」） |
| `novel-cultivation-logic-checker` | 境界、功法归属、法宝形制、战力 | 文本设定 | 无 |
| `novel-worldbuilding-validator` | 因果链、动机、时间线、段间接续 | 文本设定 | 无 |
| `short-drama-review` | 原著/剧本/设定/提示词/资产审查 | 文本与资产 | 无 |
| `short-drama-edit` | 剪辑、入出点、字幕、响度、导出 | 成片现象 | 无 |
| `byted-mediakit-image` / `byted-mediakit-video` | 画质检测、抽帧、转码、抠像、媒资理解 | 成片文件 | 无 |
| `giant-scale-scene` | 巨物尺度感提示词工程 | 稿件结构（通用提示词） | 无，产出的是通用提示词 |
| `script-to-manga` | 剧本转漫剧提示词（面向"任意 AI 视频模型"） | 稿件结构（通用） | 无 |
| `sd-script-engine` / `sd-overseas-engine` / `sd-jieshuo-engine` / `sd-recon-engine` | 剧本、海外剧、解说、采风 | 文本 | 无（出现模型名只是举例） |
| `sd-decision-engine` | 分镜选型依据（情境映射、景别配比） | 文本决策 | 无（个别条款提到 H3，属举例） |

### B 类：多模型适配层（同一 skill 内含两套以上条款，执行前必须先锁模型）

| skill | 内含哪几套 | 怎么分辨当前用哪套 |
|---|---|---|
| `short-drama-director`（总控） | Seedance 2.5 / 2.0 / MiniMax H3 / 即梦、可灵（举例） | 总控 SKILL.md 〇节「锁系统」A·模型版本，锁定后全局按该适配器 |
| `sd-qc-engine` | Seedance 侧 C1~C26（2.0 段 ≤15s、2.5 段 ≤30s）+ H3 支线 H1~H12（硬区间 4–15s） | 机检 `validate_prompt.py --model 2.5 / 2.0 / h3` |
| `sd-feed-engine`（投喂层） | 七段式（Seedance）/ H3 六段式 | 锁 **A·模型版本** 三选一；段式权威在总控 `model-adapters.md` / `h3-adapter.md` |
| `novel-storyboard`（分镜层） | 段→分镜→关键帧结构通用；**每段默认产一条 H3 稿**（英文，可切中文） | 分镜结构任何模型都能用；投 H3 之外模型时必须换适配器重写段稿 |
| `sd-combat-engine` | 打斗设计通用；落稿含 Seedance 口径为主 | 设计层通用，交付层按锁定模型改写 |
| `sd-asset-engine` | 资产三清单通用；提示词含 H3/Seedance/即梦混用 | 资产层通用，出图提示词按目标生图模型重写 |
| `short-drama-produce` | 生产执行，含 H3、Seedance 两条 | 按任务声明的模型走 |

### C 类：单模型专用（换模型即整套失效）

| skill | 绑哪个模型 | 绑死的证据 |
|---|---|---|
| `h3-prompt-writing` | MiniMax H3（T2VA/I2VA/FL2VA） | 正文 10 处 H3、只有 H3 的字段体系 |
| `h3-video-prompting` | MiniMax H3 / Hailuo 3（H3、Hailuo 03、H3 Max） | 23 份 references、176 处 H3 提及 |
| `minimax-h3` | MiniMax H3（ComfyUI 远端实例执行） | 29 处 H3、5 处 ComfyUI |
| `qwen3-tts` | Qwen TTS（音频）；兼作 H3 配音链路 | 8 处 qwen、11 处 H3 |
| `comfyui` | 本地执行容器（可跑 H3/Seedance/Seedream/Qwen/可灵/Veo） | 61 处 ComfyUI；本身不锁模型，锁的是**跑哪个工作流** |

> 本机未安装、且与 H3 链路不通用的两条单模型条目（2.5 视频引擎、Seedream 5.0 生图引擎）已从本表移除：换模型时用对应模型自带的 skill，本表不再维护这两个名字。

## 三、跨模型失效条款表（换模型前逐条查）

| 条款名 | 具体内容 | 出处 | 换到哪失效 | 取代者 / 处置 |
|---|---|---|---|---|
| **H3 六段式台词块** | 台词必须进 `<d>` 块、逐镜换行、`[Shot k]` 标切点 | `sd-feed-engine/SKILL.md` 契约 §2；`novel-storyboard/references/h3-prompt.md` | 换 Seedance | 用七段式（总控 `model-adapters.md`）；段稿整套重写，不许只改字段名 |
| **H3 段长 4–15 秒硬区间** | 单段低于 4 秒或高于 15 秒直接判不合规（机检 H1~H12） | `sd-qc-engine/references/machine-check-manual.md` L24–L27 | 换 Seedance 2.5 | 2.5 段上限 **30 秒**，走 C1~C26 口径 |
| **15 秒分段硬脚本** | Seedance 2.0 段 ≤15 秒硬门；`validate_seedance_segment_map.py` 硬编码 15 秒 | `sd-qc-engine/references/editing-transition-gate.md` L34–L36 | 换 Seedance 2.5 | 2.5 走总控 C1 口径；**禁止**用该脚本校验 2.5 的 30 秒分段图 |
| **`[SFX:]` 音效标记开关** | 2.5 建议使用、**2.0 禁用**，并连带禁顿挫词 | `sd-qc-engine/references/sound-design-template.md` L33 | 换 2.0 或 H3 | 2.0 去掉 `[SFX:]` 与顿挫词；H3 改用 soundscape/music 分层写法 |
| **H3 声音分层禁台词** | soundscape/music 段**不得含** `<d>` 台词、BGM 段不得复述台词、画外声必跟闭口证据（H9/H10） | 同上 L37 | 换 Seedance | 按 Seedance 音效标记体系重写，不套 H3 分层 |
| **H3 不出画面内字幕条** | H3 生成稿一律不带画面内字幕，靠后期压制 | `subtitle-timing-checker/SKILL.md` L45 | 换生成内嵌字幕的模型 | 先定字幕是生成内嵌还是后期压制，再定字幕校验时点 |
| **字数与图数平台上限** | 字数上限、引用图数上限都属平台参数，投喂闸门按模型卡 | `sd-feed-engine` 闸门 3、闸门 5 | 换任何模型 | 按新模型重设上限，旧上限不得沿用 |
| **素材形态 M0/M1/M2** | 「本包不持有图」契约：M1 编号占位、禁止索要图片 | `sd-feed-engine` 契约 §8 | 换到参考图驱动工作流 | 参考图驱动模式下必须挂图，M1 编号占位会交一份跑不了的稿 |

## 四、换模型的三步口径

1. **先锁模型**：确定模型版本，写进项目状态 `.qc-state.json`（`init` 时一并记录），后续所有分支按它走。
2. **只换两层**：投喂层（段式/字段）与执行层（调用哪个 skill）换掉；**校验层（A 类）全部保留不动**。
3. **查失效表**：上表 8 条逐条确认，命中就按"取代者"改，并把命中项记进报告「缺口与人工复核位」。

**禁止**：
- 禁止把 H3 六段式套到 Seedance 稿上只改字段名（结构不同，等于交废稿）。
- 禁止用 15 秒脚本校验 2.5 的 30 秒分段。
- 禁止因为本机没装某个 H3 系 skill 就把整份质检判不通过——按清单内的可执行校验器 + 人工复核位照常判。
