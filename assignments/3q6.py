students={}
#a------------
for i in range(3):
    sid=int(input("enter sid: "))
    name=str(input("enter name: "))
    students[sid]=name

print(students) 
#b----------
sorted_students_by_value=dict(sorted(students.items(), key=lambda item: item[1]))
print(sorted_students_by_value)
#c-----------
sorted_students_by_key = dict(sorted(students.items()))
print(sorted_students_by_key) 
#d-----------
enter_sid=int(input("enter sid to be searched: "))
print(students[enter_sid])



