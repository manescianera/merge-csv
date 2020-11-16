import os
import glob
import pandas as pd
import pathlib
import csv
import time

wdir = str(pathlib.Path().absolute())
rmdir = wdir + '\\rm_lines'
ndir = wdir + '\\new'
mdir = wdir + '\\merged'
extension = 'csv'

if not os.path.exists(ndir):
    os.makedirs(ndir)
    print('Created directory => ' + ndir + '\n')

if not os.path.exists(mdir):
    os.makedirs(mdir)
    print('Created directory => ' + mdir + '\n')

def remove_lines():
    os.chdir(rmdir)
    files = [i for i in glob.glob('*.{}'.format(extension))]
    count = 0
    if len(files):
        for f in files:
            with open(ndir + '\\new_' + f, 'w+', newline='') as output_file:
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
                    print('\nLines removed from => ' + f)
                    count = count + 1
                output_file.close()
    print('\nLines removed from ' + str(count) + ' files.')


def merge():
    print('\nMerging...')
    os.chdir(ndir)
    files_for_merge = [j for j in glob.glob('*.{}'.format(extension))]
    combined_csv = pd.concat(
        [pd.read_csv(f1) for f1 in files_for_merge])
    merged_name = 'merged_' + time.strftime("%Y%m%d-%H%M%S")
    merged_csv = mdir + '\\' + merged_name + '.csv'
    combined_csv.to_csv(merged_csv,
                        index=False, encoding='utf-8-sig')
    with open(merged_csv) as f:
        row_count = sum(1 for row in f)
    print('\nCSV merged as ' + merged_csv + ' (' + str(row_count) + ' rows)\n')


# TODO write a function that makes all csv under 1 mil lines long

# def check_if_mil():


remove_lines()
merge()
    

