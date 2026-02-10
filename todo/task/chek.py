from .models import TaskComp,Task
from datetime import datetime
from dateutil.relativedelta import relativedelta
class chek_creat:

    def Chek_task(self,task_id):
        pass
    def __init__(self):
        print("inside the cheking class")

from datetime import date, timedelta

def is_task_completed(task_id, task_type):
    """
    Checks whether a task is completed for the current period
    based on its task_type.
    """

    today = date.today()

    task = Task.objects.get(id=task_id)

    task_comp = (
        TaskComp.objects
        .filter(task=task)
        .order_by('-complete_on')
        .first()
    )

    # If task was never completed
    if task_comp is None:
        return False

    completed_date = task_comp.complete_on

    # ONCE → completed even once = done forever
    if task_type == "Once":
        return True

    # DAILY → completed today
    if task_type == "Daily":
        return completed_date == today

    # WEEKLY → completed in current week
    if task_type == "Weekly":
        start_of_week = today - timedelta(days=today.weekday())
        end_of_week = start_of_week + timedelta(days=6)
        return start_of_week <= completed_date <= end_of_week

    # MONTHLY → completed in current month
    if task_type == "Monthly":
        return (
            completed_date.year == today.year and
            completed_date.month == today.month
        )

    # YEARLY → completed on same day & month of current year
    if task_type == "Yearly":
        return (
            completed_date.day == today.day and
            completed_date.month == today.month and
            completed_date.year == today.year
        )

    return False
