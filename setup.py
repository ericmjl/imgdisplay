from setuptools import setup


def readfile(filename):
    with open(filename, 'r+') as f:
        return f.read()


setup(
    name="imgdisplay",
    version="2016.12.26",
    description="A command-line app to slideshow photos in a directory.",
    long_description=readfile('README.md'),
    author="Eric J. Ma",
    author_email="ericmajinglong@gmail.com",
    url="https://github.com/ericmjl/imgdisplay",
    # py_modules=['htbayes'],
    packages=['imgdisplay'],
    license=readfile('LICENSE'),
    entry_points={
        'console_scripts': [
            'imgdisplay=imgdisplay.imgdisplay:start_server'
        ]
    },
)
