.. pyBSDate documentation master file, created by
   sphinx-quickstart on Mon Jun 15 10:02:16 2020.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to pyBSDate's documentation!
====================================
   Library to convert BS date to AD date.

.. code-block:: python
   from pyBSDate import convert_BS_to_AD
   ad_date = convert_BS_to_AD(2072, 1, 10)
   print(ad_date)

   # Convert AD Date to BS
   from pyBSDate import convert_AD_to_BS
   bs_date = convert_AD_to_BS(2015, 4, 23)
   print(bs_date)

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   introduction
   installation
   quickstart
   reference

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
