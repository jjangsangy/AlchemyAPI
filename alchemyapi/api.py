from __future__ import print_function

import collections
import requests
import sys
import re

from .compat import urlencode
from .auth import Client

__all__ = ['HTTPURLEndpoints', 'AlchemyAPI', 'Client']

class HTTPURLEndpoints(collections.defaultdict):

    def __getattr__(self, key):
        try:
            return self.__dict__[key]
        except KeyError:
            return self.__getitem__(key)

    def __setattr__(self, name, value):
        if hasattr(HTTPURLEndpoints, name):
            raise AttributeError()
        else:
            self[name] = value

    def __getitem__(self, name):
        if name not in self:
            self[name] = HTTPURLEndpoints()
        return super(HTTPURLEndpoints, self).__getitem__(name)

    def serialize(self):
        base = {}
        _prune = [
            '_ipython_display_',
            '_getAttributeNames',
            '_ipython_canary_method_should_not_exist_',
            'trait_names',
        ]
        for word in _prune:
            if word in self:
                self.pop(word)
        for key, value in self.items():
            if isinstance(value, type(self)):
                base[key] = value.serialize()
            elif isinstance(value, (list, tuple)):
                base[key] = type(value)(
                    item.serialize() if isinstance(item, type(self)) else
                    item for item in value)
            else:
                base[key] = value
        return base

    @classmethod
    def build_endpoints(cls):

        webapi = HTTPURLEndpoints()

        webapi.sentiment.url  = '/url/URLGetTextSentiment'
        webapi.sentiment.text = '/text/TextGetTextSentiment'
        webapi.sentiment.html = '/html/HTMLGetTextSentiment'
        webapi.sentiment_targeted.url  = '/url/URLGetTargetedSentiment'
        webapi.sentiment_targeted.text = '/text/TextGetTargetedSentiment'
        webapi.sentiment_targeted.html = '/html/HTMLGetTargetedSentiment'
        webapi.author.url     = '/url/URLGetAuthor'
        webapi.author.html    = '/html/HTMLGetAuthor'
        webapi.keywords.url   = '/url/URLGetRankedKeywords'
        webapi.keywords.text  = '/text/TextGetRankedKeywords'
        webapi.keywords.html  = '/html/HTMLGetRankedKeywords'
        webapi.concepts.url   = '/url/URLGetRankedConcepts'
        webapi.concepts.text  = '/text/TextGetRankedConcepts'
        webapi.concepts.html  = '/html/HTMLGetRankedConcepts'
        webapi.entities.url   = '/url/URLGetRankedNamedEntities'
        webapi.entities.text  = '/text/TextGetRankedNamedEntities'
        webapi.entities.html  = '/html/HTMLGetRankedNamedEntities'
        webapi.category.url   = '/url/URLGetCategory'
        webapi.category.text  = '/text/TextGetCategory'
        webapi.category.html  = '/html/HTMLGetCategory'
        webapi.relations.url  = '/url/URLGetRelations'
        webapi.relations.text = '/text/TextGetRelations'
        webapi.relations.html = '/html/HTMLGetRelations'
        webapi.language.url   = '/url/URLGetLanguage'
        webapi.language.text  = '/text/TextGetLanguage'
        webapi.language.html  = '/html/HTMLGetLanguage'
        webapi.text.url       = '/url/URLGetText'
        webapi.text.html      = '/html/HTMLGetText'
        webapi.text_raw.url   = '/url/URLGetRawText'
        webapi.text_raw.html  = '/html/HTMLGetRawText'
        webapi.title.url      = '/url/URLGetTitle'
        webapi.title.html     = '/html/HTMLGetTitle'
        webapi.feeds.url      = '/url/URLGetFeedLinks'
        webapi.feeds.html     = '/html/HTMLGetFeedLinks'
        webapi.microformats.url  = '/url/URLGetMicroformatData'
        webapi.microformats.html = '/html/HTMLGetMicroformatData'
        webapi.combined.url  = '/url/URLGetCombinedData'
        webapi.combined.text = '/text/TextGetCombinedData'
        webapi.image.url        = '/url/URLGetImage'
        webapi.imagetagging.url = '/url/URLGetRankedImageKeywords'
        webapi.imagetagging.image = '/image/ImageGetRankedImageKeywords'
        webapi.facetagging.url    = '/url/URLGetRankedImageFaceTags'
        webapi.facetagging.image  = '/image/ImageGetRankedImageFaceTags'
        webapi.taxonomy.url  = '/url/URLGetRankedTaxonomy'
        webapi.taxonomy.html = '/html/HTMLGetRankedTaxonomy'
        webapi.taxonomy.text = '/text/TextGetRankedTaxonomy'

        return webapi.serialize()

class AlchemyAPI:

    def __init__(self, client, base='http://access.alchemyapi.com/calls'):
        self.base     = base
        self.client   = client
        self.session  = requests.session()
        self.endpoints = HTTPURLEndpoints.build_endpoints()

    def __repr__(self):
        classname = self.__class__.__name__
        return '%s(%r)' % (classname, self.client)

    def interface(self, context, flavor, data, **options):
        if context not in self.endpoints:
            return {
                'status' : 'ERROR',
                'statusInfo': 'endpoint {e} not available'.format(e=context)
            }

        # Make sure this request supports this flavor
        if flavor not in self.endpoints.get(context, ''):
            return {
                'status': 'ERROR',
                'statusInfo': 'clean text extraction for {flavor} not available'.format(flavor=flavor)
            }

        # add the data to the options and analyze
        options[flavor] = data

        return self.connect(self.endpoints[context][flavor], options)

    def connect(self, endpoint, params, post_data=bytearray()):
        """
        HTTP Request wrapper that is called by the endpoint functions. This function is not intended to be called through an external interface.
        It makes the call, then converts the returned JSON string into a Python object.

        INPUT:
        url -> the full URI encoded url

        OUTPUT:
        The response, already converted from JSON to a Python object.
        """

        # Add the API Key and set the output mode to JSON
        params['apikey'] = self.client.key
        params['outputMode'] = 'json'
        # Insert the base url


        post_url = ""
        try:
            post_url = self.base + endpoint + '?' + urlencode(params).encode('utf-8')
        except TypeError:
            post_url = self.base + endpoint + '?' + urlencode(params)

        results = ""
        try:
            results = self.session.post(url=post_url, data=post_data)
        except Exception as e:
            print(e, file=sys.stderr)
            return {'status': 'ERROR', 'statusInfo': 'network-error'}

        try:
            return results.json()
        except Exception as e:
            if results != "":
                print(results, file=sys.stderr)
            print(e, file=sys.stderr)
            return {'status': 'ERROR', 'statusInfo': 'parse-error'}
