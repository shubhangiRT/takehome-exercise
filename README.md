# PubMed Paper Search Tool

A command-line tool that searches for papers on [PubMed](https://pubmed.ncbi.nlm.nih.gov/) using a given keyword, displays results in a readable table, and saves them to a CSV file.

---

## Features

- Search PubMed with any keyword (e.g., `diabetes`, `cancer`, `COVID`)
- Extract paper titles and authors
- Output results in a formatted table using `tabulate`
- Export data to `pubmed_results.csv`
- Input validation and graceful error handling

---

## Requirements

- Python 3.10+
- [Poetry](https://python-poetry.org/docs/#installation) for dependency management

---

## Installation

1. Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/pubmed-search-tool.git
cd pubmed-search-tool


2.Install dependencies

poetry install

3.Usage
Use the following command to search:
poetry run python main.py "search_term"

example:
poetry run python main.py "diabetes"

You will see a table of results in the terminal and a file named pubmed_results.csv will be saved.

4.Error Handling
The program will show appropriate error messages if:

The input is empty or invalid

No results are found

The internet is disconnected

PubMed is unreachable

5.Sample Output
+-----+--------------------------+------------------------------+
| No. | Title                   | Authors                      |
+-----+--------------------------+------------------------------+
| 1   | Title of Paper 1         | Author A, Author B           |
| 2   | Title of Paper 2         | Author C                     |
+-----+--------------------------+------------------------------+
6.License
This project is open-source and free to use under the MIT License.

7.Author
Developed by [Thombare Shubhangi Radhakisan].
For training, interview prep, or job-ready tasks in Python.

