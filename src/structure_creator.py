import os
from typing import Dict, Any, Union
from .directory_creator import DirectoryCreator


class StructureCreator:
    """
    A class responsible for creating a directory structure based on a given configuration.

    This class works recursively to create nested directory structures and files
    as specified in the configuration dictionary.

    Attributes:
        directory_creator (DirectoryCreator): An instance of DirectoryCreator used to create directories and files.
    """

    def __init__(self, directory_creator: DirectoryCreator):
        """
        Initialize the StructureCreator with a DirectoryCreator instance.

        Args:
            directory_creator (DirectoryCreator): An instance of DirectoryCreator used to create directories and files.
        """
        self.directory_creator = directory_creator

    def create_structure(self, base_path: str, structure: Dict[str, Union[Dict, list, None]]):
        """
        Recursively create a directory structure based on the provided configuration.

        This method handles three cases:
        1. If sub_items is a dictionary, it recursively creates the structure.
        2. If sub_items is a list, it creates files for string items and recursively creates structures for dictionary items.
        3. If sub_items is None, it treats it as an empty directory.

        Args:
            base_path (str): The base path where the structure should be created.
            structure (Dict[str, Union[Dict, List, None]]): A dictionary representing the desired structure.
                Keys are directory/file names, values can be:
                - A dictionary (for nested directories)
                - A list (for files or nested structures)
                - None (for empty directories)

        Raises:
            OSError: If there's an error creating a directory or file.
        """
        for item, sub_items in structure.items():
            new_path = os.path.join(base_path, item)
            self.directory_creator.create_directory(new_path)

            if isinstance(sub_items, dict):
                self.create_structure(new_path, sub_items)
            elif isinstance(sub_items, list):
                for sub_item in sub_items:
                    if isinstance(sub_item, str):
                        self.directory_creator.create_file(os.path.join(new_path, sub_item))
                    elif isinstance(sub_item, dict):
                        self.create_structure(new_path, sub_item)
            # If sub_items is None, it's an empty directory, so we do nothing more