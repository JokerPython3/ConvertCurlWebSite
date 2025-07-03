
import requests

session = requests.Session()
url = 'https://www.instagram.com/api/v1/web/login_page/'

headers = {
    "accept": "*/*",
    "accept-language": "ar-AE,ar;q=0.9,en-US;q=0.8,en;q=0.7",
    "priority": "u=1, i",
    "referer": "https://www.instagram.com/accounts/emailsignup/",
    "sec-ch-prefers-color-scheme": "dark",
    "sec-ch-ua": "\"Not)A;Brand\";v=\"8\", \"Chromium\";v=\"138\", \"Google Chrome\";v=\"138\"",
    "sec-ch-ua-full-version-list": "\"Not)A;Brand\";v=\"8.0.0.0\", \"Chromium\";v=\"138.0.7204.97\", \"Google Chrome\";v=\"138.0.7204.97\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-model": "\"\"",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-ch-ua-platform-version": "\"10.0.0\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36",
    "x-asbd-id": "359341",
    "x-csrftoken": "ppkEJ5UbIFzPr9UJcyDtht",
    "x-ig-app-id": "936619743392459",
    "x-ig-www-claim": "0",
    "x-requested-with": "XMLHttpRequest",
    "x-web-session-id": "11ximv:ehxi67:zd1hbz"
}

response = session.get(url, headers=headers)

print(response.status_code)
print(response.text)
