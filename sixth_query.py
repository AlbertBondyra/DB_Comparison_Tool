
sixth_query="""select C2.country_code,
       C2.country_name,
       (SELECT count(*) from PATIENTS WHERE is_sick = 'TRUE'),
       (SELECT count(*) from PATIENTS WHERE is_dead = 'TRUE'),
       (SELECT count(*) from PATIENTS WHERE is_recovered = 'TRUE'),
       (SELECT count(*) from TESTS),
       count(PATIENTS.PATIENT_ID) as ilosc,
       GDP
from PATIENTS
         LEFT JOIN COUNTRIES C2 ON PATIENTS.COUNTRY_CODE = C2.country_code
INNER JOIN TESTS T on PATIENTS.patient_id = T.patient_id

where GDP >= 27000
group by C2.country_code, C2.country_name, GDP """