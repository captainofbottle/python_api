import requests


def name_parsing(people_id, expected_name):
    """
    :param people_id: id of character
    :param expected_name: name of character
    :return: This function saves a list of characters that were filmed with the character according
     to the specified parameters.
    """
    character_description = requests.get(f'https://swapi.dev/api/people/{people_id}/')
    response_character_description = character_description.json()
    url_films = response_character_description.get('films')
    character_name = response_character_description.get('name')

    assert response_character_description is not None, 'Response body is empty'
    assert expected_name == character_name, f'Expected name not equal character name,\n{expected_name}!={character_name}'

    print(f'List of film urls with {expected_name},\n{url_films}')

    new_set = []

    for i_url in url_films:

        film_description = requests.get(i_url)
        response_film_description = film_description.json()
        title_film = response_film_description.get('title')
        list_character = response_film_description.get('characters')

        assert response_film_description is not None, 'Response body is empty'
        assert list_character is not None, 'Character list is empty'
        print(f'Film : {title_film},\nList character : {list_character}')

        for j in list_character:
            new_set.append(j)

    unique_list = list(set(new_set))
    print(f'List of unique characters with {expected_name},\n{unique_list}')

    with open('list_name', 'a', encoding='utf-8') as file:
        for url_character in unique_list:
            response_url_character = requests.get(url_character)
            description_url_character = response_url_character.json()
            name = description_url_character.get('name')

            assert description_url_character is not None, 'Response body is empty'
            assert name is not None, 'Name of character is empty'
            file.write(name + '\n')

    print('List of character names successfully written to file')


name_parsing(people_id='4', expected_name='Darth Vader')