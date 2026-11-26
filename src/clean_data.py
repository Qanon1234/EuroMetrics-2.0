import pandas as pd

df = pd.read_csv("data/raw/gdp_pps.csv")

# Välj kolumnerna vi behöver
df = df[["geo", "TIME_PERIOD", "OBS_VALUE", "OBS_FLAG"]]

# Byt namn på kolumnerna
df = df.rename(columns={
    "geo": "country_code",
    "TIME_PERIOD": "year",
    "OBS_VALUE": "pps_index",
    "OBS_FLAG": "quality_flag"
})

# Validera informationen
print("Antal rader:", len(df))
print("Antal länder:", df["country_code"].nunique())
print("Första året:", df["year"].min())
print("Sista året:", df["year"].max())

# Kontrollera saknade värden
print(df.isna().sum())

# Kontrollera dubbletter
print(df.duplicated(["country_code", "year"]).sum())
# Kontrollera antal observationer per land
print(df.groupby("country_code").size())
# Spara den bearbetade statistiken
df.to_csv("data/processed/gdp_pps_2000_2025.csv", index=False)