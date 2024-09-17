import os
from .config import Config
from .structure_creator import StructureCreator

class ProjectStructureCreator:
    def __init__(self, structure_creator: StructureCreator):
        self.structure_creator = structure_creator

    def create_project_structure(self, config: Config, base_path: str):
        project_path = os.path.join(base_path, config.project_name)
        self.structure_creator.directory_creator.create_directory(project_path)
        self.structure_creator.create_structure(project_path, config.structure)

        for file in config.root_files:
            self.structure_creator.directory_creator.create_file(os.path.join(project_path, file))

        print(f"Project structure created at: {project_path}")
