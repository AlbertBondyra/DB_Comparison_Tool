first_external_query = """SELECT 'BEST_HOSPITALS' AS TBL_NM, COUNT(1) FROM BEST_HOSPITALS UNION ALL
SELECT 'CONTINENTS' AS TBL_NM, COUNT(1) FROM CONTINENTS UNION ALL
SELECT 'COUNTRIES' AS TBL_NM, COUNT(1) FROM COUNTRIES UNION ALL
SELECT 'PATIENTS' AS TBL_NM, COUNT(1) FROM PATIENTS UNION ALL
SELECT 'TESTS' AS TBL_NM, COUNT(1) FROM TESTS UNION ALL
SELECT 'DISEASE_STATUS_CHANGE' AS TBL_NM, COUNT(1) FROM DISEASE_STATUS_CHANGE UNION ALL
SELECT 'REGIONS' AS TBL_NM, COUNT(1) FROM REGIONS ;"""
oracle_first_external_query =""" select 'best_hospitals' as tbl_nm, count(*) from best_hospitals union all
select 'continents' as tbl_nm, count(*) from continents union all
select 'countries' as tbl_nm, count(*) from countries union all
select 'patients' as tbl_nm, count(*) from patients union all
select 'tests' as tbl_nm, count(*) from tests union all
select 'disease_status_change' as tbl_nm, count(*) from disease_status_change union all
select 'regions' as tbl_nm, count(*) from regions """