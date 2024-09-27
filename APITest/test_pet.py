import requests

BASEURL= "https://petstore.swagger.io/v2"

def test_pet_list():
    status = 'available'
    pet_get_response=requests.get(f"{BASEURL}/pet/findByStatus", params={"status": status})
    assert pet_get_response.status_code == 200

    pets_list = pet_get_response.json()
    print(pets_list)
    for pet in pets_list:
        assert 'id' in pet
        assert 'name' in pet
        assert 'photoUrls' in pet
        assert 'tags' in pet
        assert 'status' in pet


def test_pet_post():
    pet_data = {
        "id": 0,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "doggie",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    }

    post_response = requests.post(f"{BASEURL}/pet", json=pet_data)

    assert post_response.status_code == 200

    new_pet = post_response.json()
    assert new_pet['name'] == pet_data['name']
    assert new_pet['status'] == pet_data['status']