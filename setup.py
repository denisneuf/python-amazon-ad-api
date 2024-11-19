from setuptools import setup

setup(
    name='python-amazon-ad-api',
    version='0.6.2',
    install_requires=[
        "requests>=2.27.1,<2.33.0",
        "six~=1.16.0",
        "cachetools>=5.0,<5.6",
        "pycryptodome>=3.13,<3.22",
        "pytz>=2021.3,<2025.0",
        "confuse>=1.7,<2.1",
    ],
    packages=[
        'ad_api',
        'ad_api.api',
        'ad_api.auth',
        'ad_api.base',
        'ad_api.api.sp',
        'ad_api.api.sb',
        'ad_api.api.sd',
        'ad_api.api.dsp',
    ],
    url='https://github.com/denisneuf/python-amazon-ad-api',
    license='MIT',
    author='Daniel Alvaro',
    author_email='denisneuf@hotmail.com',
    description='Python wrapper for the Amazon Advertising API',
)
