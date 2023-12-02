#!/usr/bin/python3
'''Lists 10 commits from the repo'''
import sys
import requests
from requests.auth import HTTPBasicAuth

def main():

    def comm(i, commits):
        '''Prints commits'''
        sha = commits[i].get('sha')
        commit = commits[i].get('commit')
        author = author.get('author')
        name = author.get('name')
        print('{}: {}'.format(sha, name))

    repo = sys.argv[1]
    owner = sys.argv[2]

    response = requests.get('https://api.github.com/repos' + owner + '/'
                            + repo + '/commits', headers=headers)

    commits = response.json()
    size = len(commits)

    if size < 10:
        for i in range(0, size):
            print(commits)


if __name__ == "__main__":
    main()
