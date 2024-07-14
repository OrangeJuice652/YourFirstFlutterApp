# testsフォルダ

本フォルダでは、作成したflutterアプリケーションに対し、UIの確認テストを行うための、テストコード・テストに使用するアセットを管理する。

## 自動テストの内容

![](./air_test_package/tests/statics/top_page.png)

DeviceFarm上で起動したアプリのTOPページ上に、
staticsフォルダに用意した各UIパーツの画像が表示されているかを確認する。

- ホームアイコン
- ハートアイコン
- Likeボタン
- Nextボタン

## 画像を使ったUIパーツの識別

TOP画面上に、画像と同じUIが表示されていることの確認は、
airtest.core.apiモジュールのTemplateを使用する。

参考：[Airtest上における画像を使ったUIパーツの識別](https://airtest.doc.io.netease.com/en/IDEdocs/airtest_framework/3_airtest_image/)


