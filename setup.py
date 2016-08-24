import os

from setuptools import setup, find_packages


setup(
    name='django-smartspaceless',
    version='0.1',
    description='A Django template tag application for minifying block-level HTML elements only',
    long_description=open(os.path.join(os.path.dirname(__file__), 'README.rst')).read(),
    author='Richard Cornish',
    author_email='rich@richardcornish.com',
    url='https://github.com/richardcornish/django-smartspaceless',
    license='BSD License',
    zip_safe=False,
    include_package_data=True,
    packages=find_packages(),
    install_requires=[
        'django-htmlmin'
    ],
    test_suite='smartspaceless.tests',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Browsers',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Internet :: WWW/HTTP :: Site Management',
        'Topic :: Utilities'
    ],
)
