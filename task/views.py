from django.shortcuts import render

tasklist=['do recharage','check bankbalance','book movie ticket','change password']

employeelist=[{
    "name":"vimal",
    "age":21,
    "Salary":23000,
    "phno":{"home":23222,"office":23444}
}
,
{
    "name":"viren",
    "age":22,
    "Salary":2500,
    "phno":{"home":23333,"office":34444}
}
]
# Create your views here.
def viewtask(request):
    return render(request,"task/tasklist.html",{
        "tasklist":tasklist,
        "employeelist":employeelist
    })