import os
from .config import Config
from .structure_creator import StructureCreator

class ProjectStructureCreator:
    """
    A class responsible for creating the overall project structure.

    This class uses a StructureCreator to build the project directory structure
    and creates root files as specified in the configuration.

    Attributes:
        structure_creator (StructureCreator): An instance of StructureCreator used to create the directory structure.
    """

    def __init__(self, structure_creator: StructureCreator):
        """
        Initialize the ProjectStructureCreator with a StructureCreator instance.

        Args:
            structure_creator (StructureCreator): An instance of StructureCreator used to create the directory structure.
        """
        self.structure_creator = structure_creator

    def create_project_structure(self, config: Config, base_path: str):
        """
        Create the entire project structure based on the provided configuration.

        This method creates the project root directory, builds the directory structure,
        and creates any specified root files.

        Args:
            config (Config): A Config object containing the project configuration.
            base_path (str): The base path where the project structure should be created.

        Raises:
            OSError: If there's an error creating a directory or file.
        """
        project_path = os.path.join(base_path, config.project_name)
        self.structure_creator.directory_creator.create_directory(project_path)
        self.structure_creator.create_structure(project_path, config.structure)

        for file in config.root_files:
            if isinstance(file, str):
                self.structure_creator.directory_creator.create_file(os.path.join(project_path, file))

        print(f"Project structure created at: {project_path}")