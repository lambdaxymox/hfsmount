from setuptools import setup


config = dict(
    description = 'HFS+ mounting script.',
    author = 'Stallmanifold',
    url = 'https://github.com/stallmanifold/hfsmount',
    download_url = 'https://github.com/stallmanifold/hfsmount.git',
    author_email = 'stallmanifold@gmail.com',
    version = '0.1',
    license = "LICENSE-APACHE",
    package_dir = {'': ''},
    packages = ['hfsmount'],
    scripts = [],
    name = 'hfsmount',
    tests_require = ['pytest', 'hypothesis'],
    entry_points = {
        'console_scripts': [ 'hfsmount = hfsmount:main' ]
    }
)

setup(**config)
