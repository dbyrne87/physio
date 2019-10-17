from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import MakePaymentForm, OrderForm
from .models import OrderLineItem
from django.conf import settings
from django.utils import timezone
from products.models import Product
from datetime import datetime, timedelta
import stripe, pycronofy, os, env, json


# Create your views here.

stripe.api_key = settings.STRIPE_SECRET

@login_required()
def checkout(request):
    
    ###List Current Calendars, needed if adding further products to the range at a later date####
    #cronofy = pycronofy.Client(access_token= os.getenv("PYCRONOFY_TOKEN"))
    #calendars = cronofy.list_calendars()
    #data = (calendars)
    #print(data)
    
    ##if submitting form##
    if request.method=="POST":
        order_form = OrderForm(request.POST)
        payment_form = MakePaymentForm(request.POST)
        
        ## if the form is valid ##
        if order_form.is_valid() and payment_form.is_valid():
            order = order_form.save(commit=False)
            order.date = timezone.now()
            order.save()
            
            # get what items in the cart#
            cart = request.session.get('cart', {})
            total = 0
            for id, quantity in cart.items():
                product = get_object_or_404(Product, pk=id)
                total += quantity * product.price
                order_line_item = OrderLineItem(
                    order = order, 
                    product = product, 
                    quantity = quantity
                    )
                order_line_item.save()
                
            ## try charge the card given ##
            try:
                customer = stripe.Charge.create(
                    amount = int(total * 100),
                    currency = "EUR",
                    description = request.user.email,
                    card = payment_form.cleaned_data['stripe_id'],
                )
            
            # if the card wasn't accepted then give error #    
            except stripe.error.CardError:
                messages.error(request, "Your card was declined!")
            
            # if the payment is succesful #    
            if customer.paid:
                what_button = request.POST.get('what-button') # get the value of 'what_button' was clicked #
                b = "{},'" # remove these characters from the string #
                for char in b:
                    what_button = what_button.replace(char,"") #And replace with nothing#
                refine_what_button = what_button.split(' ') # split the string at each space into a list # 
                
                cronofy = pycronofy.Client(access_token= os.getenv("PYCRONOFY_TOKEN")) # call the cronofy api # 
                
                event = { # with these details #
                'event_uid': refine_what_button[3], # update this event id  #
                'summary': "Your Booking with C&K Physio",# update the origional summary with this  #
                'description': "email:  " + request.user.email + "  Username:  " + request.user.first_name + " " + request.user.last_name + "  Phone: " + request.POST.get('phone_number'), # The persons details #
                'start': refine_what_button[10], # appointment start date and time #
                'end': refine_what_button[12], # appointment end date and time #
                'tzid': 'Europe/Dublin', # what time zone to use #
                'location': {
                    'description': "18 Berkeley St, Phibsborough, Dublin 7, D07 TK76", # The address of the appointment #
                },  #  #
                "attendees": {
                    "invite": [
                      {
                        "email": request.user.email, # sends the user an email that they can use to accept the invitiation/get reminders #
                        "display_name": "Your Booking with C&K Physio"
                      }
                    ],
                },    
                 "reminders": [ # sets the reminders to 15min, 60min, and 1 day prior to the appointment #
                    { "minutes": 60 },
                    { "minutes": 1440 },
                    { "minutes": 15 }
                  ]
                }
                
                
                # This is used for the Pilates appointments to take multiple bookings for the one appointment slot #
                event_2 = {
                'event_uid': refine_what_button[3], # update this event id  #
                'summary': "Your Pilates Class Booking with C&K Physio", # update the origional summary with this  #
                'description': "A Booking has been made",
                'start': refine_what_button[19],# appointment start date and time #
                'end': refine_what_button[21],# appointment end date and time #
                'tzid': 'Europe/Dublin', # what time zone to use #
                'location': {
                    'description': "Twilfit House, Jervis St, North City, Dublin 1, D01 R2P0", 
                },
                "attendees": {
                    "invite": [
                      {
                        "email": request.user.email, # sends the user an email that they can use to accept the invitiation/get reminders #
                        "display_name": "Your Booking with C&K Physio"
                      }
                    ],
                },    
                 "reminders": [ # sets the reminders to 15min, 60min, and 1 day prior to the appointment #
                    { "minutes": 60 },
                    { "minutes": 1440 },
                    { "minutes": 15 }
                  ]
                }
                try:
                    cronofy.upsert_event(calendar_id = refine_what_button[1], event=event) # Try to update the google calendar through cronofy using event #
                    request.session['cart'] = {} # Reset cart back to 0 #
                    return render(request, 'success.html') # Render the success page if succesful #
                except:
                    cronofy.upsert_event(calendar_id = refine_what_button[1], event=event_2) # If the event attempt doesn't work then use event_2 #
                    request.session['cart'] = {} # Reset cart back to 0 #
                    return render(request, 'success.html')  # Render the success page if succesful #  
            else:
                messages.error(request, "Unable to take payment")
        else:
            print(payment_form.errors)
            messages.error(request, "We were unable to take a payment with that card!")
    else:
        user_details = {'full_name': request.user.first_name + " " + request.user.last_name}
        payment_form = MakePaymentForm()
        order_form = OrderForm(user_details)
    
    cart = request.session.get('cart', {})
    what_calendar = []
    if '1' in cart:
        what_calendar = ['cal_XYjaVHVZYgBgrZFs_HEpo3dw86uG4SHGyFZb0lA']
    elif '2' in cart:
        what_calendar = ['cal_XYjaVHVZYgBgrZFs_dUC2DLLCz8SKCrL07bzZmg']
    elif '3' in cart:    
        what_calendar = ['cal_XYjaVHVZYgBgrZFs_dzk27HOsMzv32vRQOsmyaQ']    
    get_date = datetime.now() + timedelta(days=1)
    start_date = datetime.strftime(get_date, '%Y-%m-%dT%H:%M:%SZ')
    future_date = datetime.now() + timedelta(days=20)
    end_date = datetime.strftime(future_date, '%Y-%m-%dT%H:%M:%SZ')
    cronofy = pycronofy.Client(access_token= os.getenv("PYCRONOFY_TOKEN"))
    events = cronofy.read_events(
    calendar_ids = what_calendar,    
    from_date = start_date,
    to_date = end_date,
    tzid='Europe/Dublin')
    refine_data = (events.json())
    return render(request, "checkout.html", {'order_form': order_form, 'payment_form': payment_form, 'publishable': settings.STRIPE_PUBLISHABLE, 'data': refine_data})
    
    
    
    