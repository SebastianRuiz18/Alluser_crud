import requests
from pprint import pprint

URL = "http://127.0.0.1:5000/users"


def update_user(user_data, user_id):
    url = "%s/%s/" % (URL, user_id)
    response = requests.put(url, json=user_data)
    if response.status_code == 204:
        print("Successfully deactivated user.")
    else:
        print("Something went wrong while trying to deactivate user.")


def get_user(user_id):
    url = "%s/%s/" % (URL, user_id)
    response = requests.get(url)
    if response.status_code == 200:
        print("User: ")
        pprint(response.json())
        return response.json().get("user")[0]
    else:
        print("Something went wrong while trying to deactivate user.")
        return ""


if __name__ == "__main__":
    user_id = input("Type in the user's id: ")
    target_user = get_user(int(user_id)) 
    active = input("Would you like to deactivate this user?(Y/N): ")
    if active == "y" or active == "Y":
        target_user["active"] = 0
    update_user(target_user, user_id)

    option = input("Would you like to see the updated user? (Y/N): ")
    if option == "y" or option == "Y":
        get_user(user_id)