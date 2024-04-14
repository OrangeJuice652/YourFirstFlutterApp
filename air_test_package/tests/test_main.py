import sys

def run_test():
    import smoke  # Run top-level commands

print("[TEST_SCRIPT]Start Airtest", file=sys.stderr) # Device Farmで標準出力がバッファリングされて見にくいのでstderrへ
run_test()
print("[TEST_SCRIPT]Finish Airtest", file=sys.stderr)