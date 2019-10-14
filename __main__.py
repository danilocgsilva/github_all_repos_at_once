
import sys
from functions import *

user = get_user()

base_api_url = get_download_address(user)

data_string = get_all_data_from_base_url(base_api_url)

# data_string = get_data_from_url(download_address)

print(data_string)
