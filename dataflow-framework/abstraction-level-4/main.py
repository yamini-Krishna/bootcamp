from processors import simple_processor, LineCounterProcessor, join_lines, split_lines_by_delimiter

def main():
    # Example of processing a stream of lines
    lines = ["hello", "world", "python", "stream", "processing"]

    # Process with a simple processor (Upper case transformation)
    print("Simple Processor Output:")
    for output in simple_processor(iter(lines)):
        print(output)

    # Process with Line Counter Processor
    print("\nLine Counter Processor Output:")
    counter_processor = LineCounterProcessor()
    for output in counter_processor(iter(lines)):
        print(output)

    # Process with Fan-In Processor (Join every two lines)
    print("\nFan-In Processor Output:")
    for output in join_lines(iter(lines)):
        print(output)

    # Process with Fan-Out Processor (Split by space)
    print("\nFan-Out Processor Output:")
    for output in split_lines_by_delimiter(iter(lines), " "):
        print(output)

if __name__ == "__main__":
    main()
