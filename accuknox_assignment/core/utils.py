import threading
from core.models import Book, LogEntry
from django.db import transaction
import time 

def check(): 
    print(f"[MAIN] Running in thread ID: {threading.get_ident()}")

    try:
        with transaction.atomic():
            Book.objects.create(title="Transactional Book")
            # raise Exception("Force rollback after signal!")
    except Exception as e:
        print("[MAIN] Exception occurred:", e)

    # Query the DB
    print("[MAIN] Books in DB:", Book.objects.count())
    print("[MAIN] Log entries in DB:", LogEntry.objects.count())

    # Show any thread IDs logged
    for log in LogEntry.objects.all():
        print(f"[LOG] Message: {log.message} | Thread ID: {log.thread_id}") 

    # to check sync, async time sleep here. 
    time.sleep(5) 
