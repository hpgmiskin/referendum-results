import csv
import json
import matplotlib.pyplot as plot

def main():

    areas = {}

    results = json.load(open('data/results.json'))

    for result in results:

        for answer in result['answers']:
            if (answer['shortText'] == 'Remain'):
                remain = answer['percentageShare']
            elif (answer['shortText'] == 'Leave'):
                leave = answer['percentageShare']

        gss = result['gss']
        areas[gss] = {
            'gss': gss,
            'remain': remain,
            'leave': leave
        }

    csv_file = csv.DictReader(open('data/education.csv', 'r'), delimiter=',', quotechar='"')

    for line in csv_file:

        code = line.get('Area code',None)
        area = areas.get(code,False)
        if (not area): continue

        area['none'] = line['No qualifications']
        area['level_1'] = line['Highest level of qualification: Level 1 qualifications']
        area['level_2'] = line['Highest level of qualification: Level 2 qualifications']
        area['level_3'] = line['Highest level of qualification: Level 3 qualifications']
        area['level_4'] = line['Highest level of qualification: Level 4 qualifications and above']


    fieldnames = ['gss','remain','leave','none','level_1','level_2','level_3','level_4']

    output_file = open('data/output.csv','w')
    csvwriter = csv.DictWriter(output_file, delimiter=',', fieldnames=fieldnames)
    csvwriter.writerow(dict((fn,fn) for fn in fieldnames))
    for area in areas.values():
         csvwriter.writerow(area)
    output_file.close()


if (__name__ == "__main__"):
    main()
