# Question 1

data pipeline from json files to PostgreSQL

## Dependecies

- pip
- psycopg2
- localhost PostgreSQL server
- Jupyter Notebook (training data)
- Pandas
- Numpy

## Insert JSON files into PostgreSQL table

Full Code in main.py files. Below is explanation per chang in Jupyter Notebook from the main.py code to insert the json field into PostgreSQL tables (complex,tower,unit)

### Insert JSON complex.json into complex table on PostgreSQL table

import the dependencies from what we use to training the data

```python
import pandas as pd
import numpy as np
import json
from sqlalchemy import create_engine
```
open the json files and make it into pandas dataframe 

```python
df = open('/home/jodie/Downloads/test/de_task (1)/complex.json')
data = df.read()
```
clean the data so pandas can read and insert to json dataframe 

```python
df = data.replace('ObjectId(','').\
replace('NumberLong(','').\
replace(')','').\
replace('\n','').\
replace('/* ', '')
```
after that, clean the command lines ```/* 1 */``` and change into ```\n``` so pandas can read the json files for new row

```
i = 0
while i < 10:
    df = df.replace(str(i)+' */','')
    i += 1
i = 0
while i < 10:
    df = df.replace(str(i)+' */','')
    i += 1
i = 0
while i < 10:
    df = df.replace(str(i)+'{','{')
    df = df.replace('}{','}\n{')
    i += 1
```

after the cleaning, the dataframe can load json and clean the null values and name the dataframe into "complex"
```
complex = pd.read_json(df,lines=True)
complex = complex.fillna('')
```

first thing we have to do is clean the value from dataframe 
```
complex['unit_rent_total']=np.where(complex['unit_rent_total']=='', 0,0)
complex['unit_sell_total']=np.where(complex['unit_sell_total']=='', 0,0)
complex['status']=np.where(complex['status']=='', 1,0)
complex['service_types'] = [','.join(map(str, l)) for l in complex['service_types']]
complex['premium_listing_available']=np.where(complex['premium_listing_available']=='', 0,0)
```

change the data types so the postgres can read the datatypes 
```
complex['_id'] = complex['_id'].astype('string') 
complex['category'] = complex['category'].astype('string') 
complex['name'] = complex['name'].astype('string') 
complex['developer_name'] = complex['developer_name'].astype('string') 
complex['address_street'] = complex['address_street'].astype('string') 
complex['address_city'] = complex['address_city'].astype('string') 
complex['address_subdistrict'] = complex['address_subdistrict'].astype('string') 
complex['address_urban'] = complex['address_urban'].astype('string') 
complex['address_province'] = complex['address_province'].astype('string') 
complex['address_zip'] = complex['address_zip'].astype('int64') 
complex['address_coordinate'] = complex['address_coordinate'].astype('string') 
complex['create_by_uid'] = complex['create_by_uid'].astype('string') 
complex['facilities'] = complex['facilities'].astype('string') 
complex['images'] = complex['images'].astype('string') 
complex['id'] = complex['id'].astype('string') 
complex['tower_total'] = complex['tower_total'].astype('int64') 
complex['branches'] = complex['branches'].astype('string') 
complex['unit_rent_total'] = complex['unit_rent_total'].astype('int64') 
complex['unit_sell_total'] = complex['unit_sell_total'].astype('int64') 
complex['developer_legal_name'] = complex['developer_legal_name'].astype('string') 
complex['land_size'] = complex['land_size'].astype('int64') 
complex['last_update_at'] = complex['last_update_at'].astype('datetime64[ns]') 
complex['last_update_by_uid'] = complex['last_update_by_uid'].astype('string') 
complex['address_country'] = complex['address_country'].astype('string') 
complex['surrounding_area'] = complex['surrounding_area'].astype('string') 
complex['address_area'] = complex['address_area'].astype('string') 
complex['create_at'] = complex['create_at'].astype('string') 
complex['status'] = complex['status'].astype('int64') 
complex['code'] = complex['code'].astype('string') 
complex['service_types'] = complex['service_types'].astype('string') 
complex['premium_listing_available'] = complex['premium_listing_available'].astype('int64') 
```

change the format of images column so the postgres can read the column as json field
```
complex['images'] = complex['images'].astype(str).str.replace("'",'"', regex=False)
complex['images'] = complex['images'].astype(str).str.replace("None",'"None"', regex=False)
complex['images'] = complex['images'].astype(str).str.replace('Children"s','childrens', regex=False)
```

finally the dataset is ready to insert into PostgreSQL complex table
```
engine = create_engine('postgresql://admin:admin@localhost:5432/postgres')
complex.to_sql('complex',engine, if_exists='replace', method=None)
```


## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
