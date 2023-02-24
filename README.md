# Learn python

## 安装 Jupyter

```shell
pip3.10 install jupyterlab
jupyter lab
```

## 虚拟环境

```shell
# 创建虚拟环境
python -m venv myvenv
pip3.10 freeze
pip3.10 freeze > requirements.txt
# 激活虚拟环境
source ./myvenv/bin/activate.csh
pip3.10 freeze
# 在虚拟环境中导入指定的包
pip3.10 install -r requirements.txt
# 离开虚拟环境
deactivate

# 临时加速
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple package_name
# 永久加速
cat ~/pip.conf
[global]
index-url = http://mirrors.aliyun.com/pypi/simple/
[install]
trusted-host = mirrors.aliyun.com
```

## C++混合编程代码

1、使用 ctypes 库加载 C++ 编写的动态链接库，参考链接：https://docs.python.org/zh-cn/3.10/library/ctypes.html

2、使用 pybind 将 C++ 编译为 Python 库，参考链接：https://github.com/pybind/python_example

3、使用 Pythran 库将 Python 直接转换为 C++ 代码，参考链接：https://pypi.org/project/pythran

```shell
pip3.10 install pythran
pythran -e 要转换的python源码.py
        -p python.optimizations.ConstantFolding
        -o output.hpp
```

### 数据采集 requests

### 数据挖掘 re BeautifulSoup pandas Scikit-learn

### 数据可视化 matplotlib Seaborn

### 定时任务 schedule

### 人脸识别 OpenCV

## Django

```shell
# 创建项目
django-admin startproject myproject
# 创建应用
cd myproject
python3 manage.py startapp testapp
# 运行Django
python3 manage.py runserver 127.0.0.1:8000
# 迁移
python3 manage.py migrate
# 创建超级用户
python3 manage.py createsuperuser
```
