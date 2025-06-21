from quixstreams import Application  # import the Quix Streams modules for interacting with Kafka
import os
from dotenv import load_dotenv, find_dotenv
import glob
import tqdm
import pandas as pd
import json

# Dynamically select .env file based on ENV (dev, prod, etc.)
#DOTENV_FILE = os.getenv("ENV_FILE", ".env")
DOTENV_FILE = ".env"

# Load env file, allow real env vars to override
load_dotenv(find_dotenv(DOTENV_FILE), override=False)


app = Application(auto_create_topics=True)  # create an Application

# stocks - OutputTopic
topic = app.topic(os.environ["stocks"])

def main():
    # make the path not relative
    data_files = glob.glob("data/*zst")
    print(f"len(data_files) {len(data_files)}")

    with app.get_producer() as producer:
        
        for file_path in tqdm.tqdm(data_files):
            print(f"Processing files {file_path}")

            data = pd.read_csv(file_path)

            for _, row in data.iterrows():
                single_row = row.to_dict()
                json_row = json.dumps(single_row)

                producer.produce(
                    topic = topic.name,
                    key=single_row['symbol'],
                    value=json_row
                )

            


    # Run the app
    # app.run(sdf)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Exiting.")
