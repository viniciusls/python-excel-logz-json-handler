import json

import pandas


def main():
    csv_data = pandas.read_csv('input.csv')
    json_str = csv_data.to_json(orient='records')
    json_array = json.loads(json_str)

    requests_status = []
    requests_time = []
    for json_obj in json_array:
        message = json.loads(json_obj['message'])['message']
        info = message.split(' | ')[0].split(' - ')

        if info[0] == 'Initializing Kevel configuration':
            continue

        requests_status.append(info[0])
        requests_time.append(info[1])

    info_dict = {
        'status': requests_status,
        'time': requests_time
    }

    df = pandas.DataFrame(info_dict)
    df.to_csv('output.csv')

main()
