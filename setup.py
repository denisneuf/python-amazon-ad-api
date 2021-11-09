from setuptools import setup

setup(
    name='python-amazon-ad-api',
    version='0.1.0',
    install_requires=[
        "requests~=2.26.0",
        "six~=1.16.0",
        "cachetools~=4.2.2",
        "pycryptodome~=3.11.0",
        "python-dotenv~=0.19.1",
        "pytz~=2021.3",
        "confuse~=1.6.0",
    ],
    packages=['ad_api','ad_api.api','ad_api.auth','ad_api.base','ad_api.api.sp','ad_api.api.sb','ad_api.api.sd'],
    url='https://github.com/denisneuf/python-amazon-ad-api',
    license='MIT',
    author='Daniel',
    author_email='info@leadtech.es',
    description='Python wrapper for the Amazon Advertising API'
)