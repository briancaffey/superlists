#from django.http import HttpResponse
from lists.models import Item, List
from django.shortcuts import redirect, render

# Create your views here.
def home_page(request):
	
	return render(request, 'home.html')


def view_list(request, list_id):
	list_l = List.objects.get(id=list_id)
	return render(request, 'list.html', {'listt':list_l})

def new_list(request):
	list_l = List.objects.create()
	Item.objects.create(text=request.POST['item_text'], listt=list_l)
	return redirect('/lists/%d/' % (list_l.id,))

def add_item(request, list_id):
	list_l = List.objects.get(id=list_id)
	Item.objects.create(text=request.POST['item_text'], listt=list_l)
	return redirect('/lists/%d/' % (list_l.id,))
