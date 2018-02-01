
from setuptools import setup

setup(name="System_Info",
    version="0.1",
    description="Basic System Info",
    url="",
    author="Elena Lanigan",
    author_email="elenalanigan93@gmail.com",
    license="GPL3",
    packages=['System_Info'],
    entry_points={
        'console_scripts':['softeng_COMP_30670=System_Info.main:main']
        }   
)