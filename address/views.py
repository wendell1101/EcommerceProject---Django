from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from address.models import BillingAddress, ShippingAddress, DefaultAddress
from address.forms import BillingAddressForm, ShippingAddressForm
from customer_profiles.models import CustomerProfile


@login_required
def billing_address(request):
    form = BillingAddressForm(request.POST or None)
    try:
        customer_profile = get_object_or_404(CustomerProfile, user=request.user)
        
        if customer_profile:
            default_address = DefaultAddress.objects.filter(customer_profile=customer_profile).first()  
        previous_address = request.POST.get('previous_address')
        print(previous_address)
        if form.is_valid():           
            house_number             = form.cleaned_data.get('house_number')
            street                   = form.cleaned_data.get('street')
            barangay                 = form.cleaned_data.get('barangay')
            city                     = form.cleaned_data.get('city')
            province                 = form.cleaned_data.get('province')
            zip_code                 = form.cleaned_data.get('zip_code')
            country                  = form.cleaned_data.get('country')            
            same_as_shipping_address = form.cleaned_data.get('same_as_shipping_address')
            save_for_next_time       = form.cleaned_data.get('save_for_next_time')            
            
            default_address = DefaultAddress.objects.filter(customer_profile=customer_profile).first()  
            if same_as_shipping_address:
                shipping = ShippingAddress(
                    customer_profile = customer_profile,
                    house_number     = house_number,
                    street           = street,
                    barangay         = barangay,
                    city             = city,
                    province         = province,
                    zip_code         = zip_code,
                    country          = country,
                )   
                shipping.save()
                billing = BillingAddress(
                    customer_profile = customer_profile,
                    house_number     = house_number,
                    street           = street,
                    barangay         = barangay,
                    city             = city,
                    province         = province,
                    zip_code         = zip_code,
                    country          = country,
                )   
                billing.save()
                
                if default_address:
                    default_address.house_number     = house_number,
                    default_address.street           = street,
                    default_address.barangay         = barangay,
                    default_address.city             = city,
                    default_address.province         = province,
                    default_address.zip_code         = zip_code,
                    default_address.country          = country,
                    default_address.save()
                
                else:
                    default_address = DefaultAddress.objects.create(
                        customer_profile = customer_profile,
                        house_number     = house_number,
                        street           = street,
                        barangay         = barangay,
                        city             = city,
                        province         = province,
                        zip_code         = zip_code,
                        country          = country,
                    )  
                    default_address.save()
                
                return redirect('checkout')             
            default_address = DefaultAddress.objects.filter(customer_profile=customer_profile).first()  
         
            if default_address:
                default_address.house_number     = house_number,
                default_address.street           = street,
                default_address.barangay         = barangay,
                default_address.city             = city,
                default_address.province         = province,
                default_address.zip_code         = zip_code,
                default_address.country          = country,
                default_address.save()
                
            else:
                default_address = DefaultAddress.objects.create(
                    customer_profile = customer_profile,
                    house_number     = house_number,
                    street           = street,
                    barangay         = barangay,
                    city             = city,
                    province         = province,
                    zip_code         = zip_code,
                    country          = country,
                )  
                default_address.save()
            
              
            billing = form.save(commit=False)
            billing.customer_profile = customer_profile            
            billing.save()            
           
            return redirect('address:shipping')       
        
    except ObjectDoesNotExist:
        pass
        
    context = {
        'form': form,
        'default_address': default_address,
    }
    return render(request, 'pages/billing_address.html',context)

@login_required
def shipping_address(request):
    form = ShippingAddressForm(request.POST or None)
    try:
        customer_profile = get_object_or_404(CustomerProfile, user=request.user)
        
        if form.is_valid():           
            house_number             = form.cleaned_data.get('house_number')
            street                   = form.cleaned_data.get('street')
            barangay                 = form.cleaned_data.get('barangay')
            city                     = form.cleaned_data.get('city')
            province                 = form.cleaned_data.get('province')
            zip_code                 = form.cleaned_data.get('zip_code')
            country                  = form.cleaned_data.get('country')                      
           
            shipping = form.save(commit=False)
            shipping.customer_profile = customer_profile
            shipping.save()
            return redirect('checkout')
           
    except ObjectDoesNotExist:
        pass
        
    context = {
        'form': form,    
    }
    return render(request, 'pages/shipping_address.html', context)
