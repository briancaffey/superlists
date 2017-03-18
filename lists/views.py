from django.core.exceptions import ValidationError
from lists.forms import ItemForm
from lists.models import Item, List
from django.shortcuts import redirect, render




# Create your views here.
def home_page(request):
	return render(request, 'home.html', {'form': ItemForm()})

def view_list(request, list_id):
	list_l = List.objects.get(id=list_id)
	form = ItemForm()
	if request.method == 'POST':
		form = ItemForm(data=request.POST)
		if form.is_valid():
			Item.objects.create(text=request.POST['text'], listt=list_l)
			return redirect(list_l)
	return render(request, 'list.html', {'listt':list_l, "form":form})

def new_list(request):
	form = ItemForm(data=request.POST)
	if form.is_valid():
		list_l = List.objects.create()
		Item.objects.create(text=request.POST['text'], listt=list_l)
		return redirect(list_l)
	else:
		return render(request, 'home.html', {"form": form})

