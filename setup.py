from setuptools import setup


config = dict(
    description = 'HFS+ mounting script.',
    author = 'Stallmanifold',
    url = 'https://github.com/stallmanifold/hfsmount',
    download_url = 'https://github.com/stallmanifold/hfsmount.git',
    author_email = 'stallmanifold@gmail.com',
    version = '0.1',
    license = "UNLICENSE",
    packages = ['hfsmount'],
    scripts = [],
    name = 'hfsmount',
    entry_points = {
        'console_scripts': [ 'hfsmount = hfsmount.hfsmount:main' ]
    }
)

setup(**config)
