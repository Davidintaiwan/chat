
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
	allen_word_count = 0
	allen_sticker_count = 0
	allen_image_count = 0
	viki_word_count = 0
	viki_sticker_count = 0
	viki_image_count = 0
	for line in lines:
		s = line.split(' ')
		time = s[0]
		name = s[1]
		
		if name == 'Allen':
			if s[2] == '貼圖':
				allen_sticker_count += 1
			elif s[2] == '圖片':
				allen_image_count += 1

			else:
				for m in s[2:]:
					allen_word_count += len(m)
		elif name == 'Viki':
			if s[2] == '貼圖':
				viki_sticker_count += 1
			elif s[2] == '圖片':
				viki_image_count += 1
			else:
				for m in s[2:]:
					viki_word_count += len(m)

	print('Allen說了', allen_word_count, '個字')
	print('Allen傳了', allen_sticker_count, "個貼圖")
	print('Allen傳了', allen_image_count, "個圖片")
	print('Viki說了', viki_word_count, '個字')
	print('Viki傳了', viki_sticker_count, "個貼圖")
	print('vIKI傳了', viki_image_count, "個圖片")
		
	return new

 # 清單的切割 前三個 n[:3] , 中間 n[2:4] 包含開始不含結尾  , 結尾 n[-2:] 最後兩個 

def write_file(filename, lines):
	with open(filename,'w', encoding='utf-8-sig') as f:
		for line in lines:
			f.write(line +  '\n')

def main():
	filename = 'LINE-Viki.txt'
	lines = read_file(filename)
	lines = convert(lines)
	#   write_file('output.txt', lines)


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
