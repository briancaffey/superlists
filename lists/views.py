from django.core.exceptions import ValidationError
from lists.models import Item, List
from django.shortcuts import redirect, render


# Create your views here.
def home_page(request):
	
	return render(request, 'home.html')


def view_list(request, list_id):
	list_l = List.objects.get(id=list_id)
	error = None

	if request.method == 'POST':
		try:
			item = Item(text=request.POST['item_text'], listt=list_l)
			item.full_clean()
			item.save()
			return redirect(f'/lists/{list_l.id}/')
		except ValidationError:
			error = "You can't have an empty list item"

	return render(request, 'list.html', {'listt':list_l, 'error': error})

def new_list(request):
	list_l = List.objects.create()
	item = Item(text=request.POST['item_text'], listt=list_l)
	try:
		item.full_clean()
		item.save()
	except ValidationError:
		list_l.delete()
		error = "You can't have an empty list item"
		return render(request, 'home.html', {"error": error})
	return redirect(f'/lists/{list_l.id}/')

