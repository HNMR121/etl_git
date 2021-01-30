import pandas as pd



df = pd.read_csv('ReportInvoiceLines2.csv',
                 sep=',', encoding='',
                 parse_dates=['Дата'],
                 na_values='.')
                       # converters={'Номенклатура': object})
#                        # index_col='Date')

print(df.info())