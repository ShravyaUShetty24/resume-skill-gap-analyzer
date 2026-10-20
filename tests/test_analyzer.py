import unittest
from modules.analyzer import analyze, contains_skill, role_catalog, from_description

class AnalyzerTests(unittest.TestCase):
    def test_word_boundary(self):
        self.assertTrue(contains_skill("Used Python and SQL", "Python"))
        self.assertFalse(contains_skill("JavaScript application", "Java"))

    def test_gap(self):
        result = analyze("Python, SQL", ["Python", "Java", "SQL"])
        self.assertEqual(result["score"], 67)
        self.assertEqual(result["missing"], ["Java"])

    def test_roles(self):
        self.assertIn("Python Developer", role_catalog())

    def test_custom(self):
        self.assertIn("SQL", from_description("Must know SQL"))

if __name__ == "__main__":
    unittest.main()
