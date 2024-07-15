# device_farmフォルダ

## TestSpec.yml

- DeviceFarmの自動テストにおいて、各工程で何を行うかコマンドを記述したファイル。
  - カスタムしたテスト環境で、テストを行いたい場合、このファイルを作成し、このファイル内でカスタムの環境構築を行う。

### TestSpec.ymlのアップロード方法

参考：[テスト実行を作成 (AWS CLI)＞ステップ 5: (オプション) カスタムテスト仕様をアップロードする](https://docs.aws.amazon.com/ja_jp/devicefarm/latest/developerguide/how-to-create-test-run.html#how-to-create-test-run-cli-step5)

- カスタムのテスト仕様のアップロードを作成

```
aws devicefarm create-upload --name TestSpec.yml --type APPIUM_PYTHON_TEST_SPEC --project-arn <DeviceFarmで作成したProjectのARN>
```

- `aws devicefarm create-upload`コマンドのレスポンスに記載されている署名付きURLに、TestSpec.ymlをアップロードする。

```
curl -T TestSpec.yml "<署名付きURL>"
```