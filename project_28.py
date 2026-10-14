import unittest


def normalize(text):
    return " ".join(text.lower().split())


class NormalizeTests(unittest.TestCase):
    def test_spaces_and_case(self):
        self.assertEqual(normalize("  HELLO   World "), "hello world")

    def test_empty_string(self):
        self.assertEqual(normalize("  "), "")


if __name__ == "__main__":
    unittest.main()
