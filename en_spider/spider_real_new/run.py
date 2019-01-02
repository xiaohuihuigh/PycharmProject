import manage
from datetime import datetime
if __name__ == "__main__":
	spider = manage.Spider()
	print "{}: spider start running...".format(datetime.now())
	spider.run()
#	print "{}: spider stop.".format(datetime.now())
