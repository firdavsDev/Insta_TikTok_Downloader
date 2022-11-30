def tiktok(link):
	import requests
	import json
	url = "https://tiktok-downloader-download-tiktok-videos-without-watermark.p.rapidapi.com/vid/index"

	querystring = {"url":link}

	headers = {
		"X-RapidAPI-Key": "54e262782emsh7c9b12dd7f332b4p158bd6jsnaee732e6c4a8",
		"X-RapidAPI-Host": "tiktok-downloader-download-tiktok-videos-without-watermark.p.rapidapi.com"
	}

	response = requests.request("GET", url, headers=headers, params=querystring)
	result = response.text
	rest = json.loads(result)
	return {"video":rest["video"][0], "music":rest["music"][0]}

