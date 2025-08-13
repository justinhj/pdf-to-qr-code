import argparse
import os
import sys

def main():
    parser = argparse.ArgumentParser(description="A simple hello world program.")
    parser.add_argument("path", help="Path to the PDF file.")
    args = parser.parse_args()

    if not os.path.exists(args.path):
        print(f"Error: File not found at {args.path}", file=sys.stderr)
        sys.exit(1)

    print(f"hello {args.path}")

if __name__ == "__main__":
    main()