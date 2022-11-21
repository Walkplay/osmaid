import argparse
from datetime import datetime
from data import *
from domain import *
from datetime import timedelta
import os


def install(args):

    writer = YAMLWriter()
    extension = ".yml"
    configFileName = "config"
    reportFileName = "report"
    print("Installing...")

    if not os.path.exists(args.output):
        os.makedirs(args.output)
        print("Create missing directory...")

    session = ConfigItem(timedelta(days=0), ["session1"])
    daily = ConfigItem(timedelta(days=1), ["daily1"])
    weekly = ConfigItem(timedelta(days=7),["weekly1"])
    monthly = ConfigItem(timedelta(days=30),["monthly1"])
    config = Config([session, daily, weekly, monthly])

    configPath = os.path.join(args.output, configFileName) + extension
    writer.save_path(configPath, config)
    print(f"Generate config file at: {configPath}")

    report = Report(0, {})

    reportPath:str = os.path.join(args.output, reportFileName) + extension
    writer.save_path(reportPath, report)
    print(f"Generate report file at: {reportPath}")


def run(args):
    reader = YAMLReader()
    writer = YAMLWriter()
    config:Config = reader.extract_text(args.configIO)
    report:Report = reader.extract_text(args.reportIO)

    currentTime = datetime.now()
    filter = Filter(currentTime)
    evaluator = Evaluator(filter, config, report)
    pathCollection = evaluator.evaluate()

    cleaner = Cleaner(pathCollection)
    cleaner.clean()

    report.update(pathCollection, currentTime.timestamp())

    args.reportIO.seek(0)
    writer.save_stream(args.reportIO, report)

    print(pathCollection)
    pass


if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog='OSMaid', description='OS-maid to clean your cache')
    parser.add_argument('--version', action='version', version='%(prog)s 0.0.1')
    subparsers = parser.add_subparsers(help='sub-command help')

    installParser = subparsers.add_parser('install', help='install help')
    installParser.add_argument("-o", dest="output", help="Install folder")
    installParser.set_defaults(func=install)

    runParser = subparsers.add_parser('run', help='run help')
    runParser.add_argument("-c", dest="configIO", type=argparse.FileType('r'))
    runParser.add_argument("-r", dest="reportIO", type=argparse.FileType('r+'))
    runParser.set_defaults(func=run)

    args = parser.parse_args()
    args.func(args)


