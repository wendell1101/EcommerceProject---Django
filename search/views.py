from django.shortcuts import render
from django.views.generic import ListView
from django.db.models import Q
from products.models import Product

class SearchProductListView(ListView):
    template_name = 'search/search_list.html'
    context_object_name = 'products'
    
    def get_queryset(self, *args, **kwargs):
        request = self.request
        query = request.GET.get('q')
        if query is not None:
            lookups = Q(title__icontains = query) | Q(description__icontains = query) | Q(category__icontains = query) | Q(label__icontains = query)
            return Product.objects.filter(lookups).distinct()
        return Product.objects.all()    
    
    def get_context_data(self, *args, **kwargs):
        context = super(SearchProductListView,self).get_context_data(*args, **kwargs)
        context['query'] = self.request.GET.get('q')
        return context
    
  

