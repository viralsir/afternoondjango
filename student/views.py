from django.shortcuts import render

student_list=[]

# Create your views here.
def newstudent(request):
    if request.POST :
        student={}
        student['name']=request.POST['sname']
        student['age']=request.POST['age']
        student_list.append(student);
        return render(request,"student/new_student.html",{"msg":"record succefully inserted."})
    else :
        return render(request,"student/new_student.html",{"msg":""})

def viewstudent(request):
    return render(request,"student/view_student.html",
                  {"studentlist":student_list})