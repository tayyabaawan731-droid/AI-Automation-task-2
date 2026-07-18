# Test Documentation

This project uses Python's built-in **unittest** framework.

## Test Cases

1. **Valid Logs**

   * Verifies that correctly formatted log entries are parsed successfully.

2. **Missing Fields**

   * Checks that malformed log lines are skipped without crashing.

3. **Bad Timestamp**

   * Verifies invalid timestamps are skipped.

4. **Empty File**

   * Ensures an empty file returns zero processed records.

5. **Duplicate Logs**

   * Verifies duplicate records are preserved in the output.

6. **Dry Run**

   * Ensures the parser works in `--dry-run` mode without creating an output CSV.

## Run the Tests

```bash
python test_parser.py
```
