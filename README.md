# pyBSDate
> Library to convert BS date to AD date.

![PyPI](https://img.shields.io/pypi/v/pyBSDate)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/pyBSDate)
![PyPI - Downloads](https://img.shields.io/pypi/dm/pyBSDate)
[![GitHub license](https://img.shields.io/github/license/SushilShrestha/pyBSDate)](https://github.com/SushilShrestha/pyBSDate/blob/master/License)


<img src="http://admin.shresthasushil.com.np/static/nepalidate/today.gif" width=300/>


Python implementation of Date conversion From Bikram Sambat(BS) to English Date(AD) and viceversa.
Conversion is done with the help of date mappings so conversion limited to 1971-2100 BS.


## Installation

If you have pip installed, simply
```
pip install pyBSDate
```

OR from source:
1. Get a copy of the project. Download zip of the project or clone this repo:
```
git clone https://github.com/SushilShrestha/pyBSDate
``` 
2. Open your terminal, navigate to the project folder and type
```
python setup.py install
```


## Usage
#### Using functions
```python
# Convert BS Date to AD
from pyBSDate import convert_BS_to_AD
ad_date = convert_BS_to_AD(2072, 1, 10)
print(ad_date)

# Convert AD Date to BS
from pyBSDate import convert_AD_to_BS
bs_date = convert_AD_to_BS(2015, 4, 23)
print(bs_date)
```

#### Class based wrappers
`bsdate` and `addate` classes are available for the date conversion. They inherit from the parent `datetime.date` class and all the functions are similar to `datetime.date` class. 

Following is the example of using the class based date.
```python
from pyBSDate import bsdate

ne_date = bsdate(2077, 2, 32)
print(ne_date.strftime("%B %d %Y, %A", lang='ne'))       # जेष्ठ ३२ २०७७, आइतबार

en_date = ne_date.addate
print (en_date.strftime("%B %d %Y, %A"))                # June 14 2020, Sunday
```

Two date objects can also be compared 
```python
import datetime
from pyBSDate import bsdate, addate

ne_date = bsdate(2077, 2, 32)
en_date = addate(2010, 1, 12)

if ne_date > en_date:
    print(ne_date.isoformat(lang='ne'))
```

Addition or substraction of `timedelta` is supported 
```python
ne_date = ne_date + datetime.timedelta(days=2)
```
For detailed information, refer to docs.

## Development setup
#### Running test
```bash
python -m unittest discover
```

## Release History
* 0.3.0rc
    * add class based wrapper for date conversion
    * update documentations
* 0.2.*
    * function based date conversion

## Meta

Distributed under the MIT license. See ``LICENSE`` for more information.

> Date mapping data taken from 
https://github.com/bahadurbaniya/Date-Converter-Bikram-Sambat-to-English-Date


## Contributing

#### Creating a pull request
1. Fork it (<https://github.com/SushilShrestha/pyBSDate/fork>)
2. Create your feature branch (`git checkout -b feature/fooBar`)
3. Commit your changes (`git commit -am 'Add some fooBar'`)
4. Push to the branch (`git push origin feature/fooBar`)
5. Create a new Pull Request

#### Submit a Bug Report
The software might include bugs, if you find one help us improve the software by reporting it as an issue (<https://github.com/SushilShrestha/pyBSDate/issues>) or send us a pull request with the solution. 

Peace ✌



