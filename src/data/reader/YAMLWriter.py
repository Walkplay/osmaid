from io import TextIOWrapper
import yaml

class YAMLWriter():

    # def __init__(self):
        # yaml.add_representer(Config, self.config_representer)
        # yaml.add_representer(ConfigItem, self.configItem_representer)


    def save_path(self, path: str, data: any):
        with open(path, 'w', encoding='utf8') as outfile:
            self.save_stream(outfile, data)

    def save_stream(self, stream: TextIOWrapper, data: any):
            yaml.safe_dump(data, stream, default_flow_style=False, allow_unicode=True)
    
    # def get_dumper(self):
    #     dumper = yaml.SafeDumper
    #     dumper.add_representer(Config, self.config_representer)
    #     dumper.add_representer(ConfigItem, self.configItem_representer)
    #     return dumper


    # def config_representer(self, dumper: SafeDumper, data:Config):
    #     return dumper.represent_mapping("!Config", {
    #         "items": data.items
    #     })

    # def configItem_representer(self, dumper: SafeDumper, data: ConfigItem):
    #     return dumper.represent_mapping("!ConfigItem", {
    #         "delta": data.delta.days,
    #         "entities": data.entities
    #     })



