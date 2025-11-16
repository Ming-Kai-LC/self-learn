"""
Data Processor - For Multi-Cursor and Editing Practice
======================================================
This file contains repetitive code patterns for practicing
multi-cursor editing and find/replace features.
"""


class DataProcessor:
    """Process various types of data."""

    def __init__(self):
        self.data = []
        self.processed_data = []
        self.error_count = 0

    def load_data(self, data):
        """Load data into processor."""
        self.data = data
        print(f"Loaded {len(data)} items")

    def process_item(self, item):
        """Process a single item."""
        # TODO: Implement processing logic
        return item.upper() if isinstance(item, str) else item

    def process_all(self):
        """Process all data items."""
        self.processed_data = []
        for item in self.data:
            try:
                processed = self.process_item(item)
                self.processed_data.append(processed)
            except Exception as e:
                self.error_count += 1
                print(f"Error processing item: {e}")

    def get_results(self):
        """Return processed results."""
        return self.processed_data


# Sample data with repetitive patterns
# Practice multi-cursor editing on these lines:
data_item_1 = "apple"
data_item_2 = "banana"
data_item_3 = "cherry"
data_item_4 = "date"
data_item_5 = "elderberry"

# Practice find and replace
old_variable_name = 10
old_variable_name = 20
old_variable_name = 30
old_variable_name = 40


def example_function_1():
    """Example function 1."""
    pass


def example_function_2():
    """Example function 2."""
    pass


def example_function_3():
    """Example function 3."""
    pass


if __name__ == "__main__":
    processor = DataProcessor()
    processor.load_data(["apple", "banana", "cherry"])
    processor.process_all()
    print(processor.get_results())
