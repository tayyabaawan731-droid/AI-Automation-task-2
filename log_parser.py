import argparse
import csv
import os
from datetime import datetime


def parse_log_file(input_file, output_file="output_parsed.csv", dry_run=False):
    processed = 0
    successful = 0
    skipped = 0
    parsed_data = []

    try:
        with open(input_file, "r") as file:
            for line in file:
                processed += 1
                line = line.strip()

                if not line:
                    skipped += 1
                    continue

                parts = line.split(",")

                if len(parts) != 4:
                    skipped += 1
                    continue

                timestamp, source_ip, event_type, status = parts

                try:
                    dt = datetime.strptime(timestamp, "%Y-%m-%dT%H:%M:%SZ")
                    timestamp = dt.strftime("%Y-%m-%dT%H:%M:%SZ")
                except ValueError:
                    skipped += 1
                    continue

                parsed_data.append([
                    timestamp,
                    source_ip,
                    event_type,
                    status
                ])
                successful += 1

        if dry_run:
            print("\n===== DRY RUN =====")
            print(f"Would process: {input_file}")
            print(f"Would create: {output_file}")
            print(f"Records Found: {successful}")
            print(f"Skipped: {skipped}")

            return {
                "processed": processed,
                "successful": successful,
                "skipped": skipped
            }

        with open(output_file, "w", newline="") as csvfile:
            writer = csv.writer(csvfile)

            writer.writerow([
                "timestamp",
                "source_ip",
                "event_type",
                "status"
            ])

            writer.writerows(parsed_data)

        print("\n===== SUMMARY =====")
        print(f"Total Lines Processed : {processed}")
        print(f"Successful Records    : {successful}")
        print(f"Skipped Records       : {skipped}")
        print(f"Output File           : {output_file}")

        return {
            "processed": processed,
            "successful": successful,
            "skipped": skipped
        }

    except FileNotFoundError:
        print("Error: Input file not found.")
        return None

    except PermissionError:
        print("Error: Permission denied.")
        return None

    except Exception as e:
        print("Unexpected Error:", e)
        return None


def main():
    parser = argparse.ArgumentParser(
        description="Security Log Parser"
    )

    parser.add_argument(
        "input_file",
        help="Path to input log file"
    )

    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Preview without creating CSV"
    )

    args = parser.parse_args()

    if not os.path.exists(args.input_file):
        print("Error: Input file does not exist.")
        return

    parse_log_file(
        args.input_file,
        "output_parsed.csv",
        args.dry_run
    )


if __name__ == "__main__":
    main()