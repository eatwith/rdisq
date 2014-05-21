import os
from setuptools import setup, find_packages

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "rdisq",
    version = "0.0.4",
    author = "Lital Natan",
    author_email = "litaln@gmail.com",
    description = ("Super minimal workload distribution framework over redis queues"),
    license = "As stated on github",
    install_requires = ["redis"],
    keywords = "",
    packages=find_packages(),
    long_description="Please see README.md",
    classifiers=[
    ],
)
