
from __future__ import annotations
import argparse
from .engine import summarize
from .utils import to_json

def main() -> None:
    parser = argparse.ArgumentParser(prog="astrorecon")
    sub = parser.add_subparsers(dest="cmd", required=True)
    c = sub.add_parser("catalog")
    c.add_argument("path")
    o = sub.add_parser("operators")
    o.add_argument("path")
    args = parser.parse_args()
    result = summarize(args.path)
    if args.cmd == "operators":
        print(to_json({"operators": result["operators"]}))
    else:
        print(to_json(result))

if __name__ == "__main__":
    main()
