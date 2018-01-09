import pandas as pd

df = pd.read_csv("supplies.csv")

df["total"] = df["Units"] * df["Unit Price"]

sales_results =  df.groupby(["Region", "Rep"])["total"].agg(["mean", "sum", "count"])

#region sales_results
regions = df.groupby(["Region"])["total"].agg(["sum"])
rep_count = df.groupby(["Region"])["Rep"].unique()
merged = regions.join(rep_count)
merged["rep_count"] =  [len(r) for r in merged["Rep"]]
merged["rep_count2"] = merged.apply(lambda row: len(row["Rep"]), axis = 1)

merged["normalized"] = merged["sum"] / merged["rep_count2"]
