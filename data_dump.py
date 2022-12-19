import pymongo
import pandas as pd
import json

client = pymongo.MongoClient("mongodb+srv://hemin59567:jecky123456@jecky59567.1fw3e.mongodb.net/?retryWrites=true&w=majority")

DATAFILE_PATH = "/config/workspace/aps_failure_training_set1.csv"
DATABASE_NAME = "aps"
COLLECTION_NAME = "sensor"


if __name__ == "__main__":
    df = pd.read_csv(DATAFILE_PATH)
    print(f"Rows and Columns :{df.shape}")

    # Covert dataframe in to Json format so that it can be dump in MongoDB
    df.reset_index(drop=True, inplace=True)

    json_record = list(json.loads(df.T.to_json()).values())
    print(json_record[0])

    # Inserting the json record in the MongoDB
    client[DATABASE_NAME][COLLECTION_NAME].insert_many(json_record)