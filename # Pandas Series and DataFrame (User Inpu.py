# Pandas Series and DataFrame (User Input Version)
import pandas as pd

n = int(input("Enter number of students: "))

rollno = []
names = []
departments = []
marks_list = []
labels = []

for i in range(n):
    print(f"\n--- Student {i+1} ---")
    rollno.append(int(input("Roll No    : ")))
    names.append(input("Name       : "))
    departments.append(input("Department : "))
    marks_list.append(int(input("Mark       : ")))
    labels.append(chr(65 + i))   # A, B, C, D, E ... (index for Series)

# Pandas Series
marks = pd.Series(marks_list, index=labels)
print("\n--- Pandas Series ---")
print(marks)

# DataFrame
data = {
    "RollNo": rollno,
    "Name": names,
    "Department": departments,
    "Mark": marks_list
}
df = pd.DataFrame(data)
print("\n--- DataFrame ---")
print(df)

print("\nAverage Mark:", round(df["Mark"].mean(), 2))

limit = int(input("\nEnter mark limit to filter: "))
print(f"\nStudents scoring above {limit}:")
print(df[df["Mark"] > limit])