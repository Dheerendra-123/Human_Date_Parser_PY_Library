import unittest
from human_date_parser import parse
from datetime import datetime, timedelta

class TestHumanDateParser(unittest.TestCase):

    def test_tomorrow(self):
        result = parse("tomorrow")
        self.assertIsNotNone(result)
        self.assertTrue(isinstance(result, datetime))

    def test_in_3_days(self):
        result = parse("in 3 days")
        expected = datetime.now() + timedelta(days=3)
        self.assertAlmostEqual(result.timestamp(), expected.timestamp(), delta=86400)

    def test_2_weeks_ago(self):
        result = parse("2 weeks ago")
        expected = datetime.now() - timedelta(days=14)
        self.assertAlmostEqual(result.timestamp(), expected.timestamp(), delta=86400)

    def test_invalid_input(self):
        result = parse("asdkjfhaskdjfh", fallback_now=False)
        self.assertIsNone(result)

    def test_next_friday(self):
        result = parse("next Friday", fallback_now=True)
        self.assertIsNotNone(result)
        self.assertTrue(result.weekday() == 4 or result.weekday() == 5)

    def test_fuzzy_phrase(self):
        result = parse("tmrw")
        self.assertIsNotNone(result)

    def test_holiday_reference(self):
        result = parse("2 weeks after Diwali")
        self.assertIsNotNone(result)

    def test_last_monday(self):
        result = parse("last Monday")
        self.assertIsNotNone(result)
        self.assertEqual(result.weekday(), 0)  # Monday


    def test_this_weekend(self):
        result = parse("this weekend")
        self.assertIsNotNone(result)
        self.assertTrue(result.weekday() in [5, 6])  # Saturday or Sunday

if __name__ == '__main__':
    unittest.main()
