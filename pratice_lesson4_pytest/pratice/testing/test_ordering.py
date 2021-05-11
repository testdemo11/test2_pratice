from time import sleep

import pytest

def test_1():
    sleep(1)
    assert True

# @pytest.mark.third
# @pytest.mark.run(order=2)
def test_2():
    sleep(1)
    assert True

@pytest.mark.run(order=1)
def test_3():
    sleep(1)
    assert True
