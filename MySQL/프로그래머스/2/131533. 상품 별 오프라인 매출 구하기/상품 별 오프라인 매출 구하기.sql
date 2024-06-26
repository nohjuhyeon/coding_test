-- 코드를 입력하세요
SELECT PRODUCT.PRODUCT_CODE, SUM(SALES_AMOUNT)*PRODUCT.PRICE AS SALES
FROM PRODUCT
INNER JOIN OFFLINE_SALE
ON PRODUCT.PRODUCT_ID = OFFLINE_SALE.PRODUCT_ID
GROUP BY PRODUCT.PRODUCT_ID
ORDER BY SALES DESC, PRODUCT_CODE