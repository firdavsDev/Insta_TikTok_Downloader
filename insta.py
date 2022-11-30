import requests
import json

def instadownloader(link):  # sourcery skip: avoid-builtin-shadow
    url = "https://instagram-downloader-download-instagram-videos-stories.p.rapidapi.com/index"

    querystring = {"url": link}

    headers = {
    "X-RapidAPI-Key": "48d1fa43f7mshc9f7adc3f18df95p12bedajsn819039a2d0a2",
    "X-RapidAPI-Host": "instagram-downloader-download-instagram-videos-stories.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    rest = json.loads(response.text)
    if 'error' in rest:
        return "error"
    dict = {}
    if rest['Type'] == 'Post-image':
        return _extracted_from_instadownloader_18('image', dict, rest)
    elif rest['Type'] == 'Post-Video':
        return _extracted_from_instadownloader_18('video', dict, rest)
    elif rest['Type'] == 'Carousel':
        return _extracted_from_instadownloader_18('carousel', dict, rest)
    else:
        return "Error"


# TODO Rename this here and in `instadownloader`
def _extracted_from_instadownloader_18(arg0, dict, rest):
    dict['type'] = arg0
    dict['media'] = rest['media']
    return dict

