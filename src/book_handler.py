import pymongo
from model import Book
import logging
import uuid

logger = logging.getLogger(__name__)


mongo_client = pymongo.MongoClient("mongodb://root:root_password@localhost:27017/")
mongo_db = mongo_client["book_database"]
books_collection = mongo_db["books"]


class BookHandler:
    def print_book(self, book: Book) -> None:
        """Prints book information"""
        print("_" * 80 + "\n")
        print(f"Book: {book.title} ({book.subtitle})")
        print(f"Description: {book.description}")
        print(f"Short Description: {book.short_description}\n")

        for chapter in book.chapters:
            print(f"| Chapter {chapter.id}: {chapter.title}")
            print(f"| Description: {chapter.description}")
            print(f"| Short Description: {chapter.short_description}\n")

            for subchapter in chapter.subchapters:
                print(f"|| Subchapter {subchapter.id}: {subchapter.title}")
                print(f"|| Description: {subchapter.description}")
                print(f"|| Short Description: {subchapter.short_description}\n")

                for section in subchapter.sections:
                    print(f"||| Section {section.id}: {section.title}")
                    print(f"||| Description: {section.description}")
                    print(f"||| Content: {section.content}\n")
        print("_" * 80)

    def save_book(self, book: Book) -> None:
        """Saves or updates a book to the MongoDB database."""
        logger.info("Saving the book")
        book_dict = book.dict()
        book_id = book_dict.pop("id")

        existing_book = books_collection.find_one({"_id": book_id})
        if existing_book:
            logger.info("Updating existing book")
            # Update the existing book
            books_collection.update_one({"_id": book_id}, {"$set": book_dict})
        else:
            logger.info("Inserting new book")
            # Insert a new book
            book_dict["_id"] = (
                book_id if book_id else str(uuid.uuid4())
            )
            books_collection.insert_one(book_dict)

    def read_book(self, book_id: int) -> Book:
        """Reads a book from the MongoDB database."""
        logger.info("Reading book with id: ", book_id)
        book_data = books_collection.find_one({"_id": book_id})
        return Book(**book_data)
