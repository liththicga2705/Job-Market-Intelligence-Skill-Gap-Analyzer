-- JOB MARKET ANALYSIS

-- 1. Total number of jobs

SELECT COUNT(*) AS total_jobs
FROM jobs_job;

-- 2. Number of Jobs by Location
SELECT location, COUNT(*) AS job_count
FROM jobs_job
GROUP BY location
ORDER BY job_count DESC;

-- 3. Number of Jobs by Employment Type
SELECT employment_type, COUNT(*) AS job_count
FROM jobs_job
GROUP BY employment_type
ORDER BY job_count DESC;

-- 4. Number of Jobs by Experience
SELECT experience, COUNT(*) AS job_count
FROM jobs_job
GROUP BY experience
ORDER BY job_count DESC;

-- 5. Average Salary
SELECT 
    AVG((salary_min + salary_max) / 2.0) AS average_salary
FROM jobs_job
WHERE salary_min IS NOT NULL
  AND salary_max IS NOT NULL;

-- 6. Minimum and Maximum Salary
SELECT
    MIN(salary_min) AS minimum_salary,
    MAX(salary_max) AS maximum_salary
FROM jobs_job
WHERE salary_min IS NOT NULL
  AND salary_max IS NOT NULL;

-- 7. Average Salary by Location
SELECT
    location,
    AVG((salary_min + salary_max) / 2.0) AS average_salary
FROM jobs_job
WHERE salary_min IS NOT NULL
  AND salary_max IS NOT NULL
GROUP BY location
ORDER BY average_salary DESC;

-- 8. Number of Jobs by Company
SELECT
    company,
    COUNT(*) AS job_count
FROM jobs_job
GROUP BY company
ORDER BY job_count DESC;

-- 9. High-Paying Job Roles
SELECT
    job_title,
    company,
    location,
    salary_min,
    salary_max
FROM jobs_job
WHERE salary_min IS NOT NULL
  AND salary_max IS NOT NULL
ORDER BY salary_max DESC;

-- 10. Experience vs Average Salary
SELECT
    experience,
    AVG((salary_min + salary_max) / 2.0) AS average_salary
FROM jobs_job
WHERE salary_min IS NOT NULL
  AND salary_max IS NOT NULL
GROUP BY experience
ORDER BY average_salary DESC;

-- 11. Overall Job Market Summary
SELECT
    COUNT(*) AS total_jobs,
    COUNT(DISTINCT company) AS total_companies,
    COUNT(DISTINCT location) AS total_locations,
    COUNT(DISTINCT job_title) AS unique_job_roles
FROM jobs_job;