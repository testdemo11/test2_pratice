import pytest
import yaml
# with open("./datas/param_a.yaml") as f:
#     result = yaml.safe_load(f)
#     print(result)
with open("./datas/param_b.yaml") as f:
    result = yaml.safe_load(f)
    print(result)

# @pytest.mark.parametrize('a',yaml.safe_load('./datas/param_a.yaml'))
# # @pytest.mark.parametrize('b',yaml.safe_load('./datas/param_b.yaml'))
# def test_param(a,b):
#     print(f"a={a},b={b}")