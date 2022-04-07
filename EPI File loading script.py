import pyodbc as odbc
import pandas as pd 


data = pd.read_csv('C:/Users/muhammad.danish/Desktop/work/Book4.csv')
df = pd.DataFrame(data)

# Create db connection instance
try:
   
    conn =  odbc.connect("Driver=ODBC Driver 11 for SQL Server;Server=10.20.30.86;Database=CJR_Stage;UID=sa;Pwd=Sol@CJR!2019TR#")
except odbc.DatabaseError as e:
    print('Database error:')
    print(str(e.value[1]))
except odbc.Error as e:
    print('Connection Error:')
    print(str(e.value[1]))

cursor = conn.cursor()
cursor = conn.cursor()
for row in df.itertuples():
    cursor.execute('''
    truncate table CJRQA.EPI ''')

for row in df.itertuples():
    cursor.execute('''
    INSERT INTO CJRQA.EPI (EPI_ID,BENE_SK,CLM_HIC_NUM,CLM_BENE_MBI_ID,CCN,ANCHOR_TYPE,DRG_CD,ANCHOR_HCPCS,FRACTURE,ANCHOR_BEG_DT,
ANCHOR_END_DT,POST_DSCH_BEG_DT,POST_DSCH_END_DT,EPI_TOTAL,EPI_IPPS,EPI_PB_PHYS,EPI_PB_ANES,EPI_IRF,EPI_SNF_PPS,
EPI_HH_PPS,EPI_OTHER,POSTEPI_TOTAL,POSTEPI_IPPS,POSTEPI_PB_PHYS,POSTEPI_PB_ANES,POSTEPI_IRF,POSTEPI_SNF_PPS,
POSTEPI_HH_PPS,POSTEPI_OTHER,EPI_TOTAL_ALLOWED,EPI_IPPS_ALLOWED,EPI_PB_PHYS_ALLOWED,EPI_PB_ANES_ALLOWED,
EPI_IRF_ALLOWED,EPI_SNF_PPS_ALLOWED,EPI_HH_PPS_ALLOWED,EPI_OTHER_ALLOWED,POSTEPI_TOTAL_ALLOWED,POSTEPI_IPPS_ALLOWED,
POSTEPI_PB_PHYS_ALLOWED,POSTEPI_PB_ANES_ALLOWED,POSTEPI_IRF_ALLOWED,POSTEPI_SNF_PPS_ALLOWED,POSTEPI_HH_PPS_ALLOWED,
POSTEPI_OTHER_ALLOWED,EPI_IPFILE,EPI_SNFILE,EPI_HHFILE,EPI_OPFILE,EPI_PBFILE,EPI_DMFILE,EPI_HSFILE,
EPI_NCBP,POSTEPI_NCBP,ANCHOR_AT_NPI,ANCHOR_OP_NPI,ANCHOR_LOS,ANCHOR_STUS_CD,BPCI_OVERLAP,ACO_OVERLAP,IMPUTATION,
DISASTER_FLAG,HAC_FIX,PERF_YEAR,COVID_DGNS_FLAG,EPI_IPANCHOR,EPI_OPANCHOR,POST_DSCH_IPADM,AGE,DUAL,HCC_CNT)
    VALUES (?,?,?,?,?,?,?,?,?,?,
            ?,?,?,?,?,?,?,?,?,?,
            ?,?,?,?,?,?,?,?,?,?,
            ?,?,?,?,?,?,?,?,?,?,
            ?,?,?,?,?,?,?,?,?,?,
            ?,?,?,?,?,?,?,?,?,?,
            ?,?,?,?,?,?,?,?,?,?,?)
''',
str(row.EPI_ID)
,str(row.BENE_SK)
,str(row.CLM_HIC_NUM)
,str(row.CLM_BENE_MBI_ID)
,str(row.CCN)
,str(row.ANCHOR_TYPE)
,str(row.DRG_CD)
,str(row.ANCHOR_HCPCS)
,str(row.FRACTURE)
,str(row.ANCHOR_BEG_DT)
,str(row.ANCHOR_END_DT)
,str(row.POST_DSCH_BEG_DT)
,str(row.POST_DSCH_END_DT)
,str(row.EPI_TOTAL)
,str(row.EPI_IPPS)
,str(row.EPI_PB_PHYS)
,str(row.EPI_PB_ANES)
,str(row.EPI_IRF)
,str(row.EPI_SNF_PPS)
,str(row.EPI_HH_PPS)
,str(row.EPI_OTHER)
,str(row.POSTEPI_TOTAL)
,str(row.POSTEPI_IPPS)
,str(row.POSTEPI_PB_PHYS)
,str(row.POSTEPI_PB_ANES)
,str(row.POSTEPI_IRF)
,str(row.POSTEPI_SNF_PPS)
,str(row.POSTEPI_HH_PPS)
,str(row.POSTEPI_OTHER)
,str(row.EPI_TOTAL_ALLOWED)
,str(row.EPI_IPPS_ALLOWED)
,str(row.EPI_PB_PHYS_ALLOWED)
,str(row.EPI_PB_ANES_ALLOWED)
,str(row.EPI_IRF_ALLOWED)
,str(row.EPI_SNF_PPS_ALLOWED)
,str(row.EPI_HH_PPS_ALLOWED)
,str(row.EPI_OTHER_ALLOWED)
,str(row.POSTEPI_TOTAL_ALLOWED)
,str(row.POSTEPI_IPPS_ALLOWED)
,str(row.POSTEPI_PB_PHYS_ALLOWED)
,str(row.POSTEPI_PB_ANES_ALLOWED)
,str(row.POSTEPI_IRF_ALLOWED)
,str(row.POSTEPI_SNF_PPS_ALLOWED)
,str(row.POSTEPI_HH_PPS_ALLOWED)
,str(row.POSTEPI_OTHER_ALLOWED)
,str(row.EPI_IPFILE)
,str(row.EPI_SNFILE)
,str(row.EPI_HHFILE)
,str(row.EPI_OPFILE)
,str(row.EPI_PBFILE)
,str(row.EPI_DMFILE)
,str(row.EPI_HSFILE)
,str(row.EPI_NCBP)
,str(row.POSTEPI_NCBP)
,str(row.ANCHOR_AT_NPI)
,str(row.ANCHOR_OP_NPI)
,str(row.ANCHOR_LOS)
,str(row.ANCHOR_STUS_CD)
,str(row.BPCI_OVERLAP)
,str(row.ACO_OVERLAP)
,str(row.IMPUTATION)
,str(row.DISASTER_FLAG)
,str(row.HAC_FIX)
,str(row.PERF_YEAR)
,str(row.COVID_DGNS_FLAG)
,str(row.EPI_IPANCHOR)
,str(row.EPI_OPANCHOR)
,str(row.POST_DSCH_IPADM)
,str(row.AGE)
,str(row.DUAL)
,str(row.HCC_CNT)


                )
conn.commit()    
print('Data Loaded successfully')
