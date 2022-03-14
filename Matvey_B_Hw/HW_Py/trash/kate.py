import traceback


def kate(employees, time_to_leave, floor_nums, employee_to_leave):
    employees_visited = 0
    target_floor = floor_nums[employee_to_leave - 1]
    flights_to_target = target_floor - 1
    stairs = 0

    # Step1: find the floor number to go to by lift
    current_floor = 0

    while employees_visited != employees:
        if current_floor == 0: # journey begins
            # which floor to go to by lift if time permits
            if time_to_leave >= flights_to_target:
                current_floor = floor_nums[0]
            elif time_to_leave < flights_to_target:
                # go straight to the the target floor by lift
                current_floor = target_floor
        elif current_floor != 0:
            # decide go up or down?
            up_index = len(floor_nums)
            top_floor = floor_nums[up_index-1]
            stairs_up = (top_floor) - current_floor
            stairs_down = current_floor - 1
            if (stairs_up >= stairs_down):
                stairs = stairs_down * 2 + stairs_up
                employees_visited = employees
            else:
                stairs = stairs_up * 2 + stairs_down
                employees_visited = employees
    print(stairs)
    return stairs


try:
    assert kate(5, 5, [1, 4, 9, 16, 25], 2) == 24
    assert kate(6, 4, [1, 2, 3, 6, 8, 25], 5) == 31
    assert kate(5, 1, [1, 2, 3, 4, 5], 3) == 6
    assert kate(5, 1, [1, 2, 3, 4, 5], 5) == 4
    assert kate(5, 2, [1, 2, 3, 4, 5], 4) == 5

except AssertionError:
    print("TEST ERROR")
    traceback.print_exc()
else:
    print("TEST PASSED")
