import requests
import ast


def get_categories_and_jokes():
    """This function displays one Chuck Norris joke from each category."""

    url_category = 'https://api.chucknorris.io/jokes/categories'
    response = requests.get(url_category)
    categories = ast.literal_eval(response.text)
    # Convert str to list
    print(f"Available categories \n{categories}")
    for i in categories:
        url_joke = f'https://api.chucknorris.io/jokes/random?category={i}'
        get_joke = requests.get(url_joke)
        info_joke = get_joke.json()
        assert get_joke.status_code == 200, f'Status code is not equal {get_joke.status_code}'
        assert info_joke is not None, 'Response body is empty'
        print(
            f"\n|Code : {get_joke.status_code}| |Reason : {get_joke.reason}| |Time : {get_joke.elapsed.total_seconds()}|")
        # Getting the code, status and time spent on the request
        print(
            f"Current url : {info_joke.get('url')} \nCategory : {i.capitalize()} \nJoke : {info_joke.get('value')}\n")
        # Getting current url, category and joke
