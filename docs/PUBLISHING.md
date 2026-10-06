# GitHub 发布步骤

仓库：[Songyou-pomelo/plain-voice](https://github.com/Songyou-pomelo/plain-voice)。已有仓库的后续更新使用 `git add`、`git commit` 和 `git push`；不重复创建仓库。以下初始化命令仅供首次配置参考。

```bash
git init
git add .
git commit -m "Add Plain Voice skill v0.3.0"
git branch -M main
git remote add origin https://github.com/Songyou-pomelo/plain-voice.git
git push -u origin main
```

上述初始化步骤只执行一次。准备发布时运行验证、单元测试和打包；GitHub Release 标记预发布，版本 `v0.3.0`，附件使用 `dist/plain-voice-skill-0.3.0.zip`。Release 说明必须标记哪些模型已测、哪些未测。

后续流程：记录失败→调整规则→回归事实保护与术语例外→重新生成粘贴版→更新版本与日志→打包发布。修改 SKILL.md 后，将正文同步到 prompts/universal.txt；验证会检查二者一致。
