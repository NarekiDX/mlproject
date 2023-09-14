from setuptools import find_packages,setup
from typing import List

eDot='-e .'
def get_requirements(file_path:str)->List[str]:
    '''
    this function return the list of requirements
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]
        
        if eDot in requirements:
            requirements.remove(eDot)
        
    return requirements


setup(
name='project1',
version='0.0.1',
author='Iqbal',
author_email='ifarhan422@gmail.com',
packages=find_packages(),
install_requires=get_requirements('requirements.txt'),

)
