# Fake Data Generator

It uses python [faker library](https://pypi.org/project/Faker/) along with some added features.

To install faker uses pip installer `pip install Faker`

### Usage
----
* Add the python file `fakedatagenerator.py` into your local project.
* Import the file using `from fakedatagenerator import fakedata as fd`
* Create instance using `FD=fd(X)`, where `X` is an integer that will decide the first index of the data
* Use `FD.Fakedatagenerator()

_Input Parameters_


                          distributionNameList=[normal], 
                          distColumnNameList=['NewColumn'], 
                          numberOfFields=10,
                          savecsv=True,
                          filename='output'
     
* distributionNameList - (List) It defines the type of distribution to use to generate numbers.
                         normal (default), binomial, exponential, poisson, uniform,beta, gamma, multinomial
                         
* distColumnNameList - (List) It defines the name of the new columns to create.
                       'NewColumn'(Default)
   
* numberOfFields - (int) It defines the number of data rwoes to create.
                   10(default)
            
* savecsv - (Boolean) Save the output as csv or not.
            True (Default)
          
* filename - (string) name of the output file to create.
             output(default)
             

_Return_

          Returns a data frame with fake data
