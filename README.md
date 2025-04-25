1. By default, Django signals are executed synchronously.
2. Django signals run in the same thread as the caller by default.
3. by default Django signals run in the same database transaction as the caller — especially for post_save, pre_save, etc.