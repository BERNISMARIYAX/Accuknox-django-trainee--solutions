from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User

# Signal receiver function
@receiver(post_save, sender=User)
def signal_receiver(sender, instance, **kwargs):
    print("Signal receiver executed.")

# Simulating the main code where a user is saved
def create_user():
    print("Creating user...")
    user = User.objects.create(username="testuser")  # This will trigger the post_save signal
    print("User created.")

# Call the function to create the user
create_user()
