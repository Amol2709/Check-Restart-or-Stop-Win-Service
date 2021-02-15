



from datetime import date
from datetime import datetime
import os

class Log:
	def __init__(self,msg):
		self.msg = msg
		out_file = open(os.getcwd()+"\\logs.txt","a")
		today = date.today()
		d2 = today.strftime("%B %d,%Y")
		now = datetime.now()
		current_time = now.strftime("%H:%M:%S")
		out_file.write("\n")
		out_file.write(self.msg+" on {} at {} ".format(d2,current_time))
		out_file.write("\n")
		out_file.close()