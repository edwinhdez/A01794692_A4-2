import sys
import argparse
from utils.file_processor import process_file

def main():
    parser = argparse.ArgumentParser(description="Process a file containing a list of items.")
    parser.add_argument('file_path', type=str, help='Path to the file containing the list of items')
    args = parser.parse_args()

    try:
        items = process_file(args.file_path)
    except FileNotFoundError:
        print(f"Error: The file '{args.file_path}' was not found.")
        sys.exit(1)
    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)

    print("Items from the file:")
    for item in items:
        print(item)

if __name__ == "__main__":
    main()