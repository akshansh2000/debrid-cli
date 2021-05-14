"""
cli for real debrid

supports: streaming videos
to implement: downloader

author: Akshansh Bhanjana (akshansh2000@gmail.com)
"""

import os

import requests
import questionary


BASE_URL = "https://api.real-debrid.com/rest/1.0"
AUTH_HEADERS = {
    "Authorization": "Bearer " + os.environ["DEBRID_TOKEN"],
}


def get_torrents_list() -> list:
    """
    retrieve list of torrents from debrid (max: 100)
    """
    pass


def get_files_list(torrent_id: str) -> list:
    """
    retrieve file list with hoster links

    ! filters files which weren't added to host
    """
    pass


def unrestrict_link(hoster_link: str) -> str:
    """
    unrestricts hoster link and generates download link
    """
    pass


def ask_user(choices: list) -> dict:
    """
    prompts user to select an option
    """
    pass


"""
get torrents list
display torrent names
select torrent
get files list
display files which were selected while adding
select file
unrestrict link
play in default media player
"""
