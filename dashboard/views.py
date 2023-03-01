from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404

from WebShop.models import Item

@login_required()
def index(request):
    items = Item.objects.filter(created_by=request.user)

    return render(request, 'core/dashboard.html', {
        'items': items,
    })

@login_required()
def delete(request, pk):
    item = get_object_or_404(Item, pk=pk, created_by=request.user)
    item.delete()