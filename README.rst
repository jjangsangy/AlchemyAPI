Python AlchemyAPI Client
=========================
A Pythonic interface for IBM Deep Learning with AlchemyAPI

AlchemyAPI is a text analysis and computer vision service utilizing
deep learning-based artificial intelligence technologies that runs on IBM.

Quickstart Guide
================

Requirements
-------------
The Python library requires that you install the `Requests`_ Python module.

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
   from alchemyapi import AlchemyAPI, Auth

   auth = Auth('$API_KEY')
   api  = AlchemyAPI(auth)

   with open('the-tree-and-the-stars.jpg', 'rb') as night_sky:
       tagging = api.interface('image_tagging', 'image', night.sky.read(), imagePostMode='raw')

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

