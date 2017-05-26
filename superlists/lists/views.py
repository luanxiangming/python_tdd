from django.shortcuts import render, redirect
from django.http import HttpResponse
from lists.models import Item, List
from django.core.exceptions import ValidationError


def home_page(request):
	return render(request, 'home.html')

def view_list(request, list_id):
	list_ = List.objects.get(id=list_id)
	error = None

	if request.method == 'POST':
		try:
			item = Item(text=request.POST['item_text'], list=list_)
			item.full_clean()
			item.save()
			return redirect('/lists/%d/' %(list_.id))
		except ValidationError:
			error = 'You cannot have an empty list item'
			
	return render(request, 'list.html', {'list': list_, 'error': error})

def new_list(request):
	list_ = List.objects.create()
	item = Item.objects.create(text=request.POST['item_text'], list=list_)
	try:
		item.full_clean()
		item.save()
	except ValidationError:
		list_.delete()
		error = 'You cannot have an empty list item'
		return render(request, 'home.html', {'error': error})
	return redirect('/lists/%d/' %(list_.id))
