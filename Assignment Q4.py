def Input(size):
    listnum=[]
    for i in range(size):
     while True:
        x = (int(input("Enter Marks of Student(0-100) : ")))
        if(x<100 and x>0):
            listnum.append(x)
            break
        else:
            print("Invalid Input")

    return listnum

def calculate_Avg(listnum):
    sum=int(0)
    size = len(listnum)
    for i in range(len(listnum)):
        sum+=listnum[i]
    avg = sum/size
    return avg
def grades(listnum):

     gradesList=['A' if marks >=90 and marks <=100 else 'B'
                if marks >=75 and marks <=89 else 'C' if marks >=60 and marks <=74
                else 'F' for marks in listnum]
     return gradesList



size  = int(input("Enter size of student : "))
listnum=Input(size)
avg=calculate_Avg(listnum)
print("average",avg)
max_marks = lambda listnum: max(listnum)
print("Max Marks:",max_marks(listnum))
print(grades(listnum))


