from datetime import datetime
import logging

import os
import json
import openai
from dotenv import load_dotenv, find_dotenv


# Define the logging configuration
logging.basicConfig(
    level=logging.NOTSET,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler(f"logs/beta2{__name__}.log"),
        logging.StreamHandler(),
    ],
)

logger = logging.getLogger(__name__)

logger.info("Hello, world!")


_ = load_dotenv(find_dotenv())  # read local .env file

# Create the book folder variables
path_month = datetime.now().strftime("%Y-%m")
path_day = datetime.now().strftime("%d")
path_day_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

# Sort the list of files by modification time (descending order)
folder_list = os.listdir(f"books/{path_month}/{path_day}")
filtered_folders = [
    folder
    for folder in folder_list
    if "index.json" in os.listdir(f"books/{path_month}/{path_day}/{folder}")
]
sorted_files = sorted(
    filtered_folders,
    reverse=True,
)
logger.debug(sorted_files)

# Get the last (largest filename) file in the folder
last_folder = sorted_files[0]

BOOK_FOLDER = f"books/{path_month}/{path_day}/{last_folder}"
logger.debug(f"BOOK_FOLDER: {BOOK_FOLDER}")
# Create the book folder structure
folders = BOOK_FOLDER.split("/")
current_folder = ""
for folder in folders:
    current_folder += folder + "/"
    if not os.path.exists(current_folder):
        os.mkdir(current_folder)

if not os.path.exists(BOOK_FOLDER):
    os.makedirs(BOOK_FOLDER)

# Load the openai api key
openai.api_key = os.getenv("OPENAI_API_KEY")


def get_completion(prompt, model="gpt-3.5-turbo", temperature=0):
    """
    Get the completion from the openai api

    Args:
        prompt (str):
            prompt to send to the api
        model (str, optional):
            openai model . Defaults to "gpt-3.5-turbo".
        temperature (int, optional):
            degree of randomness of the model's output. Defaults to 0.

    Returns:
        str: completion from the openai api
    """
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=temperature,  # this is the degree of randomness of the model's output
    )
    return response.choices[0].message["content"]


def get_completion_from_messages(messages, model="gpt-3.5-turbo", temperature=0):
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=temperature,  # this is the degree of randomness of the model's output
    )
    return response.choices[0].message["content"]


file_index_json = f"{BOOK_FOLDER}/index.json"

# Open and read the contents of the file
with open(file_index_json, "r") as f:
    file_contents = f.read()

# Print the contents of the last file
print(file_contents)

data = json.loads(file_contents)

msg = f'You are writing the book: {data["book_title"]} ({data["subtitle"]})\n'
msg += "chapters:\n"
for chapter in data["chapters"]:
    msg += f'{chapter["chapter_number"]}: {chapter["chapter_title"]} ({chapter["chapter_description"]})\n'
    for subchap in chapter["subchapters"]:
        msg += f'{subchap["subchapter_number"]}: {subchap["subchapter_title"]}\n'
msg += "\n\n"
msg += "I want you to write the subchapter 2.1: Data Preprocessing (In this subchapter, readers will learn how to clean and preprocess the data. They will learn techniques to handle missing values and format the data into a readable form.)"
msg += "The output should be a markdown file with aproximately 25 pages."

messages = [
    {
        "role": "system",
        "content": (
            "You are an author, with cheesy humor, "
            "that writes about coding, tech and ai, focused on code examples"
        ),
    },
    {
        "role": "user",
        "content": (msg),
    },
]
logger.debug(f"messages: {messages}")
with open(f"{BOOK_FOLDER}/prompt_chapter_2.1.json", mode="w") as file:
    json.dump(messages, file, indent=4)

response = get_completion_from_messages(messages, temperature=0)
logger.debug(response)

with open(f"{BOOK_FOLDER}/subchapter_2.1.md", mode="w") as file:
    file.write(response)
