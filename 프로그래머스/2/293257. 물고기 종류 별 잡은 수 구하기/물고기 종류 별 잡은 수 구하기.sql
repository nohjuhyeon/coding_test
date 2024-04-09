-- 코드를 작성해주세요
SELECT COUNT(FISH_TYPE_COUNT.FISH_TYPE) AS FISH_COUNT, FISH_TYPE_COUNT.FISH_NAME
FROM(SELECT  FISH_INFO.FISH_TYPE, FISH_NAME_INFO.FISH_NAME
FROM FISH_NAME_INFO
INNER JOIN FISH_INFO
ON FISH_NAME_INFO.FISH_TYPE = FISH_INFO.FISH_TYPE) AS FISH_TYPE_COUNT
GROUP BY FISH_TYPE_COUNT.FISH_NAME
ORDER BY FISH_COUNT DESC
