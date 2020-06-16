Quickstart
====================================
Using functions
...................................
.. code-block:: python

    from pyBSDate import convert_BS_to_AD
    ad_date = convert_BS_to_AD(2072, 1, 10)
    print(ad_date)

    # Convert AD Date to BS
    from pyBSDate import convert_AD_to_BS
    bs_date = convert_AD_to_BS(2015, 4, 23)
    print(bs_date)



Using class
...................................
.. code-block:: python

    import datetime
    from pyBSDate import bsdate, addate

    ne_date = bsdate(2077, 2, 32)
    en_date = addate(2010, 1, 12)

    if ne_date > en_date:
        print(ne_date.isoformat(lang='ne'))

    ne_date = ne_date + datetime.timedelta(days=2)

    print(ne_date.strftime("%B %d %Y, %A", lang='ne'))       # जेष्ठ ३२ २०७७, आइतबार

