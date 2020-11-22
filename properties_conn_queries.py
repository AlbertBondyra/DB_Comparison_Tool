import cx_Oracle
import config
import mysql.connector
import pymysql
import pyodbc
#file with results
filepath = 'C:\\Users\\alber\\OneDrive\\Pulpit\\PracaAlberta\\AppFiles\\queries_times.txt'
#MSSQL connection properties
#properties to local DB
# dbMSSQL = pyodbc.connect('Driver={SQL Server};''Server=DESKTOP-M7HC7EL;''Database=MSSQL;''Trusted_Connection=yes;')
#properties to Docker Server
dbMSSQL = pyodbc.connect(driver='{SQL Server}',server='DESKTOP-M7HC7EL,10016', database='Diploma_Work', uid='alamar6',pwd='intendant66R')
curMSSQL = dbMSSQL.cursor()

#MSSQL queries
sql1MSSQL = """SELECT 'BEST_HOSPITALS' AS TBL_NM, COUNT(1) FROM BEST_HOSPITALS UNION ALL
SELECT 'CONTINENTS' AS TBL_NM, COUNT(1) FROM CONTINENTS UNION ALL
SELECT 'COUNTRIES' AS TBL_NM, COUNT(1) FROM COUNTRIES UNION ALL
SELECT 'PATIENTS' AS TBL_NM, COUNT(1) FROM PATIENTS UNION ALL
SELECT 'TESTS' AS TBL_NM, COUNT(1) FROM TESTS UNION ALL
SELECT 'DISEASE_STATUS_CHANGE' AS TBL_NM, COUNT(1) FROM DISEASE_STATUS_CHANGE UNION ALL
SELECT 'REGIONS' AS TBL_NM, COUNT(1) FROM REGIONS ;"""
sql2MSSQL = """SELECT DEPICTION,age, patient_id, continent_code, country, gender, IS_SICK,IS_DEAD, PER_COUNTRY
FROM (
         (SELECT PT.patient_id,
                 CT.continent_code,
                 PT.country_code,
                 PT.country,
                 PT.age,
                 PT.gender,
                 PT.IS_DEAD,
                 PT.IS_SICK,
                 ROW_NUMBER() OVER (PARTITION BY PT.country_code ORDER BY PT.AGE DESC) AS PER_COUNTRY,
         'Top 3 aged dead patients above 90 years old per country' DEPICTION
          FROM PATIENTS PT
                   INNER JOIN COUNTRIES CT on PT.country_code = CT.country_code
          WHERE PT.IS_DEAD = 1
            AND AGE >= 90
            AND CT.continent_code IN ('EU', 'AF','AS'))
         UNION ALL
         (SELECT PT.patient_id,
                 CT.continent_code,
                 PT.country_code,
                 PT.country,
                 PT.age,
                 PT.gender,
                 PT.IS_DEAD,
                 PT.IS_SICK,
                 ROW_NUMBER() OVER (PARTITION BY PT.country_code ORDER BY PT.AGE DESC) AS PER_COUNTRY,
        'Top 3 young dead patients below 18 years old per country' DEPICTION
          FROM PATIENTS PT
                   INNER JOIN COUNTRIES CT on PT.country_code = CT.country_code
          WHERE PT.IS_DEAD = 1
            AND AGE <= 18
            AND CT.continent_code IN ('EU', 'AF','AS'))
         UNION ALL
         (SELECT PT.patient_id,
                 CT.continent_code,
                 PT.country_code,
                 PT.country,
                 PT.age,
                 PT.gender,
                 PT.IS_DEAD,
                 PT.IS_SICK,
                 ROW_NUMBER() OVER (PARTITION BY PT.country_code ORDER BY PT.AGE DESC) AS PER_COUNTRY,
         'Top 3 aged sick patients above 90 years old per country' DEPICTION
          FROM PATIENTS PT
                   INNER JOIN COUNTRIES CT on PT.country_code = CT.country_code
          WHERE PT.IS_SICK = 1
            AND AGE >= 90
            AND CT.continent_code IN ('EU', 'AF','AS'))
         UNION ALL
         (SELECT PT.patient_id,
                 CT.continent_code,
                 PT.country_code,
                 PT.country,
                 PT.age,
                 PT.gender,
                 PT.IS_DEAD,
                 PT.IS_SICK,
                 ROW_NUMBER() OVER (PARTITION BY PT.country_code ORDER BY PT.AGE DESC) AS PER_COUNTRY,
        'Top 3 young sick patients below 18 years old per country' DEPICTION
          FROM PATIENTS PT
                   INNER JOIN COUNTRIES CT on PT.country_code = CT.country_code
          WHERE PT.IS_SICK = 1
            AND AGE <= 18
            AND CT.continent_code IN ('EU', 'AF','AS'))
    ) T
WHERE T.PER_COUNTRY <= 3"""
sql3MSSQL = """select count(*) from REGIONS """
sql4MSSQL = """select count(*) from regions union all select count(*) from best_hospitals"""
sql5MSSQL = """select count(*) from countries union all select count(*) from best_hospitals"""
sql6MSSQL = """select count(*) from continents union all select count(*) from patients"""

#ORACLE connection properties
cx_Oracle.init_oracle_client(lib_dir=r"C:\app\alber\product\18.0.0\dbhomeXE\instantclient\instantclient_19_8")
dbOracle = cx_Oracle.connect( config.username,config.password, config.dsn, encoding=config.encoding)
curOracle = dbOracle.cursor()

#ORACLE queries
sql1ORACLE = """SELECT 'BEST_HOSPITALS' AS TBL_NM, COUNT(1) FROM BEST_HOSPITALS  """
sql2ORACLE = """SELECT 'REGIONS' AS TBL_NM, COUNT(1) FROM REGIONS"""
sql3ORACLE = """select * from REGIONS"""
sql4ORACLE = """select count(*) from regions union all select count(*) from best_hospitals"""
sql5ORACLE = """select count(*) from countries union all select count(*) from best_hospitals"""
sql6ORACLE = """select 2+9 from dual"""

#MySQL connection properties
# properties to Docker Server
# dbMySQL = mysql.connector.connect(host='localhost', port=52000, user='alamar6', passwd='{pfizer}', db='Diploma_Work',auth_plugin='mysql_native_password')
# curMySQL = dbMySQL.cursor()
#properties to local DB
dbMySQL = pymysql.connect('localhost', 'bondya', 'pfizer', 'Dyplomowa_DB')
curMySQL = dbMySQL.cursor()



#MySQL queries
sql2MySQL = """select continent_code from CONTINENTS ;"""
sql1MySQL = """SELECT 'BEST_HOSPITALS' AS TBL_NM, COUNT(1) FROM BEST_HOSPITALS UNION ALL
SELECT 'CONTINENTS' AS TBL_NM, COUNT(1) FROM CONTINENTS UNION ALL
SELECT 'COUNTRIES' AS TBL_NM, COUNT(1) FROM COUNTRIES UNION ALL
SELECT 'PATIENTS' AS TBL_NM, COUNT(1) FROM PATIENTS UNION ALL
SELECT 'TESTS' AS TBL_NM, COUNT(1) FROM TESTS UNION ALL
SELECT 'DISEASE_STATUS_CHANGE' AS TBL_NM, COUNT(1) FROM DISEASE_STATUS_CHANGE UNION ALL
SELECT 'REGIONS' AS TBL_NM, COUNT(1) FROM REGIONS ;"""
sql3MySQL = """select * from REGIONS ;"""
sql4MySQL = """select count(1) from REGIONS ;"""
sql5MySQL = """select count(*) from COUNTRIES ; """
sql6MySQL = """select count(*) from CONTINENTS """