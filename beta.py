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
    handlers=[logging.FileHandler(f"logs/{__name__}.log"), logging.StreamHandler()],
)

logger = logging.getLogger(__name__)

logger.info("Hello, world!")


_ = load_dotenv(find_dotenv())  # read local .env file

# Create the book folder variables
path_month = datetime.now().strftime("%Y-%m")
path_day = datetime.now().strftime("%d")
path_day_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

BOOK_FOLDER = f"books/{path_month}/{path_day}/{path_day_time}"

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


messages = [
    {
        "role": "system",
        "content": (
            "You are an author, with cheesy humor, "
            "that writes about coding, tech and ai, focused on code examples in python 3.9 or above"
        ),
    },
    {
        "role": "user",
        "content": (
            "Can you give the the chapters, and subchapters "
            "for a book about machine learning, with aproximately 500 pages \n"
            "The book should follow the most popular packages and frameworks "
            "and focus on python developement, giving fully functional examples of code \n"
            "Also write a short description of each chapter and subchapter, "
            "and how many pages it has \n\n"
            "The answer should be given in json format, "
            "with only the json content and nothing else, "
            "with the fields: "
            "book_title, subtitle, chapters (as a array), "
            "chapter_number, chapter_title, chapter_description, chapter_pages, subchapters (as a array), "
            "subchapter_number(int), subchapter_title, subchapter_description, subchapter_pages"
        ),
    },
]
logger.debug(f"messages: {messages}")
with open(f"{BOOK_FOLDER}/prompt.json", mode="w") as file:
    json.dump(messages, file, indent=4)

response = get_completion_from_messages(messages, temperature=0)
logger.debug(response)

with open(f"{BOOK_FOLDER}/index.json", mode="w") as file:
    file.write(response)

try:
    index_json = json.loads(response)
except Exception as e:
    logger.error(f"Error parsing json: {e}")
    raise e


def create_md_file(data, file_path):
    """
    Data Example:
    {
    "book_title": "Machine Learning for Dummies",
    "subtitle": "A Comprehensive Guide to Understanding ",
    "chapters": [
        {
        "chapter_number": 1,
        "chapter_title": "Introduction to Machine Learning",
        "chapter_description": "What is machine learning? Why is it important?",
        "chapter_pages": 30,
        "subchapters": [
            {
            "subchapter_number": 1.3,
            "subchapter_title": "How Machine Learning Works",
            "subchapter_description": "Fundamental steps involved",
            "subchapter_pages": 10
            }
        ]
        }
    ]
    }

    Args:
        data (_type_): _description_
        file_path (_type_): _description_
    """
    with open(file_path, mode="w") as file:
        file.write(f"# {data['book_title']}\n")
        file.write(f"{data['subtitle']}\n\n")

        for chapter in data["chapters"]:
            chapter_num = chapter["chapter_number"]
            chapter_title = chapter["chapter_title"]
            chapter_desc = chapter["chapter_description"]
            chapter_pages = chapter["chapter_pages"]

            file.write(f"# Chapter {chapter_num} - {chapter_title}\n")
            file.write(f"{chapter_desc}\n")
            file.write(f"* Pages: {chapter_pages}\n\n")

            for subchapter in chapter["subchapters"]:
                subchapter_num = subchapter["subchapter_number"]
                subchapter_title = subchapter["subchapter_title"]
                subchapter_desc = subchapter["subchapter_description"]
                subchapter_pages = subchapter["subchapter_pages"]

                file.write(f"## {chapter_num}.{subchapter_num} {subchapter_title}\n\n")
                file.write(f"{subchapter_desc}\n")
                file.write(f"* Pages: {subchapter_pages}\n\n")


create_md_file(index_json, f"{BOOK_FOLDER}/index.md")
