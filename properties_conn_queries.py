import cx_Oracle
from PyQt5.QtSql import QSqlQuery

import config
import mysql.connector
import first_query,second_query,third_query,fourth_query,fifth_query,sixth_query
import pymysql
import pyodbc
#file with results
filepath = 'C:\\Users\\alber\\OneDrive\\Pulpit\\PracaAlberta\\AppFiles\\queries_times.xls'
#MSSQL connection properties
#properties to local DB
# dbMSSQL = pyodbc.connect('Driver={SQL Server};''Server=DESKTOP-M7HC7EL;''Database=MSSQL;''Trusted_Connection=yes;')
#properties to Docker Server
dbMSSQL = pyodbc.connect(driver='{SQL Server}',server='DESKTOP-M7HC7EL,10016', database='Diploma_Work', uid='alamar6',pwd='intendant66R')
curMSSQL = dbMSSQL.cursor()
#dbMSSQL.execute("external_query3_sql3ORACLE")
#MSSQL queries
sql1MSSQL = first_query.first_external_query
sql2MSSQL= second_query.mssql_second_external_query
# sql1MSSQL = """select count(*) from continents union all select count(*) from patients"""
# sql2MSSQL= """select count(*) from continents union all select count(*) from patients"""
sql3MSSQL= third_query.third_external_query
sql4MSSQL = fourth_query.fourth_external_query
sql5MSSQL=fifth_query.fifth_mssql_external_query
# sql5MSSQL = """select count(*) from countries union all select count(*) from best_hospitals"""
sql6MSSQL =sixth_query.sixth_query
# sql6MSSQL = """select count(*) from continents union all select count(*) from patients"""

#ORACLE connection properties
cx_Oracle.init_oracle_client(lib_dir=r"C:\app\alber\product\18.0.0\dbhomeXE\instantclient\instantclient_19_8")
dbOracle = cx_Oracle.connect( config.username,config.password, config.dsn, encoding=config.encoding)
curOracle = dbOracle.cursor()

#ORACLE queries
sql1ORACLE = first_query.oracle_first_external_query
sql2ORACLE = second_query.oracle_second_external_query
# sql1ORACLE = """select 2+9 from dual"""
# sql2ORACLE = """select 2+9 from dual"""
sql3ORACLE = """select count(*) from (select patient_id from patients where patient_id in (select patient_id from disease_status_change group by patient_id having count(1) > 60)) t"""
sql4ORACLE = """select depiction,age, patient_id, continent_code, country, gender, is_sick,is_dead, per_country
from (
         (select pt.patient_id,
                 ct.continent_code,
                 pt.country_code,
                 pt.country,
                 pt.age,
                 pt.gender,
                 pt.is_dead,
                 pt.is_sick,
                 row_number() over (partition by pt.country_code order by pt.age desc) as per_country,
         'top 3 aged dead patients above 90 years old per country' depiction
          from patients pt
                   inner join countries ct on pt.country_code = ct.country_code
          where pt.is_dead = 1
            and age >= 90
            and ct.continent_code in ('eu', 'af','as'))
         union all
         (select pt.patient_id,
                 ct.continent_code,
                 pt.country_code,
                 pt.country,
                 pt.age,
                 pt.gender,
                 pt.is_dead,
                 pt.is_sick,
                 row_number() over (partition by pt.country_code order by pt.age desc) as per_country,
        'top 3 young dead patients below 18 years old per country' depiction
          from patients pt
                   inner join countries ct on pt.country_code = ct.country_code
          where pt.is_dead = 1
            and age <= 18
            and ct.continent_code in ('eu', 'af','as'))
         union all
         (select pt.patient_id,
                 ct.continent_code,
                 pt.country_code,
                 pt.country,
                 pt.age,
                 pt.gender,
                 pt.is_dead,
                 pt.is_sick,
                 row_number() over (partition by pt.country_code order by pt.age desc) as per_country,
         'top 3 aged sick patients above 90 years old per country' depiction
          from patients pt
                   inner join countries ct on pt.country_code = ct.country_code
          where pt.is_sick = 1
            and age >= 90
            and ct.continent_code in ('eu', 'af','as'))
         union all
         (select pt.patient_id,
                 ct.continent_code,
                 pt.country_code,
                 pt.country,
                 pt.age,
                 pt.gender,
                 pt.is_dead,
                 pt.is_sick,
                 row_number() over (partition by pt.country_code order by pt.age desc) as per_country,
        'top 3 young sick patients below 18 years old per country' depiction
          from patients pt
                   inner join countries ct on pt.country_code = ct.country_code
          where pt.is_sick = 1
            and age <= 18
            and ct.continent_code in ('eu', 'af','as'))
    ) t
where t.per_country <= 3"""
sql5ORACLE="""select standard_hash(UTL_I18N.STRING_TO_RAW(to_md5,'AL16UTF16LE'), 'MD5') from( select (patients.patient_id || patients.disease_start_date || patients.age || patients.gender || patients.country_code || patients.country ||coalesce(patients.region_code, 'empty') || t.result || t.currency || substr(t.currency, 1, 6) || lower(dsc.status) || patients.patient_id || patients.disease_start_date || patients.age || patients.gender || patients.country_code || patients.country || coalesce(patients.region_code, 'empty') || t.result || t.currency || substr(t.currency, 1, 3) || upper(dsc.status) )as to_md5 from patients inner join tests t on patients.patient_id = t.patient_id inner join disease_status_change dsc on patients.patient_id = dsc.patient_id where country_code in ('AE','AF','BE')order by to_md5 desc) t where rownum<=100"""
sql6ORACLE = """select c2.country_code, c2.country_name, (select count(*) from patients where is_sick = 1) as is_sick_count,  (select count(*) from patients WHERE is_dead = 1) is_dead_count, (select count(*) from patients WHERE is_recovered = 1) is_recovered_count, (select count(*) from tests) test_count, count(patients.PATIENT_ID) as patient_count, GDP from patients left join COUNTRIES c2 ON patients.country_code = c2.country_code inner join tests T on patients.patient_id = T.patient_id where GDP >= 27000 group by c2.country_code, c2.country_name, GDP order by GDP"""


#MySQL connection properties
# properties to Docker Server
dbMySQL = mysql.connector.connect(host='localhost', port=52000, user='alamar6', passwd='{pfizer}', db='Diploma_Work',auth_plugin='mysql_native_password')
curMySQL = dbMySQL.cursor()
#properties to local DB
# dbMySQL = pymysql.connect('localhost', 'bondya', 'pfizer', 'Dyplomowa_DB')
# curMySQL = dbMySQL.cursor()



#MySQL queries

sql1MySQL = first_query.first_external_query
sql2MySQL= """CREATE TABLE DETAILS_PATIENTS AS SELECT P.PATIENT_ID, P.DISEASE_START_DATE,P.AGE,P.GENDER,P.COUNTRY,P.COUNTRY_CODE,P.REGION,P.REGION_CODE,P.CITY,P.HOSPITAL_VISIT_DATE,P.INTERNATIONAL_TRAVELER,P.DOMESTIC_TRAVELER, P.EXPOSURE_START,P.EXPOSURE_END,P.VISITING_WUHAN,P.FROM_WUHAN,P.HAS_OVERWEIGHT,P.DO_SPORT,P.HAS_COMORDIBITIES,P.IS_RECOVERED,P.IS_DEAD,P.IS_SICK,P.HOSPITAL_ID,P.SYMPTOM,P.SOURCE_DETAILS,COUNTRIES.COUNTRY_NAME,COUNTRIES.LAND,COUNTRIES.POPULATION,COUNTRIES.IN_UE,COUNTRIES.IN_NATO, COUNTRIES.AREA_IN_SQ_MI,COUNTRIES.POP_DENSITY_PER_SQ_MI,COUNTRIES.COASTLINE,COUNTRIES.NET_MIGRATION,COUNTRIES.INFANT_MORTALITY,COUNTRIES.GDP,COUNTRIES.LITERACY_IN_PERCENTAGE, COUNTRIES.PHONES_PER_1000,COUNTRIES.ARABLE_IN_PERCENTAGE,COUNTRIES.CROPS_IN_PERCENTAGE,COUNTRIES.OTHER_IN_PERCENTAGE,COUNTRIES.CLIMATE_IN_PERCENTAGE,COUNTRIES.BIRTHDATE_IN_PERCENTAGE,COUNTRIES.DATEHRATE_IN_PERCENTAGE, COUNTRIES.AGRICULTURE,COUNTRIES.INDUSTRY,COUNTRIES.SERVICE, CONTINENTS.CONTINENT_NAME,CONTINENTS.SURFACE_IN_MLN_KM, CONTINENTS.PROCENTAGE_EARTH_SURFACE,CONTINENTS.LANDS_PROCENTAGE, T.TEST_START_DATE,T.CURRENCY,T.TEST_TYPE,T.HAS_GLOBAL_RECOMENDATION,T.EFFECTIVENESS,T.DRAW_METODOLOGY,T.WAITING_TIME_ON_RESULTS, T.PRICE FROM CONTINENTS INNER JOIN COUNTRIES ON COUNTRIES.CONTINENT_CODE = CONTINENTS.CONTINENT_CODE INNER JOIN PATIENTS P on COUNTRIES.COUNTRY_CODE = P.COUNTRY_CODE INNER JOIN TESTS T on P.PATIENT_ID = T.PATIENT_ID"""

# sql1MySQL = """select count(1) from REGIONS ;"""
# sql2MySQL= """select count(1) from REGIONS ;"""
sql3MySQL =  third_query.third_external_query
sql4MySQL = fourth_query.fourth_external_query
sql5MySQL = fifth_query.fifth_mysql_external_query
# sql5MySQL = """select count(*) from COUNTRIES ; """
sql6MySQL = sixth_query.sixth_query