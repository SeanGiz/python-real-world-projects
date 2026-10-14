from pathlib import Path
import shutil


def backup_file(source, destination_dir):
    source = Path(source)
    target = Path(destination_dir) / source.name
    target.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(source, target)
    return target


def main():
    original = Path("sample_to_backup.txt")
    original.write_text("example", encoding="utf-8")
    print(backup_file(original, "backups"))


if __name__ == "__main__":
    main()
