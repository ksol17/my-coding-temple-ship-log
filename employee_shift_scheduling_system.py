import copy

def shallow_copy_schedule(schedules, source_week, target_week):
    schedules[target_week] = schedules[source_week].copy()
    print(f" {target_week}'s schedule copied from {source_week} (Shallow Copy).")

def deep_copy_schedule(schedules, source_week, target_week):
    schedules[target_week] = copy.deepcopy(schedules[source_week])
    print(f"Week {target_week}'s schedule copied from {source_week} (Deep Copy).")

def modify_shift(schedules, week, employee, shift):
    if week in schedules and employee in schedules[week]:
        schedules[week][employee] = shift
        print(f"Shift updated for {employee} in Week {week}: {shift}.")
    else:
        print(f"Schedule not found for {employee} in Week {week}.")

def display_schedules(schedules):
    for week, schedule in schedules.items():
        print(f" {week}:")
        for employee, shift in schedule.items():
            print(f" {employee}: {shift}")

employee_schedules = {
    "Week 1": {"Alice": "Morning", "Bob": "Evening", "Charlie": "Night"}
}

shallow_copy_schedule(employee_schedules, "Week 1", "Week 2")
deep_copy_schedule(employee_schedules, "Week 1", "Week 3")
modify_shift(employee_schedules, "Week 2", "Alice", "Night")
display_schedules(employee_schedules)