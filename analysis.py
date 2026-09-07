import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv("student_performance_data.csv")
print("Students:",df.Student_ID.nunique())
print("Average final score:",round(df.Final_Score.mean(),2))
print("Average attendance:",round(df["Attendance_%"].mean(),2))
print("\nSubject performance:")
print(df.groupby("Subject").Final_Score.mean().sort_values(ascending=False))
print("\nStudy method performance:")
print(df.groupby("Study_Method").Final_Score.mean().sort_values(ascending=False))
print("\nCorrelation with final score:")
print(df[["Study_Hours_Per_Day","Attendance_%","Assignment_Completion_%","Sleep_Hours","Previous_Score","Final_Score"]].corr()["Final_Score"].sort_values(ascending=False))
