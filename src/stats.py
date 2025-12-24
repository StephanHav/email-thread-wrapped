def top_senders(df, n=5):
    return df["from"].value_counts().head(n)

def bottom_senders(df):
    return df["from"].value_counts().tail(1)

def top_openings(df, n=5):
    return df["opening"].value_counts().head(n)

def busiest_day(df):
    return df.groupby("weekday").size().sort_values(ascending=False)

