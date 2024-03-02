# FoodConnections

FoodConnectionsは飲食店の情報を共有するプラットフォームです。<br>
コンセプトは、「ユーザー、生産者、飲食店の三者の顔が見え、それぞれにつながりを生む」です。

ユーザーは、お気に入りの飲食店を検索し、レビューや評価を共有することができます。<br>
生産者は、自分達がどのように生産しているかアピールすることができます。<br>
飲食店は、お店の情報はもちろん、使用する食材を誰が生産しているのか明示することができます。

レスポンシブ対応しているのでスマホからもご確認いただけます。

<br />

## サービスのURL

https://foodconnections.onrender.com/foodconnections/

<br />

## テストユーザーのログイン情報

ログインせずに、ゲストとしてもご利用いただけます。<br>
それぞれのユーザーとしてログインすることで、マイページなどに表示される内容の違いをご確認いただけます。<br>

■一般ユーザー<br>
メールアドレス：test_user_02@gmail.com<br>
パスワード：test_user_02<br>

■生産者<br>
メールアドレス：komenouka@gmail.com<br>
パスワード：test_farmer_01<br>

■飲食店<br>
メールアドレス：washoku_02@gmail.com<br>
パスワード：test_restaurant_03<br>

<br />

## サービスへの想い

私は現在、農家として米作りをしています。<br>
このサービスは、一般的な「ユーザーと飲食店をつなぐ」グルメサイトに、生産者とのつながりも生み出したいという思いから生まれました。<br>
お互いの顔が見えることで、ユーザーは調理や生産のこだわりを知るきっかけとなり、生産者と飲食店はどのような人に食べてもらえているのか知ることができます。<br>
今後は、さらにユーザー間のコミュニケーションが活発になるサービスを目指しています。<br>

<br />

## 主要画面一覧
| トップ画面 |　ログイン画面 |
| ---- | ---- |
| ![FireShot Capture 001 - FoodConnections - 127 0 0 1](https://github.com/NaoyaTAKEI04/FoodConnections/assets/155603182/0e56ce5d-f676-4462-9896-eabbe8b8c56f) | ![FireShot Capture 009 - FoodConnections - 127 0 0 1](https://github.com/NaoyaTAKEI04/FoodConnections/assets/155603182/bd646da5-ff6d-46eb-808f-ecc8c7144384) |
| エリア（都道府県）検索、キーワード（店名）検索、またはカテゴリーから飲食店を検索することができます。また、管理画面で設定したおすすめ店舗がスライド表示されます。 | メールアドレスとパスワードでの認証機能を実装しています。 |

| サインアップ画面 |　検索結果画面 |
| ---- | ---- |
| ![FireShot Capture 010 - FoodConnections - 127 0 0 1](https://github.com/NaoyaTAKEI04/FoodConnections/assets/155603182/bfb19bc2-07b7-4682-8864-2f03289f4399) | ![FireShot Capture 008 - FoodConnections - 127 0 0 1](https://github.com/NaoyaTAKEI04/FoodConnections/assets/155603182/0335a12d-35f5-4cc6-a45a-6090850fdcf5) |
| サインアップ時にユーザータイプ（一般・生産者・飲食店）を登録することができます。 | 検索結果とともに、検索キーワードも表示されます。また、ページネーションも実装しています。 |

| 飲食店詳細画面 |マイページ（一般ユーザー） |
| ---- | ---- |
| ![FireShot Capture 003 - FoodConnections - 127 0 0 1](https://github.com/NaoyaTAKEI04/FoodConnections/assets/155603182/c103e85e-92a8-455b-8be9-51176d027c50) | ![FireShot Capture 007 - FoodConnections - 127 0 0 1](https://github.com/NaoyaTAKEI04/FoodConnections/assets/155603182/3a09ec44-05fc-4a39-ad9a-648fd4ad8f55) |
| 飲食店がマイページに登録した情報が表示されます。また、紐付けした生産者の情報も表示されます。画面下部にはレビュー機能を実装しています。 | 一般ユーザーのマイページには、ユーザー情報の他に、投稿したレビューが表示されます。 |

| マイページ（生産者） |マイページ（飲食店） |
| ---- | ---- |
| ![FireShot Capture 004 - FoodConnections - 127 0 0 1](https://github.com/NaoyaTAKEI04/FoodConnections/assets/155603182/4d2d4108-d042-41ee-946b-ead53bc17205) | ![FireShot Capture 005 - FoodConnections - 127 0 0 1](https://github.com/NaoyaTAKEI04/FoodConnections/assets/155603182/5f25ebe8-ee1c-4721-9704-8e4f4995b319) |
| 生産者のマイページでは、ユーザー情報の他に、飲食店の詳細ページに表示される生産者情報を登録・編集することができます。 | 飲食店のマイページでは、ユーザー情報の他に、店舗情報の登録・編集をすることができます。 |

| 店舗情報の編集画面 |
| ---- |
| ![FireShot Capture 006 - FoodConnections - 127 0 0 1](https://github.com/NaoyaTAKEI04/FoodConnections/assets/155603182/79c313e3-8c0f-4c58-bb37-fb4594ef5dc0) |
| 店舗詳細ページに表示する情報を登録・編集できます。郵便番号を入力すると自動で住所が入力されます。 |

<br />

## 機能一覧

- ユーザー登録、ログイン機能
- ユーザー情報の編集、削除機能
- レビュー投稿機能
- 画像投稿機能
- ページネーション機能
- 検索機能

<br />

## 使用技術

| Category          | Technology Stack                                     |
| ----------------- | --------------------------------------------------   |
| Frontend          | HTML, CSS, JavaScript, jQuery, Bootstrap             |
| Backend           | Python, Django                                       |
| Database          | SQLite   　　　　　　　　　　　　　　                                     |
| API               | Google Maps API                                      |
| etc.              | Git, GitHub, YubinBango                              |

<br />

## ER図

![graph-model](https://github.com/NaoyaTAKEI04/FoodConnections/assets/155603182/d478a558-3388-4114-aab3-0c382d8437e7)
