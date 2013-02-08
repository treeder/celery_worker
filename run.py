import os
os.system("./__pips__/bin/celery -A mytasks worker --loglevel=info")
