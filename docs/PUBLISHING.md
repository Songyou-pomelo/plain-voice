# GitHub 发布步骤

本地目录准备完毕后，在 GitHub 创建空仓库 `plain-voice`。将实际账户和仓库地址替换到 README；没有创建前不提供虚构可用下载链接。

```bash
git init
git add .
git commit -m "Add Plain Voice skill v0.3.0"
git branch -M main
git remote add origin https://github.com/YOUR-ACCOUNT/plain-voice.git
git push -u origin main
```

以上操作由仓库拥有者执行，本次未推送。准备发布时运行验证、单元测试和打包；GitHub Release 标记预发布，版本 `v0.3.0`，附件使用 `dist/plain-voice-skill-0.3.0.zip`。Release 说明必须标记哪些模型已测、哪些未测。

后续流程：记录失败→调整规则→回归事实保护与术语例外→重新生成粘贴版→更新版本与日志→打包发布。修改 SKILL.md 后，将正文同步到 prompts/universal.txt；验证会检查二者一致。
