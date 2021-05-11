pypi打包功能
打包需要工具：wheel setuptools
到setup对应的package路径下（pytest-encode）运行python setup.py sdist bdist_wheel
成功后对应路径下会出现几个文件夹，其中dist中有两个包，第一个是源码包，第二个是whl包，可通过pip install安装