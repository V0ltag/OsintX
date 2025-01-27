import os
import requests
from bs4 import BeautifulSoup
import argparse

def linkedin_scraper(query):
    print(f"[INFO] Searching LinkedIn profiles for '{query}'...")
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    search_url = f"https://www.linkedin.com/search/results/all/?keywords={query.replace(' ', '%20')}"
    response = requests.get(search_url, headers=headers)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        print("[INFO] LinkedIn search results fetched.")
        for link in soup.find_all('a', href=True):
            if "linkedin.com/in" in link['href']:
                print(link['href'])
    else:
        print("[ERROR] Unable to fetch LinkedIn search results. Status code:", response.status_code)

def github_scraper(username):
    print(f"[INFO] Searching GitHub for user '{username}'...")
    api_url = f"https://api.github.com/users/{username}"
    response = requests.get(api_url)
    if response.status_code == 200:
        data = response.json()
        print("[INFO] GitHub user data fetched.")
        print("Username:", data.get('login', 'N/A'))
        print("Name:", data.get('name', 'N/A'))
        print("Public Repos:", data.get('public_repos', 'N/A'))
        print("Followers:", data.get('followers', 'N/A'))
        print("Following:", data.get('following', 'N/A'))
        print("Profile URL:", data.get('html_url', 'N/A'))
    else:
        print("[ERROR] Unable to fetch GitHub user data. Status code:", response.status_code)

def main():
    parser = argparse.ArgumentParser(description="OSINT tool for LinkedIn and GitHub")
    parser.add_argument("--linkedin", help="Search query for LinkedIn profiles")
    parser.add_argument("--github", help="GitHub username to lookup")
    args = parser.parse_args()

    if args.linkedin:
        linkedin_scraper(args.linkedin)

    if args.github:
        github_scraper(args.github)

if __name__ == "__main__":
    main()
