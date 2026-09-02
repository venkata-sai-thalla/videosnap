import requests
from products.chatbot import URL
from products.models import ChatHistory
from django.contrib import messages
from django.shortcuts import render,redirect
from .models import Products
from django.conf import settings


def products_view(request):
    products = Products.objects.all()
    return render(request, 'products/products-view.html', {'products': products})


def create_products(request):

    if request.method == "POST":
        product_name= request.POST.get("product_name")
        description = request.POST.get("description")
        image=request.POST.get("image")
        price=request.POST.get("price")

        # Create the post
        products = Products.objects.create(
            name=product_name,
            description=description,
            image=image,
            price=price
        )

        # Get all uploaded images
        products = request.FILES.getlist("products")

        # Save each image
        for product in products:
            Products.objects.create(
                name=product

            )

        return redirect("products-view")

    return render(request, "products/create-products.html")


def add_to_cart(request, product_id):
    cart = request.session.get("cart", {})
    cart[str(product_id)] = cart.get(str(product_id), 0) + 1
    request.session["cart"] = cart
    return redirect("cart_view")

def cart_view(request):
    cart = request.session.get("cart", {})
    cart_items = []
    total = 0
    from .models import Products

    for product_id, quantity in cart.items():
        product = Products.objects.get(id=product_id)
        cart_items.append({"product": product, "quantity": quantity})
        total += product.price * quantity

    return render(request, "products/cart.html", {"cart_items": cart_items, "total": total})


    
def chatbot_view(request):
    user_input = ""
    text_output = ""
    if request.method == "POST":
        user_input = request.POST.get("user_input", "")
        payload = {
            "contents": [{
                "role": "user",
                "parts": [{"text": user_input}]
            }],
        }
        try:
            response = requests.post(URL, json=payload).json()
            if "candidates" in response and response["candidates"]:
                full_output = response["candidates"][0]["content"]["parts"][0]["text"]

                words = full_output.split()
                text_output = " ".join(words[:150])
                if len(words) > 150:
                    text_output += "..."

                messages.success(request, text_output)

                ChatHistory.objects.create(user_input=user_input, text_output=text_output)
            else:
                text_output = f"Error: Unexpected API response {response}"
                messages.error(request, text_output)

        except Exception as e:
            text_output = f"Error: {str(e)}"
            messages.error(request, text_output)

    chat_messages = ChatHistory.objects.all().order_by("-created_at")[1:3]

    return render(request,"products/chatbot.html",{"user_input": user_input,"text_output": text_output,"history": chat_messages})
