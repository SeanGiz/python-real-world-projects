import argparse


def build_parser():
    parser = argparse.ArgumentParser(description="Tiny todo tool")
    parser.add_argument("task", help="task name")
    parser.add_argument("--priority", choices=["low", "high"],
                        default="low")
    return parser


def main():
    args = build_parser().parse_args()
    print(f"{args.priority.upper()}: {args.task}")


if __name__ == "__main__":
    main()
