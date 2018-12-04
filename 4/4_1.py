"""
Counts which guard was asleep more time
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

    highest = 0
    best_guard = None
    for guard in guard_sleep:
        guard_total = sum(guard_sleep[guard])
        if guard_total > highest:
            highest = guard_total
            best_guard = guard

    guard_max = max(guard_sleep[best_guard])
    print(best_guard * guard_sleep[best_guard].index(guard_max))