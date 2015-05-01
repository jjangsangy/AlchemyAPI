Python AlchemyAPI Client
=========================
|Documentation| |github| |travis|

A Pythonic interface for IBM Deep Learning with AlchemyAPI

AlchemyAPI is a text analysis and computer vision service utilizing
deep learning-based artificial intelligence technologies that runs on IBM.

Quickstart Guide
================

Requirements
-------------
The Python library requires that you install the `Requests <http://docs.python-requests.org/en/latest>`__ Python module.


Install dependencies

.. code-block:: bash

    pip install -r requirements.txt

Getting Started with the Python SDK
-----------------------------------

To get started and run the example, simply:

Installation
~~~~~~~~~~~~

.. code-block:: bash

    git clone https://github.com/jjangsangy/AlchemyAPI.git && cd AlchemyAPI
    python setup.py install


Quickstart
~~~~~~~~~~~

Image Tagging


.. code-block:: python

   import json
   import os
   from alchemyapi import AlchemyAPI, Auth

   API_KEY = os.environ.get("ALCHEMY_API_KEY")

   auth = Auth(API_KEY)
   api  = AlchemyAPI(auth)

   with open('the-tree-and-the-stars.jpg', 'rb') as night_sky:
       tagging = api.interface('image_tagging', 'image', night_sky.sky.read(), imagePostMode='raw')

   json.dumps(tagging)

    {
      "status": "OK",
      "url": "http://demo1.alchemyapi.com//images/uploads/The-tree-and-the-stars.jpg",
      "totalTransactions": "4",
      "imageKeywords": [
        {
          "text": "star",
          "score": "0.999991"
        },
        {
          "text": "trail",
          "score": "0.99593"
        },
        {
          "text": "night",
          "score": "0.970688"
        },
        {
          "text": "sky",
          "score": "0.598688"
        },
        {
          "text": "star trails",
          "score": "0.524979"
        }
      ]
    }

.. image:: ./static/The-tree-and-the-stars.jpg

.. |Documentation| image:: https://readthedocs.org/projects/alchemyapi/badge/?version=master
   :target: https://readthedocs.org/projects/alchemyapi/?badge=latest

.. |github| image:: https://badge.fury.io/gh/jjangsangy%2FAlchemyAPI.svg
   :target: http://badge.fury.io/gh/jjangsangy%2FAlchemyAPI

.. |travis| image:: https://travis-ci.org/jjangsangy/AlchemyAPI.svg?branch=master
   :target: https://travis-ci.org/jjangsangy/AlchemyAP
