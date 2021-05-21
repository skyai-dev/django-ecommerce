# importing django classes and methods
from django.shortcuts import render
from django.views import View
from django.core.mail import send_mail

# importing our data models
from website.models.customer import Customer
from website.models.mail import Mail

class Contact(View):
    def get(self,request):
        return render(request,'contact.html',{})
    
    def post(self, request):
        message_name = request.POST['name']
        message_email = request.POST['email']
        message = request.POST['message']
        customer=request.session.get('customer')

        print("Customer: ", customer)
        if customer == None:
            return render(request, 'contact.html',{'error':"Please Login to Send Message"})

        mail = Mail(customer=Customer(id=customer),
                          name=message_name,
                          email=message_email,
                          message=message      
                    )
        mail.saveMail()

        # send a email
        send_mail(
            message_name,  # subject
            message,  # message
            message_email,  # from email
            ['nandurty17@gmail.com', 'narendrarty17@gmail.com'],  # to email
        )

        return render(request, 'contact.html',{'message_name':message_name})