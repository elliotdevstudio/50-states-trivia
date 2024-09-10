try: 
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'My Project',
    'author': 'Elliot',
    'url': 'URL to access it...',
    'download_url': 'Where to download it..',
    'author_email': 'elliotdevstudio@gmail.com',
    'version': '0.1',
    'install_requires': ['pytest'], 
    'packages': ['NAME'],
    'scripts': [],
    'name': 'projectname'
}

setup(**config)

