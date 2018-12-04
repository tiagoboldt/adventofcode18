"""
Identifies the guard that is most frequently asleep in a minute
"""

import re

with open('4/4.input') as f:
    guard = None
    sleep_minute = None
    guard_sleep = {}
    guard_regex = re.compile(r"Guard #(\d+)")
    minute_regex = re.compile(r":(\d+)]")
    for line in f:
        try:
            # Read guard ID
            match = guard_regex.search(line)
            guard = int(match.group(1))
        except:
            match = minute_regex.search(line)
            minute = int(match.group(1))
            if sleep_minute is None:
                sleep_minute = minute
            else:
                if guard not in guard_sleep:
                    guard_sleep[guard] = [0 for i in range(60)]
                for i in range(sleep_minute, minute):
                    guard_sleep[guard][i] += 1
                sleep_minute = None

    best_guard = None
    best_minute = 0
    highest = 0
    for guard in guard_sleep:
        guard_highest = max(guard_sleep[guard])
        if guard_highest > highest:
            highest = guard_highest
            best_guard = guard
            best_minute = guard_sleep[guard].index(guard_highest)
    print(best_guard)
    print(best_minute)
    print(best_guard * best_minute)