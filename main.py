import requests
from bs4 import BeautifulSoup
import csv
import argparse
from tabulate import tabulate
import re

# Function to perform search on PubMed
def search_pubmed(term):
    try:
        # Build PubMed search URL
        url = f"https://pubmed.ncbi.nlm.nih.gov/?term={term}"
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # Raise error for bad responses
    except requests.RequestException as e:
        print(f"Network error occurred: {e}")
        return []

    # Parse the HTML response
    soup = BeautifulSoup(response.text, 'html.parser')
    results = soup.find_all('article', class_='full-docsum')

    papers = []

    # Extract title and author from each article
    for article in results:
        title_tag = article.find('a', class_='docsum-title')
        title = title_tag.get_text(strip=True) if title_tag else "No title found"

        author_tags = article.find_all('span', class_='docsum-authors short-authors')
        authors = ', '.join(tag.get_text(strip=True) for tag in author_tags) if author_tags else "No authors listed"

        papers.append({"Title": title, "Authors": authors})

    return papers

# Function to save extracted results to a CSV file
def save_to_csv(papers, filename="pubmed_results.csv"):
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=["Title", "Authors"])
        writer.writeheader()
        writer.writerows(papers)

# Main entry point of the program
def main():
    # Handle command-line arguments
    parser = argparse.ArgumentParser(description="Search PubMed and export articles to CSV.")
    parser.add_argument("term", type=str, help="Search term for PubMed")
    args = parser.parse_args()

    # Step 5: Input validation
    if not args.term.strip():
        print("Error: Search term cannot be empty.")
        exit(1)

    if not re.match(r"^[a-zA-Z0-9\s\-]+$", args.term):
        print("Error: Search term contains invalid characters. Use only letters, numbers, spaces, and dashes.")
        exit(1)

    # Perform the search
    papers = search_pubmed(args.term)

    if not papers:
        print("No papers found or an error occurred.")
        return

    # Display results in a nice table
    print(tabulate(papers, headers="keys", tablefmt="fancy_grid"))

    # Save results to CSV file
    save_to_csv(papers)
    print("Results saved to pubmed_results.csv")


if __name__ == "__main__":
    main()
