from urllib.parse import quote


def make_message(name, task):
    subject = f"Update on {task}"
    body = f"Hello {name},\nHere is the latest update on {task}.\n"
    return subject, body


def main():
    subject, body = make_message("Maya", "Project Alpha")
    print(subject)
    print(body)


if __name__ == "__main__":
    main()
