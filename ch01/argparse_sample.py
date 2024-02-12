import argparse

parser = argparse.ArgumentParser(description="Example CLI tool.")
parser.add_argument('--echo', help="Echo the string you use here")
args = parser.parse_args()

print(args.echo)
