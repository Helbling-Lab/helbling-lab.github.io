from scholarly import scholarly
import yaml

USER_ID = "Pwd7hJYAAAAJ"
author = scholarly.search_author_id(USER_ID)
author = scholarly.fill(author, sections=['publications'])

pubs = []
# Sort publications by year (descending), then take the 5 most recent
publications = author['publications']
publications = sorted(publications, key=lambda p: p['bib'].get('pub_year', ''), reverse=True)[:5]

for pub in publications:
    bib = pub['bib']
    print(bib)  # Add this line to inspect available fields

    author_pub_id = pub.get('author_pub_id', '')
    scholar_link = (
        f"https://scholar.google.com/citations?view_op=view_citation&hl=en&user={USER_ID}&citation_for_view={author_pub_id}"
        if author_pub_id else ''
    )
    pubs.append({
        'title': bib.get('title', ''),
        'authors': bib.get('author', ''),
        'year': bib.get('pub_year', ''),
        'venue': bib.get('venue', ''),
        'url': pub.get('pub_url', ''),
        'link': bib.get('eprint_url', pub.get('pub_url', '')),
        'scholar_link': scholar_link,
        'description': '',  # For manual entry
    })

with open('_data/pubs.yml', 'w') as f:
    yaml.dump(pubs, f, allow_unicode=True)