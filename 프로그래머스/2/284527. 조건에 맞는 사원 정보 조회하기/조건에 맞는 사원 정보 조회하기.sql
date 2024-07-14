SELECT SUM(G.SCORE) AS SCORE, G.EMP_NO, E.EMP_NAME, E.POSITION, E.EMAIL
FROM HR_EMPLOYEES AS E
JOIN HR_GRADE AS G
ON E.EMP_NO = G.EMP_NO
WHERE G.YEAR = 2022
GROUP BY G.YEAR, EMP_NO
HAVING G.YEAR = 2022
ORDER BY SCORE DESC
LIMIT 1