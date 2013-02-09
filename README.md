celery_worker
=============

1. Make an iron.json file with your Iron credentials.
1. Create new virtual env in this directory: `virtualenv -p python2 python2`
1. run `source python2/bin/activate`
1. run locally to test: `celery -A mytasks worker --loglevel=info`
1. open another shell and run `source python2/bin/activate`
1. run `python myqueue.py`, you should see the task run and print the results on both terminals.
1. Run `ctrl-c` to terminate the celery process (first terminal).
1. Now let's run it on IronWorker, so first upload it: `iron_worker upload mycelery`
1. Now run it: `iron_worker queue mycelery`
1. Now queue up a task again: `python myqueue.py`. You should get the same result in this terminal, but this time Celery
is running remotely on IronWorker!  Boom!
1. Finally, let's schedule the worker to run every hour so you always have one running : `iron_worker schedule --run-every 3600 mycelery`.
Run the schedule command again if you want multiple celeries running.

