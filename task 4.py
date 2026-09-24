import pandas as pd
marks = pd.Series([85, 90, 78, 92, 88])
print("Pandas Series:")
print(marks)
students = pd.Series(
    [85, 90, 78],
    index=["Tejaswi", "Anu", "Priya"]
)
print("\nSeries with Student Names:")
print(students)
data = {
    "Name": ["Tejaswi", "Anu", "Priya"],
    "Age": [20, 21, 20],
    "Marks": [85, 90, 78]
}
df = pd.DataFrame(data)
print("Pandas DataFrame:")
print(df)
print("\nDataFrame Columns:",df.columns)
print("\nDataFrame Shape:",df.shape)
print("\nDataFrame Information:",df.info())