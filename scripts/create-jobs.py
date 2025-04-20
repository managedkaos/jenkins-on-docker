import os
import settings
import requests


endpoint = os.environ.get('ENDPOINT', 'http://localhost:60000')
username = os.environ.get('USERNAME', 'michael')
password = os.environ.get('PASSWORD', 'demo')

try:
    # Get headers with API token
    headers = settings.get_jenkins_headers(endpoint, username, password)
except Exception as e:
    print(f"Error getting Jenkins headers: {e}")
    exit(1)

for team in settings.TEAMS:
    print(f"Processing team: {team}")

    # First check if the team folder exists
    if not settings.check_item_exists(endpoint, username, password, team):
        print(f"\tTeam folder {team} does not exist, skipping jobs...")
        continue

    for job_type in settings.JOBS:
        job_name = f"{team}-{job_type}"
        job_path = f"{team}/{job_name}"

        print(f"\tChecking job: {job_name}")

        # Check if job already exists
        if settings.check_item_exists(endpoint, username, password, job_path):
            print(f"\t\tJob {job_name} already exists, skipping...")
            continue

        print(f"\t\tCreating job: {job_name}")

        # Create the job using the template
        response = requests.post(
            f"{endpoint}/job/{team}/createItem",
            params={'name': job_name},
            headers=headers,
            auth=(username, password),
            data=settings.JOB_CONFIG_TEMPLATE
        )

        if response.status_code == 200:
            print(f"\t\t\tSuccessfully created job {job_name}")
        else:
            print(f"\t\t\tFailed to create job {job_name}. Status code: {response.status_code}")
            print(f"\t\t\tResponse: {response.text}")
