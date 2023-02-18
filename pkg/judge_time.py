import judge_time_module as jtm

def parse_time(time: str) -> int:
    """Parse a time string to an integer.
    Args:
        time (str): Time string to parse.
    Returns:
        int: Parsed time.
    """
    time = time.strip()
    if time.isdigit():
        return int(time)
    else:
        raise ValueError("Time must be an integer.(In parse_time)")

def main():
    time, time_range = input("input time: "), input("input time range: ")

    time = parse_time(time)
    time_range = tuple(map(parse_time, time_range.split("-")))

    ans = jtm.is_time_in_range(time, time_range)

    print(ans)

if __name__ == "__main__":
    main()