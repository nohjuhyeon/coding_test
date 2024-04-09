-- 코드를 작성해주세요
SELECT COUNT(LENGTHNONE.ID) AS FISH_COUNT
FROM(SELECT ID,
CASE 
WHEN LENGTH <= 10 THEN NULL
ELSE LENGTH
END
AS LENGTH
FROM FISH_INFO
WHERE LENGTH IS NULL) AS LENGTHNONE