import requests, json, base64
text = """Lorem ipsum dolor sit amet, consectetur adipiscing elit."""
def query(text):
    json_data = {
        'query': 'http://[your server]/cite?data='+base64.b64encode(text.encode()).decode().split("=")[0],
        'type': 'query',
        'requestedSourceType': 'journal-article',
        'orderBy': 'relevance',
    }

    resp = requests.post('https://autocite.cgs.scribbr.com/autocite', json=json_data).json()
    if "error" in resp:
        return resp["error"]
    response = requests.get('https://autocite.cgs.scribbr.com/autocite/'+resp["requestId"])
    out = base64.b64decode(json.loads(response.text.split("\n")[1].split("data: ")[1])["sources"][0]["data"]["title"].encode()).decode()
    return out
print(query(text))
