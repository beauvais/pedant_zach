import requests
import scraperwiki
import lxml.html

'''Idea is to generate a list of links to
blog posts containing a search term
(variable: term)
'''

# The search pattern for URI's in Wordpress is:
# http://zachbeauvais.com/?s=search_term&submit=Search


term = "pedantry"
site = "http://zachbeauvais.com"

payload = {'s': str(term), 'submit': 'Search'}
r = requests.get(site, params=payload)
html = r.text
root = lxml.html.fromstring(html)

for el in root.cssselect("h1.entry-title a"):
    link = el.cssselect("a")
    text = el.text_content()
    data = {
        'uri': link[0].attrib['href'],
        'post-title': str(text),
        'search-term': str(term)
    }
    if el is not None:
        print link
        print text
        print data
        scraperwiki.sqlite.save(unique_keys=['uri'], data=data)
    else:
        print "No results."
