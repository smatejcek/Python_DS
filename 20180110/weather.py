import pandas as pd

df = pd.read_csv("KCLT.csv")

#Covert text date field to actual date
df["date"] = pd.to_datetime(df.date)

temp_range = df[(df["actual_mean_temp"] < 19) | (df["actual_mean_temp"] > 86)][["date", "actual_mean_temp"]]
eighty_one =  df[df["actual_mean_temp"] == 81]


df = pd.read_excel("Long-Term-Unemployment-Statistics.xlsx")
