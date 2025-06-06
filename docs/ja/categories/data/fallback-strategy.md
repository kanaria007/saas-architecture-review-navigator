---
title: 非同期処理のフォールバック戦略が設計されているか？
layer: [DeepDive]
category: データ
tags: [fallback, retry, ordering]
bloom_level: Evaluate
license: MIT
---

# 非同期処理のフォールバック戦略が設計されているか？（失敗時の再実行順序やデータの重複生成防止などの考慮）

> Type: DeepDive  
> Category: データ  
> Audience: 設計リーダー / SRE / インフラ設計者 / レビュー担当者

---

## 背景・概要

非同期処理では、失敗や遅延が前提となる

そこで「どう再試行するか」「それでも駄目ならどうするか」を設計時に決めておく必要がある

これがフォールバック戦略。**単なるリトライだけでなく、重複対策・順序制御・人手介入なども含めて設計する**

---

## 例

- 通知送信失敗時は最大3回まで再試行し、それでも失敗したらエラーチャンネルに転送して手動処理
- API呼び出しが特定の例外（HTTP 429など）を返した場合は、指数バックオフ戦略で再試行する
- 再試行による重複登録を避けるため、自然キーでの存在チェックを明示的に実装する

---

## よくある失敗例

- 通知送信エラー時にリトライもされず、ユーザーに何も通知されないまま放置
- 全イベント処理が再試行され、同じリクエストが複数回走ってシステム障害に
- 処理の再実行が順序を崩して、ステータス遷移に矛盾が発生

---

## FAQ

**Q. バックオフ戦略って何？**

A. 再試行間隔を徐々に伸ばすことで、集中アクセスを避けてリカバリしやすくする手法。指数バックオフ（2倍, 4倍…）が代表例

**Q. 失敗した処理を「捨てる」のはアリ？**

A. 通知系・分析系など「ベストエフォートで許容される」処理ならアリだが、業務処理や課金系はNG。業務インパクトの程度で設計を変えるべき

---

## 関連観点

- [イベントのリトライ時にデータの不整合が生じないか？](https://zenn.dev/articles/de377cd64f906a/edit)
- [非同期処理と同期処理の適用範囲が適切か？](https://zenn.dev/kanaria007/articles/fd762dcfb04e28)
- [依存する外部サービスの障害時の影響を考慮しているか？](https://zenn.dev/kanaria007/articles/c7769a08ffc3af)
- [障害時のデータ復旧手順が考慮されているか？](https://zenn.dev/kanaria007/articles/2afe288e82b98f)
