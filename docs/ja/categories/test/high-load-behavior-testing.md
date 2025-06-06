---
title: 高負荷時の挙動を確認する負荷テストが計画されているか？
layer: [DeepDive]
category: テスト
tags: [負荷試験, スケーラビリティ, テスト計画]
bloom_level: Evaluate
license: MIT
---

# 高負荷時の挙動を確認する負荷テストが計画されているか？

> Type: DeepDive  
> Category: テスト  
> Audience: 設計リーダー / SRE / インフラ設計者 / レビュー担当者

---

## 背景・概要

本番リリース後に高負荷で障害が発覚するケースは多く、特にバッチやイベント駆動システムでは負荷ピークの想定が難しい

**ピーク時アクセス・大量データ処理・スケール境界を意識した負荷テスト**を設計段階で計画しておくことで事前の品質担保につながる

---

## 例

- 通常10件/秒の処理に対して、30件/秒・60件/秒での耐久テストを事前実施
- 定時バッチが走る時間帯にリクエストを集中させて、DBのスロークエリを計測
- マネージドなコンテナ実行環境（例：GCP Cloud Run、AWS Fargate、Azure Container Apps）で、CPUスケーリングが期待通りに動作するかを負荷試験ツール（Gatling, Locust, k6 など）で検証

---

## よくある失敗例

- 通常のテストは通ったが、同時リクエスト100件でタイムアウト・高負荷により失敗
- スレッドプール数やDB接続数が制限に達し、全体が遅延
- テスト環境と本番でスケーラビリティ設定が異なっており、想定外の挙動

---

## FAQ

**Q. 負荷テストはいつ実施する？**

A. 本番リリース直前ではなく、**設計段階で「どの機能に負荷テストが必要か」を決めておくことが重要**。開発終盤で入れるのはリスクが高く、何かあるとリリースにはまず間に合わない

**Q. テスト対象はどこまで広げる？**

A. 通信系（API/Queue）だけでなく、**DB・バッチ・Pub/Sub・ログ出力なども含めた総合的な観点が必要**

---

## 関連観点

- [表示データ量が適切に制限されており、パフォーマンスが考慮されているか？](https://zenn.dev/kanaria007/articles/b7676e3c4c15dc)
- [API のレスポンス時間が適切か？](https://zenn.dev/kanaria007/articles/bd9c05cf6b60ae)
