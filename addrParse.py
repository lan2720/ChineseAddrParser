# coding:utf-8

import re

cities = {u'上海':None, u'上海市':None}

def cnParse(s):
	i, leftStr = longestMatching(s, cities)

	reStr = (u'(?P<province>[\u4e00-\u9fa5]+?(?:省|特别行政区|特区))'
			u'?(?P<city>[\u4e00-\u9fa5]+?(?:市|自治州|地区|盟))'
			u'?(?P<nearby>[\u4e00-\u9fa5]*?(?:近郊))'
			u'?(?P<county>[\u4e00-\u9fa5]+?(?:县))'
			u'?(?P<rural>[\u4e00-\u9fa5]+?(?:乡))'
			u'?(?P<district>[\u4e00-\u9fa5]+?(?:区))'
			u'?(?P<town>[\u4e00-\u9fa5]+?(?:街道|镇))'
			u'?(?P<village>[\u4e00-\u9fa5]+?(?:村|里|小区|社区))'
			u'?(?P<ip>[\u4e00-\u9fa5]+?(?:园区|工业区|高新区))'
			u'?(?P<road>[\u4e00-\u9fa5]+?(?:胡同|巷|路|公路|道|街))'
			u'?(?P<lane>[0-9]+?(?:弄))'
			u'?(?P<roadnum>[甲_乙_丙_0-9_-]+?(?:号))*')

	repat = re.compile(reStr)
	grouphehe = re.match(repat, leftStr)
	d = grouphehe.groupdict()
	if i != "":
		d['city'] = i
	else:
		d['city'] = None
	return d

def longestMatching(s, dictionary):
	"""
	str中从头开始逐个和字典中的词匹配，匹配到了就返回开头切割的词和剩余的str
	"""
	if isinstance(s, str):
		s = s.decode('utf-8')
	elif isinstance(s, unicode):
		pass
	else:
		raise ValueError("The argument must be string.",)

	maxIdx = 0
	maxLen = 0
	for key in cities.keys():
		if maxLen < len(key):
			maxLen = len(key)

	for i in range(maxLen+1):
		if s[:i] in cities:
			maxIdx = i
	return (s[:maxIdx], s[maxIdx:])

def main():
	s = u'上海近郊青浦区沪青平公路'
	d = cnParse(s)
	# Print result
	for key, value in d.items():
		if value != None:
			print key, value

if __name__ == '__main__':
	main()