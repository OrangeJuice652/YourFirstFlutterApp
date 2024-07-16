# YourFirstFlutterApp

## 概要

「初めてのFlutterアプリ」のハンズオン
アプリケーションの機能は下記を参照

https://codelabs.developers.google.com/codelabs/flutter-codelab-first?hl=ja#0

また、作成したアプリケーションに対し、UIテストを行うテスト環境を作成した。

## UIテスト

初めてのFlutterアプリを、仮想デバイス上（AWSDeviceFarm）で起動し、自動テストを行う仕組みを作成した。詳細は、下記フォルダのREADME.mdを確認

- `/air_test_package`
  - テストコード・テスト環境でインストールするパッケージを管理
  - 各パッケージについては、`/air_test_package/README.md`参照
- `/device_farm`
  - AWSDeviceFarmのテストにおいて、各工程に実行するスクリプトを記載した定義ファイル（TestSpec.yml）
  - TestSpecの登録方法は、`/device_farm/README.md`参照

### ビルド -> UIテスト

Jenkinsのジョブ内で、本Flutterアプリケーションをビルド＆UIテストを行うことを想定している。
[アプリのビルド＆UIテストを実行するためのインフラ構築](https://github.com/OrangeJuice652/JenkinsOnEC2/tree/main)
