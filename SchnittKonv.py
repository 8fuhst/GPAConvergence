from matplotlib import pyplot as plt

list_of_grades = []
last_val = 0
credit_sum = 0
# Enter your Modules in the lst dict. 'Modulename': [Grade, Amount of Credits]
lst = {'Examplemodule 1': [1.0, 6],
       'Examplemodule 2': [3.0, 9],
       'Examplemodule 3': [2.0, 3]
       }

for i in lst.values():
    last_val = last_val + i[0]*i[1]
    credit_sum = credit_sum + i[1]
    list_of_grades.append(last_val / credit_sum)

print("Current Grade-Average: " + str(list_of_grades[len(list_of_grades) - 1]))
plt.title = 'Grade Convergence'
x = [j for j in range(0, len(lst))]
convergence_line_x = [0, len(list_of_grades)]
convergence_line_y = [list_of_grades[len(list_of_grades) - 1], list_of_grades[len(list_of_grades) - 1]]
plt.xticks(x, lst.keys())
plt.plot(list_of_grades)
plt.plot(convergence_line_x, convergence_line_y, '#000000')
plt.show()
