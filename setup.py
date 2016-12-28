try:
        from setuptools import setup, find_packages
except ImportError:
        from distutils.core import setup

setup(
    name='pyquickbase',
    version='0.2.5',
    py_modules=['quickbase'],
    packages=find_packages(),
    description='pyQuickBase is a Python interface for the Intuit QuickBase API',
    long_description=open('README.rst').read(),
    classifiers=['Development Status :: 4 - Beta', 'Intended Audience :: Developers',
                 'Intended Audience :: Information Technology',
                 'License :: OSI Approved :: MIT License',
                 'Programming Language :: Python :: 2.7',
                 'Topic :: Software Development :: Libraries :: Python Modules',
                 'Operating System :: OS Independent',
                 'Environment :: Web Environment'
                 ],
    install_requires=[
        'lxml==3.2.1',
        'requests==2.12.4',
        'chardet>= 2.1.1',
    ],
)
