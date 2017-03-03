#from django.http import HttpResponse
from lists.models import Item, List
from django.shortcuts import redirect, render

# Create your views here.
def home_page(request):
	
	return render(request, 'home.html')


def view_list(request):
	items = Item.objects.all()
	return render(request, 'list.html', {'items':items})

def new_list(request):
	list_l = List.objects.create()
	Item.objects.create(text=request.POST['item_text'], listt=list_l)
	return redirect('/lists/the-only-list-in-the-world/')