import argparse

from Util.CustomError import CustomError


class ArgumentParser(argparse.ArgumentParser):
    def error(self, message):
        raise CustomError(message)
