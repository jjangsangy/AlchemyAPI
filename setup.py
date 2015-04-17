"""
Python AlchemyAPI Client:
    A Pythonic interface for IBM Deep Learning
"""

from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand

from version import __version__, __release__, __build__

class NoseTestCommand(TestCommand):
    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        import nose
        nose.run_exit(argv=['nosetests'])

setup(
    name='alchemyapi',
    version=__version__,
    description=__doc__,
    author='Sang Han',
    author_email='jjangsangy@gmail.com',
    maintainer='Sang Han',
    maintainer_email='jjangsangy@gmail.com',
    long_description=open('README.rst').read().decode('utf-8'),
    license='Apache License 2.0',
    url='https://github.com/jjangsangy/AlchemyAPI',
    packages=find_packages(),
    setup_requires=['nose'],
    test_suite='nose.collector',
    platforms='any',
    cmdclass={'test': NoseTestCommand},
    install_requires=['requests'],
    zip_safe=False,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Environment :: Web Environment',
        'Programming Language :: Unix Shell',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Text Processing :: Linguistic',
        'Topic :: Utilities',
    ],
)
