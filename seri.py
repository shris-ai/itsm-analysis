from setuptools import find_packages, setup
from typing import List

def get_requirements()->List[str]:
    """
    Returns list of requirements.
    """
    list_requirement:List[str]=[]
    try:
        with open('requirements.txt', 'r') as file:
            lines = file.readlines()                
            for line in lines:
                # Ignore whitespaces in line
                requirement = line.strip()
                # Ingnore empty line and line with '-e .'
                if requirement and requirement != '-e .':
                    list_requirement.append(requirement)
    except FileNotFoundError:
        print("requirements.txt file not found!")

    return list_requirement

'''
setup(
    name="itsm-analysis",
    version="0.0.1",
    author="Shristi Gautam",
    author_email="shristigautam13@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements()
)
'''