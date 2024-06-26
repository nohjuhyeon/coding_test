-- 코드를 작성해주세요
SELECT HR_EMPLOYEES.EMP_NO, HR_EMPLOYEES.EMP_NAME, SCORE_BOARD.GRADE, (SCORE_BOARD.PERCENT * HR_EMPLOYEES.SAL) AS BONUS FROM (SELECT EMP_NO,
CASE
WHEN AVG(SCORE) >= 96 THEN 'S'
WHEN AVG(SCORE) >= 90 THEN 'A'
WHEN AVG(SCORE) >= 80 THEN 'B'
ELSE 'C'
END
AS GRADE,
CASE
WHEN AVG(SCORE) >= 96 THEN 0.2
WHEN AVG(SCORE) >= 90 THEN 0.15
WHEN AVG(SCORE) >= 80 THEN 0.1
ELSE 0
END
AS PERCENT
FROM HR_GRADE
GROUP BY EMP_NO) SCORE_BOARD
INNER JOIN HR_EMPLOYEES
ON SCORE_BOARD.EMP_NO = HR_EMPLOYEES.EMP_NO
ORDER BY HR_EMPLOYEES.EMP_NO