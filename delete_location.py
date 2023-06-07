import requests


def delete_and_check_location():
    """This function removes some created locations from the previous file(creating_location), checks that the
    locations are removed, then writes the existing locations to the new file """

    base_url = 'https://rahulshettyacademy.com'
    resource_delete = '/maps/api/place/delete/json'
    query = '?key=qaclick123'

    with open('list_place_id') as list_place:
        place_id = list_place.readlines()

        for all_place_id in range(1, 4, 2):

            body_request = {
                "place_id": f'{place_id[all_place_id].strip()}'
            }

            delete_url = base_url + resource_delete + query
            response_delete = requests.delete(delete_url, json=body_request)
            result_delete = response_delete.json()

            assert result_delete is not None, 'Received empty response body'
            assert response_delete.status_code == 200, f'Incorrect status received response code {response_delete.status_code}'
            assert result_delete.get("status") == 'OK', 'Incorrect field value received "status"'

            print(f'Location with place_id deleted : {place_id[all_place_id].strip()} Status code : {response_delete.status_code}\nResponse body : {result_delete}')

        for i_place_id in place_id:

            i_place_id = i_place_id.rstrip('\n\r')
            resource_get = '/maps/api/place/get/json'
            get_url = base_url + resource_get + query + '&place_id=' + i_place_id
            response_get = requests.get(get_url)
            result_get = response_get.json()

            assert response_get.status_code == 200 or 404, f'Incorrect status received response code {response_get.status_code}'
            assert result_get is not None, 'Received empty response body'

            if response_get.status_code == 200:

                with open('new_list_place_id', 'a') as new_file:

                    new_file.write(i_place_id + '\n')
                    print(f'Location with place_id : {i_place_id} exists and is written to a new file "new_list_place_id"')

            else:
                print(f'Location with place_id : {i_place_id} not exist')