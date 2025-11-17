# Data transformation

# Function to calculate the increase amount

# Function to transform data


def transform(data):
    # update and add 325 to "montant cotisation" of year  "2014" and add 700 to "montant cotisation" of year "2020" as cot_update
    df_jour = data.groupby("weekday")["cnt"].sum().reset_index()
    df_jour = df_jour.sort_values(by="cnt", ascending=False)
    print(df_jour)
    return data
