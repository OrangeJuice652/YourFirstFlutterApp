# YourFirstFlutterApp

## 概要

初めてのFlutterアプリのハンズオン

https://codelabs.developers.google.com/codelabs/flutter-codelab-first?hl=ja#0

## UIテスト

初めてのFlutterアプリを、仮想デバイス上（AWSDeviceFarm）で起動し、自動テストを行う仕組みを作成した。詳細は、下記フォルダのREADME.mdを確認

- `/air_test_package`
  - テストコード・テスト環境でインストールするパッケージを管理
- `/device_farm`
  - AWSDeviceFarmのテストにおいて、各工程に実行するスクリプトを記載した定義ファイル（TestSpec.yml）を買う脳

### ビルド -> UIテスト

Jenkinsのジョブ内で、本Flutterアプリケーションをビルド＆UIテストを行うことを想定している。
[ビルド＆テスト環境は、JenkinsOnEC2リポジトリのREADME参照](https://github.com/OrangeJuice652/JenkinsOnEC2/tree/main)

## TODO
- FlutterAppの機能について、READMEを記載
