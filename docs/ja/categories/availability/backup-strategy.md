---
title: バックアップ戦略が定義されているか？
layer: [Structure, DeepDive]
category: 災害対策・可用性
tags: [backup, fault-tolerance, disaster-recovery]
bloom_level: Apply
license: MIT
---

# バックアップ戦略が整理されているか？

> Type: Structure, DeepDive  
> Category: 災害対策・可用性  
> Audience: 設計リーダー / SRE / インフラ設計者 / レビュー担当者

---

## 背景・概要

障害だけでなく、人為的な誤操作・論理的な破損・データ汚染などのリスクに備えて、**適切な頻度・保持期間・保存先**でバックアップを設計しておくことが必要

復元可能性と運用の実現性の両立が鍵

---

## 例

- Cloud SQL（GCP）／Amazon RDS（AWS）／Azure SQL Databaseなど主要なRDBMSに対し、自動バックアップ設定を有効化し、7日間保持
- 重要なマスターデータは日次スナップショットを取得し、別リージョンに保存
- 分析基盤は永続ストレージ（例：オブジェクトストレージ）へのエクスポート設計を行い、再分析・監査対応を可能にする（例：BigQuery（GCP）→ Cloud Storage、Redshift（AWS）→ S3、Azure Synapse → Blob Storage）

---

## よくある失敗例

- バックアップ設定はあるが、リストアの検証がされておらず復元できなかった
- バックアップファイルが同じリージョンにあり、災害時に同時に失われた
- 保持期間が短すぎて過去のデータが消えていた

---

## FAQ

**Q. フルバックアップと差分バックアップ、どちらが良い？**

A. RTO（復旧時間）重視ならフル、ストレージ節約なら差分で。GCPなどのマネージドサービスなら併用も可能かな

**Q. バックアップ頻度はどれくらい？**

A. データの重要度による。重要データは1時間ごと、普通のデータは日次で十分など用途に応じて決定すべき。コスト💸とパフォーマンスにも影響があるので総合的に判断されたい

---

## 関連観点

- [障害発生時のリカバリ手順が整理されているか？](https://zenn.dev/kanaria007/articles/877af2e2d38b24)
- [障害時のデータ復旧手順が考慮されているか？](https://zenn.dev/kanaria007/articles/2afe288e82b98f)
