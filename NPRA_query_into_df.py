
#from unittest import result
import csv
import pyodbc as odbc
import pandas as pd 
import numpy as np
from datetime import date, datetime
print('butt b')
try:
   
    conn =  odbc.connect("Driver=ODBC Driver 11 for SQL Server;Server=10.20.30.86;Database=CJR_Stage;UID=sa;Pwd=Sol@CJR!2019TR#")
except odbc.DatabaseError as e:
    print('Database error:')
    print(str(e.value[1]))
except odbc.Error as e:
    print('Connection Error:')
    print(str(e.value[1]))


data = pd.read_sql_query('''SELECT 
    [CCN]
    ,[DRG_CD]
    ,[EPI_ID]
    ,[FRACTURE]
    ,[PERF_YEAR]
    ,[Updated TP]
    ,[Updated Wage]
    ,DISASTER_FLAG
    ,COVID_DGNS_FLAG
    ,ANCHOR_BEG_DT
    ,cast(EPI_TOTAL as decimal(20,2)) EPI_TOTAL
    ,cast(HIGH_COST_THRESHOLD as decimal(20,2)) HIGH_COST_THRESHOLD

FROM [CJR_Stage].[CJRQA].[VW_QA_DATA]
where perf_year = '5.1'

 ''', con=conn)
df = pd.DataFrame(data)

df['STD TP 100%'] = df['Updated TP'] / 0.97
df['QA TP STD'] = df['STD TP 100%'] * 0.98
df['Raw TP (100%)-ND'] = df['STD TP 100%'] * df['Updated Wage']
df['QA TP Raw'] = df['QA TP STD'] * df['Updated Wage']
df['Disaster Spend'] = np.where( 
    np.logical_and(np.logical_or(np.logical_or(df['DISASTER_FLAG'] == '1', df['COVID_DGNS_FLAG'] == '1') 
                 ,np.logical_and(df['ANCHOR_BEG_DT'] >= '1/31/2020', df ['ANCHOR_BEG_DT'] <= '3/31/2021') 
                  )
                ,df['EPI_TOTAL'] > df['QA TP STD'])
, df['QA TP STD'] ,df['EPI_TOTAL'])    

df['Disaster Adjusted Spend'] = np.where( df['HIGH_COST_THRESHOLD'] < df['Disaster Spend'] , df['HIGH_COST_THRESHOLD'],df['Disaster Spend'])
df['Final Spend ND'] = df['Disaster Adjusted Spend'] * df['Updated Wage']
df['NPRA ND'] = df['QA TP Raw'] - df['Final Spend ND']
now = datetime.today()
data_1 = pd.read_csv(r'C:/Users/muhammad.danish/Downloads/Patient_Search_Tool_crosstab.csv',encoding='utf-16',sep='\t',header=0)
#data_1.to_csv(path, encoding='utf-8', index=False)
df_1 = pd.DataFrame(data_1)
df_1.columns = df_1.columns.str.replace(' ' ,'_')
df_1.columns = df_1.columns.str.replace('_%' ,'')
df_1.rename(columns = {'_NPRA':'NPRA','No._Of_Readmission':'Readmission'}, inplace = True)


df_cd = pd.merge(df,df_1, how='inner', left_on = 'EPI_ID', right_on = 'Episode_ID')
#df_cd['Final'] = df_cd["Total_spend"].replace('[\$,]','', regex=True, inplace=True).astype(float)


df_cd['Final1'] = df_cd['Total_Spend'].replace('[\$,]','', regex=True,).astype(float)
df_cd['Finaltp'] = df_cd['Target_Spend'].replace('[\$,]','', regex=True,).astype(float)
df_cd['FinalNPRA'] = df_cd['NPRA'].replace('[\$,]','', regex=True,).astype(float)




df_cd['Spend Difference'] = df_cd['Final1'] - df_cd['Final Spend ND']
df_cd['Target Price Difference'] = df_cd['Finaltp'] - df_cd['QA TP Raw']
df_cd['NPRA Difference'] = df_cd['NPRA'] - df_cd['NPRA ND']

df_cd.to_csv (r'C:\Users\muhammad.danish\Desktop\work\Results\NPRA_Result_'+now.strftime("%Y-%m-%d")+'_'+now.strftime("%H.%M")+'.csv',
             index = False)
print('Data Validation for patient search completed')
