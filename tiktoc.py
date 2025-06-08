import requests

username = "thegrandnagus"
url = 'https://www.tiktok.com/@' + username

user_agent = {
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36',
}

r = requests.get(url, headers = user_agent).text
print(r)

start = '"desc":"@thegrandnagus '
end = ' - Watch awesome short videos created by B wags'
stats= r[r.find(start)+len(start):r.rfind(end)]

print(stats)

x = stats.split(' ')
print (x[0] + " " + x[2]+ " " + x[4])

