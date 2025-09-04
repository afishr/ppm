import subprocess
import sys


def run_pip(args):
  return subprocess.run([sys.executable, "-m", "pip"] + args, capture_output=True)


def pip_freeze():
  output = run_pip(["freeze"]).stdout.decode('utf-8')

  with open("requirements.txt", "w", encoding="utf-8") as f:
    f.write(output)


def pip_install(args):
  run_pip(["install"] + args)
  pip_freeze()


def pip_uninstall(args):
  run_pip(["uninstall", "-y"] + args)
  pip_freeze()


def pip_list(unknown):
  run_pip(["list"] + unknown)
