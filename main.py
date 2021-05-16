"""
cli for real debrid

supports: streaming videos
to implement: downloader

author: Akshansh Bhanjana (akshansh2000@gmail.com)
"""

import os
import sys
import json

from requests import get, post
from questionary import rawselect


BASE_URL = "https://api.real-debrid.com/rest/1.0"
AUTH_HEADERS = {
    "Authorization": "Bearer " + os.environ["DEBRID_TOKEN"],
}

TORRENTS_LIST = None


def get_torrents_list() -> None:
    """
    retrieve list of torrents from debrid (max: 100)
    """
    response = json.loads(
        get(f"{BASE_URL}/torrents?limit=36", headers=AUTH_HEADERS).text
    )

    global TORRENTS_LIST
    TORRENTS_LIST = [{
        "id": torrent['id'],
        "name": torrent['filename'],
    } for torrent in response]


def get_files_list(torrent_id: str) -> list:
    """
    retrieve file list with hoster links

    ! filters files which weren't added to host
    """
    response = json.loads(
        get(
            f"{BASE_URL}/torrents/info/{torrent_id}",
            headers=AUTH_HEADERS,
        ).text
    )

    files_list = []

    index = 0
    for file_info in response["files"]:
        if file_info["selected"]:
            files_list.append({
                "name": file_info["path"][1:],
                "hoster_link": response["links"][index]
            })

            index += 1

    return files_list


def unrestrict_link(hoster_link: str) -> str:
    """
    unrestricts hoster link and generates download link
    """
    response = json.loads(
        post(
            f"{BASE_URL}/unrestrict/link",
            headers=AUTH_HEADERS,
            data={"link": hoster_link},
        ).text
    )

    return response["download"]


def ask_user(choices: list) -> dict:
    """
    prompts user to select an option
    """
    indices = dict()

    for index, item in enumerate(choices):
        indices[item["name"]] = index

    choice = rawselect(
        "What do you want to watch?",
        choices=[file_info["name"] for file_info in choices],
    ).ask()

    return choices[indices[choice]]
