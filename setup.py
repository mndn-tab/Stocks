"""how to publish package to pypi

### source: ArjanCodes https://www.youtube.com/watch?v=5KEObONUkik
            python docs https://packaging.python.org/

### My practice file is located at colab:
    https://colab.research.google.com/drive/1RxCT59KNh6ldm2fVl4WN16vEdBkI1T0E


Project explaination:
create virtual environment,
in "Python Environment" tab, click "open in power shell"
!pip install setuptools, twine, wheel (use powershell in the virtual env folder)
!python setup.py bdist_wheel sdist (use powershell in the root folder, cause setup.py is in root folder
                                    this will create source dist as well as binary dist(wheel))
!twine check dist/* (check the integrity of those distributions.) 
!twine upload -r testpypi dist/* (upload it to test.pypi.org)
when prompted, enter:
username = __token__
password = <my TestPyPI API Token>
         = pypi-AgENdGVzdC5weXBpLm9yZwIkZWEzNTE1YzItNDAzOC00NTJjLWFiMTYtODk5ZjdjZDY3ZDZjAAIqWzMsIjUwODM0NGU1LTQ2MDMtNDE3NC1iY2YxLWU1Zjc0NjYwOTQxYyJdAAAGIMoTO-D-T-wH1_MRF-fFMQcUxJhvJBjRY2zL5z9CExbL
Finally, you can check your project at https://test.pypi.org/project/stocks-mndn/

Notes:
update .gitignore to ignore build, dist and .egg-info files.
no need of requirements.txt due to the setup.py dev option

"""
from setuptools import setup, find_packages

setup(
    name='Stocks_App',
    version='0.6.0',
    packages=find_packages(), #Set packages to a list of all packages(have __init.py__) in your project
    py_modules=["stock/main.py"], #If your project contains any single-file Python modules that aren’t part of a package
    # package_data={'sample': ['package_data.dat'],}, # additional files to be installed into package, it is a dict {package name : a list of relative path names}
    install_requires=["pandas>=1.2.4", "numpy>=1.20.1"
    ],
    author='mndn',
    author_email='mndn.tab@gmail.com',
    description='This is a short description of stocks project',
    long_description='This is a longer description of stocks project.',
    long_description_content_type='text/markdown',
    url='https://github.com/mndn-tab/Stocks',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.7',
)


