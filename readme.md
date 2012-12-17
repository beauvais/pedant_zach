Here is a quick, Python scraperwiki script (it's home [here][1]) to search a wordpress blog for a single keyword, returning the resulting links into scraperwiki's sqlite store.

The script is setup to look for posts containint the word *pedantry*, and to run on http://zachbeauvais.com.

Changing the variables *site* and *term* to another wordpress blog and keyword respectively should let you return the same kinds of results on any standard WP blog.

The data structure is very simple, the search page displays a list of <code><h1></code> tags containing linked title text for each post matching the search.

The results are stored in python dict form with three keys:

<code>
    data = {
    
        'uri': link[0].attrib['href'],
        
        'post-title': str(text),
        
        'search-term': str(term)
        
    }
    </code>
    
[1]: https://scraperwiki.com/scrapers/search_zachs_blog_for_pedantry/