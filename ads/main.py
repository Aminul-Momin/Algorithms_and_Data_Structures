import logging
from ads.utils.utils import BASE_DIR


def main():
    logging.basicConfig(
        level=logging.DEBUG,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        datefmt='%m/%d/%Y %H:%M:%S',
        filename=BASE_DIR/"logs/root_logs.log",
        filemode="w"
    )

if __name__ == "__main__":
    main()
