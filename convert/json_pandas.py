import pandas as pd

df = pd.read_json('data.json', encoding='windows-1251')
print(df.info())