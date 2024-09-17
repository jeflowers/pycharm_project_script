import argparse

class CLIParser:
    @staticmethod
    def parse_args():
        parser = argparse.ArgumentParser(description="Create project directory structure from a configuration file.")
        parser.add_argument("config_file", help="Path to the configuration file (YAML, JSON, or CSV)")
        parser.add_argument("--output", default=".", help="Output directory for the project structure")
        return parser.parse_args()
