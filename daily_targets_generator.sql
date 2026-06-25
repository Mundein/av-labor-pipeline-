-- Create static operational targets mapped by market and role constraints
CREATE OR REPLACE TABLE `project-11261b9f-cb0f-47d2-b2c.av_labor_staging.daily_targets` AS
SELECT 
    CAST(date AS DATE) AS date,
    market,
    role,
CASE
    WHEN market = 'Los Angeles' AND role = 'Driver' THEN 25
    WHEN market = 'San Diego' AND role = 'Driver' THEN 25
    WHEN market = 'Chicago' AND role = 'Driver' THEN 25
    WHEN market = 'San Francisco' AND role = 'Driver' THEN 25
    WHEN market = 'San Francisco' AND role = 'Advanced Driver' THEN 25
    WHEN market = 'San Diego' AND role = 'Advanced Driver' THEN 25
    ELSE 10
END AS target
FROM 
    `project-11261b9f-cb0f-47d2-b2c.av_labor_staging.clean_daily_labor_summary`;
