# Data transformation

# Function to calculate the increase amount

# Function to transform data


def transform(data):
    # calcul des moyennes par jour
    data_daily = data.groupby("date")["CPU_Usage"].mean().reset_index()
    data_daily = data_daily.sort_values(by="CPU_Usage", ascending=False)

    print("Moyenne d'utilisation du CPU par jour :")
    print(data_daily)

    print("##############################")

    # calcul des moyennes par heure
    data_hourly = data.groupby("heure")["CPU_Usage"].mean().reset_index()
    data_hourly = data_hourly.sort_values(by="CPU_Usage", ascending=False)

    print("Moyenne d'utilisation du CPU par heure :")
    print(data_hourly)

    print("##############################")

    # calcul des moyennes par jour
    data_daily = data.groupby("date")["Memory_Usage"].mean().reset_index()
    data_daily = data_daily.sort_values(by="Memory_Usage", ascending=False)

    print("Moyenne d'utilisation du Memory par jour :")
    print(data_daily)

    print("##############################")

    data_hourly = data.groupby("heure")["Memory_Usage"].mean().reset_index() 
    data_hourly = data_hourly.sort_values(by="Memory_Usage", ascending=False)

    print("Moyenne d'utilisation du Memory par heure :")
    print(data_hourly)

    return data
