---
title: APIスキーマがシステム全体で一貫しているか？
layer: [Structure]
category: API・権限・セキュリティ
tags: [スキーマ整合性, スキーマ進化, フロント連携]
bloom_level: Apply
license: MIT
---

# API のスキーマが適切に設計され、他の API との整合性があるか？

> Type: Structure  
> Category: API・権限・セキュリティ  
> Audience: 設計初心者 / 設計中のチーム / レビュワー

---

## 背景・概要

APIスキーマは他チーム・他システムとの契約であり後から変更しづらい、**整合性の乱れは連鎖的な障害や運用コストの増大を招く**

特に共通的なエンティティの表現（User, Taskなど）に関しては、**プロジェクト横断で整合性を保つことが重要**

---

## 例

- 共通項目（id, status, created_at）の命名・型を統一
- 内部のEnum/値オブジェクトの表現をAPIでも可能な限り一致させる
- 適切にネストされた構造体や、REST風のURL設計（/users/{id}/tasks）をする。後者はgRPCで不要になるかも

---

## よくある失敗例

- 同じ意味のフィールドuser_uuidとuidなどが混在
- スキーマが内製的すぎてAPI利用者が実装を読まないと理解できない
- 外部向けAPIに内部設計がそのままが露出していて、リファクタが困難

---

## FAQ

**Q. 内部モデルとAPIスキーマの設計は分けるべき？**

A. 基本的には分けるべき。ただし外部入出力用のDTOを設けて必要に応じてアダプター層を用意してマッピングするとよい

**Q. 他チームのAPIと整合性がとれていない場合は？**

A. 必要に応じてAdapterパターンやMapper/TranslatorなどによるDTO <–> Domainの変換器で吸収すればよいが、長期的には統一を検討すべき

---

## 関連観点

- [破壊的変更を避けるための互換性保持の設計がされているか？](https://zenn.dev/kanaria007/articles/e36029117ba81b)
- [APIの権限管理が適切に設計されているか？](https://zenn.dev/kanaria007/articles/03fb36eb3d41f3)
- [変更の影響範囲が整理され、必要なコンポーネントの再利用が考慮されているか？](https://zenn.dev/kanaria007/articles/95f9d91567a9ee)
- [影響範囲が適切に分析されているか？](https://zenn.dev/kanaria007/articles/889dbfe28a793e)
