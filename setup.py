from distutils.core import setup

setup(
    name='ClassicUPS',
    version='0.1.9',
    author='Olexandr Shalakhin',
    author_email='olexandr@shalakhin.com',
    url='http://github.com/OShalakhin/ClassicUPS/',
    packages=['ClassicUPS'],
    description='Usable UPS Integration in Python',
    long_description=open('README.rst').read(),
    keywords=['UPS'],
    # install_requires=[
    #     'dict2xml',
    #     'xmltodict==0.4.2'
    # ],
    classifiers=[
        'Programming Language :: Python',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Intended Audience :: Developers',
        'Development Status :: 4 - Beta'
    ]
)

# To update pypi: `python setup.py register sdist bdist_wininst upload`
