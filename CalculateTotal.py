import pandas as pd
import argparse
import sys


parser = argparse.ArgumentParser()

parser.add_argument("-I", "--input", help="Path to the input .csv from star.vote. (eg. ~/Desktop/starvoting_ballots_1234678_20210414010104.csv)")
parser.add_argument("-O", "--output", help="Path to the output file (eg. ~/Desktop/totalvotes.csv)")

args = parser.parse_args()

if args.input and args.output:
     print("Starting...")
else:
     print("Lacking parameters, terminating. Try running with --help (-h).")
     sys.exit(0)


results = pd.read_csv(args.input)

voteTime = results['voteTime'].tolist()

for iv in range(1, 68):
     results.loc[iv] = results.loc[iv] + results.loc[iv-1]

for ib in range(0, 68):
     results.loc[ib, 'voteTime'] = voteTime.__getitem__(ib)


results.to_csv(args.output)
print(results)