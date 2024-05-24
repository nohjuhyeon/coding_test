-- 코드를 입력하세요
SELECT CAR_FEE.HISTORY_ID, 
CASE 
WHEN CAR_DISCOUNT.DISCOUNT_RATE IS NULL THEN CAR_FEE.FEE 
ELSE ROUND((CAR_FEE.FEE*((100-CAR_DISCOUNT.DISCOUNT_RATE)*0.01)))
END AS FEE FROM (SELECT * ,
CASE 
WHEN CAR_FEE.DATE_DIFF >= 90 THEN 90
WHEN CAR_FEE.DATE_DIFF >= 30 THEN 30
WHEN CAR_FEE.DATE_DIFF >= 7 THEN 7
ELSE 0                                                                        
END AS DURATION,
CAR_FEE.DATE_DIFF*CAR_FEE.DAILY_FEE AS FEE FROM 
(SELECT CAR_RENTAL_COMPANY_RENTAL_HISTORY.history_id, CAR_RENTAL_COMPANY_RENTAL_HISTORY.car_id,(DATEDIFF(DATE_FORMAT(CAR_RENTAL_COMPANY_RENTAL_HISTORY.END_DATE,"%Y-%m-%d"),DATE_FORMAT(CAR_RENTAL_COMPANY_RENTAL_HISTORY.START_DATE,"%Y-%m-%d"))+1) AS DATE_DIFF, CAR_RENTAL_COMPANY_CAR.DAILY_FEE
FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
INNER JOIN CAR_RENTAL_COMPANY_CAR 
ON CAR_RENTAL_COMPANY_RENTAL_HISTORY.CAR_ID = CAR_RENTAL_COMPANY_CAR .CAR_ID
WHERE CAR_RENTAL_COMPANY_CAR .CAR_TYPE = '트럭') CAR_FEE) CAR_FEE
LEFT JOIN (SELECT CASE 
WHEN DURATION_TYPE = '7일 이상' THEN 7
WHEN DURATION_TYPE = '30일 이상' THEN 30
WHEN DURATION_TYPE = '90일 이상' THEN 90
END AS DURATION,DISCOUNT_RATE
FROM CAR_RENTAL_COMPANY_DISCOUNT_PLAN
WHERE CAR_TYPE = '트럭') AS CAR_DISCOUNT
ON CAR_FEE.DURATION = CAR_DISCOUNT.DURATION 
ORDER BY FEE DESC, CAR_FEE.HISTORY_ID DESC