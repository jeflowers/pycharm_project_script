from src.config_loader import ConfigLoader
from src.config import Config
from src.directory_creator import DirectoryCreator
from src.structure_creator import StructureCreator
from src.project_structure_creator import ProjectStructureCreator
from src.cli_parser import CLIParser

class Application:
    def __init__(self, config_loader: ConfigLoader, project_structure_creator: ProjectStructureCreator, cli_parser: CLIParser):
        self.config_loader = config_loader
        self.project_structure_creator = project_structure_creator
        self.cli_parser = cli_parser

    def run(self):
        args = self.cli_parser.parse_args()
        try:
            config_data = self.config_loader.load(args.config_file)
            config = Config(config_data)
            self.project_structure_creator.create_project_structure(config, args.output)
        except Exception as e:
            print(f"An error occurred: {e}")

def main():
    config_loader = ConfigLoader()
    directory_creator = DirectoryCreator()
    structure_creator = StructureCreator(directory_creator)
    project_structure_creator = ProjectStructureCreator(structure_creator)
    cli_parser = CLIParser()
    
    app = Application(config_loader, project_structure_creator, cli_parser)
    app.run()

if __name__ == "__main__":
    main()
