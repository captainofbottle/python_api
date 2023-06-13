import requests
import csv


def create_reaction(header, react):
    with open(header) as h:
        reader_h = csv.reader(h)
        for j in reader_h:
            cookie = {
                'Cookie': f'{j[0]}',
            }
            with open(react) as r:
                reader_r = csv.reader(r)
                for i in reader_r:
                    body = {
                        "code": f"{i[0]}",
                        "message_id": f"{i[1]}"
                    }
                    url = "https://api.pachca.com/api/v3/reactions"
                    reactions = requests.post(url, headers=cookie, json=body)
                    print(
                        f"Status : {reactions.status_code} {reactions.reason}, Time : {reactions.elapsed.total_seconds()}")


def delete_reaction(header, react):
    with open(header) as h:
        reader_h = csv.reader(h)
        for j in reader_h:
            cookie = {
                'Cookie': f'{j[0]}',
            }
            with open(react) as r:
                reader_r = csv.reader(r)
                for i in reader_r:
                    body = {
                        "code": f"{i[0]}",
                        "message_id": f"{i[1]}"
                    }
                    url = "https://api.pachca.com/api/v3/reactions"
                    reactions = requests.delete(url, headers=cookie, json=body)
                    print(
                        f"Status : {reactions.status_code} {reactions.reason}, Time : {reactions.elapsed.total_seconds()}")





