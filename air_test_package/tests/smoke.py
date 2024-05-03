# 起動確認程度の簡単なスモークテスト
import os
from airtest.core.api import *

CWD = os.getcwd()
PKG = os.environ['APP_PACKAGE']
LOG_DIR = os.environ['LOG_DIR']
ADB_PATH = os.environ['ADB_PATH']
SERIAL_NO = os.environ['SERIAL_NO']
auto_setup(devices=[f'Android:///{SERIAL_NO}?adb_path={ADB_PATH}'])


if PKG not in device().list_app():
    install(os.environ['DEVICEFARM_APP_PATH'])
start_app(PKG)

try:
    # 画面左上のアイコンの確認
    assert_exists(
        Template(
            filename=r"tests/statics/home_icon.png",
            target_pos=1,
        )
    )

    assert_exists(
        Template(
            filename=r"tests/statics/heart_icon.png",
            target_pos=1,
        )
    )

    # 画面中央のボタンの確認
    assert_exists(
        Template(
            filename=r"tests/statics/like_button.png",
            target_pos=5,
        )
    )

    assert_exists(
        Template(
            filename=r"tests/statics/next_button.png",
            target_pos=5,
        )
    )
finally:
    uninstall(PKG)