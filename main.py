import json

import pandas


def main():
    csv_data = pandas.read_csv('input.csv')
    json_str = csv_data.to_json(orient='records')
    json_array = json.loads(json_str)

    requests_timestamp = []
    requests_status = []
    requests_time = []
    for json_obj in json_array:
        json_message = json.loads(json_obj['message'])
        timestamp = json_message['time']
        message = json_message['message']
        info = message.split(' | ')[0].split(' - ')

        if info[0] == 'Initializing Kevel configuration':
            continue

        requests_timestamp.append(timestamp)
        requests_status.append(info[0])
        requests_time.append(info[1].replace('ms', ''))

    info_dict = {
        'timestamp': requests_timestamp,
        'status': requests_status,
        'time': requests_time
    }

    df = pandas.DataFrame(info_dict)
    df.to_csv('output.csv')

main()
