import requests
import sys
from multiprocessing import Pool

def request(url):
    try:
        with requests.Session() as session:
            result = session.get("https://" + url)
            if result.status_code == 200:
                print("[+] Subdomain discovered --> " + url)
    except requests.exceptions.RequestException as e:
        pass

def main():
    target_url = "google.com"

    # Open word list
    with open("subdmainwordlist.txt", "r") as wordlist:
        wordlist = [line.strip() for line in wordlist]

    # Use multiprocessing to parallelize requests
    with Pool(processes=8) as pool:
        pool.map(request, [word + "." + target_url for word in wordlist])

if __name__ == "__main__":
    main()
