
create a virtualenv, install deps

export FLASK_CONFIG=development

export FLASK_APP=run.py

export FLASK_DEBUG=1


flask run

localhost:5000

list all routes : 
 http://localhost:5000/help


-------
Implementation

For miniredis, decided to create 3 seperate classes
for StringMap, ListMap and MapMap

Due to time constraints, decided against using inheritance

Therefore, there may be code duplication between classes.



// 



