# 人话 · Plain Voice

面向中文自媒体的创作与编辑 Skill。支持有稿轻改、重构、诊断、查错字与无稿共创。

保留六类严格表达规则：说教、假顿悟、模板反转、口号升华、抽象词组合、机械结构。保护原意与事实；明确笔误直接修复，可能改义的错字先确认。

当前版本 **0.3.0，预发布**。格式及辅助脚本已进行本地检查；跨模型创作行为尚未验收。不判断文字是不是 AI 写的，不保证流量，不承诺“零 AI 味”。

## 安装：和普通 Skill 一样

在要写稿的项目文件夹中打开终端，执行：

```bash
npx skills add YOUR-ACCOUNT/plain-voice
```

按提示选择正在使用的 AI 工具，安装到当前项目即可。之后在该工具中打开这个项目使用。需要电脑已安装 Node.js，首次安装需要联网。`YOUR-ACCOUNT` 是待替换的 GitHub 账号；仓库尚未发布，这条仓库命令目前是发布模板。

需要在所选工具的所有项目使用时，加 `--global`：

```bash
npx skills add YOUR-ACCOUNT/plain-voice --global
```

本地已有本项目时，安装源换成本地文件夹：

```powershell
npx skills add "E:\Projects\plain-voice"
```

命令使用开源 [Skills CLI](https://github.com/vercel-labs/skills)，支持选择 Codex、Claude Code 等工具。不要照抄其他项目的名称。此项目的 CLI 安装流程尚未实测。

### 不用命令：手动复制

从 GitHub 的 **Code → Download ZIP** 下载并解压，将 `SKILL.md` 放到创作项目的对应位置：

| 工具 | 项目内位置 | 调用 |
| --- | --- | --- |
| Codex | `.agents/skills/plain-voice/SKILL.md` | `$plain-voice` |
| Claude Code | `.claude/skills/plain-voice/SKILL.md` | `/plain-voice` |

已有同名技能时先备份再替换。安装后重新打开项目或刷新技能列表。

WorkBuddy 等提供技能导入入口的平台，按其入口导入 `dist/plain-voice-skill-0.3.0.zip`；具体支持以当前客户端为准。豆包等未提供 Skill 安装入口的聊天工具，复制 `prompts/universal.txt` 到新对话再发任务。

核心规则不需要 Python、API Key 或 RAG。Python 安装脚本及详细平台说明放在 [备用安装说明](docs/INSTALL-ADVANCED.md)，普通用户无需运行。

安装只需选择工具与安装范围；不需要部署网站、启动服务或配置数据库。只适用于支持 Skills 的宿主，其他聊天平台使用通用提示词。

## 怎么使用

| 模式 | 示例 |
|---|---|
| 轻改 | 轻改这条口播，保留观点与冷幽默，不新增事实。 |
| 重构 | 重构这篇图文，允许调整顺序，列出关键结构变化。 |
| 诊断 | 只指出六类表达问题，先不改全文。 |
| 查错字 | 只查错字；明显笔误直接修，影响意思的地方向我确认。 |
| 无稿共创 | 想写关于工作边界的口播，没有亲历故事，先给三个角度。 |

可补充：用途、受众、必留信息、修改力度、喜欢的表达样例。无需每次填全；已有上下文就继续工作。默认有稿轻改，无稿补必要创作依据。需要保留引用或专名时明确说明。

## VS Code 中使用

1. **文件 → 打开文件夹**，选择此项目。或在终端运行 `code E:\Projects\plain-voice`（需安装 `code` 命令）。
2. 打开 Markdown 文件，按 `Ctrl+Shift+V` 预览文档。
3. 安装到创作项目后，通过已安装、已登录的 Codex／Claude Code 工具调用。VS Code 单独打开文本不会执行模型。
4. `.vscode/tasks.json` 提供验证与打包任务，可在“终端 → 运行任务”使用；它们检查／打包文件，不自动生成文案。

Codex 的 IDE 扩展见 [官方说明](https://learn.chatgpt.com/docs/codex/ide)。模型使用遵循宿主账户权限和费用，Skill 不自带模型。

## 测试与限制

```bash
python scripts/validate.py
python -m unittest discover -s tests -v
python scripts/lint_text.py examples/sample.txt
python scripts/package.py
```

词汇扫描是人工审核线索：不自动改文、不检测同义绕行、不理解引用是否适用、不验证原意或事实。行为用例及模型记录见 `evals/`。基线是同模型下普通提示词，比较完整时间、原意保护、事实保护、改动采纳及歧义处理。每次在新会话运行，避免项目作者上下文掩盖规则缺口。

## 发布与贡献

发布步骤见 [发布说明](docs/PUBLISHING.md)，改规则及反馈要求见 [贡献说明](CONTRIBUTING.md)。[MIT License](LICENSE) 允许复用本项目规则与代码；不授予宿主模型或第三方内容的权利。

## 0.3.0：从词表到全文检查

保留六类禁令，增加重复解释、机械对称、潜台词翻译、空结尾等全文检查。单个常见词不自动判错；叙事留白不会用于删减教程步骤。设计来源、边界、示例见 [设计说明](docs/DESIGN.md)。新增八个行为评估案例待执行。
