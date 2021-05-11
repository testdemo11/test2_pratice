# -*- coding:utf-8 -*-
__author__ = 'Tnew'

import pytest


@pytest.mark.parametrize('name',['哈利','博波特'])
def test_hk(name):
    print(name)