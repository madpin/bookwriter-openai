import argparse
import json
import os
from logger import initialize_logger

logger = initialize_logger(__name__)

from openai_local import get_completion, get_completion_from_messages
from utils import get_new_book_path, get_last_book_path
from src.main import main as main_v2


# def function1a():
#     print("Function 1a called")


# def function1b():
#     print("Function 1b called")


# def function2a():
#     print("Function 2a called")


# def function2b():
#     print("Function 2b called")


def create_index():
    # Your application logic goes here
    book_path = get_new_book_path("books_consultant")

    messages = [
        {
            "role": "system",
            "content": (
                "You are an author, with cheesy humor, "
                "that writes about business, tech and consulting, focused on code examples language"
            ),
        },
        {
            "role": "user",
            "content": (
                "Can you give the the chapters, subchapters and sections "
                "for a book about how to be a tech consultant, with aproximately 500 pages \n"
                "The book should follow the most popular business advances "
                "Also write a short description of each chapter and subchapter, "
                "and how many pages it has \n\n"
                "The answer should be given in json format, "
                "with only the json content and nothing else, "
                "with the fields: "
                "book_title, subtitle, chapters (as a array), "
                "chapter_number, chapter_title, chapter_description, chapter_pages, subchapters (as a array), "
                "subchapter_number(int), subchapter_title, subchapter_description, subchapter_pages, sections (as a array),"
                "section_number(int), section_title, section_description, section_pages"
            ),
        },
    ]

    logger.debug(f"messages: {messages}")
    with open(f"{book_path}/prompt.json", mode="w") as file:
        json.dump(messages, file, indent=4)

    response = get_completion_from_messages(messages, temperature=0)
    logger.debug(response)

    with open(f"{book_path}/index.json", mode="w") as file:
        file.write(response)

    try:
        index_json = json.loads(response)
    except Exception as e:
        logger.error(f"Error parsing json: {e}")
        raise e

    def create_md_file(data, file_path):
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

                    file.write(
                        f"## {chapter_num}.{subchapter_num} {subchapter_title}\n\n"
                    )
                    file.write(f"{subchapter_desc}\n")
                    file.write(f"* Pages: {subchapter_pages}\n\n")

                    for section in subchapter["sections"]:
                        section_num = section["section_number"]
                        section_title = section["section_title"]
                        section_desc = section["section_description"]
                        section_pages = section["section_pages"]

                        file.write(
                            f"### {chapter_num}.{subchapter_num}.{section_num} {section_title}\n\n"
                        )
                        file.write(f"{section_desc}\n")
                        file.write(f"* Pages: {section_pages}\n\n")

    create_md_file(index_json, f"{book_path}/index.md")


def create_section(section_complete: str):
    try:
        input_chapter, input_subchapter, input_section = section_complete.split(".")
    except Exception:
        raise "Invalid section format. Should be: chapter.subchapter.section"
    logger.info(
        f"input_chapter: {input_chapter}, "
        f"input_subchapter: {input_subchapter}, "
        f"input_section: {input_section}"
    )
    book_path = get_last_book_path()
    file_index_json = f"{book_path}/index.json"
    # Open and read the contents of the file
    with open(file_index_json, "r") as f:
        file_index_json_content = f.read()
    book = json.loads(file_index_json_content)

    # msg = f'You are writing the book: {book["book_title"]} ({book["subtitle"]})\n'
    # msg += "chapters:\n"
    # for chapter in book["chapters"]:
    #     msg += f'{chapter["chapter_number"]}: {chapter["chapter_title"]} ({chapter["chapter_description"]})\n'
    #     for subchap in chapter["subchapters"]:
    #         msg += f'{subchap["subchapter_number"]}: {subchap["subchapter_title"]}\n'
    # msg += "\n\n"
    # msg += "I want you to write the subchapter 2.1: Data Preprocessing (In this subchapter, readers will learn how to clean and preprocess the data. They will learn techniques to handle missing values and format the data into a readable form.)"
    # msg += "The output should be a markdown file with aproximately 25 pages."
    section_to_use = None
    # book_title = book["book_title"]
    for chapter in book["chapters"]:
        logger.debug(
            f'chapter_number: {chapter["chapter_number"]}, input_chapter: {input_chapter}'
        )
        if str(input_chapter) != str(chapter["chapter_number"]):
            continue
        for subchapter in chapter["subchapters"]:
            if str(input_subchapter) != str(subchapter["subchapter_number"]):
                continue
            for section in subchapter["sections"]:
                if input_section == str(section["section_number"]):
                    section_to_use = section
                    break
    logger.debug(f"section_to_use: {section_to_use}")
    if section_to_use is None:
        raise Exception("Section not found")
    msg = f"""You are responsible for write the section:
    Title: {section_to_use["section_title"]}
    Description: {section_to_use["section_description"]}
    Write aproximately: {section_to_use["section_pages"]} pages
    Add an introduction in the beggining of the section
    then get deeper and add some examples in python
    you have available any dataset in sklearn.datasets or seaborn.load_dataset
    And the output should be a markdown file
    """

    messages = [
        {
            "role": "system",
            "content": (
                "You are an expert machine learning developer and author, "
                "with a cheesy humor, "
                "that writes about coding, tech and ai, "
                "always giving code examples highly explaned, "
                f"feel free to add descriptions of images encapsulated in `{([])}` "
                "where needed for the better understanding "
                "using python >= 3.9"
            ),
        },
        {
            "role": "user",
            "content": (msg),
        },
    ]
    logger.debug(f"messages: {messages}")
    if not os.path.exists(f"{book_path}/sections"):
        os.makedirs(f"{book_path}/sections")

    with open(f"{book_path}/sections/prompt_{section_complete}.json", mode="w") as file:
        json.dump(messages, file, indent=4)

    response = get_completion_from_messages(messages, temperature=0.5)
    logger.debug(response)

    with open(f"{book_path}/sections/section_{section_complete}.md", mode="w") as file:
        file.write(response)


def v2():
    main_v2()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Description of your program")
    subparsers = parser.add_subparsers(dest="command", help="Sub-command help")

    # create the parser for the "function1" command
    parser_function1 = subparsers.add_parser(
        "create_index",
        help="Create the index of the book",
    )
    # parser_function1.add_argument(
    #     "-a", "--argument1a", help="Description for argument1a", required=True
    # )
    # parser_function1.add_argument(
    #     "-b", "--argument1b", help="Description for argument1b", required=True
    # )

    # create the parser for the "function2" command
    parser_function2 = subparsers.add_parser(
        "create_section", help="Will create a section"
    )

    v2_function = subparsers.add_parser("v2", help="Let's start v2")
    parser_function2.add_argument(
        "-s", "--section", help="Which section should I genenrate", required=True
    )
    # parser_function2.add_argument(
    #     "-b", "--argument2b", help="Description for argument2b", required=True
    # )

    args = vars(parser.parse_args())

    if args["command"] == "create_index":
        create_index()

    elif args["command"] == "create_section":
        create_section(args["section"])

    elif args["command"] == "v2":
        v2()
