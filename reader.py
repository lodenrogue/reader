import sys
import requests
from bs4 import BeautifulSoup

def extract_paragraphs(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    paragraphs = soup.find_all('p')

    for paragraph in paragraphs:
        text = paragraph.get_text()
        cleaned = text.replace('\n', ' ')
        print(cleaned)

# Check if the URL argument is provided
if len(sys.argv) < 2:
    print("Please provide a URL as an argument.")
    sys.exit(1)

# Extract the URL from the command-line argument
url = sys.argv[1]
extract_paragraphs(url)

