from .models import TaskComp,Task


class chek_creat:

    def Chek_task(self,task_id):
        pass
    def __init__(self):
        print("inside the cheking class")

def chek_date(task_id):
    task=Task.objects.get(id=task_id)
    task_chek=TaskComp.objects.filter(task=task).first()

    if task_chek is not None:
        return task_chek.complete_on
        
    return None

def exist_chek(task_id,task_type):
    if task_type=="Once":
        print("inside the once chek")
        date=chek_date(task_id=task_id)

        if date is None  :
            return False
        
        else:
            return True
        # chek the task is exist or not
        # if exist then return true else false
    elif task_type=="Daily":
        print("inside the daily chek")

        date=chek_date(task_id=task_id)
        print(f"the date is {date}")

        if date is not None:
            return True
        
        else:
            return False
        # chek the task is exist or not
        # if exist then return true else false
    elif task_type=="Weekly":
        print("inside the weekly chek")
        # chek the task is exist or not
        # if exist then return true else false
    elif task_type=="Monthly":
        print("inside the monthly chek")
        # chek the task is exist or not
        # if exist then return true else false
    elif task_type=="Yearly":
        print("inside the yearly chek")
        # chek the task is exist or not
        # if exist then return true else false