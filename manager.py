from datetime import datetime
import json, shutil, pathlib

class task_manager:
    """"task_manager class will create tasks and apply commands to the tasks"""
    def __init__(self,id=None,description=None,status='todo',createdAt=None,updatedAt=None):
        self.id=id
        self.description=description
        self.status=status
        self.createdAt=createdAt
        self.updatedAt=updatedAt
    def add_task(self, descript):
        task = task_manager()
        task.id=len(tasks) # add an array containing tasks later which will grab how many tasks we have from the json file
        task.description = descript
        task.createdAt=datetime.now().strftime('%Y-%m-%d %H:%M:%S')

