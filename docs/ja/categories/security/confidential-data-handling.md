---
title: 機密データの取り扱いにおいて、適切な暗号化やトークナイゼーションが実装されているか？
layer: [DeepDive]
category: API・権限・セキュリティ 
tags: [encryption, tokenization, sensitive-data]
bloom_level: Analyze
license: MIT
---

# 機密データの取り扱いにおいて、適切な暗号化やトークナイゼーションが実装されているか？

> Type: DeepDive  
> Category: API・権限・セキュリティ  
> Audience: 設計リーダー / SRE / インフラ設計者 / レビュー担当者

---

## 背景・概要

個人情報や請求情報などの機密データを扱う場合、**漏洩しても意味をなさないように**するのが最低限のセキュリティラインになる

保存時（at rest）・送信時（in transit）の暗号化、場合によってはトークン化も必要

GDPRやISMSなどの外部要件を満たす上でも必須になる

---

## 例

- データベース上ではメールアドレスや銀行口座をAES256で暗号化し保存
- 社内の一部システムからも復号不要なため、ランダムな一方向ハッシュでトークナイズ
- Cloud KMS・AWS KMS・Key Vaultで暗号鍵を管理し、権限管理・ローテーションを自動化

---

## よくある失敗例

- 暗号化されているが鍵がソースコードにハードコードされている
- HTTP通信で送信されており、in-transitの暗号化が不十分
- 暗号化はされているが、データベースバックアップから復元できる構造で漏洩リスクが残存

---

## FAQ

**Q. 暗号化とトークナイゼーションの違いは？**

A. 暗号化は復号可能。トークナイゼーションは元データとの対応表（マッピング）を保持する構造で復号不要なケースに使う

**Q. Cloud プロバイダ(GCP、AWS、Azureなど)が暗号化してるならアプリ側は不要？**

A. 自動で暗号化してくれるのは便利だがアプリケーション層での暗号化（カスタム鍵管理）も求められるケースはあるかな

- テナントごとに暗号鍵を分けたい
- CS担当者は名前と電話番号だけ見られるが、銀行口座や金額は見られないなど、のカラム単位での復号制御

---

## 関連観点

- [セキュリティリスク（機密データの取り扱い、認証・認可）が考慮されているか？](https://zenn.dev/kanaria007/articles/cb4a6fe7106f2a)
- [API の認証・認可が適切に実装されているか？](https://zenn.dev/kanaria007/articles/a53418ef47c504)
- [ログの記録方法が適切であり、トラブルシューティングに必要な情報が取得できるか？](https://zenn.dev/kanaria007/articles/a19bf86edf5798)
