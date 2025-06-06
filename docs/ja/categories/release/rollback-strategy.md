---
title: ロールバック手順が用意されているか？
layer: [DeepDive]
category: リリース・ロールバック
tags: [rollback, failure-handling, deployment]
bloom_level: Analyze
license: MIT
---

# ロールバック手順が用意されているか？

> Type: DeepDive  
> Category: リリース・ロールバック  
> Audience: 設計リーダー / SRE / インフラ設計者 / レビュー担当者

---

## 背景・概要

本番での問題発生時、**即時に元の状態に戻せる手順（ロールバック）があるかどうか**はサービス信頼性(SLA)の鍵になる

ゼロから作業するのではなく、**事前に自動化・手順化されたロールバック設計をすべき**

---

## 例

- コンテナ実行基盤（例：Cloud Run, AWS App Runner, Azure Container Apps）でリビジョン機能を活用し、トラフィックを旧バージョンへ即時切り替え可能にする
- DBマイグレーションは 巻き戻し可能な設計で、rollback.sql を事前用意
- ロールバック実施後の影響範囲（ログ・通知・ユーザー影響）も明記

---

## よくある失敗例

- リリース直後に問題発覚したが、旧バージョンに戻す方法が用意されておらず対応に数時間
- DBスキーマ変更後にエラーが出たが、差分リカバリ用SQLがなく、巻き戻しできなかった
- 機能フラグだけ戻してUIが非対応のままで混乱

---

## FAQ

**Q. ロールバックは毎回必要？**

A. ケースバイケースだが**重要機能・スキーマ変更・外部連携がある機能は必ず用意すべき**。軽微なUI修正などの場合は不要という判断もあり得る

**Q. 巻き戻せないDB変更はどう扱う？**

A. バックアップ取得・二重書き込み・非破壊変更などでリスクを下げる設計が必要

---

## 関連観点

- [破壊的変更を避けるための互換性保持の設計がされているか？](https://zenn.dev/kanaria007/articles/e36029117ba81b)
- [システム停止が必要な場合、最小限に抑えられるように計画されているか？](https://zenn.dev/kanaria007/articles/bc767346d55ab2)
- [重大な変更に対する影響分析が適切に行われているか？](https://zenn.dev/kanaria007/articles/a2ea5e205100b8)
