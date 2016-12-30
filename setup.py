from setuptools import setup, find_packages


def readfile(filename):
    """
    A helper function for reading a file.
    """
    with open(filename, 'r+') as f:
        return f.read()


def requirements():
    """
    A helper function for passing requirements in from `requirements.txt`.
    """
    requirements = []
    with open('requirements.txt', 'r+') as f:
        for line in f.readlines():
            requirements.append(line.strip('\n'))
    return requirements


setup(
    name="imgdisplay",
    version="2016.12.26.19.35",
    description="A command-line app to slideshow photos in a directory.",
    long_description=readfile('README.md'),
    author="Eric J. Ma",
    author_email="ericmajinglong@gmail.com",
    url="https://github.com/ericmjl/imgdisplay",
    install_requires=requirements(),
    packages=find_packages(),
    license=readfile('LICENSE'),
    entry_points={
        'console_scripts': [
            'imgdisplay=imgdisplay.imgdisplay:start_server'
        ]
    },
    package_data={
        'static': 'imgdisplay/static/*',
        'templates': 'imgdisplay/templates/*',
    },
    include_package_data=True,
)
