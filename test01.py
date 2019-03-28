# class test():
# 	pass
#
# print(test() == test())
# print(id(test())== id(test()))

# import threading
#
# sum = 0
# # loopSum = 200000
# loopSum = 3
#
# def myAdd():
# 	global sum, loopSum
# 	for i in range(1, loopSum):
# 		sum += 1
# 		print('InAdd: ', sum)
#
#
# def myMinu():
# 	global sum, loopSum
# 	for i in range(1, loopSum):
# 		sum -= 1
# 		print('InMinu: ', sum)
#
#
# if __name__ == '__main__':
# 	print("Starting ....{0}".format(sum))
#
# 	# 开始多线程的实例，看执行结果是否一样
# 	t1 = threading.Thread(target=myAdd, args=())
# 	t2 = threading.Thread(target=myMinu, args=())
#
# 	t1.start()
# 	t2.start()
#
# 	t1.join()
# 	t2.join()
#
# 	print("Done .... {0}".format(sum))


import os
from multiprocessing import Process


def run_proc(name):
	print('Child process %s (%s) running' %(name, os.getpid()))


if __name__ == '__main__':
	print('Parent Process %s' % os.getpid())
	for i in range(3):
		p = Process(target=run_proc, args=(str(i), ))
		print('Process will start')
		p.start()
	p.join()
	print('Process end.')
