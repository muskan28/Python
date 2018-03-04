#Program to create a thread using the threading module

import threading
import time

class myThread(threading.Thread):  #create a sub class
	def __init__(self,name,count):
		threading.Thread.__init__(self)
		self.name = name
		self.count = count
	def run(self):
		print("\n Starting " + self.name)
		i=0
		while i<self.count:
			display(self.name,i)
			time.sleep(1)
			i=i+1
		print("\n Exiting " + self.name)
def display(threadName,i):
		print("\n", threadName,i)
		
#create new threads

thread1 = myThread("ONE", 5)
thread2 = myThread("TWO", 5)

#start new threads
thread1.start()
thread2.start()
thread1.join()
thread2.join()
print("\nExiting Main thread")		
	
