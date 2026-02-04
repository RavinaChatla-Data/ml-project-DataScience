from setuptools import find_packages,setup 
from typing import List

def get_requiremets(file_path:str)-> List[str]:
    '''
    This function will return all the requirements
    '''
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace('\n','') for req in requirements]
    return requirements

setup(
    name = 'MLProject',
    version = '0.0.1',
    author = 'Ravina',
    author_email = 'ravina11368@gmail.com',
    packages = find_packages(),
    requires_install = get_requiremets('requirements.txt')
)