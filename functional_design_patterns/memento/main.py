from todo import ToDo

my_list = ToDo()
my_list.add_goal('Buy something')
my_list.add_goal('Fix the computer')
my_list.add_goal('Read the book')
my_list.end_goal(1)
my_list.show_goals(False)
my_list.undo()
print()
my_list.show_goals()
