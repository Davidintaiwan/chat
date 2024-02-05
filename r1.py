
# 讀取檔案
def read_file(filename):
	lines = []
	with open(filename, 'r',encoding='utf-8-sig') as f:
		for line in f:
			lines.append(line.strip())
	return lines


def convert(lines):
	new = []
	person = None
	for line in lines:
		if line == 'Allen':
			person = 'Allen'
			continue
		elif line == 'Tom':
			person = 'Tom'
			continue
		if person:
			new.append(person + ': ' + line)
	return new
def write_file(filename, lines):
	with open(filename,'w', encoding='utf-8-sig') as f:
		for line in lines:
			f.write(line +  '\n')

def main():
	filename = 'input.txt'
	lines = read_file(filename)
	lines = convert(lines)
	write_file('output.txt', lines)


main()






# 修改檔案

#def convert(filename, lines):
#	lines = []
#	with open(filename, 'w', encoding='utf-8-sig') as f:
#		for line in lines:
#			if 'Allen' in line:   # 只剩下對話
#				continue # 繼續
#			else:
#				f.write('Allen'+ ':' + line + '\n')
#			if 'Tom' in line:
#				continue
#			else:
#				f.write('Tom' + ':' + line +'\n')
#	return lines
