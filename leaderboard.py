from _jury_list import get_jury_list
from _juror_preferences import get_juror_preferences

import sys

if len(sys.argv) != 3:
    print("Usage: leaderboard.py [year] [identifier]")
    sys.exit()


year, identifier = sys.argv[1:]
base_url = f"https://www.radioeins.de/musik/top_100/{year}/{identifier}"

jury_list = get_jury_list(base_url)

preferences = []

for juror in jury_list:
    preferences.append(get_juror_preferences(base_url, juror))