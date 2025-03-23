WITH TotalPlays AS (
    SELECT COUNT(*) AS Total_Play
    FROM Coach_Scheme
    WHERE Down = 1
)
SELECT 
    Formation, 
    Play, 
    (COUNT(*) * 100.0) / (SELECT Total_Play FROM TotalPlays) AS Percent_Chance
FROM Coach_Scheme 
WHERE Yard_Line > 20 AND Down = 1
GROUP BY Formation;
