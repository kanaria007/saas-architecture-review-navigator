---
title: ドメインの権限管理が適切に設計されているか？
layer: [Structure, DeepDive]
category: ドメイン
tags: [authorization, permission, domain-logic]
bloom_level: Evaluate
license: MIT
---

# ドメインの権限管理が適切に設計されているか？

> Type: Structure, DeepDive  
> Category: ドメイン  
> Audience: 設計初心者 / 設計中のチーム / レビュワー

---

## 背景・概要

業務において**誰が何をできるか/できないか**は重要な制約事項であり、実装の初期から考慮しておかないと後のセキュリティ事故・バグ・混乱の原因となる。
**ドメイン層で表現すべきか、アプリケーション層で制御すべきかの切り分けも重要**

---

## 例

- Task.canApprove(user: User): Boolean のような問いかけ型のメソッドは設けず、Task.approve(user: User)内で権限制御するか、複雑な場合はTaskApprovalPolicyのようなポリシードメインを作成する
- ロールや権限はEnum/DB/sealed interfaceなどで管理し、表示・ユーザー操作の制御は画面やAPIで行う
- 各ユースケース（ApplicationService）では権限チェックを**明示的に記述**して曖昧さを排除する

---

## よくある失敗例

- 「一部の画面では表示されるが、操作はできない」など中途半端な制御になる
- フロント側でしか制御されておらず、APIを直接叩けば何でもできてしまう状態
- 権限制御がコードベースのあちこちに散らばっており、**ロール追加や変更時にミスが頻発**

---

## FAQ

**Q. 権限チェックはユースケースかドメインか？**

A. ケースバイケース。ドメインでは「このデータに対して誰が何をできるか」を制御し、ユースケースでは「業務上その操作が可能か」を判断するのが無難と思われる

**Q. 権限のソースはEnumかDBかどこにおく？**

A. 小規模ならEnum、大規模ならDBやStrategy(Policy)パターンを使って柔軟に実装できる

---

## 関連観点

- [APIの権限管理が適切に設計されているか？](https://zenn.dev/kanaria007/articles/03fb36eb3d41f3)
- [ドメインオブジェクトが適切に抽象化され、アプリケーション層と適切に分離されているか？](https://zenn.dev/kanaria007/articles/2454bcc637fa86)
