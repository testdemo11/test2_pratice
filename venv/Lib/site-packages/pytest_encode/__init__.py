# -*- coding:utf-8 -*-
__author__ = 'Tnew'

from typing import List

import pytest


def pytest_collection_modifyitems(session: "Session", config: "Config", items: List["Item"]) -> None:
    for item in items:
        print(item.name)
        print(item._nodeid)
        #测试用例的名字
        item.name = item.name.encode('utf-8').decode('unicode-escape')
        #测试用例的路径
        item._nodeid = item.nodeid.encode('utf-8').decode('unicode-escape')
        if 'login' in item.nodeid:
            item.add_marker(pytest.mark.login)
    items.reverse()