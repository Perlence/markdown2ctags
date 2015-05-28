from setuptools import setup

setup(
    name='markdown2ctags',
    license='BSD',
    author='John Szakmeister',
    author_email='john@szakmeister.net',
    description='Generate ctags-compatible tags files for Markdown documents.',
    url='https://github.com/jszakmeister/markdown2ctags',
    download_url='https://github.com/jszakmeister/markdown2ctags/archive/master.zip',
    version='0.1.2',
    py_modules=['markdown2ctags'],
    zip_safe=False,
    entry_points={
        'console_scripts': [
            'markdown2ctags = markdown2ctags:run',
        ]
    },
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'License :: OSI Approved :: BSD License',
        'Operating System :: Windows',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Topic :: Software Development',
        'Topic :: Text Processing',
        'Topic :: Text Processing :: Indexing',
        'Topic :: Utilities',
    ],
)
