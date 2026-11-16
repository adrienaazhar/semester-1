import pandas

data = pandas.read_csv("lifestyle_data.csv")

# What data type is `data` as output from the `read_csv()` method?

# For each of the following pieces of information, try and use pandas to find the answer from the dataset in 'data'
# - You can open the csv file to see what data is available.
# - Use the pandas documentation to explore functions that you can use.
# - Leave your code under the comments.

# 1. Find the total number of students
total_students = len(data)
print(total_students)

# 2. Find the mean average GPA
mean_gpa = data["GPA"].mean()
print(mean_gpa)

# 3. Find the standard deviation of sleep hours
sleep_std = data["Sleep_Hours_Per_Day"].std()
print(sleep_std)

# 4. Find the maximum study hours
max_study_hours = data["Study_Hours_Per_Day"].max()
print(max_study_hours)

# 5. Sort students by social hours (ascending)
sorted_students = data.sort_values(
    by="Social_Hours_Per_Day",
    ascending=True
)
print(sorted_students)

# 6. Add a Total_hours column
data["Total_hours"] = (
    data["Study_Hours_Per_Day"]
    + data["Extracurricular_Hours_Per_Day"]
    + data["Sleep_Hours_Per_Day"]
    + data["Social_Hours_Per_Day"]
    + data["Physical_Activity_Hours_Per_Day"]
)
print(data)

# 7. Filter students with high stress
high_stress = data[data["Stress_Level"] == "High"]
print(high_stress)

# 8. Filter students with low stress
low_stress = data[data["Stress_Level"] == "Low"]
print(low_stress)

# 9. Compare average GPA by stress level
average_gpa_by_stress = data.groupby("Stress_Level")["GPA"].mean()
print(average_gpa_by_stress)
