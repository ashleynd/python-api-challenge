from flask import Flask, render_template, request
import requests

"""
Squirro Coding Challenge
May 2022
"""

app = Flask(__name__)

@app.route('/')
def connect():
    return render_template("search_form.html")

def disconnect(self):
        """Disconnect from the source."""
        # Nothing to do
        pass

def getDataBatch(search_query):
    res = requests.get(f"https://api.nytimes.com/svc/search/v2/articlesearch.json?begin_date=20120101&q={search_query}&api-key=AQ7HzqoGRaAzP4KGMWebITYkHEHy8wbk", params={'query': 'water', 'query': search_query})

    data = res.json()
    # results = data["response"]["docs"]

    abstract = data["response"]["docs"][0]["abstract"]
    url = data["response"]["docs"][0]["web_url"]
    snippet = data["response"]["docs"][0]["snippet"]
    paragraph = data["response"]["docs"][0]["lead_paragraph"]
    source = data["response"]["docs"][0]["source"]
    multimedia = data["response"]["docs"][0]["multimedia"][0]
    headline = data["response"]["docs"][0]["headline"]["main"]
    keyword = data["response"]["docs"][0]["keywords"][0]["value"]
    publish_date = data["response"]["docs"][0]["pub_date"]
    author = data["response"]["docs"][0]["byline"]["original"]
    id = data["response"]["docs"][0]["_id"]
    uri = data["response"]["docs"][0]["uri"]
    # print('*********************************')
    # print(snippet, author)
    # print('*********************************')

    results = {
        'abstract': abstract,
        'url': url,
        'headline': headline,
        'snippet': snippet, 
        'paragraph': paragraph,
        'source': source,
        'publish_date': publish_date,
        'author': author,
        'keyword': keyword,
        'id': id,
        'uri': uri,
        'multimedia': multimedia
        }
    return results

@app.route('/search_results')
def getSchema():
    search_query = request.args["search_query"]
    results = getDataBatch(search_query)
    return render_template("search_form.html", results=results)
