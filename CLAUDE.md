# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This project is a Python script that extracts hyperlinks from a PDF file and generates an HTML report. The main script is `main.py`.

## Common Commands

- **Install dependencies:** `uv pip install .`
- **Run the script:** `uv run python main.py <path_to_pdf>`

## Code Architecture

- `main.py`: The single script containing all the logic.
  - `extract_links(path)`: Extracts links from the given PDF file.
  - `create_html_report(links, pdf_name)`: Generates an HTML report from the extracted links.
  - `main()`: Parses command-line arguments and orchestrates the link extraction and report generation.
