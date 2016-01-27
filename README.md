# pyBSDate
Python implementation of Date conversion From Bikram Sambat(BS) to English Date(AD) and viceversa.
Conversion is done with the help of date mappings so conversion limited to certain range of date.

###Installation Instruction
1. Get copy of the project. Get zip of the project or ```git clone https://github.com/SushilShrestha/pyBSDate```  from your terminal
2. Go to your terminal, navigate to the project folder and type
```python setup.py install```
3. Validate from your python console.
```import pyBSDate```

###Usage
```python
#Convert BS Date to AD
from pyBSDate import convert_BS_to_AD
adDate = convert_BS_to_AD(2072, 1, 10)
print adDate

#Convert AD Date to BS
from pyBSDate import convert_AD_to_BS
bsDate = convert_AD_to_BS(2015, 4, 23)
print bsDate
```
Date mapping data taken from 
https://github.com/bahadurbaniya/Date-Converter-Bikram-Sambat-to-English-Date
