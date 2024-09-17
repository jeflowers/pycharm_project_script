import os
from typing import Dict, Any
from .directory_creator import DirectoryCreator

class StructureCreator:
    def __init__(self, directory_creator: DirectoryCreator):
        self.directory_creator = directory_creator

    def create_structure(self, base_path: str, structure: Dict[str, Any]):
        for item, sub_items in structure.items():
            new_path = os.path.join(base_path, item)
            self.directory_creator.create_directory(new_path)
            if isinstance(sub_items, list):
                for sub_item in sub_items:
                    self.directory_creator.create_file(os.path.join(new_path, sub_item))
            elif isinstance(sub_items, dict):
                self.create_structure(new_path, sub_items)
