#!/usr/bin/env python

import sys
from package import Package
import argparse

if __name__ == "__main__":
    args = argparse.ArgumentParser(description="PS4 PKG tool")
    args.add_argument("cmd", choices=["info", "extract", "dump"], help="Dump information about a PKG")
    args.add_argument("pkg", help="A PKG")
    args.add_argument("--file", required="extract" in sys.argv, help="Extract file (by ID or name)")
    args.add_argument("--out", required="--file" in sys.argv or "dump" in sys.argv, help="Output location for file")
    args = args.parse_args()

    target = Package(args.pkg)

    if args.cmd == "info":
        target.info()
    elif args.cmd == "extract":
        target.extract(args.file, args.out)
    elif args.cmd == "dump":
        target.dump(args.out)
