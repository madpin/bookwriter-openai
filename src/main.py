from logger import initialize_logger

logger = initialize_logger(__name__)  #

from book_handler import BookHandler  # noqa: E402
from dummy import book  # noqa: E402
import logging  # noqa: E402

logger = logging.getLogger(__name__)


def main():
    i1 = input("test 123: ")
    print(i1)


if __name__ == "__main__":
    logger.info("Starting a new Jouney")
    bh = BookHandler()
    bh.print_book(book)
    bh.save_book(book)
