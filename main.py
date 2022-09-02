import requests
from datetime import datetime

username = 'james369'
token = 'grrgdfdgshnytdjub'
graph_id = 'graph3'

pixela_endpoint = "https://pixe.la/v1/users"

# user_params = {
#     'token': token,
#     'username': username,
#     'agreeTermsOfService': 'yes',
#     'notMinor': 'yes',
# }
#
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{username}/graphs"

# graph_config = {
#     'id': graph_id,
#     'name': "Cycling graph",
#     'unit': "Km",
#     'type': 'float',
#     'color': "ajisai",
# }

# Request Header
headers = {
    "X-USER-TOKEN": token
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

pixel_creation_endpoint = f"{pixela_endpoint}/{username}/graphs/{graph_id}"

yesterday = datetime(year=2022, month=8, day=17)
today = datetime.now()

pixel_data = {
    'date': yesterday.strftime('%Y%m%d'),
    'quantity': input("How many kilometers did you cycle today? "),
}

# response = requests.post(url=pixel_creation_endpoint, json=pixel_data, headers=headers)
# print(response.text)

update_endpoint = f"{pixela_endpoint}/{username}/graphs/{graph_id}/{yesterday.strftime('%Y%m%d')}"

# new_pixel_data = {
#     'quantity': '5.6',
# }

# response = requests.put(url=update_endpoint, json=new_pixel_data, headers=headers)
# print(response.text)

delete_endpoint = f"{pixela_endpoint}/{username}/graphs/{graph_id}/{yesterday.strftime('%Y%m%d')}"

response = requests.delete(url=delete_endpoint, headers=headers)
print(response.text)
