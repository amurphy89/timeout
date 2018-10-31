#!/user/bin/env python3
import json
import os
import sys


from pprint import pprint


from helpers import print_venues
from timeout import check_venues


ROOT_DIR = os.path.abspath(".")


def main():

    try:
        names = sys.argv[1::]
        users = []
        venues = []

        with open(os.path.join(ROOT_DIR, "users.json")) as f:
            users = json.load(f)
            users = [x for x in users if x["name"] in names]
        with open(os.path.join(ROOT_DIR, "venues.json")) as f:
            venues = json.load(f)

        venues = check_venues(users, venues)
        print_venues(venues)

    except Exception as ex:
        print(ex)


if __name__ == "__main__":
    main()