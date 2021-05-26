#! python3
"""
(10 points) 
Create a class object for a student.
It should have the following properties
str name
str studentNumber
int grade
list courses - to corresepond with course names
list grades - to correspond with grades

It should have the following methods:
average()       - determines the mathematical average of all course grades
getHonorRoll()  - determines the average of the top 5 courses if there are at least 5 courses.
                  returns True if the average is 86 or higher (on the honor roll)
                  returns False if not on the honor roll
showCourses()   - prints a list of all courses
showGrade(int)  - takes 1 parameter, the index of the list
                - displays the course name and grade
getCourses(list)- Receives a list of courses and stores that in the class property
getGrades(list) - Receives a list of grades and stores that in the class property
constructor     - should require the student name, studentNumber and grade (in that order)
"""

class student:

    # properties should be listed first
    name=""
    studentNumber=""
    grade=0
    courses=[]
    grades=[]

    def __init__(self,name,studentNumber,grade,courses=[],grades=[]): # You will need to create your own input parameters for all methods
        self.name=name
        self.studentNumber=studentNumber
        self.grade=grade
        self.courses=courses
        self.grades=grades

    def __del__(self):
        print("Thanks for using, quitting now")

    def average(self):
        lst=self.grades
        return sum(lst)/len(lst)
    
    def getHonorRoll(self):
        lst=self.grades
        lst.sort()
        top5=lst[-1]+lst[-2]+lst[-3]+lst[-4]+lst[-5]
        top5=int(top5/5)
        if top5>=86:
            return True
        else:
            return False

    def showCourses(self):
        lst=self.courses
        return print(lst)

    def showGrade(self,index):
        course=self.courses[index]
        grade=self.grades[index]
        return print("The grade of "+course+" is "+grade+".")

    def getCourses(self,list):
        self.courses=list
        print("The courses are stored")

    def getGrades(self,list):
        self.grades=list
        print("The grades are stored")


def main():
    # This contains test data that will be used by the autograder.
    # do not modify this function

    st1 = student("Anita Bath","91334",11)
    st1.getCourses( ["English","Math","PE","Computers","History","Biology","Japanese"] )
    st1.getGrades( [91, 94, 87, 99, 82, 100, 73])

    st2 = student("Joe Lunchbox","12346", 11)
    st2.getCourses( ["English","Math","Physics","Computers","Geography","Chemistry","French"] )
    st2.getGrades( [71, 98, 93, 95, 68, 81, 71])




main()