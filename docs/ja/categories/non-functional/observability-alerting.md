---
title: 監視対象が適切に設計され、異常時の通知が設定されているか？
layer: [Structure, DeepDive]
category: 非機能要件・運用
tags: [observability, alerting, monitoring]
bloom_level: Apply
license: MIT
---

# 監視対象が適切に設計され、異常時の通知が設定されているか？

> Type: Structure, DeepDive  
> Category: 非機能要件・運用
> Audience: 設計リーダー / SRE / インフラ設計者 / レビュー担当者

---

## 背景・概要

障害の兆候を早期に察知するには、**設計時点での監視ポイント定義**が極めて重要

リトライ回数、エラーレート、レスポンス遅延、CPU使用率など、「どこを見れば異常がわかるか？」を明確にし、通知基準と通知先まで決めておく

---

## 例

- キューサイズが一定以上に膨らんだらSlack通知されるよう監視設定
- Cloud Logging（GCP）・CloudWatch Logs（AWS）・Azure Monitor Logsなどのエラーログが特定条件を満たすとPagerDutyへ連携
- 重要APIの99パーセンタイルのレスポンスタイムを監視ダッシュボードで可視化

---

## よくある失敗例

- 障害は起きていたが、通知が来ずユーザー報告で発覚
- 通知は来たが誤検知が多く、アラート疲れで無視されていた
- アラートがAPI単位でなくインフラ単位でしか取れず、原因調査に時間がかかる

---

## FAQ

**Q. どのレイヤーを監視すべき？**

A. インフラ（CPU/メモリ）、アプリケーション（エラーレート）、ビジネス（処理件数の異常）など、複数レイヤーを俯瞰してカバーすべき

**Q. 通知先はどう決める？**

A. システムの重要度・担当範囲に応じてSlack/メール/インシデント管理ツール(例:PagerDuty)などを使い分ける。自動化できる運用フローが望ましい

---

## 関連観点

- [障害発生時のリカバリ手順が整理されているか？](https://zenn.dev/kanaria007/articles/877af2e2d38b24)
- [重要な処理において、フェイルオーバー設計が組み込まれているか？](https://zenn.dev/kanaria007/articles/ad9366091c2b4d)
- [障害時のデータ復旧手順が考慮されているか？](https://zenn.dev/kanaria007/articles/2afe288e82b98f)
