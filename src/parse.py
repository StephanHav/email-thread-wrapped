def parse(df):
    df["year"] = df["date"].dt.year
    df["month"] = df["date"].dt.month
    df["weekday"] = df["date"].dt.day_name()
    df["hour"] = df["date"].dt.hour
    df["length"] = df["body"].str.len()
    df["opening"] = df["body"].str.split("\n").str[0]
    return df

