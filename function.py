def score_list_creator(file_name):
    """Take a file and convert all numbers into tuplets. Used as football /
    scores finder."""
    f = open(file_name)
    results_data = f.read()
    f.close()
    actual_results_list = []
    tmp = []
    for c in results_data:
        if c in "0,1,2,3,4,5,6,7,8,9".split(","):
            tmp.append(int(c))
        if len(tmp) == 2:
            actual_results_list.append(tmp)
            tmp = []
    return(actual_results_list)

def wc_calculator(list1,list2):
    """Convert football scores into points in a scale of 3 for the /
    exact match, 2 for goal difference and 1 for correct tendency"""
    total_points = 0
    for (x,y) in zip(list1, list2):
        if x[0] == y[0] and x[1] == y[1]:
          points = 3
        elif x[0] - y[0] == x[1] - y[1]:
          points = 2
        elif x[0] > x[1] and y[0] > y[1]:
          points = 1
        elif x[0] < x[1] and y[0] < y[1]:
          points = 1
        else:
          points = 0
        total_points += points
    print("You has {} points.".format(total_points))

#Applyng list_creator function to csv files with actual and guessed WC 2018
#scores.
list_actual_results = score_list_creator("actual_results.csv")
list_guessed_results_group1 = score_list_creator("guessed_results_group1.csv")
list_guessed_results_group2 = score_list_creator("guessed_results_group2.csv")
list_guessed_results_group3 = score_list_creator("guessed_results_group3.csv")
list_guessed_results_group4 = score_list_creator("guessed_results_group4.csv")
list_guessed_results_group5 = score_list_creator("guessed_results_group5.csv")
list_guessed_results_group6 = score_list_creator("guessed_results_group6.csv")

#Applying the wc_calculator function to the lists created
print("\n\nGroup 1:")
wc_calculator(list_actual_results,list_guessed_results_group1)
print("\nGroup 2:")
wc_calculator(list_actual_results,list_guessed_results_group2)
print("\nGroup 3:")
wc_calculator(list_actual_results,list_guessed_results_group3)
print("\nGroup 4:")
wc_calculator(list_actual_results,list_guessed_results_group4)
print("\nGroup 5:")
wc_calculator(list_actual_results,list_guessed_results_group5)
print("\nGroup 6:")
wc_calculator(list_actual_results,list_guessed_results_group6)
print("\n")
