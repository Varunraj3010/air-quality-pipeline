-- 1. Daily average PM2.5
SELECT time::date AS day, ROUND(AVG(pm2_5)::numeric, 1) AS avg_pm25
FROM readings
GROUP BY day
ORDER BY day;

-- 2. Worst 5 hours
SELECT time, pm2_5
FROM readings
ORDER BY pm2_5 DESC
LIMIT 5;

-- 3. Days with average PM2.5 above 60
SELECT time::date AS day, ROUND(AVG(pm2_5)::numeric, 1) AS avg_pm25
FROM readings
GROUP BY day
HAVING AVG(pm2_5) > 60
ORDER BY day;

-- 4. Hour-of-day pattern (when is air worst?)
SELECT EXTRACT(HOUR FROM time) AS hour, ROUND(AVG(pm2_5)::numeric, 1) AS avg_pm25
FROM readings
GROUP BY hour
ORDER BY hour;