def format_string(typ, track, school_name, team, duration=None):
    return "| {:<10} | ({:^3}) | {:<60} | Team {} | {duration:^8} |".format(
        typ + ":",
        track,
        school_name,
        team,
        duration="" if duration is None else "({:.2f}s)".format(duration),
    )


if __name__ == "__main__":
    from school_name import SchoolName

    tests = [
        {"key": "Start", "track": "A", "school_code": "B", "team": 2, "duration": None},
        {"key": "Finish", "track": "B", "school_code": "A", "team": 1, "duration": 12},
        {
            "key": "Submitted",
            "track": "A",
            "school_code": "C",
            "team": 3,
            "duration": 11,
        },
    ]

    for test in tests:
        school_name = SchoolName.get(test["school_code"])
        print(
            format_string(
                test["key"], test["track"], school_name, test["team"], test["duration"]
            )
        )

