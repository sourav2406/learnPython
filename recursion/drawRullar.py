def draw_line(tick_length,tick_lable=''):
	line = '-'*tick_length
	if tick_lable:
		line+=' '+tick_lable
	print(line)

def draw_interval(center_length):
	if center_length>0:
		draw_interval(center_length-1)
		draw_line(center_length)
		draw_interval(center_length-1)

def draw_ruller(num_inch,major_length):
	draw_line(major_length,'0')
	for j in range(1,1+num_inch):
		draw_interval(major_length-1)
		draw_line(major_length,str(j))

if __name__ == '__main__':
	num_inch = int(input("Enter number of inch: "))
	major_length = int(input("Enter major length: "))
	draw_ruller(num_inch,major_length)