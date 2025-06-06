---
title: バックエンドのボトルネックが発生しない設計になっているか？
layer: [Structure, DeepDive]
category: パフォーマンス・スケーラビリティ
tags: [backend, throughput, system-limits]
bloom_level: Analyze
license: MIT
---

# バックエンドのボトルネックが発生しない設計になっているか？

> Type: Structure, DeepDive  
> Category: パフォーマンス・スケーラビリティ  
> Audience: 設計リーダー / SRE / インフラ設計者 / レビュー担当者

---

## 背景・概要

パフォーマンス劣化や障害の多くは、DB・API・キューなどのバックエンドのボトルネックが原因

処理分離、非同期化、キューイング、負荷分散を活用することでこれを回避可能

---

## 例

- 一括アップロード処理を同期APIではなくバッチ処理に分離
- ドキュメントの登録をPub/Sub・Amazon SNS/SQS・Azure Service Bus経由で非同期化し、API負荷と切り離し
- Cloud Tasks・Amazon SQS + Lambda（AWS）・Azure Queue Storage + Functionsでワーカー数を動的に調整できるよう設計

---

## よくある失敗例

- 画像処理やPDF生成などの重たい処理をリクエスト内に含め、タイムアウト
- N+1クエリが原因で1テナントの利用で全体に影響
- バックグラウンド処理をただのスレッドで実装し、Worker障害時の再実行が不能

---

## FAQ

**Q. どこがボトルネックになるか分からない**

A. 想定ケースを書き出し、SplunkなどのプロファイラやAPMで可視化すべき。まずは重い処理、同期化されたI/Oを疑う

**Q. スレッド実行とキューの違いは？**

A. スレッドは同一プロセス内で処理され高速だが、**失敗時の再試行や監視が困難で信頼性に欠ける**。キューは処理を外部化し、失敗時の再送・監視・耐障害性に優れる

---

## 関連観点

- [外部サービスの負荷増大時の影響を最小限にするための設計があるか？](https://zenn.dev/kanaria007/articles/a3b0bd840de61a)
- [キャッシュ戦略が適切に考慮されているか？](https://zenn.dev/kanaria007/articles/f2b137ea3cd959)
- [API のレスポンス時間が適切か？](https://zenn.dev/kanaria007/articles/bd9c05cf6b60ae)
