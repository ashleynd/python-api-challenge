import argparse
import logging
import requests

"""
Skeleton for Squirro Delivery Hiring Coding Challenge
August 2021
"""


log = logging.getLogger(__name__)


class NYTimesSource(object):
    """
    A data loader plugin for the NY Times API.
    """
    headline=""
    paragraph=""
    publish_date=""
    id=""
    abstract=""
    keywords=""

    def __init__(self, headline, paragraph, publish_date, id, abstract, keywords):
            self.headline=headline
            self.paragraph=paragraph
            self.publish_date=publish_date
            self.id=id
            self.abstract=abstract
            self.keywords=keywords

    def connect(self, inc_column=None, max_inc_value=None):
        log.debug("Incremental Column: %r", inc_column)
        log.debug("Incremental Last Value: %r", max_inc_value)

    def disconnect(self):
        """Disconnect from the source."""
        # Nothing to do
        pass

    def getDataBatch(self, batch_size):
        """
        Generator - Get data from source on batches.

        :returns One list for each batch. Each of those is a list of
                 dictionaries with the defined rows.
        """
        # TODO: implement - this dummy implementation returns one batch of data


        def __str__(self):
            return f"Title {self.headline}, Body: {self.paragraph}, Created at: {self.publish_date}, Id: {self.id}, Abstract: {self.abstract}, Keywords: {self.keywords}"
        # Gather data needed from API
        yield [
            {
                "abstract": data["response"]["docs"][0]["abstract"],
                "paragraph": data["response"]["docs"][0]["lead_paragraph"],
                "headline": data["response"]["docs"][0]["headline"]["main"],
                "keywords": data["response"]["docs"][0]["keywords"][0]["value"],
                "publish_date": data["response"]["docs"][0]["pub_date"],
                "id": data["response"]["docs"][0]["_id"]
            }
        ]

    def getSchema(self):
        """
        Return the schema of the dataset
        :returns a List containing the names of the columns retrieved from the
        source
        """

        schema = [
            "title",
            "body",
            "created_at",
            "id",
            "summary",
            "abstract",
            "keywords",
        ]

        return schema


if __name__ == "__main__":
    response = requests.get('https://api.nytimes.com/svc/search/v2/articlesearch.json?begin_date=20120101&q={query}&api-key=AQ7HzqoGRaAzP4KGMWebITYkHEHy8wbk')
    data = response.json()
    config = {
        "api_key": "NYTIMES_API_KEY",
        "query": "Silicon Valley",
    }
    # Positional arguments being pass into the class 
    source = NYTimesSource('headline', 'paragraph', 'publish_date', 'id', 'abstract', 'keywords')

    # This looks like an argparse dependency - but the Namespace class is just
    # a simple way to create an object holding attributes.
    source.args = argparse.Namespace(**config)

    for idx, batch in enumerate(source.getDataBatch(10)):
        print(f"{idx} Batch of {len(batch)} items")
        for item in batch:
            print(f"  - {item['id']} - {item['headline']}")
