-- Clean raw shift logs and fix data type inconsistencies
SELECT 
  PARSE_DATE('%Y-%m-%d', CAST(date AS STRING)) AS date,
  INITCAP(market) AS market,
  role,
  headcount_present,
  total_hours_logged
FROM `project-1216b1b9f.av_labor_staging.raw_shift_logs`;
