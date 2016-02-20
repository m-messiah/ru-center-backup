from setuptools import setup
from os.path import join, dirname

setup(
    name='ru-center-backup',
    version='1.1',
    url='https://github.com/m-messiah/ru-center-backup',
    license='MIT',
    author='m_messiah',
    author_email='m.muzafarov@gmail.com',
    description='RU-CENTER DNS-MASTER backup',
    long_description=open(join(dirname(__file__), 'README.rst')).read(),
    scripts=["ru-center-backup"],
    install_requires=["requests"],
    keywords='ru-center nic.ru dns dns-master backup',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: System Administrators',
        'Topic :: Utilities',
        'License :: OSI Approved :: MIT License',

        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
    ],
)
