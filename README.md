# 企业微信机器人消息发送 Action

[![GitHub issues](https://img.shields.io/github/issues/guangzhengli/wecom-notification-action)](https://github.com/guangzhengli/wecom-notification-action/issues)
[![GitHub forks](https://img.shields.io/github/forks/guangzhengli/wecom-notification-action)](https://github.com/guangzhengli/wecom-notification-action/network)
[![GitHub stars](https://img.shields.io/github/stars/guangzhengli/wecom-notification-action)](https://github.com/guangzhengli/wecom-notification-action/stargazers)
[![GitHub license](https://img.shields.io/github/license/guangzhengli/wecom-notification-action)](https://github.com/guangzhengli/wecom-notification-action/blob/main/LICENSE)

## 基础用法
使用 `wecom-notification-action` 定时发送固定消息到企业微信机器人，使用方法如下所示：
```yml
name: wecom/wechat-work robot notification action

on:
  schedule:
    - cron:  '0 0 * * *'

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout
        uses: actions/checkout@v2
      - name: wecom robot action
        uses: guangzhengli/wecom-notification-action@main
        with:
          webhook: ${{ secrets.WECOM_WEBHOOK_KEY}}
          is_at_all: "false"
          type: "message"
          message: "test content"
```
首先按照 GitHub action 基本配置方法，可以自定义 name 和 on，分别是 action 名称和触发条件，例如上面 `on:schedule` 表示使用 cron 定时。具体细节可以查看 [github actions onschedule](https://docs.github.com/en/actions/using-workflows/workflow-syntax-for-github-actions#onschedule)。

`robot notification action` 字段定义如下所示：
* webhook: 企业微信机器人 webhook url key, 在创建企业微信机器人后，可以得到 Webhook URL: webhook/send?key=xxx, 那么字段配置为xxx即可,例如 0xxxxxxx-0000-1111-2222-fexxxxxxxxx。这里为保护自己的 key，可以将 key 放置在 [github secret](https://docs.github.com/en/actions/security-guides/encrypted-secrets) 中。即 `Settings` -> `Secrets` -> `Actions` -> `Repository secrets`。
* is_at_all: false/true。是否 @all @所有人。
* type: 默认为 message，代表为固定消息发送。
* message: 如果 type 选择 message, 则必须加上需要发送的内容，例如上面会发送内容 `test content`。

## 高级用法
发送固定的消息并不能满足大多数人的需求，绝大多数人使用机器人还是想要一些自动化的功能，例如定时提醒和我主要想实现的循环提醒等功能。

例如使用下面这个 action 表示的功能为，默认在每天 UTC 00:00 时，读取根目录下文件名为 `members.txt` 文件第一行内容，发送给企业微信机器人，并且将第一行内容放置最后一行，做到循环提醒的功能，每天提醒的功能都可以自己自定义。

```yml
name: wecom/wechat-work robot notification action

on:
  schedule:
    - cron:  '0 0 * * *'

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout
        uses: actions/checkout@v2
      - name: wecom robot action
        uses: guangzhengli/wecom-notification-action@main
        with:
          webhook: ${{ secrets.WECOM_WEBHOOK_KEY}}
          is_at_all: "false"
          type: "file"
          file_name: "members.txt"
          file_read_type: "first"
          file_write_type: "loop"
```

上面例子中字段意思如下所示：
* type: file 表示消息从文件当中读取。
* file_name: 文件名字，如上所示读取根目录下 `members.txt` 文件，默认读取第一行。
* file_read_type: 默认是 first 读取第一行, 可以定义为这几个属性，first:第一行; random:随意一行; all:所有内容
* file_write_type: 默认是 loop 循环写，意思为读取完成后, 是否进行写操作, loop:循环, 第一行放置最后一行; delete:删除, nothing:不操作。

## 更多用法
目前这个 action 是为了满足我的功能需求设计，可能并不是特别通用，如果你有好的设计，可以在 [Issue](https://github.com/guangzhengli/wecom-notification-action/issues) 或者 [Discussions](https://github.com/guangzhengli/wecom-notification-action/discussions) 中提出，争取把这个设计为更通用的 action，谢谢。