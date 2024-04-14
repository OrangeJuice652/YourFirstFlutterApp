# 起動確認程度の簡単なスモークテスト
import os
from airtest.core.api import *

CWD = os.getcwd()
PKG = os.environ['APP_PACKAGE']
LOG_DIR = os.environ['LOG_DIR']
auto_setup(__file__, logdir=LOG_DIR, devices=["Android:///", ])

if PKG not in device().list_app():
    install(CWD + "/" + os.environ['APP_PATH'])
start_app(PKG)

assert_exists(Template(r"tests/statics/top_page.png", "スタート画面があること"))

uninstall(PKG)