
import requests

response = requests.get('https://api.nytimes.com/svc/search/v2/articlesearch.json?begin_date=20120101&q={query}&api-key=AQ7HzqoGRaAzP4KGMWebITYkHEHy8wbk',
                    params={'query': 'New York City'})

data = response.json()

res = data["response"]["docs"][0]

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
print('*********************************')
# print(res)
print(headline)
print(snippet)
print(paragraph)
print(author)
print(source)
print('*********************************')




# import requests

# def execute():
#   requestUrl = "https://api.nytimes.com/svc/search/v2/articlesearch.json?begin_date=20120101&q=weather&api-key=AQ7HzqoGRaAzP4KGMWebITYkHEHy8wbk"
#   requestHeaders = {
#     "Accept": "application/json"
#   }

#   response = requests.get(requestUrl, headers=requestHeaders)

#   print(response.text)

# if __name__ == "__main__":
#   execute()
