from setuptools import setup, find_packages

VERSION = '0.0.1'
DESCRIPTION = 'IssuetrakAPI v1 Python wrapper'

setup(
		name='IssuetrakAPI',
		version=VERSION,
		author='Will McElhenney',
		author_email='wmcelhenney93@gmail.com',
		description=DESCRIPTION,
		packages=find_packages(),
        install_requires=[requests], # add any additional packages that 
        # needs to be installed along with your package. Eg: 'caer'
        
        keywords=['python', 'Issuetrak', 'API'],
        classifiers= [
            "Development Status :: 3 - Alpha",
            "Intended Audience :: Education",
            "Programming Language :: Python :: 3",
            "Operating System :: MacOS :: MacOS X",
            "Operating System :: Microsoft :: Windows",
        ]
)