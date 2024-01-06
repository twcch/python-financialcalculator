import logging


class LogController:

    def __init__(self, log_path):
        self.set(log_path)

    def set(self, log_path):
        logging.basicConfig(
            filename=log_path,
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s')
