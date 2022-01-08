import argparse
from data import Config
from data.CleanDate import CleanDate
from domain.Evaluator import Evaluator
from reader.YAMLReader import YAMLReader


def main():
    parser = argparse.ArgumentParser(description='OS-maid to clean your cache')
    addArguments(parser)
    args = parser.parse_args()
    reader = YAMLReader()
    text = reader.extract_text(args.configPath)
    config = Config(**text)
    text = reader.extract_text(args.dataPath)
    date = CleanDate(**text)
    evaluator = Evaluator()
    folders = evaluator.evaluate(config, date)
    print(folders)


def addArguments(par: argparse.ArgumentParser):
    par.add_argument("-c", dest="configPath", type=str)
    par.add_argument("-d", dest="dataPath", type=str)


if __name__ == "__main__":
    main()
