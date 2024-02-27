from typing import (
    Any,
    Dict,
    Iterable,
    List,
    Optional,
    Tuple,
    Union,
)

import yt_dlp


def get_video_info(
    input_string: str,
) -> Dict:
    """Retrieve Youtube Video infomation from given string

    Parameters
    ----------
    input_string : str
        A Youtube video id or a URL
    """
    ydl_opts = {}
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        try:
            video_info = ydl.extract_info(
                input_string,
                download=False,
            )
            return_data = video_info
            # print(video_info)
        except:
            return_data = {}
    return return_data


def get_youtube_video_id(
    input_string: str,
) -> str:
    """Return Youtube Video id from given string

    Parameters
    ----------
    input_string : str
        A Youtube video id or a URL
    """
    return_data = ''
    video_info = get_video_info(input_string)
    if 'id' in video_info:
        return_data = video_info['id']

    return return_data
