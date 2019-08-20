from setuptools import setup


config = dict(
    description = 'HFS+ mounting script.',
    author = 'LambdaXymox',
    url = 'https://github.com/lambdaxymox/hfsmount',
    download_url = 'https://github.com/lambdaxymox/hfsmount.git',
    author_email = 'lambda.xymox@gmail.com',
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
