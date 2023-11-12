# **AirBnB clone - The console ⬛**

![](https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2018/6/65f4a1dd9c51265f49d0.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20231111%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20231111T194537Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=1aff79216f7e94e1a4712284d6dd63b485c2deeff0824606bf3ed0d9b655cff2)
A command interpreter to manipulate data without a visual interface, like in a Shell (perfect for development and debugging)

## General:
+ How to create a Python package
+ How to create a command interpreter in Python using the `cmd` module
+ What is Unit testing and how to implement it in a large project
+ How to serialize and deserialize a Class
+ How to write and read a JSON file
+ How to manage `datetime`
+ What is an `UUID`
+ What is `*args` and how to use it
+ What is `**kwargs` and how to use it
+ How to handle named arguments in a function

## Usage exemple:
* **This shell should work like this in interactive mode:**
```shell
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
* **Also in non-interactive mode:**
```shell
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
* **Some command usage exemple:**
```shell
user@ubuntu:~/AirBnB_clone$ ./console.py
(hbnb) all MyModel
** class doesnt exist **
(hbnb) show BaseModel
** instance id missing **
(hbnb) show BaseModel My_First_Model
** no instance found **
(hbnb) create BaseModel
49faff9a-6318-451f-87b6-910505c55907
(hbnb) create User
77ccf49a-8918-3492-07f1-102163112333
(hbnb) all BaseModel
["[BaseModel] (49faff9a-6318-451f-87b6-910505c55907) {'created_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903293), 'id': '49faff9a-6318-451f-87b6-910505c55907', 'updated_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903300)}"]
(hbnb) destroy
** class name missing **
(hbnb) destroy BaseModel
(hbnb) all BaseModel
[]
(hbnb) 
```
* There is more just type help to see all available commands:
```shell
(hbnb) help

Documented commands (type help <topic>):
========================================                  
EOF  all  count  create  destroy  help  quit  show  update
                                                          
(hbnb) help all
Prints all string representation of all instances based or not on
        the class name. Usage: $ all BaseModel or $ all
(hbnb) help create
Creates a new instance of BaseModel, saves it (to the JSON file)
        and prints the id. Usage: $ create BaseModel
(hbnb) 
```

## AUTHORS/CONTRIBUTORS
* **Chamour15** <wafae.chamour@gmail.com>
* **dakhamohammed** <isanagy@live.fr>

