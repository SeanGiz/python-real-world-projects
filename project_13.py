from pathlib import Path


def make_plan(names, prefix):
    return [(name, f"{prefix}_{index:03d}{Path(name).suffix}")
            for index, name in enumerate(sorted(names), 1)]


def main():
    for before, after in make_plan(["b.jpg", "a.jpg"], "photo"):
        print(f"{before} -> {after}")


if __name__ == "__main__":
    main()
