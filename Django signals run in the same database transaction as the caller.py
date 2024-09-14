from django.db import transaction
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist

# Signal receiver function
@receiver(post_save, sender=User)
def signal_receiver(sender, instance, **kwargs):
    try:
        # Trying to query the user created in the same transaction
        user = User.objects.get(username="testuser")
        print(f"Signal receiver can access the user: {user.username}")
    except ObjectDoesNotExist:
        print("Signal receiver cannot access the user (transaction not committed yet)")

# Simulating the main code where a user is saved inside a transaction
def create_user():
    with transaction.atomic():  # Begin transaction
        print("Transaction started, creating user...")
        user = User.objects.create(username="testuser")  # This will trigger the post_save signal
        print("User created but transaction not yet committed.")
        # Transaction is still open here, signal should have access if it's in the same transaction

# Call the function to create the user inside a transaction
create_user()
