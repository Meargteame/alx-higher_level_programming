import argparse

# Create the parser
parser = argparse.ArgumentParser(description='Process some integers.')

# Define positional arguments
parser.add_argument('arg1', help='The first argument')
parser.add_argument('arg2', help='The second argument')

# Define an optional argument

# Parse the arguments
args = parser.parse_args()

# Access and print the arguments
print('Argument 1:', args.arg1)
print('Argument 2:', args.arg2)
