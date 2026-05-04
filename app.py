import os

def run_command(user_input):
    # ❌ Vulnerable a command injection
    os.system("ping -c 1 " + user_input)

run_command("127.0.0.1; ls")
