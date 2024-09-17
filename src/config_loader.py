import yaml
import json
import csv
import os
from typing import Dict, Any

class ConfigLoader:
    @staticmethod
    def load_yml(file_path: str) -> Dict[str, Any]:
        with open(file_path, 'r') as config_file:
            return yaml.safe_load(config_file)

    @staticmethod
    def load_json(file_path: str) -> Dict[str, Any]:
        with open(file_path, 'r') as config_file:
            return json.load(config_file)

    @staticmethod
    def load_csv(file_path: str) -> Dict[str, Any]:
        with open(file_path, 'r') as config_file:
            return dict(csv.reader(config_file))

    @classmethod
    def load(cls, file_path: str) -> Dict[str, Any]:
        _, file_extension = os.path.splitext(file_path)
        if file_extension in ['.yml', '.yaml']:
            return cls.load_yml(file_path)
        elif file_extension == '.json':
            return cls.load_json(file_path)
        elif file_extension == '.csv':
            return cls.load_csv(file_path)
        else:
            raise ValueError(f"Unsupported file format: {file_extension}")
