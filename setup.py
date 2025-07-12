from setuptools import setup, find_packages

with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='human-date-parser',
    version='0.1.1',  # <-- also bump the version to publish again
    packages=find_packages(),
    install_requires=[
        'dateparser>=1.1.0'
    ],
    author='Dheerendra Vikram Dixit',
    author_email='dheerendradixit321@gmail.com',
    description='Convert natural language date strings into Python datetime objects.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/Dheerendra-123/Human_Date_Parser_PY_Library.git',
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: MIT License',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    python_requires='>=3.7, <4',
)
