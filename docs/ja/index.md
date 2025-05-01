# SaaS Architecture Review Navigator

> なぜこれが存在するのか？: [Read the Manifesto](../../manifesto.md)
>
> 分散システム設計における思考の盲点を減らすための、設計観点ナビゲーター
> 実務でよく聞かれる質問・盲点も交えながら、設計品質を上げる観点を体系的にまとめる試みです
> **50+ perspectives / 12 categories / 2 structural levels** — all mapped and linked.

---

## 🧭 これは何？

このドキュメントは、SaaSの現場で必要と思われる設計観点を体系化したものです

イベント駆動・非同期設計・マルチテナント対応・分散トランザクション・災害対策など、現代的な分散型SaaSに求められる領域を概ねカバーしていると思います

- ドメインモデル
- データ構造 & 整合性  
- API 設計 & スキーマ  
- イベント駆動
- パフォーマンス & スケーラビリティ  
- 認証認可 & セキュリティ  
- テスト & リリース
- 可用性 & 障害対応  
- 非機能 & 運用要件

各観点は「背景・概要」「例」「よくある失敗例」「FAQ」「関連観点」によって構成されており、現実の実務に耐えるよう設計しています

- 🔍 背景・概要  
- ✅ 例
- ⚠️ よくある失敗例
- ❓ FAQ
- 🔗 関連観点

### 🧠 Human カテゴリって？

純粋な技術観点から一歩踏み出し、それを支えるもの

- 個人の成長を “システム” として設計する
- 自律的な改善ループを回す
- メンター／リーダー育成を仕組み化する

といった **人間面の設計フレームワーク** を設計しました
技術チェックリストとは少し毛色が違いますが、「エンジニアの長期的成長を加速する足場」としてご活用ください

---

## 🚀 使い方 3 パターン

### 1. 設計や実装フェーズで

- [ナビゲーションマップ](navigation-map.md) から関連カテゴリを開き、設計やコードを書く前に問いをチェック
- `.md` ファイルの質問や例を設計資料に引用しながら活用する

### 2. レビュー中に

- PR やレビュー用テンプレに、該当 `.md` へのリンクを貼って共通チェックリストに
- チェックリストとしてレビュアーと著者間の共通言語にする

### 3.障害やインシデント後に

   `availability/` や `non-functional/` を参照して、復旧戦略や監視の観点を洗い直す

---

## 📂 カテゴリ一覧

- 🧩 [`Common`](categories/common/design-justification.md) — design reasoning, tradeoff clarity  
- 🏷️ [`Domain`](categories/domain/domain-permissions.md) — abstraction, constraints, permissions  
- 📦 [`Data`](categories/data/lifecycle-clarity.md) — schema lifecycle, migration, indexing  
- 🌐 [`API`](categories/api/api-schema-coherence.md) — contract design, versioning, authz  
- 🔁 [`Event`](categories/async/sync-async-alignment.md) — async design, retries, fallout zones  
- 📊 [`Performance`](categories/performance/indexing-strategy.md) — latency, scale, resource limits  
- 🎨 [`UI`](categories/ui/component-reuse-impact.md) — rendering cost, notification design  
- 🧪 [`Test`](categories/test/impact-scope-analysis.md) — boundary tests, load, acceptance  
- 🚀 [`Release`](categories/release/release-strategy-planning.md) — rollout strategy, rollback design  
- 🔰 [`Availability`](categories/availability/failover-design.md) — failure response, backup, recovery  
- 🛡 [`Non-functional`](categories/non-functional/security-risks.md) — monitoring, security, ops  
- 🔐 [`Security`](categories/security/authn-authz-implementation.md) — authn/authz, sensitive data  
- 🧠 [`Human`](categories/human/growth-framework-design.md) — growth systems, reflection, mentorship

---

## 🧩 Structural Levels

- **Structure**: 設計の基本構造や責務分離、原則的判断を扱います
- **DeepDive**: パフォーマンス、非同期、障害系などの高難度・境界領域を扱います

---

## 🧠 設計哲学

> これはチュートリアルではなく「問いのカタログ」です  
> **書く前に “いい質問” を投げる** ための道具です
> 初心者からアーキテクトクラスでも学びがあるよう設計しているので、ぜひ有効活用してください

---

## 💬 Meta

- Created by [Kanaria](https://zenn.dev/kanaria007)  
- 日本語で執筆 → AI と二人三脚で英訳
- Licensed under MIT  
- Contributions welcome (see [CONTRIBUTING.md](contributing.md))
