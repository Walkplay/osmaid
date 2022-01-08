import yaml


class YAMLReader():
    """Extract text from a .yml file"""
    def load_data_source(self, path: str, file_name: str) -> str:
        with open(path + file_name, "r") as stream:
            try:
                print(yaml.safe_load(stream))
            except yaml.YAMLError as exc:
                print(exc)
    

    def extract_text(self, full_file_path: str) -> dict:
        with open(full_file_path, "r") as stream:
            try:
                return yaml.safe_load(stream)
            except yaml.YAMLError as exc:
                print(exc)