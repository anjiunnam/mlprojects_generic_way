# This setup.py file will help us to build our machine learning project/application as a package and can be deployed where ever we want
# So that anyone can use it by downloading the package


from setuptools import setup, find_packages
from typing import List


HYPEN_E_DOT = '-e .'
def get_requirements(file_path:str)->List[str]:
    '''
    This function will return the list of requirements
    '''
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n","") for req in requirements]
        
        # If we have any specific version of package mentioned in requirements.txt we can handle it here
        # For example: if we want to ignore specific version of package we can do it here
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    return requirements


setup(
    name="ml_project_package",
    version="0.0.1",
    author="Chinna Anjaneyulu",
    author_email="prasannaanji2001@gmail.com",
    packages=find_packages(),
    
    install_requires=get_requirements('requirements.txt')
     #install_requires=[
      #  "pandas",
       # "numpy",
        # "scikit-learn",
        # "flask",
        # "seaborn"
    #]
)