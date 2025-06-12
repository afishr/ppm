import argparse
import subprocess
import sys

def run_pip(args):
    subprocess.run([sys.executable, "-m", "pip"] + args)

def main():
    parser = argparse.ArgumentParser(description="ppm - a pip wrapper like npm")
    subparsers = parser.add_subparsers(dest="command")

    subparsers.add_parser("install").add_argument("package", nargs="+")
    subparsers.add_parser("uninstall").add_argument("package", nargs="+")
    subparsers.add_parser("list")

    args, unknown = parser.parse_known_args()

    if args.command == "install":
        run_pip(["install"] + args.package + unknown)
    elif args.command == "uninstall":
        run_pip(["uninstall", "-y"] + args.package + unknown)
    elif args.command == "list":
        run_pip(["list"] + unknown)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
