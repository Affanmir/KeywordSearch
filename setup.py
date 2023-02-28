import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()


setuptools.setup(
     name='Inverted Index Keyword Search',  
     version='0.1',
     scripts=['keyword_search.py'] ,
     author="Affan Amir Mir",
     author_email="affanmir95@gmail.com",
     description="A inverted index lookup utility function",
     long_description=long_description,
    long_description_content_type="text/markdown",
     url="",
     packages=setuptools.find_packages(),
     install_requires=[
        'nltk',
    ],
     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
     ],
 )