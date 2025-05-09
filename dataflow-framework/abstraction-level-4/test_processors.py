import unittest
from processors import LineCounterProcessor, join_lines, split_lines_by_delimiter

class TestProcessors(unittest.TestCase):
    
    def test_line_counter(self):
        processor = LineCounterProcessor()
        result = list(processor(iter(["line1", "line2", "line3"])))
        self.assertEqual(result, [
            "Line 1: line1",
            "Line 2: line2",
            "Line 3: line3"
        ])
    
    def test_join_lines(self):
        result = list(join_lines(iter(["line1", "line2", "line3", "line4"])))
        self.assertEqual(result, [
            "line1 line2",
            "line3 line4"
        ])
    
    def test_split_lines(self):
        result = list(split_lines_by_delimiter(iter(["hello world", "python stream"]), " "))
        self.assertEqual(result, ["hello", "world", "python", "stream"])

if __name__ == "__main__":
    unittest.main()
