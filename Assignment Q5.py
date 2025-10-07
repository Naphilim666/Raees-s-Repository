attendance = [
    (101, ['P', 'A', 'P', 'P', 'P']),
    (102, ['P', 'P', 'A', 'P', 'A']),
    (103, ['A', 'P', 'A', 'P', 'P']),
    (104, ['P', 'P', 'P', 'P', 'P'])
]

def attendance_percentage(attendance_data):
    for i in range(len(attendance_data)):
        sid=attendance_data[i][0]
        total=len(attendance_data[i][1])
        count = 0
        for j in range(total):
            if attendance_data[i][1][j] == 'P':
                count += 1

        percentage = (count/total)*100
        print("sid :",sid,"attendence: ",percentage,"%\n")

def low_attendance_students(attendance_data, threshold):
    lowList=[]
    for i in range(len(attendance_data)):
        sid = attendance_data[i][0]
        total = len(attendance_data[i][1])
        count = 0
        for j in range(total):
            if attendance_data[i][1][j] == 'P':
                count += 1

        if((count / total) * 100) < threshold:
            lowList.append(sid)
    return lowList

def daily_absences(attendance_data):

    total = len(attendance_data[0][1])
    abs=[0] * total
    for i in range(len(attendance_data)):
        for j in range(total):
            if attendance_data[i][1][j] == 'A':
                abs[j]+=1
    for d in range(total):
      print("Day",d+1," : ",abs[d],"absences")

attendance_percentage(attendance)
print("Low Attendence Students:",low_attendance_students(attendance, 75.0),"\n")
daily_absences(attendance)