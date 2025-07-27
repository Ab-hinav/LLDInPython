
from enum import Enum

from datetime import datetime,timedelta

class TASK_STATUS(Enum):
    TODO = 1
    IN_PROGRESS = 2
    DONE = 3

class SEARCH_BY(Enum):
    ASSIGNED_TO_USER = 1
    TASK_NAME = 2
    TASK_STATUS = 3
    TASK_DUE_DATE=4
    TASK_PRIORITY = 5

class TASK_PRIORITY(Enum):
    LEVEL_1 = 1
    LEVEL_2 = 2


class Task:

    def __init__(self,id,name,priority:TASK_PRIORITY,due_date:datetime,status:TASK_STATUS,user=None):
        self._id = id
        self._name = name
        self._priority = priority
        self._due_date = due_date
        self._status = status
        self._assigned_to = user

    def mark_status(self,status):
        self._status = status

    def assign_task(self, user):
        self._assigned_to = user

    def get_assigned_to(self):
        return self._assigned_to

    def task_reminder(self):
        if datetime.now() > self._due_date:
            print("Task is overdue")
        if datetime.now() == self._due_date:
            print("Task is due today")
        if self._due_date - timedelta(days=1) == datetime.now():
            print("Task is due tomorrow")

    def __str__(self):
        return f'{self._id} {self._name} {self._priority} {self._due_date} {self._status} {str(self._assigned_to)}'
        


class User:

    def __init__(self,name:str,email:str):
        self.__name = name
        self.__email = email
        self.__tasks = []

    def add_task(self, task:Task):
        self.__tasks.append(task)
        print("Task added successfully")

    def compeleted_tasks(self):
        return [task for task in self.__tasks if task._status == TASK_STATUS.DONE]
    
    def get_task_history(self):
        print(f'getting task histoy for ${self.__name} ------')
        for task in self.__tasks:
            print(task._name, task._status, task._due_date)
        print('---------')
    
    def remove_task(self, task:Task):
        self.__tasks.remove(task)
        print("Task removed successfully")

    def __str__(self):
        if self is None:
            print("User is None")
            return
        return f'{self.__name} {self.__email}'

    def __repr__(self):
        return f'User :{self.__name} {self.__email}'
    

class TaskManager:

    __instance = None
    __is_initialized = False

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super(TaskManager,cls).__new__(cls)
        return cls.__instance

    def __init__(self):
        if TaskManager.__is_initialized:
            return
        TaskManager.__is_initialized = True
        self.__tasks = []

    def create_task(self, task:Task):
        self.__tasks.append(task)
        user = task.get_assigned_to()
        user.add_task(task)
        print("Task created successfully")

    def delete_task(self,task:Task):
        self.__tasks.remove(task)
        user = task.get_assigned_to()
        user.remove_task(task)
        print("Task deleted successfully")

    def update_task(self, task:Task, status:TASK_STATUS):
        task.mark_status(status)
        print("Task updated successfully")

    def get_task_history(self, user:User):
        return user.compeleted_tasks()
    
    def search_task(self,search_term,option):
        if option == SEARCH_BY.TASK_NAME:
            return [task for task in self.__tasks if task._name == search_term]
        elif option == SEARCH_BY.TASK_STATUS:
            return [task for task in self.__tasks if task._status == search_term]
        elif option == SEARCH_BY.TASK_DUE_DATE:
            return [task for task in self.__tasks if task._due_date == search_term]
        elif option == SEARCH_BY.TASK_PRIORITY:
            return [task for task in self.__tasks if task._priority == search_term]
        elif option == SEARCH_BY.ASSIGNED_TO_USER:
            return [task for task in self.__tasks if task._assigned_to == search_term]
        else:
            return []


    
