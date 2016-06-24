import csv
import json

def main():

    areas = {}

    results = json.load(open('data/results.json'))

    for result in results:

        for answer in result.pop('answers'):
            if (answer['shortText'] == 'Remain'):
                remain = answer['percentageShare']
            elif (answer['shortText'] == 'Leave'):
                leave = answer['percentageShare']

        gss = result['gss']
        area = {
            'gss': gss,
            'remain': remain,
            'leave': leave
        }
        area.update(result)
        areas[gss] = area

    csv_file = csv.DictReader(open('data/education.csv', 'r'), delimiter=',', quotechar='"')

    labels = [
        'No qualifications',
        # 'Highest level of qualification: Level 1 qualifications',
        # 'Highest level of qualification: Level 2 qualifications',
        # 'Highest level of qualification: Level 3 qualifications',
        'Highest level of qualification: Level 4 qualifications and above'
    ]

    for line in csv_file:

        code = line.get('Area code',None)
        area = areas.get(code,False)
        if (not area): continue

        for label in labels:
            area[label] = float(line[label])

    series = [
        {
            'name': label,
            'data': [
                {
                    'x': area['remain'],
                    'y': float(area.get(label)),
                    'name': area['name']
                }
                for area in areas.values()
                if area.get(label)
            ]
        }
        for label in labels
    ]

    data = list(areas.values())
    json.dump(data,open('client/data.json','w'),indent=4)
    json.dump(series,open('client/series.json','w'),indent=4)


if (__name__ == "__main__"):
    main()
