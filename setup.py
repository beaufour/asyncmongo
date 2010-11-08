import os
from distutils.core import setup

version = '0.0.2'

setup(
    name="asyncmongo",
    version=version,
    keywords=["mongo", "mongodb", "pymongo", "asyncmongo", "tornado"],
    long_description=open(os.path.join(os.path.dirname(__file__),"README.md"), "r").read(),
    description="Asyncronus library for accessing mongodb built upon the tornado IOLoop.",
    author="Jehiah Czebotar",
    author_email="jehiah@bit.ly",
    url="http://github.com/bitly/asyncmongo",
    packages=['asyncmongo'],
    requires=['pymongo (>=1.9)', 'tornado'],
    # download_url="http://github.com/downloads/bitly/asyncmongo/asyncmongo-%s.tar.gz" % version,
)