# 企业微信机器人消息发送 Action

How to use:
```
- name: wecom robot action
uses: guangzhengli/wecom-notification-action@main
with:
  webhook: ${{ secrets.WECOM_WEBHOOK_KEY}}
  is_at_all: 'false'
  message: test content
```