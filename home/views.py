from rest_framework.decorators import api_view
from rest_framework.response import Response

# we have to write a decorator this decorator will tell what are the 
# metds this method will handel
@api_view(['GET', 'POST'])
def index(request):
    courses = {
        'c_name': 'Python',
        'learn' : ['flask', 'django', 'flask'],
        'name': [1,2,3,4,5]
    }
    if request.method == 'GET':
        name = request.GET.get('name')
        age = request.GET.get('age')
        lname = request.GET.get('lastName')
        # print(Response.GET.get('name', 'age', 'lastname'))
        print(name, age, lname)
        print("get method")
        return Response(courses)
    elif request.method == 'POST':
        data = request.data
        print('************')
        print(data)
        return Response('data entered successfully')
       
    return Response(courses)

''''

Serelizer -> simplest working 
a seralizer converts the data  into json format 

A class which helps us to seleralize 
the data from query set to json frmat

'''