"""
Reading an excel file and extracting few columns from it.
Create a new excel file with those extracted data.
"""

import pandas as pd
import numpy as np

#store the file name
#ex_file = 'C:\Users\Akash\Desktop\some dev\POR Inventory latest.xlsx'

#Read the input file
df_file = pd.read_excel(r'C:\Users\user\Desktop\SomeDev\POR Inventory latest.xlsx',sheet_name='owssvr')

df_data = pd.DataFrame(df_file, columns = ['PVID','Project Name','Anthem IT Manager','Release Date & Month'])

year = ((df_data['Release Date & Month'] != 'TBD') & ( df_data['Release Date & Month'].str.contains('/2019')))
#year = ((df_data['Release Date & Month'] != 'TBD') & (object((list((df_data['Release Date & Month'].str.split('/'))[0][2] == '2019')))))

df_ref_data = df_data[year]

#print(df_ref_data.head())  #Display first few data

#write data in new excel sheet
writer = pd.ExcelWriter(r'C:\Users\user\Desktop\SomeDev\pandas_simple.xlsx', engine='xlsxwriter')

df_ref_data.to_excel(writer,sheet_name='info',index=0)
writer.save()
