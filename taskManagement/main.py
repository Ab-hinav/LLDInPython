
from datetime import datetime
from util import TaskManager,Task,TASK_PRIORITY,TASK_STATUS,User,SEARCH_BY



if __name__ == "__main__":
    
    user1 = User('abhiTest','abhins@gmail.com')
    user2 = User('abhiTest2', 'XXXXXXXXXXXXXXXXX')
    task1 = Task(1,'task1',TASK_PRIORITY.LEVEL_1,datetime(2025,6,26),TASK_STATUS.TODO,user1)
    task2 = Task(2, 'task2', TASK_PRIORITY.LEVEL_2, datetime(2025, 6, 26), TASK_STATUS.TODO, user2)
    task3 = Task(3, 'task3', TASK_PRIORITY.LEVEL_1, datetime(2025, 6, 26), TASK_STATUS.IN_PROGRESS, user1)
    task4 = Task(4, 'task4', TASK_PRIORITY.LEVEL_2, datetime(2025, 6, 26), TASK_STATUS.TODO, user2)
    
    t1 = TaskManager()
    
    t1.create_task(task1)
    t1.create_task(task2)
    t1.create_task(task3)
    t1.create_task(task4)

    t1.get_task_history(user1)

    t1.update_task(task1, TASK_STATUS.DONE)

    a = t1.search_task('task1', SEARCH_BY.TASK_NAME)
    for a1 in a:
        print(a1)

    b = t1.search_task(user1, SEARCH_BY.ASSIGNED_TO_USER)
    for a1 in b:
        print(a1)


