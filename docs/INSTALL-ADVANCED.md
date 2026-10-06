# 备用安装与平台说明

## 下载

- 打开 [GitHub 仓库](https://github.com/Songyou-pomelo/plain-voice)，选择 **Code → Download ZIP**，解压后打开项目目录。
- 或使用下面的命令下载：

```bash
git clone https://github.com/Songyou-pomelo/plain-voice.git
cd plain-voice
```

需要技能 ZIP 时，在项目目录运行 `python scripts/package.py`，生成 `dist/plain-voice-skill-0.3.0.zip`。若仓库提供 Release 附件，也可直接下载；源码上传不代表 Release 已发布。

## 安装

Skill 的运行宿主是 AI 工具，`SKILL.md` 本身不是 Python 程序。核心文本无需 Python、API Key、RAG 或第三方依赖；下面的可选安装脚本需要 Python 3.10+。

### Codex：项目级

```powershell
python scripts/install.py --platform codex --project 'E:\Projects\你的内容项目'
```

将核心文件复制到目标项目的 `.agents/skills/plain-voice/`，不会修改其他 Skill，不覆盖已存在同名目录。打开目标项目，在 Codex 中输入：

```text
$plain-voice 轻改下面的口播文案，保留事实和立场，只给稿。
【粘贴原稿】
```

可在 `/skills` 或技能选择入口检查发现情况，必要时重启。实际位置与调用方式见 [Codex 官方技能文档](https://learn.chatgpt.com/docs/build-skills)。

### Claude Code：项目级

```powershell
python scripts/install.py --platform claude --project 'E:\Projects\你的内容项目'
```

文件放在 `.claude/skills/plain-voice/`。在目标项目中启动 Claude Code，调用：

```text
/plain-voice 诊断下面的稿件，先不要全文改写。
【粘贴原稿】
```

见 [Claude Code 官方技能文档](https://code.claude.com/docs/en/skills)。

### WorkBuddy

如果当前版本提供本地 Skill 导入，使用打包后的技能 ZIP／文件夹，按客户端入口导入；不假定不同版本导入入口相同。若没有导入入口，使用下方粘贴方式。安装与使用效果尚未在 WorkBuddy 验收。参考 [WorkBuddy 技能说明](https://www.workbuddy.cn/docs/workbuddy/From-Beginner-to-Expert-Guide/Function-Description/Skills-Market)。

### 豆包、其他聊天工具

打开 `prompts/universal.txt`，复制全部内容到新对话，然后发送任务与原稿。若工具提供自定义指令，可按其长度限制保存规则，但不要截断后声称全规则有效。新对话需重新加载；对话过长或规则失效时重发。这里是提示词使用，不声称原生 Skill 安装成功。

### 手动安装 / macOS / Linux

Python 安装脚本跨平台使用。也可在目标项目中创建对应的技能目录，复制根目录 `SKILL.md`；`agents/openai.yaml` 是可选 Codex 展示元数据。核心是自包含文件，无需复制开发脚本。

脚本拒绝覆盖：更新前备份已有目录，在确认旧目录用途后手动替换；不提供自动递归删除。未执行全局安装，不修改用户主目录。

