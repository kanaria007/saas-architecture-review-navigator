---
title: イベントのリトライ設計と遅延の影響が考慮されているか？
layer: [Structure, DeepDive]
category: イベント・非同期処理
tags: [リトライ戦略, バックオフ, イベント処理]
bloom_level: Analyze
license: MIT
---

# 非同期イベントの遅延やリトライ処理の影響を考慮した設計になっているか？

> Type: Structure, DeepDive  
> Category: Async  
> Audience: Engineers building event-driven systems, workflows, or async pipelines

---

## 背景・概要

非同期イベントの**遅延・リトライ・重複発生**は、システム運行で必然的に発生するものであり、あらかじめ業務影響を想定しておく必要がある

---

## 例

- メール送信を10分遅延しても業務に支障がないと設計に明記
- 同一イベントが複数回届いても安全な冪等処理を設計する
- Google Cloud Task・AWS SQS / Step Functions・ Azure Queue / Durable Functionsのリトライポリシー（最大試行回数、間隔など）を考慮

---

## よくある失敗例

- リトライ時に二重処理が行われ、二重請求や二重登録になる
- キュー詰まりで処理遅延し、ユーザーへ通知が届かない
- 冪等設計されておらず、失敗後のリカバリでバグが発生

---

## FAQ

**Q. イベント系の処理の冪等性ってどう担保する？**

A. **一意のイベントIDを記録して処理済みか判定する**、または「Insert if not exists」のような排他制御で回避する

**Q. 遅延の許容範囲ってどう決める？**

A. ユーザー体験や業務フローと照らし、**具体的な秒数・分単位で関係者と合意を取るとよい**（例：通知は30秒以内など）

---

## 関連観点

- [サービス間のデータ整合性が保証されているか？](https://zenn.dev/kanaria007/articles/b97134137d3316)
- [同期・非同期の設計方針が妥当で、業務要件を満たしているか？](https://zenn.dev/kanaria007/articles/a5ebb695385877)
