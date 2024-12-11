from django.shortcuts import render

# Create your views here.
# def show_details(request,my_id):
    # print(my_id)
#     return render(request,'enroll/show.html',{'id':my_id})

def home(request):
    return render(request,'enroll/home.html')

def show_details(request,my_id):
    if my_id==1:
        student={'id':my_id,"name":'Binod'}
    if my_id==2:
        student={'id':my_id,"name":'Bijaya'}
    if my_id==3:
        student={'id':my_id,"name":'Saroj'}

    return render(request,'enroll/show.html',student)


def show_subdetails(request,my_id,my_subid):
    if my_id==1 and my_subid==5:
        student={'id':my_id,"name":'Binod',"info":"sub details"}
    if my_id==2 and my_subid==6:
        student={'id':my_id,"name":'Bijaya',"info":"sub details"}
    if my_id==3 and my_subid==7:
        student={'id':my_id,"name":'Saroj',"info":"sub details"}
    return render(request,'enroll/show.html',student)