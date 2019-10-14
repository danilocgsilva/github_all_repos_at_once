import sys
import requests

def get_user():
    try:
        return sys.argv[1]
    except IndexError:
        return __tries_get_useralias_from_user__()


def get_data_from_url(url: str):
    json_data = requests.get(url)
    return json_data.text
    

def get_download_address(user: str):
    base_address = 'https://api.github.com/users/{}/repos'

    return base_address.format(user)


def get_all_data_from_base_url(base_api_url: str) -> str:

    data_string = get_data_from_url(base_api_url)
    return data_string


def __tries_get_useralias_from_user__():
    user = __ask_useralias__()
    while user == "":
        print("You provided an empty user alias.")
        user = __ask_useralias__()

    return user


def __ask_useralias__():
    return input("Please, provides the user alias from github: ")



