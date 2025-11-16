"""
Test File Operations
Validates all file handling functionality in Module 06
"""

import csv
import json
import os
import sys
from pathlib import Path

# Fix encoding for Windows console
if sys.platform == "win32":
    import io

    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding="utf-8")


class FileOperationTester:
    def __init__(self):
        self.results = {"total_tests": 0, "passed": 0, "failed": 0, "errors": []}
        self.data_dir = Path(__file__).parent.parent / "data" / "sample_files"

    def test_file_exists(self, filename):
        """Test if a file exists"""
        self.results["total_tests"] += 1
        filepath = self.data_dir / filename

        if filepath.exists():
            self.results["passed"] += 1
            return True, f"✅ File exists: {filename}"
        else:
            self.results["failed"] += 1
            error = f"❌ File not found: {filename}"
            self.results["errors"].append(error)
            return False, error

    def test_text_file_reading(self):
        """Test reading text file"""
        self.results["total_tests"] += 1
        try:
            filepath = self.data_dir / "sample.txt"

            # Test reading entire file
            with open(filepath, "r", encoding="utf-8") as f:
                content = f.read()

            if not content:
                raise ValueError("File is empty")

            # Test reading lines
            with open(filepath, "r", encoding="utf-8") as f:
                lines = f.readlines()

            if not lines:
                raise ValueError("No lines read")

            # Count words
            word_count = len(content.split())
            line_count = len(lines)

            self.results["passed"] += 1
            return True, f"✅ Text file read: {line_count} lines, {word_count} words"

        except Exception as e:
            self.results["failed"] += 1
            error = f"❌ Text file reading failed: {e}"
            self.results["errors"].append(error)
            return False, error

    def test_csv_reading(self):
        """Test reading CSV file"""
        self.results["total_tests"] += 1
        try:
            filepath = self.data_dir / "students.csv"

            # Read CSV
            with open(filepath, "r", encoding="utf-8") as f:
                reader = csv.DictReader(f)
                students = list(reader)

            if not students:
                raise ValueError("No data in CSV")

            # Verify structure
            expected_fields = {"Name", "Age", "Grade", "City"}
            actual_fields = set(students[0].keys())

            if expected_fields != actual_fields:
                raise ValueError(
                    f"CSV structure mismatch. Expected: {expected_fields}, Got: {actual_fields}"
                )

            self.results["passed"] += 1
            return True, f"✅ CSV file read: {len(students)} records"

        except Exception as e:
            self.results["failed"] += 1
            error = f"❌ CSV reading failed: {e}"
            self.results["errors"].append(error)
            return False, error

    def test_json_reading(self):
        """Test reading JSON file"""
        self.results["total_tests"] += 1
        try:
            filepath = self.data_dir / "config.json"

            # Read JSON
            with open(filepath, "r", encoding="utf-8") as f:
                data = json.load(f)

            if not data:
                raise ValueError("JSON is empty")

            # Verify structure
            required_keys = {"application", "version", "settings", "user", "resources"}
            actual_keys = set(data.keys())

            if not required_keys.issubset(actual_keys):
                raise ValueError(
                    f"JSON structure incomplete. Missing: {required_keys - actual_keys}"
                )

            # Verify nested structure
            if "theme" not in data["settings"]:
                raise ValueError("Missing 'theme' in settings")

            self.results["passed"] += 1
            return True, f"✅ JSON file read: {len(data)} top-level keys"

        except Exception as e:
            self.results["failed"] += 1
            error = f"❌ JSON reading failed: {e}"
            self.results["errors"].append(error)
            return False, error

    def test_file_writing(self):
        """Test writing to files"""
        self.results["total_tests"] += 1
        try:
            test_file = self.data_dir / "test_output.txt"

            # Write to file
            test_content = "This is a test file.\nSecond line.\n"
            with open(test_file, "w", encoding="utf-8") as f:
                f.write(test_content)

            # Read back
            with open(test_file, "r", encoding="utf-8") as f:
                read_content = f.read()

            if read_content != test_content:
                raise ValueError("Written content doesn't match read content")

            # Clean up
            test_file.unlink()

            self.results["passed"] += 1
            return True, "✅ File writing works correctly"

        except Exception as e:
            self.results["failed"] += 1
            error = f"❌ File writing failed: {e}"
            self.results["errors"].append(error)
            return False, error

    def test_csv_writing(self):
        """Test writing CSV files"""
        self.results["total_tests"] += 1
        try:
            test_file = self.data_dir / "test_output.csv"

            # Write CSV
            test_data = [{"name": "Test1", "value": "10"}, {"name": "Test2", "value": "20"}]

            with open(test_file, "w", newline="", encoding="utf-8") as f:
                writer = csv.DictWriter(f, fieldnames=["name", "value"])
                writer.writeheader()
                writer.writerows(test_data)

            # Read back
            with open(test_file, "r", encoding="utf-8") as f:
                reader = csv.DictReader(f)
                read_data = list(reader)

            if len(read_data) != len(test_data):
                raise ValueError("CSV row count mismatch")

            # Clean up
            test_file.unlink()

            self.results["passed"] += 1
            return True, "✅ CSV writing works correctly"

        except Exception as e:
            self.results["failed"] += 1
            error = f"❌ CSV writing failed: {e}"
            self.results["errors"].append(error)
            return False, error

    def test_json_writing(self):
        """Test writing JSON files"""
        self.results["total_tests"] += 1
        try:
            test_file = self.data_dir / "test_output.json"

            # Write JSON
            test_data = {"test": "value", "number": 42, "nested": {"key": "value"}}

            with open(test_file, "w", encoding="utf-8") as f:
                json.dump(test_data, f, indent=4)

            # Read back
            with open(test_file, "r", encoding="utf-8") as f:
                read_data = json.load(f)

            if read_data != test_data:
                raise ValueError("JSON data mismatch")

            # Clean up
            test_file.unlink()

            self.results["passed"] += 1
            return True, "✅ JSON writing works correctly"

        except Exception as e:
            self.results["failed"] += 1
            error = f"❌ JSON writing failed: {e}"
            self.results["errors"].append(error)
            return False, error

    def test_path_operations(self):
        """Test path operations"""
        self.results["total_tests"] += 1
        try:
            # Test path existence
            if not self.data_dir.exists():
                raise ValueError("Data directory doesn't exist")

            # Test path construction
            test_path = self.data_dir / "sample.txt"
            if not test_path.exists():
                raise ValueError("Cannot construct path correctly")

            # Test getting parent
            parent = test_path.parent
            if parent != self.data_dir:
                raise ValueError("Parent path incorrect")

            self.results["passed"] += 1
            return True, "✅ Path operations work correctly"

        except Exception as e:
            self.results["failed"] += 1
            error = f"❌ Path operations failed: {e}"
            self.results["errors"].append(error)
            return False, error

    def run_all_tests(self):
        """Run all file operation tests"""
        print("=" * 60)
        print("FILE OPERATIONS TEST SUITE")
        print("=" * 60)
        print()

        tests = [
            ("Sample Text File Exists", lambda: self.test_file_exists("sample.txt")),
            ("Students CSV File Exists", lambda: self.test_file_exists("students.csv")),
            ("Config JSON File Exists", lambda: self.test_file_exists("config.json")),
            ("Text File Reading", self.test_text_file_reading),
            ("CSV File Reading", self.test_csv_reading),
            ("JSON File Reading", self.test_json_reading),
            ("Text File Writing", self.test_file_writing),
            ("CSV File Writing", self.test_csv_writing),
            ("JSON File Writing", self.test_json_writing),
            ("Path Operations", self.test_path_operations),
        ]

        for test_name, test_func in tests:
            print(f"Testing: {test_name}")
            success, message = test_func()
            print(f"  {message}")
            print()

        self.print_summary()

    def print_summary(self):
        """Print test summary"""
        print("=" * 60)
        print("TEST SUMMARY")
        print("=" * 60)
        print(f"Total Tests: {self.results['total_tests']}")
        print(f"✅ Passed: {self.results['passed']}")
        print(f"❌ Failed: {self.results['failed']}")
        print()

        if self.results["failed"] > 0:
            print("ERRORS:")
            for error in self.results["errors"]:
                print(f"  {error}")
            print()

        if self.results["failed"] == 0:
            print("🎉 ALL FILE OPERATIONS TESTS PASSED!")
        else:
            print("⚠️ SOME TESTS FAILED")

        print("=" * 60)


if __name__ == "__main__":
    tester = FileOperationTester()
    tester.run_all_tests()
