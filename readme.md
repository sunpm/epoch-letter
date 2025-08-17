# 流年之书 (EpochLetter) 📮

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

一个基于 GitHub Actions 的零成本、去中心化时间胶囊服务。为你封存今日的思绪，寄给未来的自己。

---

## 📖 项目简介 (About)

**流年之书 (EpochLetter)** 是一个独特的项目，它允许您向未来的自己发送邮件。不同于中心化的网站服务，ChronoPost 采用了一种完全去中心化的模式，充分利用了 GitHub 生态系统。

您只需要 Fork 这个项目，它就会在您自己的仓库中，成为一个只属于您的、完全独立的私人时间胶囊服务。所有的数据（您的信件内容、邮箱地址）都安全地存放在您自己的仓库中，由您完全掌控。

这一切都运行在 GitHub Actions 的免费额度上，真正实现了**零成本**运行。

## ✨ 核心特性 (Features)

- **💌 完全免费**: 无需服务器，无需付费，所有功能均基于 GitHub 的免费服务。
- **🔐 数据主权**: 您的所有信件和私人信息都存储在您自己的 GitHub 仓库中，绝不外泄。
- **🚀 高度自动化**: “Git Push 即 API”。您只需修改一个文件并推送，剩下的交给 GitHub Actions。
- **🎨 个性化展示**: 每个 Fork 的项目都可以拥有自己的 GitHub Pages 展示墙，展示您想公开的信件。
- **🔧 易于部署**: 只需三步（Fork -> 配置密钥 -> 修改文件），即可拥有自己的时间胶囊服务。

## 📺 视频教程地址

[Youtube](https://www.youtube.com/watch?v=X8DjOHr0D84)

[Bilibili](https://www.bilibili.com/video/BV1XyYrzuEJY)

## 快速上手 (Getting Started)

只需简单几步，即可启动您的流年之书。

### 1. 配置 Resend

您需要一个免费的 Resend API Key 来发送邮件。

前往 [Resend](https://resend.com/) 自行查阅相关教程。

### 2. Fork 本项目

- 点击本仓库页面右上角的 **Fork** 按钮。
- Settings->Secrets and variables->Actions->New repository secret
  添加 RESEND_API_KEY 和 RESEND_FROM 两个密钥
- 如果需要展示时间胶囊：Settings->Pages->Build and deployment->Source: GitHub Actions

### 3. 添加你的第一个时间胶囊

克隆您自己的 Fork 仓库到本地，然后编辑 `_data/capsules.yml` 文件，添加您的第一条内容：

```yaml
- content: "你好，世界！

    这是我的第一个未来胶囊测试。

    "
  delivery_date: "2025-08-11" # 请修改为您的目标日期
  display_on_fork: false # 是否在您的展示墙上展示
  email: test@gmail.com # 请修改为您的邮箱地址
  id: 1
  status: scheduled
  subject: 一封测试邮件 # 邮件主题
```

## 欢迎关注我

> [!IMPORTANT]  
> 关注公众号获取教程，后续有更新会第一时间在公众号里发布。

![码道禅心](images/码道禅心.png)

## 捐赠

如果你觉得本项目帮助了你，请作者喝一杯咖啡，你的支持是作者最大的动力。

| 微信支付                                                              | 支付宝支付                                                              |
| --------------------------------------------------------------------- | ----------------------------------------------------------------------- |
| <div align="center"><img src="images/微信收款.png" width="50%"></div> | <div align="center"><img src="images/支付宝收款.jpg" width="50%"></div> |
