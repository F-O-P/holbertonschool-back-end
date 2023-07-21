#!/usr/bin/python3
''' This script will gather data from an employee ID and returns
    information about his/her list progress '''
import requests
import sys

def get_employee_name(employee_id):
    ''' This function will return the name of the employee '''
    url = "{}/{}".format(base_url, employee_id)
    response = requests.get(url)
    return response.json().get("name")

def get_assigned_tasks(employee_id):
    ''' This function will return the number of all tasks
        assigned to that the employee '''
    url = "{}/{}/todos".format(base_url, employee_id)
    response = requests.get(url)
    return len(response.json())

def get_completed_tasks(employee_id):
    ''' This function will return the number of tasks
        that the employee has completed '''
    finished_tasks = 0
    url = "{}/{}/todos".format(base_url, employee_id)
    response = requests.get(url)
    for task in response.json():
        if task.get("completed"):
            finished_tasks += 1
    return finished_tasks

def print_employee_status(employee_name, completed_tasks, assigned_tasks):
    ''' This function will return the information about the employee'''
    print("Employee {} is done with tasks({}/{}):".format(employee_name, completed_tasks, assigned_tasks))

if __name__ == "__main__":
    employee_id = sys.argv[1]
    base_url = "https://jsonplaceholder.typicode.com/users"
    employee_name = get_employee_name(employee_id)
    assigned_tasks = get_assigned_tasks(employee_id)
    completed_tasks = get_completed_tasks(employee_id)
    print_employee_status(employee_name, completed_tasks, assigned_tasks)
