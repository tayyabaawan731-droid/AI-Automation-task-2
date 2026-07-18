import unittest
import os
from log_parser import parse_log_file


class TestLogParser(unittest.TestCase):

    def test_valid_logs(self):
        result = parse_log_file(
            "test_sample_logs/valid_logs.txt",
            "valid_output.csv"
        )

        self.assertEqual(result["successful"], 3)
        self.assertEqual(result["skipped"], 0)

    def test_missing_fields(self):
        result = parse_log_file(
            "test_sample_logs/missing_fields.txt",
            "missing_output.csv"
        )

        self.assertEqual(result["successful"], 0)
        self.assertEqual(result["skipped"], 3)

    def test_bad_timestamp(self):
        result = parse_log_file(
            "test_sample_logs/bad_timestamp.txt",
            "bad_output.csv"
        )

        self.assertEqual(result["successful"], 0)
        self.assertEqual(result["skipped"], 2)

    def test_empty_file(self):
        result = parse_log_file(
            "test_sample_logs/empty_file.txt",
            "empty_output.csv"
        )

        self.assertEqual(result["processed"], 0)
        self.assertEqual(result["successful"], 0)
        self.assertEqual(result["skipped"], 0)

    def test_duplicate_logs(self):
        result = parse_log_file(
            "test_sample_logs/duplicate_logs.txt",
            "duplicate_output.csv"
        )

        self.assertEqual(result["successful"], 3)

    def test_dry_run(self):
        result = parse_log_file(
            "test_sample_logs/valid_logs.txt",
            "dry_output.csv",
            dry_run=True
        )

        self.assertEqual(result["successful"], 3)
        self.assertFalse(os.path.exists("dry_output.csv"))


if __name__ == "__main__":
    unittest.main()