from collections import defaultdict
from optparse import OptionParser
import os


def get_files_in_folder(s):
    ans = []
    for i in os.listdir(s):
        path = os.path.join(s, i)
        if os.path.isfile(path):
            ans.append(path)
    return ans


parser = OptionParser()
parser.add_option("--input-dir", dest="input_dir")
parser.add_option("--model", dest="save_path")
args, _ = parser.parse_args()

dct = defaultdict(list)


def process(text):
    s = text.split()
    arr = []
    for i in range(len(s)):
        s_ = ''.join(filter(str.isalnum, s[i])).lower()
        if s_ != '':
            arr.append(s_)

    for i in range(len(arr) - 1):
        prefix = arr[i]
        word = arr[i + 1]
        dct[prefix].append(word)


if args.input_dir is None:
    process(input("Enter text to train>"))
else:
    for i in get_files_in_folder(args.input_dir):
        process(open(i, encoding="utf-8").read())

out_file = open(args.save_path, 'w')
print(dict(dct), file=out_file)
out_file.close()
