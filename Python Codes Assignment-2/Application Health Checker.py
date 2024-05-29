import requests
import time

def check_application_status(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return 'up'
        else:
            return 'down'
    except requests.ConnectionError:
        return 'down'

def main():
    url = input("Enter the URL of the application to check: ")
    interval = int(input("Enter the interval (in seconds) between checks: "))

    while True:
        status = check_application_status(url)
        print(f"Application status: {status}")
        time.sleep(interval)

if __name__ == "__main__":
    main()
