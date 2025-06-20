from quixstreams import Application  # import the Quix Streams modules for interacting with Kafka
import os
from dotenv import load_dotenv, find_dotenv

# Dynamically select .env file based on ENV (dev, prod, etc.)
#DOTENV_FILE = os.getenv("ENV_FILE", ".env")
DOTENV_FILE = ".env"

# Load env file, allow real env vars to override
load_dotenv(find_dotenv(DOTENV_FILE), override=False)


app = Application()  # create an Application

# stocks - OutputTopic
stocks = app.topic(os.environ["stocks"])

# input_topic = app.topic("input-topic-name")

def main():
    """
    Your code goes here.
    See the Quix Streams documentation for more examples:
    https://quix.io/docs/quix-streams/quickstart.html
    """

    # Process incoming data using Streaming DataFrame
    # sdf = app.dataframe(input_topic)

    # Print incoming data
    # sdf.print()

    # Produce data to the output topic
    # sdf = sdf.to_topic(stocks)

    # Run the app
    # app.run(sdf)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Exiting.")
