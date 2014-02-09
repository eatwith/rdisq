redisq
======

Super minimal framework for working with redis worker/consumer queues for distributed apps.


examples
==========
Please see the examples dir


Quick but full start
==========
# Install redis (apt-get install redis, or yum, or... well... you get it :)
# Install redis python module 
# Install this module
# Write a simple worker (worker.py)
```
from rdisq.config import SimpleRedisConfig
from rdisq import Rdisq

class MyWorker(Rdisq):
    # Notice, all the exported workload methods are prefixed with q_
    q_do_work(self, param1, param2, param3=None):
        # Just return a simple dict, but technically we can do w/e we like here
        data = {
            "first": param1,
            "second": param2,
            "key_arg": param3,
            }
        return data

# We can instantiate our worker right away
queue_config = SimpleQueueConfig("my_queue_prefix")
worker = MyWorker(queue_config)

# Since this is an example, lets also start the blocking processing loop here
if __name__ == '__main__':
    worker.process() # Blocking loop
    
```
# Write a simple consumer that can use this worker
```
from worker import worker # notice we imported the instance, not the class

# NOTICE: we omitted the 'q_' prefix of the method
print worker.do_work("p1", "sasfas", param3="a")  # prints '''{"first":"p1", "seconds":"sasfas", "key_arg":"a"}'''

# We can also call the async one and get a callback object
response = worker.async_do_work("p1", "sasfas") # returns a Response object
print response.wait() # blocks until a response (or a timeout), prints '''{"first":"p1", "seconds":"sasfas", "key_args":None}'''

```
