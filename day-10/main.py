import requests

url = "https://www.advantageonlineshopping.com/"

try:
    response = requests.get(url, timeout=15)
    response.raise_for_status()

    print("Status:", response.status_code)
    print("Content-Type:", response.headers.get("Content-Type"))
    print("\nPage Preview:\n")
    print(response.text[:1000])

except requests.exceptions.RequestException as e:
    print("Request failed:", e)

