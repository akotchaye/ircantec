import logging
import os

# raw_data = pd.read_csv("C:/myproject/ircantec/data/raw/raw_ircantec.csv", sep=";")


def clean(raw_data, file_path):
    # Check if the DataFrame is empty
    if raw_data.empty:
        logging.error("The DataFrame is empty. Please check the input data.")
        return None
    # Convert effectif_cotisants into int
    raw_data["weekday"] = raw_data["weekday"].astype("string")
    # Convert effectif_cotisants into int
    raw_data["weekday"] = raw_data["weekday"].str.replace("0", "Dimanche")
    raw_data["weekday"] = raw_data["weekday"].str.replace("1", "Lundi")
    raw_data["weekday"] = raw_data["weekday"].str.replace("2", "Mardi")
    raw_data["weekday"] = raw_data["weekday"].str.replace("3", "Mercredi")
    raw_data["weekday"] = raw_data["weekday"].str.replace("4", "jeudi")
    raw_data["weekday"] = raw_data["weekday"].str.replace("5", "vendredi")
    raw_data["weekday"] = raw_data["weekday"].str.replace("6", "samedi")

    # save the cleaned file in the processes directory
    raw_data.to_csv(file_path, index=False)

    # Verify the persistance

    if os.path.exists(file_path):
        logging.info("Fichier persisté avec succès :", file_path)
    else:
        logging.info("Fichier non trouvé.")

    return raw_data
