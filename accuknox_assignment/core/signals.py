import threading
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Book, LogEntry

@receiver(post_save, sender=Book)
def log_book_creation(sender, instance, **kwargs):
    current_thread = threading.get_ident()
    print(f"[SIGNAL] Running in thread ID: {current_thread}")
    
    LogEntry.objects.create(
        message=f"Created book: {instance.title}",
        thread_id=current_thread
    )
    print("[SIGNAL] Log entry created.")
