import requests
import time

url = ''  # Replace with your app's URL

while True:
    try:
        response = requests.get(url)
        print(f'Pinged {url}, Status Code: {response.status_code}')
    except Exception as e:
        print(f'An error occurred: {e}')
    time.sleep(600)  # Wait for 10 minutes before the next ping
