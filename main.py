import unittest
from parameterized import parameterized


def cut_article(title: str) -> str:
    title = title.strip()
    words = title.split()
    count = 0
    short_title = []
    if len(words) == 1 and len(words[0]) <= 25:
        return words[0]
    for word in words:
        count += len(word) + 1
        if count <= 25:
            short_title.append(word)
        else:
            short_title[-1] += '...'
            break
    return " ".join(short_title)


class TestCutArticle(unittest.TestCase):

    @parameterized.expand([
        ("", ""),
        ("This is a short string", "This is a short string"),
        ("This is a string exactly 25 characters", "This is a string exactly..."),
        ("This is a string longer than 25 characters", "This is a string longer..."),
        ("Thisstringhasnospacesinit", "Thisstringhasnospacesinit"),
        ("  This string has spaces at the beginning", "This string has spaces..."),
        ("This string has special characters like $&@!%", "This string has special..."),
        ("This string has numbers like 1234567890", "This string has numbers..."),
    ])
    def test_cut_article(self, input_string, expected_output):
        with self.subTest(input_string=input_string):
            self.assertEqual(cut_article(input_string), expected_output)


if __name__ == '__main__':
    unittest.main()
