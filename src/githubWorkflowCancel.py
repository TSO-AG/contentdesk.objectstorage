import requests
import json
from base64 import b64encode
from nacl import encoding, public
from os import getenv
import os
from dotenv import find_dotenv, load_dotenv
import glob

load_dotenv(find_dotenv())

GITHUB_TOKEN = getenv('GITHUB_TOKEN')
GITHUB_OWNER = getenv('GITHUB_OWNER')
GITHUB_REPO = getenv('GITHUB_REPO')

def main():
    print("STARTING WORKFLOW STOPPING")
    # Personal Access Token
    token = GITHUB_TOKEN

    # Repository details
    owner = GITHUB_OWNER
    repo = GITHUB_REPO

    # Headers
    headers = {
        'Authorization': f'Bearer {token}',
        'Accept': 'application/vnd.github+json',
    }

    # Get all running workflows in the queue
    print(f'Getting all running workflows in the queue for {owner}/{repo}')
    response = requests.get(f'https://api.github.com/repos/{owner}/{repo}/actions/runs?status=in_progress&per_page=100', headers=headers)

    print(f'Found {len(response.json()["workflow_runs"])} running workflows')

    # Cancel all running workflows
    for run in response.json()['workflow_runs']:
        if run['status'] == 'queued' or run['status'] == 'in_progress':
            run_id = run['id']
            response = requests.post(f'https://api.github.com/repos/{owner}/{repo}/actions/runs/{run_id}/cancel', headers=headers)
            print(f'Cancelled workflow {run_id}: {response.status_code}')

if __name__ == '__main__':
    main()