import setuptools

import sphinx_search


with open('README.md', 'r') as fh:
    long_description = fh.read()


setuptools.setup(
    name='furo-sphinx-search',
    version=sphinx_search.__version__,
    author='Harshil Mehta',
    author_email='ilovebhagwan@gmail.com',
    description='Sphinx extension to enable search as you type for docs hosted on Read the Docs '\
                'with the furo theme.',
    url='https://github.com/harshil21/furo-sphinx-search',
    license='MIT',
    packages=setuptools.find_packages(exclude=['tests']),
    long_description=long_description,
    long_description_content_type='text/x-rst',
    include_package_data=True,
    zip_safe=False,
    keywords='sphinx search readthedocs furo',
    python_requires='>=3.6',
    project_urls={
        'Documentation': 'https://github.com/harshil21/furo-sphinx-search/',
        'Bug Reports': 'https://github.com/harshil21/furo-sphinx-search/issues',
        'Source': 'https://github.com/harshil21/furo-sphinx-search/',
    },
    classifiers=[
        'Development Status :: 4 - Beta',
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Framework :: Sphinx :: Extension',
    ],
)
