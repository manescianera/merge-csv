import os
import glob
import pandas as pd
import csv

# wdir = '/Users/zgs_prsnl/Documents/projects/merge-csv/'
wdir = ''
extension = 'csv'
os.chdir(wdir + 'rm_lines')

files = [i for i in glob.glob('*.{}'.format(extension))]

if len(files):
    for f in files:
        with open(wdir + 'bin/new_' + f, 'w+') as output_file:
            with open(wdir + 'rm_lines/' + f) as input_file:
                writer = csv.writer(
                    output_file, delimiter=',', quotechar='\"', quoting=csv.QUOTE_NONNUMERIC)
                reader = csv.reader(input_file)

                line_index = 0

                for row in reader:
                    if (line_index > 2):
                        writer.writerow(row)
                    line_index = line_index + 1
                input_file.close()
            output_file.close()

os.chdir(wdir + 'bin')

files_for_merge = [j for j in glob.glob('*.{}'.format(extension))]
combined_csv = pd.concat(
    [pd.read_csv(f1) for f1 in files_for_merge])
combined_csv.to_csv(wdir + "combined_csv.csv",
                    index=False, encoding='utf-8-sig')
