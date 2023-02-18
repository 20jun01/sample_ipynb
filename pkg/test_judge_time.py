import pytest
import judge_time_module as jtm
import judge_time as jt

def test_check_time():
    assert jtm.check_time(0) == True
    assert jtm.check_time(23) == True
    assert jtm.check_time(24) == False
    assert jtm.check_time(-1) == False

def test_validate_time():
    with pytest.raises(TypeError):
        jtm.validate_time("0")
    with pytest.raises(ValueError):
        jtm.validate_time(24)

def test_validate_time_range():
    with pytest.raises(TypeError):
        jtm.validate_time_range([0, 1])
    with pytest.raises(TypeError):
        jtm.validate_time_range((0, "1"))
    with pytest.raises(ValueError):
        jtm.validate_time_range((0,))
    with pytest.raises(ValueError):
        jtm.validate_time_range((0, 24))
    assert jtm.validate_time_range((0, 0)) == None

def test_is_time_in_range():
    assert jtm.is_time_in_range(0, (0, 0)) == True
    assert jtm.is_time_in_range(0, (0, 1)) == True
    assert jtm.is_time_in_range(1, (0, 1)) == False
    assert jtm.is_time_in_range(0, (1, 0)) == False
    assert jtm.is_time_in_range(1, (1, 0)) == True
    assert jtm.is_time_in_range(2, (1, 0)) == True

def test_parse_time():
    assert jt.parse_time("0") == 0
    assert jt.parse_time("23") == 23


def test_all():
    test_check_time()
    test_validate_time()
    test_validate_time_range()
    test_is_time_in_range()
    test_parse_time()


if __name__ == "__main__":
    test_all()
