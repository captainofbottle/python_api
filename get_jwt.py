import requests


def get_jwt():
    """This function writes the tokens of 100 users to a file"""

    url = 'https://api.pachca.com/users/sign_in'
    for i in range(0, 100):
        i += 1
        body = {
            "user": {
                "email": f"mike+owner{i}@pachca.com",
                "password": "aezakmi"
            }
        }
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
            'Accept': 'application/json',
            'Accept-Encoding': 'gzip, deflate, br',
            'Connection': 'keep-alive',
            'Cache-Control': 'no-cache',
            'Content-Type': 'application/json',
            'x-api': 'true'
        }
        response = requests.post(url, json=body, headers=headers)
        dict_cook = response.cookies.get_dict()
        strings = []
        for key, item in dict_cook.items():
            strings.append("{}: {}".format(key.capitalize(), item))
        result = f"=".join(strings)
        result = result[1:502]
        result = result.replace(':', '=')
        line = f'j{result}'
        with open('list_jwt', 'a') as file:
            file.write(line + '\n')
