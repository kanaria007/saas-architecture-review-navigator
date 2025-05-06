---
title: APIと内部の権限制御が一致しているか？
layer: [Structure]
category: API・権限・セキュリティ
tags: [認可, ドメインロジック, 一貫性]
bloom_level: Analyze
license: MIT
---

# APIの権限管理が適切に設計されているか？

> Type: Structure  
> Category: API・権限・セキュリティ  
> Audience: 設計初心者 / 設計中のチーム / レビュワー

---

## 背景・概要

APIにはユーザー・ロールごとの権限管理が求められる

権限管理は**セキュリティの要**であり、設計ミスは**インシデントに直結**するが、特にBtoBシステムではユーザーごとに細かな操作制御が必要となるため、**責務の分離と明示的な設計**が必須

**これを怠り設計段階で権限と振る舞いの分離がされていないと、漏洩や不正アクセスが発生しやすい**

セキュリティインシデントはBtoBにとっては致命的なため意識した開発が必須

---

## 例

- **ドメイン層**: Document.canView(user) のようなprivate関数で、業務ルールとしての操作許可をドメインオブジェクト内部で表現する
- **ユースケース層**: requirePermission(user, Action.VIEW_DOCUMENT) をユースケースの冒頭で呼び出し、権限制御を明示的に行う
- エンドポイントごとに必要権限を明示的に設計しておく
- APIレスポンスで非表示にするのではなく、リクエスト段階で権限制御して早期returnする

---

## よくある失敗例

- UI側で非表示にしているだけで、APIには誰でもアクセスできてしまう
- 権限ロジックが複数箇所に分散していて、変更時に考慮漏れして整合性が崩壊
- 誰がどこまで操作できるのか仕様に書かれておらず、ドメインでの操作可否とユースケースでの権限制御が**混同**され、責務が不明瞭

---

## FAQ

**Q. 権限の定義はどこで持つべき？**

A. サーバーサイドでRole/PermissionをEnumなどで明示的に定義し、誰が何をできるか一目で把握できるのが望ましい。例えばval rolePermissions = mapOf(Role.ADMIN to setOf(VIEW_DOCUMENT, APPROVE_TASK, EXPORT_CSV),Role.USER to setOf(VIEW_DOCUMENT))のようにマッピングするなど

**Q. 権限の種類が増えてきたら？**

A. ポリシーベースの動的な権限設計に移行する。例えばclass ViewDocumentPolicy : Policy<User, Document>を定義するなどしてPolicyクラスごとの条件分岐により 「誰が」「何に対して」「どんな条件で」操作できるかを制御する。しかしこのやり方は複雑化するので慎重に判断されたい

---

## 関連観点

- [ドメインの権限管理が適切に適用されているか？](https://zenn.dev/kanaria007/articles/4f94d9ebd61705)
- [API のスキーマが適切に設計され、他の API との整合性があるか？](https://zenn.dev/kanaria007/articles/14fca7fc6ea047)
- [セキュリティリスク（機密データの取り扱い、認証・認可）が考慮されているか？](https://zenn.dev/kanaria007/articles/cb4a6fe7106f2a)
