
# CRUD Operation On Pizza Detail API

In this API You can fetch the pizza detail eg. size , type and toppings of pizza.
Also you can edit , delete and create new pizza detail.


## Run Locally

Clone the project

```bash
  git clone https://github.com/RahmankhanA/c3_project/
```

Go to the project directory

```bash
  cd c3_project/pizza
```

Install dependencies

```bash
  pip install  -r requirements.txt

```

Initial Setup

```bash
  install the mongodb 
  create the database 
  change the database name in settings.py
  
```

Start the server

```bash
    python manage.py runserver
```

  
## Documentation

There are the following methods in the  Pizza Detail API

###  1 GET Method to fetch the pizza Detail
    you can fetch all the pizza detail which is avaible in the database
    http://127.0.0.1:8000/api/get/
    by using the above endpoint you will get all the detail
    if you are using this in the local machine the above url is working well
    otherwise use  http://domain-name/api/get/

    example 

    import requests

    url = "http://127.0.0.1:8000/api/get/"

    response = requests.request("GET", url)

    print(response.text)

  

###  2 POST Method to fetch the pizza Detail According to the filter
    you  can filter the pizza detail according to the pizzaType and pizzaSize
    there are only two type of pizza accepted here regular and square

    example

    import requests

    url = "http://127.0.0.1:8000/api/get/"

    payload={'pizzaType': 'square',
    'pizzaSize': 'large'}


    response = requests.request("POST", url,  data=payload)

    print(response.text)


###  3 PUT Method to Update the Pizza Detail
    By using PUT method you can edit the existing pizzaDetail 
    here you should edit the detail by using the unique id(60cf26ace66f19c66eb58666) of pizzaDetail

    Example


    import requests

    url = "http://127.0.0.1:8000/api/update/60cf26ace66f19c66eb58666?pizzaTopping=onion&pizzaSize=medium&pizzaType=regular"

    payload={'pizzaType': 'regular',
    'pizzaSize': 'medium',
    'pizzaTopping': 'onion'}
  
    response = requests.request("PUT", url,  data=payload, )

    print(response.text)

###  4 DELETE Method to Delete the Pizza Detail
    By using DELETE method you can delete the existing pizzaDetail 
    here you should delete the detail by using the unique id(60cf26ace66f19c66eb58666) of pizzaDetail

    Example 

    import requests

    url = "http://127.0.0.1:8000/api/delete/60cf26a6e66f19c66eb58664"

    response = requests.request("DELETE", url)

    print(response.text)


###  5 POST Method to create new  Pizza Detail
    You can create new pizza Detail to add in the database
    You should provide the pizza detail eg. pizzaType, pizzaSize and Toppings of pizza

    Example
    import requests

    url = "http://127.0.0.1:8000/api/post?pizzType=square&pizzaSize=small&pizzaTopping=onion"

    payload={'pizzaType': 'square',
    'pizzaSize': 'large',
    'pizzaTopping': 'orange'}
    files=[

    ]
    headers = {}

    response = requests.request("POST", url, headers=headers, data=payload, files=files)

    print(response.text)

## Features

- Fetch the pizza detail along with filter
- Edit the pizza detail
- Delete the pizza detail
- Create new  pizza detail

  
