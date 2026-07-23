import os
import requests
from app.utils.config import settings


GITHUB_API = "https://api.github.com"

def get_pr_files(
    owner,
    repo,
    pr_number
):

    url = (
        f"{GITHUB_API}/repos/"
        f"{owner}/{repo}/pulls/"
        f"{pr_number}/files"
    )


    headers = {
        "Accept": "application/vnd.github+json",
        "Authorization": f"Bearer {settings.GITHUB_TOKEN}"
    }


    response = requests.get(
        url,
        headers=headers
    )

    print(response.status_code)
    print(response.text)
    response.raise_for_status()


    return response.json()