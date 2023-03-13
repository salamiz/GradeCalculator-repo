# NAME: Zulkifli Temitope Salami	
# DATE: 11/10/2022
# PROGRAM DESCRIPTION: A Program to Calculate the midterm grades of a user, using the course outline as a point 
# of reference. Inputs for the program will be the marks for each assessment, ordered by type. The assessments 
# include the Pre-Class Activities, In Class Exercises, and Assignments. Once the user finishes their entry, 
# the output will be the user’s grade as a percentage and the user’s percentage for each type of assessment.
# PROGRAM NAME: Grade Calculator
#######################################################################################################################################



# Declarations:
# pre_class_grade as a list
pre_class_grade = list ()
# in_class_grade as a list
in_class_grade = list ()
# assignments_grade as a list
assignments_grade = list ()
# PERCENT_CONVERSION as a constant
PERCENT_CONVERSION = 100
# MINIMUM_GRADE as a constant
MINIMUM_GRADE = 0
# MAXIMUM_PRE_CLASS_GRADE as a constant
MAXIMUM_PRE_CLASS_GRADE = 4
# TOTAL_PRE_CLASS_GRADE as a constant
TOTAL_PRE_CLASS_GRADE = 28
# MAXIMUM_IN_CLASS_GRADE as a constant
MAXIMUM_IN_CLASS_GRADE = 4
# TOTAL_IN_CLASS_GRADE as a constant
TOTAL_IN_CLASS_GRADE = 32
# MAXIMUM_ASSIGNMENT_GRADE as a constant
MAXIMUM_ASSIGNMENT_GRADE = 10
# TOTAL_ASSIGNMENT_GRADE as a constant
TOTAL_ASSIGNMENT_GRADE = 40
# Number of assesment type
NUMBER_OF_ASSESMENT_TYPE = 3




# Display a “Welcome to a Grade Calculation Program”
print("Welcome to a Grade Calculation Program")
# Input:
# Declare a function grade_function for input weight, grade name and grade list.
# Create a for loop to allow input for the weight number of times for each grade name, with each entry 
# validated as between  0 and weight inclusive.
def grade_function(weight,MAXIMUM_GRADE,grade_name,grade,TOTAL_GRADE):
    grade = list()
    for index in range (0,weight):
        need_input = True
        while need_input == True:
            try:
                entry = float(input("\nEnter your mark on the "+grade_name+ " "+ str(index + 1)+" : "))
            except:
                print("The input has to be a number.")
                continue
            if entry < MINIMUM_GRADE or entry > MAXIMUM_GRADE: 
                print(f"The input has to be between 0 and {MAXIMUM_GRADE} inclusive")
                continue
            else:
                need_input = False
            grade.append(entry)  
    print("\nThe list of each ",grade_name," is:"+str(grade))
    sum_grade = 0.0
    for value in grade:
        sum_grade += value  
    # Calculate the percentage using (sum_pre_class / TOTAL_PRE_CLASS_GRADE) * PERCENT_CONVERSION
    grade_percent = (sum_grade / TOTAL_GRADE) * PERCENT_CONVERSION
    print("\nThe percentage grade in",grade_name,"is: "+str(round(grade_percent,2)))
    return grade_percent
# Each grade type percent as a float
pre_class_percent = float
in_class_percent = float
assignment_percent = float
# Call the function using weight, Maximum Grade Input, Name of Assesment, Assesment list, and Total assesment grade; 
# equal to each assessment type percent
pre_class_percent = grade_function(7,MAXIMUM_PRE_CLASS_GRADE,"Pre-Class Activity",pre_class_grade,TOTAL_PRE_CLASS_GRADE)
in_class_percent = grade_function(8,MAXIMUM_IN_CLASS_GRADE,"In-Class Activity",in_class_grade,TOTAL_IN_CLASS_GRADE)
assignment_percent = grade_function(4,MAXIMUM_ASSIGNMENT_GRADE,"Assignments",assignments_grade,TOTAL_ASSIGNMENT_GRADE)
# Declare a variable total_percent and add the three previous percentage together.
total_percent = (pre_class_percent + in_class_percent + assignment_percent)/NUMBER_OF_ASSESMENT_TYPE
# Output:
# Display a message stating the total percentage and percentage of each assessment type
print("\nThe total percentage grade is: "+str(round(total_percent,2))+
"\nThe percentage grade in Pre-Class Activity is: "+str(round(pre_class_percent,2))+
"\nThe percentage grade in In-Class Activity is: "+str(round(in_class_percent,2))+
"\nThe percentage grade in Assignments Activity is: "+str(round(assignment_percent,2)))
# Prompt the user to end the program
input("\n\nPress Enter to end Program.....")




