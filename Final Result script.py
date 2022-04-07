import pyodbc as odbc
import pandas as pd 
#import datetime as datetime
from datetime import date, datetime

# Create db connection instance
try:
   
    conn =  odbc.connect("Driver=ODBC Driver 11 for SQL Server;Server=10.20.30.86;Database=CJR_Stage;UID=sa;Pwd=Sol@CJR!2019TR#")
except odbc.DatabaseError as e:
    print('Database error:')
    print(str(e.value[1]))
except odbc.Error as e:
    print('Connection Error:')
    print(str(e.value[1]))
sql_query = pd.read_sql_query(''' 
                              Select * from CJRQA.Validation_Results
                            
                              '''
                              ,conn)

df = pd.DataFrame(sql_query)
now = datetime.today()
#Output_Path = 'C:\\Users\\muhammad.danish\\Desktop\\work\\Results\\Test_'+{now.strftime("%Y-%m-%d")}+'_to_'+{now.strftime("%H.%M")}+'.csv'
df.to_csv (r'C:\Users\muhammad.danish\Desktop\work\Results\Validation_Result_'+now.strftime("%Y-%m-%d")+'_'+now.strftime("%H.%M")+'.csv',
             index = False)

conn.commit()    
print('Executed successfully')
