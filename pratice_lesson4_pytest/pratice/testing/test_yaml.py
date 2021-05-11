import pytest
import yaml

with open('./datas/param_a.yaml') as f:
    data = yaml.safe_load(f)
    print(data)
    print(type(data))
    data1 = yaml.safe_load(f)
    print(type(data1))


