import requests
import ast
from translate import Translator


def get_joke_by_user():
    """This function asks the user for the category they want to get the Chuck Norris joke for."""

    url_category = 'https://api.chucknorris.io/jokes/categories'
    response = requests.get(url_category)
    categories = ast.literal_eval(response.text)
    # Convert str to list
    print(f"Available categories \n{categories}")

    user_category = input()

    if user_category in categories:
        url_joke = f'https://api.chucknorris.io/jokes/random?category={user_category}'
        get_joke = requests.get(url_joke)
        info_joke = get_joke.json()

        joke = info_joke.get('value')
        category = ' '.join(info_joke.get('categories'))
        # Convert list to str

        assert get_joke.status_code == 200, f'Статус код не равен {get_joke.status_code}'
        assert info_joke is not None, 'Тело ответа пустое'

        translator = Translator(to_lang='ru')
        translation_category = translator.translate(category)
        translation_joke = translator.translate(joke)
        # Translation into russian categories and jokes

        print(f'Selected category : {category.capitalize()}\nYour joke : {joke}\n')
        print(f'Выбранная категория : {translation_category.capitalize()}\nВаша шутка : {translation_joke}')

    else:
        print('Указанной категории не существует.\nХотите расскажу шутку про Чака Норриса?\ny - да\nn - нет')
        answer = input()

        if answer == 'y':
            url_random_joke = 'https://api.chucknorris.io/jokes/random'
            get_random_joke = requests.get(url_random_joke)
            info_random_joke = get_random_joke.json()
            print(info_random_joke.get('value'))

        elif answer == 'n':
            print('(︺︹︶)')

        else:
            print('Вы и тут умудрились ошибиться... (-_-)')
