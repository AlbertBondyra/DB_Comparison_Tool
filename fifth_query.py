fifth_mysql_external_query="""select CONVERT(md5(TO_MD5), CHAR(32)) from (SELECT concat (PATIENTS.PATIENT_ID ,
       PATIENTS.DISEASE_START_DATE , PATIENTS.AGE , PATIENTS.gender , PATIENTS.country_code , PATIENTS.country ,
       coalesce(PATIENTS.REGION_CODE, 'EMPTY') , T.result , T.currency , SUBSTR(T.currency, 1, 6) ,
       lower(DSC.status) ,
       PATIENTS.PATIENT_ID ,
       PATIENTS.DISEASE_START_DATE , PATIENTS.AGE , PATIENTS.gender , PATIENTS.country_code , PATIENTS.country ,
       coalesce(PATIENTS.REGION_CODE, 'EMPTY') , T.result , T.currency , SUBSTR(T.currency, 1, 3) ,
       upper(DSC.status)) as TO_MD5
from PATIENTS
         INNER JOIN TESTS T on PATIENTS.patient_id = T.patient_id
         INNER JOIN DISEASE_STATUS_CHANGE DSC on PATIENTS.patient_id = DSC.patient_id
where country_code in ('AE','AF','BE') order by TO_MD5 DESC ) T limit 100; """
fifth_mssql_external_query="""SELECT CONVERT( VARCHAR(32),HASHBYTES('MD5',TO_MD5),2) FROM (SELECT TOP 100* FROM (
SELECT concat (PATIENTS.PATIENT_ID ,
       PATIENTS.DISEASE_START_DATE , PATIENTS.AGE , PATIENTS.gender , PATIENTS.country_code , PATIENTS.country ,
       coalesce(PATIENTS.REGION_CODE, 'EMPTY') , T.result , T.currency , SUBSTRING(T.currency, 1, 6) ,
       lower(DSC.status) ,
       PATIENTS.PATIENT_ID ,
       PATIENTS.DISEASE_START_DATE , PATIENTS.AGE , PATIENTS.gender , PATIENTS.country_code , PATIENTS.country ,
       coalesce(PATIENTS.REGION_CODE, 'EMPTY') , T.result , T.currency , SUBSTRING(T.currency, 1, 3) ,
       upper(DSC.status)) as TO_MD5

from PATIENTS
         INNER JOIN TESTS T on PATIENTS.patient_id = T.patient_id
         INNER JOIN DISEASE_STATUS_CHANGE DSC on PATIENTS.patient_id = DSC.patient_id
where country_code in ('AE','AF','BE') ) T order by TO_MD5 DESC)T2"""
# fifth_oracle_external_query = """select  standard_hash(utl_i18n.string_to_raw(to_md5,'al16utf16le'), 'md5') from(
# select (patients.patient_id ||
#        patients.disease_start_date || patients.age || patients.gender || patients.country_code || patients.country ||
#        coalesce(patients.region_code, 'empty') || t.result || t.currency || substr(t.currency, 1, 6) ||
#        lower(dsc.status) ||
#        patients.patient_id ||
#        patients.disease_start_date || patients.age || patients.gender || patients.country_code || patients.country ||
#        coalesce(patients.region_code, 'empty') || t.result || t.currency || substr(t.currency, 1, 3) ||
#        upper(dsc.status) )as to_md5
#
# from patients
#          inner join tests t on patients.patient_id = t.patient_id
#          inner join disease_status_change dsc on patients.patient_id = dsc.patient_id
# where country_code in ('ae','af','be')order by to_md5 desc) t where rownum<=100;"""

