# air_test_packageフォルダ

AWSDeviceFarm上の自動テストの際に使用するテストコードや、テストに必要なパッケージを管理するフォルダ
本フォルダのファイルを、下記手順に従い圧縮＆アップロードする。

[Appium と AWSDeviceFarm による作業](https://docs.aws.amazon.com/ja_jp/devicefarm/latest/developerguide/test-types-appium.html)

## 自動テストの内容について

- /testsフォルダ配下のREADME.md参照

## pythonランタイムについて

自動テストを実行するpythonランタイムは、通常AWSDeviceFarmが用意したpythonが使用されるが、バージョンが固定される（2.7.9 もしくは 3.7.4）。
古いバージョンで固定されると使用するライブラリによっては、互換性がとれない恐れがあるため、local環境で、バージョン3.9のpythonランタイムファイル(`/air_test_package/python`)を作成し、これで自動テストのスクリプトを実行するようにした。
（TestSpec.ymlで環境変数を書き換えることで、実行するpythonランタイムの変更ができる。詳細のやり方は、下記参照）

参考：[自分でカスタマイズしたpythonランタイムの準備方法](https://hackerslab.aktsk.jp/2022/12/05/000000#%E3%83%86%E3%82%B9%E3%83%88%E3%82%B9%E3%82%AF%E3%83%AA%E3%83%97%E3%83%88%E5%AE%9F%E8%A1%8C%E7%92%B0%E5%A2%83)

## TODO

`ssl`フォルダの説明を記載する。
