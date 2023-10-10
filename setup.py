from setuptools import find_packages,setup
from typing import List

constant = "-e."

def getRequirement(filePath:str)->List[str]:
   requirements = []
   with open(filePath) as fileObject : 
      requirements = fileObject.readlines()
      requirements = [req.replace("/n","") for req in requirements]

      if constant in requirements:
         requirements.remove(constant)
      return requirements 


setup(
    name = "DiamondPricePrediction",
    version = "0.0.1",
    author = "Abhi Verma",
    author_email= "onthewayabhi@gmail.com",
    install_requires =getRequirement('requirements.txt'),
    packages = find_packages(),
)