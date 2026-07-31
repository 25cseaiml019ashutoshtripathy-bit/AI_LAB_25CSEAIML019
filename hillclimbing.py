def objective_function(x):
    return -(x**2)+10

def hill_climbing(start,step_size,max_iterations):
    current=start
    current_value=objective_function(current)

    for i in range (max_iterations):
        left=current-step_size
        right=current+step_size

        left_value=objective_function(left)
        right_value=objective_function(right)

        if left_value>current_value:
            current=left
            current_value=left_value
        elif right_value>current_value:
            current=right
            current_value=right_value
        else :
            break

    return current,current_value

#main program...
start=float(input("enter the starting value :"))
step_size=float(input("enter the step size : "))
max_iteration=int(input("enter maximum iteration : "))

best_position,best_value=hill_climbing(start,step_size,max_iteration)
print("best position = ",best_position)
print("maximum value = ",best_value)
    