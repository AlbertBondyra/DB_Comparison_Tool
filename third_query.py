third_external_query = """SELECT COUNT(*) FROM (SELECT PATIENT_ID FROM PATIENTS WHERE patient_id IN (SELECT PATIENT_ID FROM DISEASE_STATUS_CHANGE GROUP BY PATIENT_ID HAVING COUNT(1) > 60)) T; """
