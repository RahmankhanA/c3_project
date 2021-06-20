
from rest_framework import serializers, status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .serializer import PizzaSerializer
from .models import Pizza
# Create your views here.



@api_view(['GET', 'POST' ])
def get_pizzaDetail(request):
    try:
        pizzaList=Pizza.objects.all()


        # print(request.data.pizzaType,request.data.pizzaSize)
    except Pizza.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    
    if request.method =='GET':
        serializer=PizzaSerializer(pizzaList, many=True)
        # print(serializer.data)
        return Response(serializer.data)

    if request.method == 'POST':
        filteredList=[]
        both=False
        pizzatype=False
        pizzasize=False

        try:
            if request.data['pizzaType'] != None and request.data['pizzaSize'] != None:
                both=True
               
        except:
            pass
        try:
            if request.data['pizzaType'] != None:
                pizzatype=True
                
        except:
            pass
        try:
            if request.data['pizzaSize'] != None:
                pizzasize=True
                
        except :
            if both or pizzasize or pizzatype:
                pass
            else:
                return Response( status=status.HTTP_404_NOT_FOUND)
        
        for pizza in pizzaList:
            if both:
                if pizza.pizzaType == request.data['pizzaType'] and pizza.pizzaSize == request.data['pizzaSize']:
                    filteredList.append(pizza)
            elif pizzatype:
                if pizza.pizzaType == request.data['pizzaType']:
                    filteredList.append(pizza)
            elif pizzasize:
                if pizza.pizzaSize == request.data['pizzaSize']:
                    filteredList.append(pizza)

        serializer=PizzaSerializer(filteredList, many=True)
        return Response(serializer.data)



    
@api_view(['PUT', ])
def update_pizzaDetail(request, id):
    try:
        global target
        target = False
        pizzaList=Pizza.objects.all()
        
        for pizza in pizzaList:
            if str(pizza._id)==str(id):
                target=True
                break
            
    except Pizza.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "PUT":
        serializer=PizzaSerializer(pizza, data=request.data)
        data={}

        if serializer.is_valid():
            serializer.save()
            data['succes']='update succesfull'
            return Response(data=data)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['DELETE', ])
def delete_pizzaDetail(request, id):   
    try:
        global target
        target = False
        pizzaList=Pizza.objects.all()
        # list=[]
        for pizza in pizzaList:
            if str(pizza._id)==str(id):
                target=True
                break
            
    except Pizza.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    print("this is before operation ", target)
    if request.method == "DELETE" and target==True:
        operation=pizza.delete()
        data={}
       
        if operation:
            data['succes']='delete succesfull'
        else:
            data['failure']='delete failed'

        return Response(data=data, status=200)
    data={}
    data['failed'] = 'Pizza is not found try another one'
    return Response(data=data,status=status.HTTP_404_NOT_FOUND)



@api_view(['POST', ])
def post_pizzaDetail(request):
    pizzaModel=Pizza()

    if request.method =='POST':
        serializers= PizzaSerializer(pizzaModel, data=request.data)
        # print(request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)

        return Response(serializers.errors, status= status.HTTP_400_BAD_REQUEST)
   

   
