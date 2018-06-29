#Function to iterate over 2 football scores lists,comparing actual and guessed results of the 2018 World Cup, asssigning points and printing the values.

def wc_calculator(list1,list2):
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
