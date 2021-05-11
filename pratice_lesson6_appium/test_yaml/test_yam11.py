# -*- coding:utf-8 -*-
__author__ = 'Tnew'

import yaml
y = yaml.safe_load(open('../test_yaml/test.yaml','r',encoding='utf-8'))
print(type(y))