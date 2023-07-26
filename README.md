# Todo list webservice
> This is a Django web service that allows users to manage tasks, task tags, and track their completion status. With this web service, users can perform various CRUD (Create, Read, Update, Delete) operations on tasks and associated tags.

## Features
* Create Task: Users can create new tasks with relevant details like task name, description, due date, etc.
* Create Task Tags: Users can assign one or multiple tags to each task for better organization and categorization.
* Mark Task Completion: Users can mark tasks as completed or not completed to track their progress.
* Update Task Information: Users have the flexibility to modify task details and associated tags if needed.
* Delete Task: If a task is no longer required, users can delete it from the system.


## Links

- Repository: https://github.com/Andriy-Sydorenko/todo-list
- Issue tracker: https://github.com/Andriy-Sydorenko/todo-list/issues
  - In case of sensitive bugs like security vulnerabilities, please contact
    sidorenkoandrij217@gmail.com directly instead of using issue tracker. I value your effort
    to improve the security and privacy of this project!


## Installing / Getting started


A quick introduction of the setup you need to get run a project.
1. Fork a repo.
2. Use this command ```git clone the-link-from-your-forked-repo```. 
   - You can get the link by clicking the Clone or download button in your repo.
3. Open the project folder in your IDE.
4. Open a terminal in the project folder. 
5. If you are using PyCharm - it may propose you to automatically create venv for your project and install requirements in it, but if not:
    - For Windows:
    ```shell
    python -m venv venv
    venv\Scripts\activate
    pip install -r requirements.txt
    ```
   - For Mac OS:
    ```shell
    python -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
    ```
6. Run create migration file, using 
    ```shell
    python manage.py makemigrations
    ```
    Then migrate file, using
    ```shell
    python manage.py migrate
    ```
7. Create superuser to see extended functionality of the website:
    ```shell
    python manage.py createsuperuser
    ```

8. Then, to run a project, use this command:
    ```shell
    python manage.py runserver 
    ```

## Licensing

One really important part: Give your project a proper license. Here you should
state what the license is and how to find the text version of the license.
Something like:

"The code in this project is licensed under MIT license."
