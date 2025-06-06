---
title: パフォーマンステストの実施有無が決定されているか？
layer: [Structure]
category: テスト
tags: [性能試験, 非機能要件, スロークエリ]
bloom_level: Apply
license: MIT
---

# パフォーマンステストの実施有無が決定されているか？

> Type: Structure  
> Category: テスト  
> Audience: 設計初心者 / 設計中のチーム / レビュワー

---

## 背景・概要

パフォーマンス劣化はユーザー離脱やSLA違反の原因になる

**設計段階でボトルネックが疑われる箇所は早期に負荷検証の計画を立てるべき**

---

## 例

- ドキュメント一覧画面で月次数万件超のドキュメントが表示されるため、DBインデックスの確認と性能試験を計画する
- 書き込みバッチが1日10万件のデータ更新を行うため、**更新処理のロック/排他/キュー戦略**に対して性能計測を行う
- 新たに外部APIとの連携が増えたため、APIレスポンスタイム測定とキャッシュの導入を検討する

---

## よくある失敗例

- 本番導入後に初めて遅延が発覚し、DB負荷が原因とわかる
- パフォーマンステストが未実施で、非同期バッチが日をまたいで失敗する
- AWSやGCPのスロットリング制限に引っかかって想定外の再試行が多発

---

## FAQ

**Q. どんなときに性能試験を実施すべき？**

A. 大量データ処理・バッチ・重いJOIN・非同期処理・外部API連携の追加時には**必ず検討すべき**

**Q. 本番相当の試験環境が用意できない場合は？**

A. 最低限、**ダミーデータによるローカル検証とスロークエリログ(実行計画)の分析**を行うべき

---

## 関連観点

- [影響範囲が適切に分析されているか？](https://zenn.dev/kanaria007/articles/889dbfe28a793e)
