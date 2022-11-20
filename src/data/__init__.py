from datetime import timedelta
from data.Config import Config
from data.ConfigItem import ConfigItem
from data.Report import Report
from data.reader.YAMLReader import YAMLReader
from data.reader.YAMLWriter import YAMLWriter
import yaml
from yaml import SafeDumper


def config_representer(dumper: SafeDumper, data:Config):
    return dumper.represent_mapping("!Config", {
        "items": data.items
    })

def config_constructor(loader: yaml.SafeLoader, node: yaml.nodes.MappingNode) -> Config:
    return Config(**loader.construct_mapping(node))

def configItem_representer(dumper: SafeDumper, data: ConfigItem):
    return dumper.represent_mapping("!ConfigItem", {
        "delta": data.delta.days,
        "entities": data.entities
    })

def configItem_constructor(loader: yaml.SafeLoader, node: yaml.nodes.MappingNode) -> ConfigItem:
    values = values = loader.construct_mapping(node)
    delta = timedelta(days = values["delta"])
    entities = values["entities"]
    return ConfigItem(delta, entities)

def report_representer(dumper: SafeDumper, data: Report):
    return dumper.represent_mapping("!Report", {
        "lastRun": data.lastRun,
        "table": data.table
    })

def report_constructor(loader: yaml.SafeLoader, node: yaml.nodes.MappingNode) -> Report:
    return Report(**loader.construct_mapping(node))

    
yaml.SafeLoader.add_constructor("!Config", config_constructor)
yaml.SafeLoader.add_constructor("!ConfigItem", configItem_constructor)
yaml.SafeLoader.add_constructor("!Report", report_constructor)

yaml.SafeDumper.add_representer(Config, config_representer)
yaml.SafeDumper.add_representer(ConfigItem, configItem_representer)
yaml.SafeDumper.add_representer(Report, report_representer)


