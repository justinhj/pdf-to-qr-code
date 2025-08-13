import argparse
import os
import sys
from PyPDF2 import PdfReader

def extract_links(path):
    links = {}
    reader = PdfReader(path)
    for i, page in enumerate(reader.pages):
        page_links = []
        if '/Annots' in page:
            for annot in page['/Annots']:
                obj = annot.get_object()
                if obj.get('/Subtype') == '/Link':
                    a = obj.get('/A')
                    if a:
                        uri = a.get_object().get('/URI')
                        if uri and (uri.startswith('http://') or uri.startswith('https://')):
                            page_links.append(uri)
        if page_links:
            links[i + 1] = page_links
    return links

def main():
    parser = argparse.ArgumentParser(description="A program to extract links from a PDF.")
    parser.add_argument("path", help="Path to the PDF file.")
    args = parser.parse_args()

    if not os.path.exists(args.path):
        print(f"Error: File not found at {args.path}", file=sys.stderr)
        sys.exit(1)

    links = extract_links(args.path)
    print(links)

if __name__ == "__main__":
    main()
