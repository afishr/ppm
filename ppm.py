import argparse
from pip_tools import pip_install, pip_uninstall, pip_list, pip_freeze


def main():
  parser = argparse.ArgumentParser(description="ppm - an npm-like pip wrapper")
  subparsers = parser.add_subparsers(dest="command")

  subparsers.add_parser("install").add_argument("package", nargs="+")
  subparsers.add_parser("uninstall").add_argument("package", nargs="+")
  subparsers.add_parser("list")
  subparsers.add_parser("freeze")

  args, unknown = parser.parse_known_args()

  if args.command == "install":
    pip_install(args.package + unknown)
  elif args.command == "uninstall":
    pip_uninstall(args.package + unknown)
  elif args.command == "list":
    pip_list(unknown)
  elif args.command == "freeze":
    pip_freeze()
  else:
    parser.print_help()


if __name__ == "__main__":
  main()
