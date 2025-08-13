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

def create_html_report(links, pdf_name):
    html = f"""
<!DOCTYPE html>
<html>
<head>
<title>PDF Link Report for {pdf_name}</title>
<style>
  body {{ font-family: sans-serif; margin: 2em; }}
  h1 {{ color: #333; }}
  h2 {{ color: #555; border-bottom: 1px solid #ccc; padding-bottom: 5px; }}
  ul {{ list-style-type: none; padding-left: 0; }}
  li {{ margin-bottom: 5px; }}
  a {{ text-decoration: none; color: #0066cc; }}
  .page-container {{ border: 1px solid #ddd; border-radius: 5px; padding: 15px; margin-bottom: 15px; }}
</style>
</head>
<body>
<h1>Link Report for {pdf_name}</h1>
"""
    if not links:
        html += "<p>No links found in this PDF.</p>"
    else:
        for page_num, page_links in links.items():
            html += f'<div class="page-container">'
            html += f"<h2>Page {page_num}</h2>"
            html += "<ul>"
            for link in page_links:
                html += f'<li><a href="{link}" target="_blank">{link}</a></li>'
            html += "</ul>"
            html += "</div>"

    html += """
</body>
</html>
"""
    return html

def main():
    parser = argparse.ArgumentParser(description="A program to extract links from a PDF and generate an HTML report.")
    parser.add_argument("path", help="Path to the PDF file.")
    args = parser.parse_args()

    if not os.path.exists(args.path):
        print(f"Error: File not found at {args.path}", file=sys.stderr)
        sys.exit(1)

    links = extract_links(args.path)
    pdf_name = os.path.basename(args.path)
    html_content = create_html_report(links, pdf_name)
    
    report_filename = 'report.html'
    with open(report_filename, "w") as f:
        f.write(html_content)
        
    print(f"Report generated successfully: {report_filename}")

if __name__ == "__main__":
    main()
