
create a virtualenv, install deps

    export FLASK_CONFIG=development

    export FLASK_APP=run.py

    export FLASK_DEBUG=1


    flask run

    localhost:5000

list all routes : 
    http://localhost:5000/help


--------
Examples

    localhost:5000/str/set_kv

    localhost:5000/list/set_kv

    localhost:5000/map/set_kv


-------
Implementation

For miniredis, decided to create 3 seperate classes
for StringMap, ListMap and MapMap

Due to time constraints, decided against using inheritance

Therefore, there may be code duplication between classes.


For api, 3 seperate controllers for each map type

-------



