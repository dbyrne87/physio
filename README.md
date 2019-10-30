# Code Institute Milestone Project — 4
## [Physio](https://candkphysio.herokuapp.com/)
![Screenshot of website homepage](https://candkphysio.s3-eu-west-1.amazonaws.com/media/images/homepage.jpg)
A website designed to allow users to easily browse the appointments available and book a time that suits them should they wish, the business owner benefits by allowing the public book appointments 24hrs a day without the need of answering the phone or replying to emails freeing up time to offer more appointment slots. 

This website can be used for,
1.  By the customer to view each type service on offer.
2.  By the customer to find out the benefits of each service and what is involved
3.  By the customer to find what times are available for each service
4.  Allow the customer to pay for the service upfront. Avoiding having the business to always have change available and the customer to remember to bring cash with them on each visit. 
5.  Get email reminders to confirm and remind both the business and customer/s involved about the service day and time to help avoid people not showing to the appointment. 
***
### User Stories

— I have a bad back / muscle pain / tightness where is there a local physiotherapy clinic to help me?
— I would love to do Pilates classes I would like to find out who does them locally to me?
— I am in heavy training for an upcoming event and need to recover as fast as possible, I wonder could I rent a session for recovery boots.  
— It's late in the evening and I want to book an appointment, nowhere is open now can I book online? 
— I am finished work tomorrow early I wonder could I get a physio session at 4pm tomorrow.
— I never remember to have cash on me I wonder could I pay for the session using my card?
***
## UX

Firstly a set of wire frame diagrams where made to show the layout of the website on different screen sizes and was also used to iron out any potential issues that arose before coding the website.[Link To Wire frame](https://www.lucidchart.com/invitations/accept/6ad16a41-9497-447f-bf89-9483427c5df7)

The websites layout is designed as simply and as user-friendly as possible while allowing the user to easily navigate through the website to find, view and book a range of services, the user can easily find the service they would like to find through a carousel or individual product cards. 

Using Bootstrap and CSS, depending on the users screen size, content is modified or removed to make all the content easily read and interacted with no matter of what device is being used.

The colour scheme throughout the website compliments the professional look and feel the business is trying to portray and does not interfere with the usability or readability of the site. 
Information easily available to the user and is not overwhelming or hard to follow as the user makes their way through the site. 

As the user interacts with the website they are informed using messages or success pages that the process was successful or why it wasn't.
***
## Features
![Website Home Page](https://candkphysio.s3-eu-west-1.amazonaws.com/media/images/homepage.jpg)

The main goal of the homepage / products page of the site is to show the user what services are available and gives them a professional look and feel that fits into what the business is trying to portray. The carousel scrolls through each one of the 3 services available, these include a professional looking image and some short text to promote the service and business.
Under the carousel are bootstrap cards which have a short message to give the user some basic information about the service. 
Both the Carousel and Cards have buttons that bring the user to find out more about the service and allows them to book it. 

The Navbar & Footer is kept the same throughout the site. If the user is logged in then a "Log Out" button is shown, otherwise a "Log In" link is shown. 
A User must be logged in to proceed to the checkout page, if they are not, and they click they are brought to the Login/ Sign Up page.
Any User is allowed in the Contact Us page but must add an email address to be allowed to send a message. 
Social media links in the Navbar allows all users, to see the websites social media accounts and keep up to date on new features, promoted places etc. *no social media accounts are setup for this website at present and are for display only.

![Log In Page](https://candkphysio.s3-eu-west-1.amazonaws.com/media/images/log-in-page.jpg)
The page is broken down into 2 sections,
1)The Login section allows already registered users to sign in using their Username/Email Address and password, if the user was attempting to book an appointment then it will redirect them to the checkout page otherwise it will bring them to the products page. On submitting the details it is checked against what's in the database and if it matches the user is logged in. If the username or password is incorrect the site returns a message explaining why the process was not successful.
![Register Page](https://candkphysio.s3-eu-west-1.amazonaws.com/media/images/register-page.jpg)
2)The Register section is just a button that brings the user to the Register Page and allows the user to add their details. The fields to fill out are kept to a minimum to make sure the user does not feel overwhelmed.

![Forgot Password Page](https://candkphysio.s3-eu-west-1.amazonaws.com/media/images/forgot-password.jpg)
The forgot password page is a simple one field form that allows the user to reset their password should they have forgotten it. When clicking the button the user will receive a message to check their email that has been sent, they can then use this to reset their password using a link. 

![About Us Page](https://candkphysio.s3-eu-west-1.amazonaws.com/media/images/about-us-page.jpg)
This page gives the user a brief description of the business owners, their background and experience (* using Lorem ipsum for now)
The remainder of the page explains what services the business provide in detail. This is section is built using the Django flat page application, one of the main benefits of using this is that it allows the business owners update this section in the backend without having to go into the html code.

![Contact Us Page](https://candkphysio.s3-eu-west-1.amazonaws.com/media/images/contact-us.jpg)
Any User is allowed in the Contact Us page but must add an email address to be able to send a message to the business. Both the User and the Business receive a copy of the email. 

![Cart Page](https://candkphysio.s3-eu-west-1.amazonaws.com/media/images/cart-page.jpg)
If a user interacts with a button in the carousel or card in the homepage they will be brought to the cart page which provides a more detailed description about the session and a button to book the appointment. 

![Checkout Page Upper](https://candkphysio.s3-eu-west-1.amazonaws.com/media/images/checkout-page-one.jpg)
The Checkout Page is broken into 3 sections,
1) The heading just displays the title and cost of the session the user has chosen, this is mainly here to confirm what they are booking and how much the session will cost them.
2) The Book a Date & Time section gives the user the available date and times that they can book, this is taken from a list of events in Google calendar. Each appointment type has a different calendar in the business. When clicked a tick appears on the button chosen to confirm this has been picked. When a session in an individual appointment has been booked it will no longer appear in this list of buttons. Group sessions will always give the available appointment buttons, for every booking the user is added to the list of guests in the google calendar giving the business owners a list of how many bookings they have for that session.
![Checkout Page Lower](https://candkphysio.s3-eu-west-1.amazonaws.com/media/images/checkout-page-two.jpg)
3)The third section is taking the customers details and card details, all fields must be filled in to process the booking and messages are provided should they not fill out something properly. The address fields are not necessarily needed for the booking but could be used in the future for promotional material and to give the business an idea of where their customers are coming from which would help with focusing google ads etc. 

![Booking Confirmation Google](https://candkphysio.s3-eu-west-1.amazonaws.com/media/images/booking-confirmation-google.jpg)
When the Booking is made the event in Google Calendar is updated and both the business owner and customer is emailed to confirm. A single guest or multiple guests (if it's a group booking) can be emailed from here if the appointment time changes etc. 

***
## Future Development
To develop the website even further given more time I would,

 — Limit the amount of bookings for a group booking.
 
 — Use the Cronofy Api further to allow both the User and Business update, modify and delete bookings from the site and not having to go to their calendar, Or use a paid Calendly account and embed its features to the site. 
 
 — Use the cronofy built in booking module to make the checkout page a bit more elegant,, Or use a paid Calendly account and embed its features to the site.  (https://docs.cronofy.com/developers/ui-elements/slot-picker/#element-permissions)
 
 — When the user is signing up to the site get their address details and then populate this data into the checkout page to avoid the user entering their details on every booking. 
 
 — Use something like Twilio to contact/remind customers about their appointments to keep 'no shows' to a minimum.
***
## Technologies Used
HTML5 & CSS3
Used for displaying the content and layout.

[Bootstrap](https://getbootstrap.com/)
Used to make the website clean and responsive.
Also used its built in features such as Carousel and Alert fields.

[jQuery](http://code.jquery.com/)
Required for the Stripe and some features in the checkout and success page.

[Python](https://www.python.org/)
Was used to write the logic of the site with the help of the Django framework

[LucidChart](https://www.lucidchart.com/pages/home)
To Develop the Wire frames 

[Font Awesome](https://fontawesome.com/)
To provide icons for the social media links, Website icon and button and tab icons.
 
[Google Fonts](https://fonts.google.com/)
The website uses the "Singlet" font throughout.  
 
[Django](https://www.djangoproject.com/) v1.11
The project was built from this framework.  

[Sqlite](https://www.sqlite.org/index.html) 
Used for development of the site locally

[PostgreSQL](https://www.postgresql.org/)
Used in Heroku as the finished sites database.  

[Heroku](https://www.heroku.com/)
Used to host the finished website and can be viewed by the public

[Git/Github](https://github.com)
Used for version control when site is in development and currently used by Heroku to make sure it has the latest version of the project.

[Stripe](https://stripe.com)
Used for the payment functionality in the site. Currently, in Developer mode.
***
## Testing
As the website was being built I used the built in features of [Cloud9](https://aws.amazon.com/cloud9/) and Google Chrome's built in developer tools. 

After each section was developed I,
1. Made sure the content was responsive and laid out correctly as per the original wire frame on desktop, tablet and mobile devices using the Chrome developer tools.
2. Made sure the code layout is correctly indented so it can be easily read. 
3. I used the [W3C Validator](https://validator.w3.org/), to make sure both the HTML and CSS was up to current standards and best practice. 
4. Check that data was displaying and updating correctly as I would expect.
***
### User scenarios:

 1. Land on a page,

	Do you know what the website is for.
	   Is the page clear and user-friendly. 
	   Do you know what to do to find what you are looking for easily?
		
 2. Products,
 
	 Are the Titles, Short/Long Descriptions easy to understand.
        Is the layout of the page what you would typically expect?
        Did you feel you had enough information?
        Was the pricing clear and easily found?
	 
 4. Checkout/ Booking Page
 
	 Was it what you expected?
        Was the page hard to understand follow or read?
        Did you have all the information you needed to make a booking?


— I tested the website on Chrome, Microsoft Edge and Firefox. I haven't found any issues so far.
***
### Real User Testing

When I felt the website was finished,
I asked friends and family to use the website and to give me feedback on issues they found or suggestions they had.

Some mentioned that the carousel buttons didn't work and where causing the website to crash, after investigating I realised that Heroku treated the products slightly different and this needed to be updated to point to the correct product, this issue was also the same for the Time/Date buttons which in Heroku was showing the same calendar for all appointment types. This was fixed by updating the python code to point to the correct calendar ID depending on what appointment was chosen. 

A recommendation was to add a footer to the site with contact, address details etc. as this information wasn't currently on the site. 
***
### Bugs

Family members, Friends or myself cannot find any bugs currently causing issues in the site. 
***
## Deployment

This project is deployed on Heroku: https://candkphysio.herokuapp.com/

Static files are currently hosted in AWS from an S3 Bucket

Firstly setup your Google Calender with the following,
![Add Calendars](https://candkphysio.s3-eu-west-1.amazonaws.com/media/images/add-calender.jpg)
1) Setup the sub-calendars, from your own calendar on the left side click the + button and "Create New Calendar" and setup each sub-calendar as required.
![Boots Appointments Setup](https://candkphysio.s3-eu-west-1.amazonaws.com/media/images/boots-appointment-setup.jpg)
![Physio Appointments Setup](https://candkphysio.s3-eu-west-1.amazonaws.com/media/images/physio-appointment-setup.jpg)
![Pilates Appointments Setup](https://candkphysio.s3-eu-west-1.amazonaws.com/media/images/pilates-appointment-setup.jpg)
![Appointments Setup](https://candkphysio.s3-eu-west-1.amazonaws.com/media/images/appointments-setup.jpg)
2)Using the "Create" button in Google Calendar you can now setup appointments, see the above images for reference. Only the Title, Day & Time and Sub-Calendar are required. Everything else is updated when a customer makes a booking. **If you want the appointments to repeat on certain days etc. you can update the "Does not Repeat" option see the Pilates Image for reference. 
***
##### Local Deployment
To run this application locally, 

Clone this GitHub repository by either clicking the green Clone or download button and downloading the project as a zip-file, or by entering the following into the Git CLI terminal: — git clone https://github.com/dbyrne87/physio.git

After adding the files to your preferred editor, make sure you are working in the correct folder in TERMINAL this can be done by (cd . Or cd)

Do a search and remove all '#' before import env in the projects files. 
In the physio model settings.py file, '#' out import dj_database_url (line 12) and DATABASES = {'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))} (line 96) while removing '#' on lines 89-94

Create a.env file containing the following environmental variables (This will need to be updated with your own credentials and passwords):
#############################################################################
import os 

os.environ.setdefault("STRIPE_PUBLISHABLE", 'STRIPE PUBLISHABLE KEY HERE')
os.environ.setdefault("STRIPE_SECRET", 'STRIPE Secret KEY HERE')
os.environ.setdefault("C9_HOSTNAME", 'CLOUD9 HOSTNAME (MAY NOT BE NEEDED)')
os.environ.setdefault("SECRET_KEY",'ENVIRONMENT SECRET KEY HERE')

os.environ.setdefault("EMAIL_HOST", 'SUCH AS 'smtp.gmail.com')
os.environ.setdefault("EMAIL_HOST_USER", 'EMAIL TO USE')
os.environ.setdefault("EMAIL_HOST_PASSWORD", 'SPECIAL KEY NOT YOUR USUAL PASSWORD')

os.environ.setdefault("PYCRONOFY_TOKEN", 'CRONOFY TOKEN')

os.environ.setdefault("AWS_SECRET_KEY_ID", 'AWS TOKEN')
os.environ.setdefault("AWS_SECRET_ACCESS_KEY", 'AWS TOKEN')

os.environ.setdefault("DATABASE_URL", 'URL TAKEN FROM HEROKU SETTINGS')

#############################################################################
You must create accounts with both Stripe and Amazon S3.

Install all requirements from the requirements.txt file: sudo -H pip3 -r requirements.txt.
At the terminal prompt, type python manage.py run server. Django should now start running locally.
Type the following commands into the terminal to create the database: 
python manage.py makemigrations 
and 
python manage.py migrate.
To have access to Django Admin Panel, you must generate a superuser: 
python manage.py createsuperuser.
***
##### Remote Deployment
In order to implement this project on Heroku, the following must be completed:

Create a requirements.txt file: pip3 freeze --local > requirements.txt.

Create a Procfile to tell Heroku what type of application is being deployed using gunicorn, and how to run it: 
web: gunicorn ecommerce.SGI:application.

Do a search and add a '#' before all import env in the projects files. 
In the physio model settings.py file, remove the '#' on import dj_database_url (line 12) and DATABASES = {'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))} (line 96) while adding '#' on lines 89-94

Sign up for or log into your Heroku account, create your project app, and click the 
Deploy tab. Select Connect GitHub as the Deployment Method, and select Enable Automatic Deployment.
In the Heroku Settings tab, click on the Reveal Con fig Vars button to configure environmental variables as in the local deployment above (You will need to copy/paste all of the.env key value pairs into the con fig variables and add the SECRET_KEY).
In the Resources tab, go to the Add-ons section and add the Heroku Postgres add-on. Choose the Hobby level when prompted. This will give you a remote database to use for your project. The database URI will be located in the Con fig Vars in the Settings tab.

The app will now be deployed and built by Heroku and will be ready to run.

Re-build the migrations and create a superuser to your new remote database using:
python manage.py makemigrations.
python manage.py migrate.
python manage.py createsuperuser.

To host your static files and media files you can sign up for a free AWS account and proceed to the S3 section. From the S3 buckets section, you'll need to create a new unique bucket.
After creating your AWS S3 Bucket, you should now be able to push the static files to AWS using this command: 
python manage.py collectstatic.
Sign up for a free Stripe account. Navigate to the Developers section, and click on API Keys. You should have two confidential keys, (Publishable Key and Secret Key) which need to be added to your.env file, as well as your Heroku config vars.

Your project should be completely setup and ready for remote deployment!
***
## Credits
Pretty Printed for a helpful video setting up email in Django
(https://www.youtube.com/watch?v=X7DWErkNVJs)

Django documentation to help with explaining
Flat pages and other smaller issues I had in developing the site
(https://docs.djangoproject.com/en/1.11/ref/contrib/flatpages/)

Stack overflow for helping with 
Explaining the Try Else Statements
(https://stackoverflow.com/questions/19522990/python-catch-exception-and-continue-try-block)
as well as some smaller issues I had

Cronofy for their Google Calendar Integration Api and easy to follow documentation
(https://www.cronofy.com/)
***
### Acknowledgments

Used W3C to check my HTML and CSS is correct and up to standard.
[W3C Validator](https://validator.w3.org/)

W3schools for refreshing my knowledge on simple coding challenges I faced that I haven't used in a while. 
https://www.w3schools.com/