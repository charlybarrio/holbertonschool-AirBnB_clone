
# AirBnB clone - The console :technologist:   


This is the first part to the AirBnB clone Proyect, where we work with HTML/CSS templating, database storage, API, front-end integration… 
But first, the console. :computer:

On this proyect we started with: 
- Put in place parent class called BaseModel
- serealization and deserealization:
```
    instance <-> Dictionary <-> Json string <-> file 
```
- create classes used for AirBnB (inherit from BaseModel): 
    
    **User, State, City, Amenity, Place, Review**

- Create the first abstracted storage engine of the project: File storage

- Create all unittests to validate all our classes and storage engine





## Tech Stack

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)



## Learning objectives :books:

What did you learn while building this project?

- How to create a Python package
- How to create a command interpreter in Python using the cmd module
- What is Unit testing and how to implement it in a large project
- How to serialize and deserialize a Class
- How to write and read a JSON file
- How to manage datetime
- What is an UUID
- What is *args and how to use it
- What is **kwargs and how to use it
- How to handle named arguments in a function



## Requirements :white_check_mark:

- Ubuntu 20.04 LTS
- Python3
- Pycodestyle (version 2.7.*)
## Console commands :computer:

```
(hbnb)help

Documented commands (type help <topic>):
========================================
EOF  all  create  destroy  help  quit  show  update

(hbnb)
```

- *create:* Creates a new instance of BaseModel and prints the id.

- *show:* Prints the string representation of an instance based on the class name and id

- *destroy:* Deletes an instance based on the class name and id

- *all:* Prints all string representation of all instances based or not on the class name

- *update:* Updates an instance based on the class name id by adding or updating attribute

## Usage/Examples :toolbox:

That is how the console works in interactive mode:
```
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
$
```

And in non-interactive mode:
```
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
```




## Running Tests :test_tube:

To run tests, run the following command

Interactive mode:
```
python3 -m unittest discover tests 
```
Non-Interactive mode:
```
 echo "python3 -m unittest discover tests" | bash
```




## Installation :wrench:

```bash
  git clone https://github.com/C-Mauro/holbertonschool-AirBnB_clone.git
```
    
## Authors

- [@Charly Barrio](https://github.com/charlybarrio)
- [@ Camila Mauro](https://github.com/C-Mauro)


