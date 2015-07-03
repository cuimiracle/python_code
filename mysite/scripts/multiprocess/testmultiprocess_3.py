#!/usr/bin/env python
import multiprocessing, time, signal
p = multiprocessing.Process(target=time.sleep, args=(1000,))
print p, p.is_alive()

p.start()
print p, p.is_alive()
print p.pid
p.terminate()
time.sleep(0.1)
print p, p.is_alive()

print signal.SIGTERM

p.exitcode == -signal.SIGTERM