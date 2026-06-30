from setuptools import find_packages, setup
from typing import List

Hype_E_dot = '-e .'
def get_requirements(file_path:str)->List[str]:
    '''
    This function will return list of requirements
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace('\n',' ') for req in requirements]

        if Hype_E_dot in requirements:
            requirements.remove(Hype_E_dot)

    return requirements



setup(
    name ="capstone-project",
    version='0.0.1',
    author='Munna Kumar',
    author_email='munna13041503@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)