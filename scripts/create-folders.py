import os
import settings
import requests


endpoint = os.environ.get('ENDPOINT', 'http://localhost:60000')
username = os.environ.get('USERNAME', 'michael')
password = os.environ.get('PASSWORD', 'demo')

try:
    # Get headers with API token
    headers = settings.get_jenkins_headers(endpoint, username, password)
    print(headers)
except Exception as e:
    print(f"Error getting Jenkins headers: {e}")
    exit(1)

for team in settings.TEAMS:
    print(f"Checking folder for team: {team}")

    # Check if folder already exists
    if settings.check_item_exists(endpoint, username, password, team):
        print(f"\tFolder for {team} already exists, skipping...")
        continue

    print(f"\tCreating folder for team: {team}")

    # Create the folder using the template
    response = requests.post(
        f"{endpoint}/createItem",
        params={'name': team},
        headers=headers,
        auth=(username, password),
        data=settings.FOLDER_CONFIG_TEMPLATE
    )

    if response.status_code == 200:
        print(f"\t\tSuccessfully created folder for {team}")
    else:
        print(f"\t\tFailed to create folder for {team}. Status code: {response.status_code}")
        print(f"\t\tResponse: {response.text}")
