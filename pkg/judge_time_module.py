import pytest

def check_time(time: int) -> bool:
    """Check if a time is valid.
    Args:
        time (int): Time to check.
    Returns:
        bool: True if time is valid, False otherwise.
    """
    if time > 23 or time < 0:
        return False
    else:
        return True

def validate_time(time: int) -> None:
    """Validate a time.
    Args:
        time (int): Time to validate.
    Raises:
        TypeError: If time is not an integer.
        ValueError: If time is not between 0 and 23.
    """
    if not isinstance(time, int):
        raise TypeError("Time must be an integer.")
    if check_time(time) == False:
        raise ValueError("Time must be between 0 and 23.")

def validate_time_range(time_range: tuple) -> None:
    """Validate a time range.
    Args:
        time_range (tuple): Time range to validate.
    Raises:
        TypeError: If time range is not a tuple.
        TypeError: If time range is not a tuple of integers.
        ValueError: If time range is not a tuple of two values.
        ValueError: If time range is not between 0 and 23.
    """
    if not isinstance(time_range, tuple):
        raise TypeError("Time range must be a tuple.")
    if len(time_range) != 2:
        raise ValueError("Time range must be a tuple of two values.")
    validate_time(time_range[0])
    validate_time(time_range[1])

def is_time_in_range(time: int, time_range: tuple) -> bool:
    """Check if a time is in a time range.
    Args:
        time (int): Time to check.
        time_range (tuple): Time range to check.
    Returns:
        bool: True if time is in time range, False otherwise.
    """

    """Validate input."""
    validate_time(time)
    validate_time_range(time_range)

    """Check if time is in time range."""
    if time_range[0] == time_range[1]:
        return True
    if time_range[0] <= time_range[1]:
        return time_range[0] <= time < time_range[1]
    else:
        return time_range[0] <= time or time < time_range[1]