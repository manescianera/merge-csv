import os
import glob
import pandas as pd
import pathlib
import csv
import time

wdir = str(pathlib.Path().absolute())
rmdir = wdir + '\\rm_lines'
bindir = wdir + '\\bin'
extension = 'csv'

if not os.path.exists(rmdir):
    os.makedirs(rmdir)

if not os.path.exists(bindir):
    os.makedirs(bindir)
    print('Created directory => ' + bindir + '\n')

os.chdir(wdir + '\\rm_lines')

files = [i for i in glob.glob('*.{}'.format(extension))]

if len(files):
    for f in files:
        with open(bindir + '\\new_' + f, 'w+', newline='') as output_file:
            with open(rmdir + '\\' + f) as input_file:
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

print('Lines removed.\n')

os.chdir(bindir)

files_for_merge = [j for j in glob.glob('*.{}'.format(extension))]
combined_csv = pd.concat(
    [pd.read_csv(f1) for f1 in files_for_merge])
merged_name = 'merged_' + time.strftime("%Y%m%d-%H%M%S")
combined_csv.to_csv(wdir + "\\" + merged_name + '.csv',
                    index=False, encoding='utf-8-sig')

print('CSV merged as ' + wdir + '\\' + merged_name + '\n')
