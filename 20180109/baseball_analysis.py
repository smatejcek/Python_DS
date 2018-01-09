import pandas as pd
import morestats as ms

df = pd.read_csv("baseball.csv")

avg_height = ms.means(df["Height"])
avg_weight = ms.means(df["Weight"])
avg_age = ms.means(df["Age"])

teams = df.groupby(["Team"]).mean()

arizona = teams.loc["ARZ"]

tall = teams.sort_values(by = ["Height"], ascending = False).head(1)

tall_team = teams.idxmax()["Height"]

maximums = teams.idxmax #Maximums of all columns

slice1 = teams.loc["BAL":"CLE", "Height":"Weight"]
