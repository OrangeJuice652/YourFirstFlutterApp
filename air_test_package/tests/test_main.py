import sys

def register_force_kill():
    import time
    import subprocess

    def run_shell(cmd):
        print(cmd, file=sys.stderr)
        process = subprocess.Popen(cmd, stderr=subprocess.PIPE, stdout=subprocess.PIPE, shell=True)
        stdout, stderr = process.communicate(timeout=150)
        exit_code = process.returncode
        print("stdout: ", stdout, " stderr: ", stderr, " exit_code: ", exit_code, file=sys.stderr)

    def teardown():
        print("[TEST_SCRIPT]teardown", file=sys.stderr)
        run_shell("ps aux | grep rotationwatcher") # 確認用
        run_shell("pkill -f rotationwatcher")
        time.sleep(1) # Wait for rotationwatcher to terminate
        run_shell("ps aux | grep rotationwatcher") # 確認用

    from airtest.utils.snippet import reg_cleanup
    reg_cleanup(teardown) # Insert into airtest termination process

def run_test():
    import smoke  # Run top-level commands

print("[TEST_SCRIPT]Registration of forced termination", file=sys.stderr)
register_force_kill()
print("[TEST_SCRIPT]Start Airtest", file=sys.stderr) # Device Farmで標準出力がバッファリングされて見にくいのでstderrへ
run_test()
print("[TEST_SCRIPT]Finish Airtest", file=sys.stderr)