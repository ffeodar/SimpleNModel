from optparse import OptionParser
from random import choice
from pickle import load

parser = OptionParser()
parser.add_option("--length", dest="length")
parser.add_option("--model", dest="load_path")
parser.add_option("--prefix", dest="prefix")

args, _ = parser.parse_args()

dct = load(open(args.load_path, 'rb'))

text = []

if args.prefix is None:
    text = [choice(list(dct.keys()))]
else:
    text = [args.prefix]

for i in range(1, int(args.length)):
    text.append(choice(dct[text[-1]]))
print(*text)
