import csv
import sys
import datetime

##################################################
##################################################
def first_ride(reader):
    lastDay = None   # since the row is already sorted by time in the csv file, this way works
    for rider in reader:
        day = datetime.datetime.strptime(rider['starttime'], '%Y-%m-%d %H:%M:%S+%f')
        if lastDay!=day.date():
            lastDay = day.date()
            yield rider
##################################################
##################################################

if __name__=='__main__':
    if len(sys.argv)<2:
        sys.stderr.write('USAGE: python %s <INPUT_CSV>\n' % sys.argv[0])
        sys.exit(1)
    
    with open(sys.argv[1], 'r') as fi:
        reader = csv.DictReader(fi)
        for row in first_ride(reader):
            print ','.join(map(row.get, reader.fieldnames))

