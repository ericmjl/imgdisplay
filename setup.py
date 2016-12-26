from setuptools import setup, find_packages


def readfile(filename):
    with open(filename, 'r+') as f:
        return f.read()


setup(
    name="imgdisplay",
    version="2016.12.26.19.35",
    description="A command-line app to slideshow photos in a directory.",
    long_description=readfile('README.md'),
    author="Eric J. Ma",
    author_email="ericmajinglong@gmail.com",
    url="https://github.com/ericmjl/imgdisplay",
    install_requires=['click==6.6',
                      'Flask==0.11.1',
                      'pywebview==1.3',
                      ],
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
