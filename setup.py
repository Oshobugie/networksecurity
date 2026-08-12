'''
The setup.py is an essential part of packaging and distributing Python projects. It is used by setuptools(or distutils in older Python versions) to define the configuration  of your project, such as its metadata, dependcies, and more
'''

from setuptools import setup, find_packages
from typing import List

def get_requirements()-> List[str]:
    """
    This function reads the requirements.txt file and returns a list of dependencies.
    """
    requirement_lst: List[str] = []
    try: 
        with open('requirements.txt') as file:
            #Read lines from the file 
            lines = file.readlines()
            ## Process each line
            for line in lines:
                # Strip whitespace and ignore comments
                requirement = line.strip()
                #ignore empty lines and -e.
                if requirement and requirement != "-e .":
                    requirement_lst.append(requirement)
    except FileNotFoundError:
        print("requirements.txt file not found.")

    return requirement_lst

print(get_requirements())


setup(
    name="NetworkSecurity",
    version="0.0.1",
    author="Kanabe Oshobugie",
    author_email="oskanabe55@example.com",
    packages=find_packages(),
    install_requires=get_requirements()
)