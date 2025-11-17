import logging
import os
import pandas as pd

# raw_data = pd.read_csv("C:/myproject/ircantec/data/raw/raw_ircantec.csv", sep=";")


def clean(raw_data, file_path):
    # Check if the DataFrame is empty
    if raw_data.empty:
        logging.error("The DataFrame is empty. Please check the input data.")
        return None
    # réccuperation de la date avec création d'une nouvelle colonne
    raw_data["Time"] = pd.to_datetime(raw_data["Time"], errors="coerce")
    raw_data["date"] = raw_data["Time"].dt.date
    raw_data["heure"] = raw_data["Time"].dt.time
    # save the cleaned file in the processes directory
    raw_data.to_csv(file_path, index=False)

    # Verify the persistance

    if os.path.exists(file_path):
        logging.info(f"Fichier persisté avec succès : {file_path}")
    else:
        logging.info("Fichier non trouvé.")

    return raw_data
