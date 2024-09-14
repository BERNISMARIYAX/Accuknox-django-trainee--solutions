import threading
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User

# Signal receiver function
@receiver(post_save, sender=User)
def signal_receiver(sender, instance, **kwargs):
    print(f"Signal receiver is running in thread: {threading.current_thread().name}")

# Simulating the main code where a user is saved
def create_user():
    print(f"Main process is running in thread: {threading.current_thread().name}")
    user = User.objects.create(username="testuser")  # This will trigger the post_save signal

# Call the function to create the user
create_user()
