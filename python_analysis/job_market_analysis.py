import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

# Connect to Django SQLite database
connection = sqlite3.connect(r"C:\Users\Sanjay Kumar\DjangoFresh\db.sqlite3")

# Load job data from database
query = "SELECT * FROM jobs_job"

df = pd.read_sql_query(query, connection)

print(df)

print("\nColumn Names:")
print(df.columns)

print("\nDataset Information:")
print(df.info())

# Jobs by Location
location_counts = df["location"].value_counts()

print("\nJobs by Location:")
print(location_counts)

# Jobs by Employment Type
employment_counts = df["employment_type"].value_counts()

print("\nJobs by Employment Type:")
print(employment_counts)

# Jobs by Experience
experience_counts = df["experience"].value_counts()

print("\nJobs by Experience:")
print(experience_counts)

# Average Salary
df["average_salary"] = (df["salary_min"] + df["salary_max"]) / 2

average_salary = df["average_salary"].mean()

print("\nAverage Salary:")
print(round(average_salary, 2), "LPA")

# Minimum and Maximum Salary
minimum_salary = df["salary_min"].min()
maximum_salary = df["salary_max"].max()

print("\nSalary Range:")
print("Minimum Salary:", minimum_salary, "LPA")
print("Maximum Salary:", maximum_salary, "LPA")

# Average Salary by Location
salary_by_location = df.groupby("location")["average_salary"].mean().sort_values(ascending=False)

print("\nAverage Salary by Location:")
print(salary_by_location)

# Jobs by Company
company_counts = df["company"].value_counts()

print("\nJobs by Company:")
print(company_counts)

# High-Paying Job Roles
high_paying_jobs = df.sort_values("salary_max", ascending=False)

print("\nHigh-Paying Job Roles:")
print(high_paying_jobs[["job_title", "company", "location", "salary_min", "salary_max"]])

# Experience vs Average Salary
experience_salary = (
    df.groupby("experience")["average_salary"]
    .mean()
    .sort_values(ascending=False)
)

print("\nExperience vs Average Salary:")
print(experience_salary)

# Most Demanded Skills
skills = df["skills"].str.split(",")

all_skills = skills.explode().str.strip()

skill_counts = all_skills.value_counts()

print("\nMost Demanded Skills:")
print(skill_counts)

# Overall Job Market Summary
total_jobs = len(df)
total_companies = df["company"].nunique()
total_locations = df["location"].nunique()
unique_roles = df["job_title"].nunique()

print("\nOverall Job Market Summary:")
print("Total Jobs:", total_jobs)
print("Total Companies:", total_companies)
print("Total Locations:", total_locations)
print("Unique Job Roles:", unique_roles)

# Save analyzed data for Power BI
df.to_csv(r"C:\Users\Sanjay Kumar\DjangoFresh\python_analysis\job_market_analyzed.csv", index=False)

print("\nAnalysis file saved successfully!")

# Jobs by Location Chart
location_counts.plot(kind="bar")

plt.title("Number of Jobs by Location")
plt.xlabel("Location")
plt.ylabel("Number of Jobs")
plt.xticks(rotation=0)

plt.tight_layout()
plt.show()

# Jobs by Employment Type Chart
employment_counts.plot(kind="bar")

plt.title("Number of Jobs by Employment Type")
plt.xlabel("Employment Type")
plt.ylabel("Number of Jobs")
plt.xticks(rotation=0)

plt.tight_layout()
plt.show()

# Jobs by Experience Chart
experience_counts.plot(kind="bar")

plt.title("Number of Jobs by Experience Level")
plt.xlabel("Experience")
plt.ylabel("Number of Jobs")
plt.xticks(rotation=45)

plt.tight_layout()
plt.show()

# Average Salary by Location Chart
salary_by_location.plot(kind="bar")

plt.title("Average Salary by Location")
plt.xlabel("Location")
plt.ylabel("Average Salary (LPA)")
plt.xticks(rotation=0)

plt.tight_layout()
plt.show()

# Salary by Job Role
df.plot(
    x="job_title",
    y=["salary_min", "salary_max"],
    kind="bar"
)

plt.title("Salary Range by Job Role")
plt.xlabel("Job Role")
plt.ylabel("Salary (LPA)")
plt.xticks(rotation=45)

plt.tight_layout()
plt.show()

# Most Demanded Skills Chart
top_skills = skill_counts.head(10)

top_skills.plot(kind="bar")

plt.title("Top 10 Most Demanded Skills")
plt.xlabel("Skill")
plt.ylabel("Number of Job Postings")
plt.xticks(rotation=45)

plt.tight_layout()
plt.show()

# Jobs by Company Chart
company_counts.plot(kind="bar")

plt.title("Number of Jobs by Company")
plt.xlabel("Company")
plt.ylabel("Number of Jobs")
plt.xticks(rotation=45)

plt.tight_layout()
plt.show()