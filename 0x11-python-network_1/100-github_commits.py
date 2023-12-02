#!/usr/bin/python3
'''Displais last 10 commits'''
import sys
import requests


def main():

    def print_commit(commit):
        '''Prints commit details'''
        sha = commit.get('sha')
        author = commit.get('commit').get('author').get('name')
        print(f'{sha}: {author}')

    repo = sys.argv[1]
    owner = sys.argv[2]

    headers = {"Accept": "application/vnd.github.v3+json"}
    url = f"https://api.github.com/repos/{owner}/{repo}/commits"
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        commits = response.json()
        for commit in commits:
            print_commit(commit)
    else:
        print("Failed to retrieve commits.")


if __name__ == "__main__":
    main()
