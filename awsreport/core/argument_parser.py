import argparse

class CliArgumentParser():
    def argument_parser(self):
        parser = argparse.ArgumentParser()

        parser.add_argument('--ami', '--images',
                            action="store_true",
                            required=False)

        parser.add_argument('--sg', '--securitygroup',
                            action="store_true",
                            required=False)

        parser.add_argument('--cidr',
                            required=False)

        parser.add_argument('--owner', '--imagesowner',
                            required=False)

        parser.add_argument('--elasticip',
                            action="store_true",
                            required=False)

        parser.add_argument('--iam',
                            action="store_true",
                            required=False)

        parser.add_argument('--iam-max-age',
                            required=False)

        args = parser.parse_args()

        return args
