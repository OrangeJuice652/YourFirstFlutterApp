# 起動確認程度の簡単なスモークテスト
import os
from airtest.core.api import *

CWD = os.getcwd()
PKG = os.environ['APP_PACKAGE']
LOG_DIR = os.environ['LOG_DIR']
ADB_PATH = os.environ['ADB_PATH']
SERIAL_NO = os.environ['SERIAL_NO']
print(f'Android:///{SERIAL_NO}?adb_path={ADB_PATH}')
auto_setup(devices=[f'Android:///{SERIAL_NO}?adb_path={ADB_PATH}'])

if PKG not in device().list_app():
    install(CWD + "/" + os.environ['APP_PATH'])
start_app(PKG)

assert_exists(Template(r"tests/statics/top_page.png", "スタート画面があること"))

uninstall(PKG)