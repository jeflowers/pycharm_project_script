import os

class DirectoryCreator:
    @staticmethod
    def create_directory(path: str):
        os.makedirs(path, exist_ok=True)

    @staticmethod
    def create_file(path: str):
        open(path, 'a').close()
