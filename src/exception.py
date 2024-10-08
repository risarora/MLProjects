import sys
from src.logger import logging


def error_message_details(error, exc_tb):
    file_name = exc_tb.tb_frame.f_code.co_filename
    line_number = exc_tb.tb_lineno
    error_message = f"Error occurred in Python script {file_name} at line {line_number}: {str(error)}"
    return error_message

class CustomException(Exception):
    def __init__(self, error_message):
        super().__init__(error_message)
        self.error_message = error_message

    def __str__(self):
        return self.error_message

def main():
    try:
        a = 1/0
    except Exception as e:
        exc_tb = sys.exc_info()[2]
        logging.error(error_message_details(e, exc_tb))
        raise CustomException(error_message_details(e, exc_tb))

if __name__ == "__main__":
    main()