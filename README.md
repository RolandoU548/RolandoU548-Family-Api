<!-- hide -->
# Family Static API
<!-- endhide -->

The Jackson Family needs a static API! We need to build the *data structures* and create API endpoint to interact with it using Postman.

## 🌱  How to start this project

This project comes with the necessary files to start working immediately.

We recommend opening this very same repository using a provisioning tool like [Codespaces](https://4geeks.com/lesson/what-is-github-codespaces) (recommended) or [Gitpod](https://4geeks.com/lesson/how-to-use-gitpod). Alternatively, you can clone it on your local computer using the `git clone` command.

This is the repository you need to open:

```txt
https://github.com/breatheco-de/exercise-family-static-api
```

**👉 Please follow these steps on** [how to start a coding project](https://4geeks.com/lesson/how-to-start-a-project).

## 💻 Installation

2. Install the project dependencies by running `$ pipenv install`.

3. Get inside the virtual environment by running `$ pipenv shell`

4. Start the server by running `$ pipenv run start`

5. Test your code by running `$ pipenv run test`

## ✅ Automatic grading

Test your code by running `$ pipenv run test`

## 📝 Instructions

1) Create the code needed to implement the API endpoints described further below.  

2) The only two files you have to edit are:  

- `src/datastructure.py`: Contains the class with the rules on how to manage the family members.  
- `src/app.py`: Contains the API, it uses the Family as data structure. 
	
3) We have prepared a set of automated tests that will give you an idea if your code is correct, run the tests by typing `$ pipenv run test` on the command line.  

## Data structures

Every **member** of the Jackson family must be a dictionary - the equivalent of [Objects Literals in JS](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Working_with_Objects) - and have these values:

```python
    + id: Int
    + first_name: String
    + last_name: String (Always Jackson)
    + age: Int > 0
    + lucky_numbers: Array of int
```
The **family** data-structure will be a class with the following structure:

```python
class Family:

    def __init__(self, last_name):
        self.last_name = last_name
        # example list of members
        self._members = [{
            "id": self._generateId(),
            "first_name": "John",
            "last_name": last_name
        }]

    # read-only: Use this method to generate random members ID's when adding members into the list
    def _generateId(self):
        return random.randint(0, 99999999) //import random 

    def add_member(self, member):
        ## you have to implement this method
        ## append the member to the list of _members
        pass

    def delete_member(self, id):
        ## you have to implement this method
        ## loop the list and delete the member with the given id
        pass

    def update_member(self, id, member):
        ## you have to implement this method
        ## loop the list and replace the member with the given id
        pass

    def get_member(self, id):
        ## you have to implement this method
        ## loop all the members and return the one with the given id
        pass

    def get_all_members(self):
        return self._members
```

Note: don't forget to initialize the class: `jackson_family = FamilyStructure('Jackson')` *before* the routes.

## These are the initial Family Members

```md
John Jackson
33 Years old
Lucky Numbers: 7, 13, 22

Jane Jackson
35 Years old
Lucky Numbers: 10, 14, 3

Jimmy Jackson
5 Years old
Lucky Numbers: 1
```

## Endpoints

This API must have 4 endpoints. They all return JSON:

### 1) Get all family members:

Which returns all members of the family.

```md
GET /members

status_code: 200 if success. 400 if bad request (wrong info) screw up, 500 if the server encounter an error

RESPONSE BODY (content-type: application/json):

[], // List of members.

```

### 2) Retrieve one member

Which returns the member of the family where `id == member_id`.

```md
GET /member/<int:member_id>

RESPONSE (content_type: application/json):

status_code: 200 if success. 400 if bad request (wrong info) screw up, 500 if the server encounter an error

body: //the member's json object

{
    "id": Int,
    "first_name": String,
    "age": Int,
    "lucky_numbers": List
}

```

### 3) Add (POST) new member

Which adds a new member to the family data structure.

```md
POST /member

REQUEST BODY (content_type: application/json):

{
    first_name: String,
    age: Int,
    lucky_numbers: [],
    id: Int *optional
}

RESPONSE (content_type: application/json):

status_code: 200 if success. 400 if a bad request (wrong info) screw up, 500 if the server encounters an error

body: empty
```

Keep in mind that POST request data dictionary may contain a key and a value for this new member `id`.
- If it does not, your API should randomly generate one when adding family members.
- If it does include it, that is the value to be used for such end.

### 4) DELETE one member

Which deletes a family member with `id == member_id`

```md
DELETE /member/<int:member_id>

RESPONSE (content_type: application/json):

status_code: 200 if success. 400 if a bad request (wrong info) screw up, 500 if the server encounters an error

body: {
    done: True
}    

```

## Requirements

- All requests and responses should be in content/type: application/json
- Response codes must be `200` for success, `400` for bad request or `404` for not found.
- These exercises do not include a database, everything must be done in Runtime (RAM).

This and many other projects are built by students as part of the 4Geeks Academy [Coding Bootcamp](https://4geeksacademy.com/us/coding-bootcamp) by [Alejandro Sanchez](https://twitter.com/alesanchezr) and many other contributors. Find out more about our [Full Stack Developer Course](https://4geeksacademy.com/us/coding-bootcamps/part-time-full-stack-developer), and [Data Science Bootcamp](https://4geeksacademy.com/us/coding-bootcamps/datascience-machine-learning).