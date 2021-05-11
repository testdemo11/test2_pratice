from time import sleep

import pytest

#pytest test_rerun.py --reruns 3  --reruns-delay 1 命令运行

def test_rerun1():
    sleep(0.5)
    assert 1 == 2

def test_rerun2():
    sleep(0.5)
    assert 2 == 2

@pytest.mark.flaky(reruns=5,reruns_delay=1)
def test_rerun3():
    sleep(0.5)
    assert 3 == 2
