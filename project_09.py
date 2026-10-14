import json
from pathlib import Path


def save_settings(path, settings):
    Path(path).write_text(json.dumps(settings, indent=2),
                          encoding="utf-8")


def load_settings(path):
    return json.loads(Path(path).read_text(encoding="utf-8"))


def main():
    path = Path("project_settings.json")
    save_settings(path, {"theme": "dark", "autosave": True})
    print(load_settings(path))


if __name__ == "__main__":
    main()
