import requests
from bs4 import BeautifulSoup
import markdown

def fetch_publications(scholar_id):
    url = f"https://scholar.google.com/citations?hl=en&user=3mSNkMkAAAAJ&view_op=list_works&authuser=1&sortby=pubdate"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    publications = []
    for item in soup.select('.gsc_a_tr'):
        title = item.select_one('.gsc_a_t a').text
        authors = item.select_one('.gsc_a_t .gs_gray').text
        year = item.select_one('.gsc_a_y').text
        link = 'https://scholar.google.com' + item.select_one('.gsc_a_t a')['href']
        publications.append((title, authors, year, link))

    return publications

def generate_markdown(publications):
    md_content = "# Publications\n\n"
    for title, authors, year, link in publications:
        md_content += f"### [{title}]({link})\n"
        md_content += f"{authors} - {year}\n\n"
    return md_content

if __name__ == "__main__":
    scholar_id = 'YOUR_SCHOLAR_ID'
    publications = fetch_publications(scholar_id)
    md_content = generate_markdown(publications)
    
    with open('publications.md', 'w') as f:
        f.write(md_content)
