# import the necessary packages
import os
import csv
import pathlib


def batchGet(filename):
    with open(filename) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        rowCounter = 0
        for row in csv_reader:
            #this row 0 check is only here because I was getting a weird UTF8 character if my CSV started on row 0
            #possibly fix by switching from csv import to pandas and accessing column row items
            if row == 0:
                print('beginning...')
            else:
                name = row[1]
                noSpaceName = name.replace(' ','')
                path = pathlib.Path.cwd().joinpath('dataset', noSpaceName)
                print(path)
                os.mkdir(path)
                os.system(f'python search_bing_api.py --query "{name}" --output dataset/{noSpaceName}')
                rowCounter += 1
            print(f'{rowCounter} completed')


batchGet('/Users/alexander.watanabe/Developer/ImageDataBuilder/femaleArtists.csv')