import requests


headers = {
    'Authorization': '54b1691adf0cf8e78fc49bdff7803ec36fd2555e',
    'Content-Type': 'application/json',
}

data = '{ "long_url": "https://github.com/ashutosh1919/masterPortfolio.git" }'

response = requests.post('https://api-ssl.bitly.com/v4/shorten', headers=headers, data=data)
url = response.json()

print(url['link'])
