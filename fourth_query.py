fourth_external_query ="""SELECT DEPICTION,age, patient_id, continent_code, country, gender, IS_SICK,IS_DEAD, PER_COUNTRY
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