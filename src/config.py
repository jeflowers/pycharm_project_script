from typing import Dict, Any

class Config:
    def __init__(self, config_data: Dict[str, Any]):
        self.project_name = config_data['project_name']
        self.structure = config_data['structure']
        self.root_files = config_data.get('root_files', [])
