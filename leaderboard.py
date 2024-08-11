from _jury_list import get_jury_list

import sys

if len(sys.argv) != 3:
    print("Usage: leaderboard.py [year] [identifier]")
    sys.exit()


year, identifier = sys.argv[1:]
base_url = f"https://www.radioeins.de/musik/top_100/{year}/{identifier}"

jury_list = get_jury_list(base_url)