names = list(input("Enter names separated by commas:").split(','))
assignments = list(map(int,input("Enter assignment conuts separated by commas:").split(',')))
grades = list(map(int,input("Enter grades separated by commas:").split(",")))
i = 0
while i < len(names):
    print("This is a reminder that you have {} assignments left to submit before you can graduate. Your current grade is {} and can increase to {} if you submit all assignments before the due date.".format(names[i],grades[i],2*assignments[i]+grades[i]))
    i+=1
