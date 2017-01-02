try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup
from pip.req import parse_requirements
from src.flask_app_generator import __version__

install_reqs = parse_requirements('requirements.txt', session='hack')
reqs = [str(ir.req) for ir in install_reqs]

setup(
    name='flask_app_generator',
    version=__version__,
    packages=['flask_app_generator'],
    package_dir={'flask_app_generator': 'src/flask_app_generator'},
    package_data={'': [
        'config/*', 'templates/*', 'templates/.gitignore',
        'templates/html/*', 'templates/views/*', 'templates/static'
    ]},
    include_package_data=True,
    install_requires=reqs,
    entry_points={
        'console_scripts': [
            'flask-app-generator=flask_app_generator.run:main'],
    },
    author='Claude.Seo',
    author_email='ehdaudtj@gmail.com',
    url='https://github.com/SeoDongMyeong/flask-app-generator',
    description='Flask Project Generator',
    keywords=['flask', 'flask-project', 'flask-generator'],
    license='MIT License'
)
