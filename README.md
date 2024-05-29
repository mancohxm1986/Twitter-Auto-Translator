# 推特自动翻译发布插件

这是一个推特自动翻译发布插件，能够自动获取指定的推特账号最新推文，翻译成中文并发布到你的推特账号上。该插件提供一个简单的前端页面，用于配置 API 凭证、目标账号和自动化任务设置。

## 功能
- 获取指定推特账号的最新推文
- 翻译推文为中文
- 发布翻译后的推文到用户自己的推特账号
- 提供前端配置页面
- 支持自动化任务设置

## 目录结构
```plaintext
.
├── .github
│   └── workflows
│       └── tweet.yml
├── templates
│   └── index.html
├── config.json
└── main.py
```

## 前置条件
- Python 3.x
- Twitter API 凭证
- GitHub 账号

## 安装与配置

1. 克隆代码仓库：
    ```bash
    git clone https://github.com/your_username/twitter-auto-translator.git
    cd twitter-auto-translator
    ```

2. 安装依赖：
    ```bash
    pip install tweepy googletrans==4.0.0-rc1 flask
    ```

3. 配置 Twitter API 凭证和目标账号：
    - 打开 `config.json` 文件，填写 Twitter API 凭证和目标账号信息：
    ```json
    {
        "CONSUMER_KEY": "your_consumer_key",
        "CONSUMER_SECRET": "your_consumer_secret",
        "ACCESS_TOKEN": "your_access_token",
        "ACCESS_TOKEN_SECRET": "your_access_token_secret",
        "TARGET_ACCOUNT": "target_account",
        "CRON_SCHEDULE": "0 0 * * *"
    }
    ```

## 使用方法

1. 运行 Flask 应用，打开前端配置页面：
    ```bash
    python main.py
    ```

2. 在浏览器中访问 `http://127.0.0.1:5000`，填写并保存配置。

3. 手动运行脚本：
    ```bash
    python main.py
    ```

4. 配置 GitHub Actions 实现自动化任务：
    - 在 `.github/workflows/tweet.yml` 文件中，确保 `CRON_SCHEDULE` 设置正确。

## 贡献
欢迎提出问题和拉取请求。如果有重大更改，请先打开问题讨论你想做的更改。

## 许可证
[MIT](https://choosealicense.com/licenses/mit/)
