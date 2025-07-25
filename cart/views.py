from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import CartItem
from .serializers import CartItemSerializer
from django.shortcuts import render, redirect
# Create your views here.

@api_view(['GET', 'POST'])
def cart_items(request):
    if request.method == 'GET':
        items = CartItem.objects.all()
        serializer = CartItemSerializer(items, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = CartItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)




def add_cart_form(request):
    if request.method == 'POST':
        CartItem.objects.create(
            product_name=request.POST['product_name'],
            quantity=request.POST['quantity'],
            price=request.POST['price']
        )
        return redirect('add-cart')
    return render(request, 'cart/cart_form.html')
