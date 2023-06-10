from datetime import datetime
import os
from logger import initialize_logger

logger = initialize_logger(__name__)


def get_new_book_path(books_root_folder: str = "books") -> str:
    # Create the book folder variables
    path_month = datetime.now().strftime("%Y-%m")
    path_day = datetime.now().strftime("%d")
    path_day_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

    books_folder = f"{books_root_folder}/{path_month}/{path_day}/{path_day_time}"

    # Create the book folder structure
    folders = books_folder.split("/")
    current_folder = ""
    for folder in folders:
        current_folder += folder + "/"
        if not os.path.exists(current_folder):
            os.mkdir(current_folder)

    if not os.path.exists(books_folder):
        os.makedirs(books_folder)

    return books_folder


def get_last_book_path(contain_file="index.json") -> str:
    # Create the book folder variables

    # Sort the list of files by modification time (descending order)
    books_folder = "books"
    books_files = os.listdir(books_folder)

    month_folder = sorted(books_files, reverse=True)[0]
    month_fullpath = f"{books_folder}/{month_folder}"
    month_files = os.listdir(month_fullpath)

    day_folder = sorted(month_files, reverse=True)[0]
    day_fullpath = f"{books_folder}/{month_folder}/{day_folder}"

    logger.info(f"day_fullpath: {day_fullpath}")
    day_files = os.listdir(day_fullpath)
    logger.info(f"day_files: {day_files}")

    if contain_file:
        day_files = [
            folder
            for folder in day_files
            if contain_file in os.listdir(f"{day_fullpath}/{folder}")
        ]
    # print(f"day_files: {day_files}")
    time_folder = sorted(day_files, reverse=True)[0]
    time_fullpath = f"{books_folder}/{month_folder}/{day_folder}/{time_folder}"
    # time_files = os.listdir(time_fullpath)

    return time_fullpath
