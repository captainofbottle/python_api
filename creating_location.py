import requests


def create_and_check_location():
    """This function creates location and writes its place_id to text file, then checks that created locations
    exist """

    base_url = 'https://rahulshettyacademy.com'
    resource_add = '/maps/api/place/add/json'
    query = '?key=qaclick123'
    post_url = base_url + resource_add + query

    body_request = {
        "location": {
            "lat": -38.383494,
            "lng": 33.427362
        }, "accuracy": 50,
        "name": "Frontline house",
        "phone_number": "(+91) 983 893 3937",
        "address": "29, side layout, cohen 09",
        "types": [
            "shoe park",
            "shop"
        ],
        "website": "http://google.com",
        "language": "French-IN"
    }

    with open('list_place_id', 'a+') as file_a:

        for i in range(5):
            response_post = requests.post(post_url, json=body_request)
            result_post = response_post.json()
            place_id = result_post.get('place_id')

            assert response_post.status_code == 200, f'Status code is not equal {response_post.status_code}'
            assert result_post.get('status') == 'OK', f'Field status is not equal {result_post.get("status")}'
            assert result_post.get('place_id') is not None, 'Received empty place_id'
            print(f"Location has been created, its data: \n{result_post}")

            file_a.write(place_id + '\n')
            print(f"place_id : {place_id} created location is written to a file 'list_place_id'")

    with open('list_place_id') as file_r:

        for i_place_id in file_r:
            i_place_id = i_place_id.rstrip('\n\r')
            resource_get = '/maps/api/place/get/json'
            get_url = base_url + resource_get + query + '&place_id=' + i_place_id
            response_get = requests.get(get_url)
            result_get = response_get.json()

            assert response_get.status_code == 200, f'Status code is not equal {response_get.status_code}'
            assert response_get is not None, 'Received an empty response body'
            print(f"Location with specified place_id : {i_place_id} found, its data: \n{result_get}")
