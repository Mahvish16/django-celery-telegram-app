from celery import shared_task
import uuid
from django.core.mail import send_mail
from .models import EmailVerification,RegisterUser  

@shared_task
def SendEmail(user_id):
    user = RegisterUser.objects.get(id=user_id)
    if not user.email:
            print("No email found for user.")
            return
    token = uuid.uuid4()
    EmailVerification.objects.create(user=user, token=token)
    verification_url = f"http://localhost:8000/verify-email/{token}/"
    send_mail(
        "Verify your email",
        f"Please click on the link to verify your email: {verification_url}",
        'mahvish.ruhi@gmail.com',
        [user.email],
        fail_silently=False 
    )

    
