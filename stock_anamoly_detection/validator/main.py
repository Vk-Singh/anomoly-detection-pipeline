from quixstreams import Application  # import the Quix Streams modules for interacting with Kafka
import os
from dotenv import load_dotenv, find_dotenv
import json

# File to validate the data from the producer
DOTENV_FILE = ".env"

# Load env file, allow real env vars to override
load_dotenv(find_dotenv(DOTENV_FILE), override=False)


app = Application(auto_create_topics=True)  # create an Application

# stocks - OutputTopic
input_topic = app.topic(os.environ["input_topic"])
output_topic = app.topic(os.environ("output_topic"))

def main():
    pass
            


    # Run the app
    # app.run(sdf)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Exiting.")
