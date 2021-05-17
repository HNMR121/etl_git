import requests
import pandas as pd
import datetime as dt

url = 'https://www.fedstat.ru/indicator/dataGrid.do?id=31328'
response = requests.get(url,headers=headers)
dict_ross = response.json()['results']
df = pd.DataFrame(columns=['region_name','year','product_type','volume'])
for i in dict_ross:
    for key, value in i.items():
        if key.split('dim')[1].split('_')[0]!='57831':
            region = i['dim57831']
            year = key.split('dim')[1].split('_')[0]
            df = df.append({'region_name': region,'year':year,'product_type':'Вся посевная площадь','volume':value}, ignore_index=True)
            
df['volume'] = df['volume'].replace(r',',  '.', regex=True).astype(float)
df['period_begin'] = df['year'].apply(lambda x: dt.datetime.strptime('01.01.' + x,'%d.%m.%Y'))
df['period_end'] = df['year'].apply(lambda x: dt.datetime.strptime('31.12.' + x,'%d.%m.%Y'))
df['year'] = df['year'].astype(int)
cols = ['region_name',
 'year',
 'period_begin',
 'period_end',
 'product_type',
 'volume']
df = df[cols]

import sqlalchemy
engine = sqlalchemy.create_engine("mssql+pyodbc://@{LT-FADEEV\SQLEXPRESS}/{Test}?driver=SQL+Server+Native+Client+11.0?trusted_connection=yes")
df.to_sql(r'rosst',con = engine,\
        if_exists='replace',\
        index = False
            )

