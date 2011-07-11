Pencil's documentation
======================

Pencil is a simple wrapper around `Graphite URL API <http://graphite.wikidot.com/url-api-reference>`_

You can report bugs and discuss features on the `issues page <https://github.com/20minutes/pencil/issues>`_.

Installation
------------

1. Either check out Pencil from Github_ or to pull a release off PyPI_ ::
   
	pip install pencil


.. _GitHub: http://github.com/20minutes/pencil
.. _PyPI: http://pypi.python.org/pypi/pencil


Usage
-----

Pencil is straightforward to use :

.. code-block:: python
	
	>>> from pencil import Pencil
	>>> pencil = Pencil(begin="-12hours").set_title("Network").add_metric("front.network.eth0.if_*").area_mode("stacked")
	>>> pencil.url("http://graphite.local/render/", 510, 318)
	'http://graphite.local/render/?fontName=Helvetica&lineMode=slope&from=-12hours&target=front.network.eth0.if_%2A&title=Network&areaMode=stacked&graphType=line&height=318&bgcolor=FFFFFF&width=510&template=alphas&fgcolor=000000'

API
---

.. autoclass:: pencil.Pencil
   	:members:

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

