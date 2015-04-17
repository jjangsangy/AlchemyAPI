from __future__ import print_function

import sys
import os
import nose

try:
    import unittest2 as unittest
except ImportError:
    import unittest

from ..api import AlchemyAPI

__all__ = ['TestAPI']

test_text = 'Bob broke my heart, and then made up this silly sentence to test the PHP SDK'
test_html = '<html><head><title>The best SDK Test | AlchemyAPI</title></head><body><h1>Hello World!</h1><p>My favorite language is PHP</p></body></html>'
test_url = 'http://www.nytimes.com/2013/07/13/us/politics/a-day-of-friction-notable-even-for-a-fractious-congress.html?_r=0'
test_jpg = 'pigeon.jpg'


class TestAPI(unittest.TestCase):

    def setUP(self):
        if not 'ALCHEMY_API_KEY' in os.environ:
            raise AssertionError('API Key needed to run Unit Tests')
        KEY = of.environ.get('ALCHEMY_API_KEY')
        self.key = AlchemyAPI(KEY)

    def tearDown(self):
        del self.key

    # Entities
    def test_entities(self):
        print('Checking entities . . . ')
        response = alchemyapi.entities('text', test_text)
        self.assertTrue(response['status'] == 'OK')
        response = alchemyapi.entities('html', test_html)
        self.assertTrue(response['status'] == 'OK')
        response = alchemyapi.entities('url', test_url)
        self.assertTrue(response['status'] == 'OK')
        response = alchemyapi.entities('random', test_url)
        self.assertTrue(response['status'] == 'ERROR')  # invalid flavor
        print('Entity tests complete!')
        print('')


    # Keywords
    def test_keywords(self):
        print('Checking keywords . . . ')
        response = alchemyapi.keywords('text', test_text)
        self.assertTrue(response['status'] == 'OK')
        response = alchemyapi.keywords('html', test_html)
        self.assertTrue(response['status'] == 'OK')
        response = alchemyapi.keywords('url', test_url)
        self.assertTrue(response['status'] == 'OK')
        response = alchemyapi.keywords('random', test_url)
        self.assertTrue(response['status'] == 'ERROR')  # invalid flavor
        print('Keyword tests complete!')
        print('')


    # Concepts
    def test_concepts(self):
        print('Checking concepts . . . ')
        response = alchemyapi.concepts('text', test_text)
        self.assertTrue(response['status'] == 'OK')
        response = alchemyapi.concepts('html', test_html)
        self.assertTrue(response['status'] == 'OK')
        response = alchemyapi.concepts('url', test_url)
        self.assertTrue(response['status'] == 'OK')
        response = alchemyapi.concepts('random', test_url)
        self.assertTrue(response['status'] == 'ERROR')  # invalid flavor
        print('Concept tests complete!')
        print('')


    # Sentiment
    def test_sentiment(self):
        print('Checking sentiment . . . ')
        response = alchemyapi.sentiment('text', test_text)
        self.assertTrue(response['status'] == 'OK')
        response = alchemyapi.sentiment('html', test_html)
        self.assertTrue(response['status'] == 'OK')
        response = alchemyapi.sentiment('url', test_url)
        self.assertTrue(response['status'] == 'OK')
        response = alchemyapi.sentiment('random', test_url)
        self.assertTrue(response['status'] == 'ERROR')  # invalid flavor
        print('Sentiment tests complete!')
        print('')


    # Targeted Sentiment
    def test_target_sentiment(self):
        print('Checking targeted sentiment . . . ')
        response = alchemyapi.sentiment_targeted('text', test_text, 'heart')
        self.assertTrue(response['status'] == 'OK')
        response = alchemyapi.sentiment_targeted('html', test_html, 'language')
        self.assertTrue(response['status'] == 'OK')
        response = alchemyapi.sentiment_targeted('url', test_url, 'Congress')
        self.assertTrue(response['status'] == 'OK')
        response = alchemyapi.sentiment_targeted('random', test_url, 'Congress')
        self.assertTrue(response['status'] == 'ERROR')  # invalid flavor
        response = alchemyapi.sentiment_targeted('text', test_text,  None)
        self.assertTrue(response['status'] == 'ERROR')  # missing target
        print('Targeted sentiment tests complete!')
        print('')


    # Text
    def test_text(self):
        print('Checking text . . . ')
        response = alchemyapi.text('text', test_text)
        self.assertTrue(response['status'] == 'ERROR')  # only works for html and url content
        response = alchemyapi.text('html', test_html)
        self.assertTrue(response['status'] == 'OK')
        response = alchemyapi.text('url', test_url)
        self.assertTrue(response['status'] == 'OK')
        print('Text tests complete!')
        print('')


    # Text Raw
    def test_raw(self):
        print('Checking raw text . . . ')
        response = alchemyapi.text_raw('text', test_text)
        self.assertTrue(response['status'] == 'ERROR')  # only works for html and url content
        response = alchemyapi.text_raw('html', test_html)
        self.assertTrue(response['status'] == 'OK')
        response = alchemyapi.text_raw('url', test_url)
        self.assertTrue(response['status'] == 'OK')
        print('Raw text tests complete!')
        print('')


    # Author
    def test_author(self):
        print('Checking author . . . ')
        response = alchemyapi.author('text', test_text)
        self.assertTrue(response['status'] == 'ERROR')  # only works for html and url content
        response = alchemyapi.author('html', test_html)
        self.assertTrue(response['status'] == 'ERROR')  # there's no author in the test HTML
        response = alchemyapi.author('url', test_url)
        self.assertTrue(response['status'] == 'OK')
        print('Author tests complete!')
        print('')


    # Language
    def test_language(self):
        print('Checking language . . . ')
        response = alchemyapi.language('text', test_text)
        self.assertTrue(response['status'] == 'OK')
        response = alchemyapi.language('html', test_html)
        self.assertTrue(response['status'] == 'OK')
        response = alchemyapi.language('url', test_url)
        self.assertTrue(response['status'] == 'OK')
        response = alchemyapi.language('random', test_url)
        self.assertTrue(response['status'] == 'ERROR')  # invalid flavor
        print('Language tests complete!')
        print('')


    # Title
    def test_title(self):
        print('Checking title . . . ')
        response = alchemyapi.title('text', test_text)
        self.assertTrue(response['status'] == 'ERROR')  # only works for html and url content
        response = alchemyapi.title('html', test_html)
        self.assertTrue(response['status'] == 'OK')
        response = alchemyapi.title('url', test_url)
        self.assertTrue(response['status'] == 'OK')
        print('Title tests complete!')
        print('')


    # Relations
    def test_relation(self):
        print('Checking relations . . . ')
        response = alchemyapi.relations('text', test_text)
        self.assertTrue(response['status'] == 'OK')
        response = alchemyapi.relations('html', test_html)
        self.assertTrue(response['status'] == 'OK')
        response = alchemyapi.relations('url', test_url)
        self.assertTrue(response['status'] == 'OK')
        response = alchemyapi.relations('random', test_url)
        self.assertTrue(response['status'] == 'ERROR')  # invalid flavor
        print('Relation tests complete!')
        print('')


    # Category
    def test_category(self):
        print('Checking category . . . ')
        response = alchemyapi.category('text', test_text)
        self.assertTrue(response['status'] == 'OK')
        response = alchemyapi.category('html', test_html, {'url': 'test'})
        self.assertTrue(response['status'] == 'OK')
        response = alchemyapi.category('url', test_url)
        self.assertTrue(response['status'] == 'OK')
        response = alchemyapi.category('random', test_url)
        self.assertTrue(response['status'] == 'ERROR')  # invalid flavor
        print('Category tests complete!')
        print('')


    # Feeds
    def test_feeds(self):
        print('Checking feeds . . . ')
        response = alchemyapi.feeds('text', test_text)
        self.assertTrue(response['status'] == 'ERROR')  # only works for html and url content
        response = alchemyapi.feeds('html', test_html, {'url': 'test'})
        self.assertTrue(response['status'] == 'OK')
        response = alchemyapi.feeds('url', test_url)
        self.assertTrue(response['status'] == 'OK')
        print('Feed tests complete!')
        print('')


    # Microformats
    def test_microformats(self):
        print('Checking microformats . . . ')
        response = alchemyapi.microformats('text', test_text)
        self.assertTrue(response['status'] == 'ERROR')  # only works for html and url content
        response = alchemyapi.microformats('html', test_html, {'url': 'test'})
        self.assertTrue(response['status'] == 'OK')
        response = alchemyapi.microformats('url', test_url)
        self.assertTrue(response['status'] == 'OK')
        print('Microformat tests complete!')
        print('')
        print('')

    # imagetagging
    def test_imagetagging(self):
        print('Checking imagetagging . . . ')
        response = alchemyapi.imageTagging('text', test_text)
        self.assertTrue(response['status'] == 'ERROR')
        response = alchemyapi.imageTagging('html', test_html)
        self.assertTrue(response['status'] == 'ERROR')
        response = alchemyapi.imageTagging('url', test_url)
        self.assertTrue(response['status'] == 'OK')
        response = alchemyapi.imageTagging('image', test_jpg)
        self.assertTrue(response['status'] == 'OK')
        print('Image tagging tests complete!')
        print('')
        print('')

    # combined
    def test_combined(self):
        print('Checking combined . . . ')
        response = alchemyapi.combined('text', test_text)
        self.assertTrue(response['status'] == 'OK')
        response = alchemyapi.combined('html', test_html)
        self.assertTrue(response['status'] == 'ERROR')
        response = alchemyapi.combined('url', test_url)
        self.assertTrue(response['status'] == 'OK')
        print('Combined tests complete!')
        print('')
        print('')

    # taxonomy
    def test_taxonomy(self):
        print('Checking taxonomy . . . ')
        response = alchemyapi.taxonomy('text', test_text)
        self.assertTrue(response['status'] == 'OK')
        response = alchemyapi.taxonomy('html', test_html, {'url': 'test'})
        self.assertTrue(response['status'] == 'OK')
        response = alchemyapi.taxonomy('url', test_url)
        self.assertTrue(response['status'] == 'OK')
        print('Taxonomy tests complete!')
        print('')
        print('')

    # image
    def test_image_extraction(self):
        print('Checking image extraction . . . ')
        response = alchemyapi.imageExtraction('text', test_text)
        self.assertTrue(response['status'] == 'ERROR')
        response = alchemyapi.imageExtraction('html', test_html)
        self.assertTrue(response['status'] == 'ERROR')
        response = alchemyapi.imageExtraction('url', test_url)
        self.assertTrue(response['status'] == 'OK')
        print('Image Extraction tests complete!')
        print('')
        print('')


if __name__ == '__main__':
    _stdout = sys.stdout
    sys.stdout = open(os.devnull, 'w')
    nose.main()
    sys.stdout = _stdout
    print('**** All tests complete! ****')
