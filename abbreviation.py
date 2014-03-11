
def isAbbr(abbr, str):

	abbrLen = len(abbr)

	hashtable = {}
	for char in xrange(0,abbrLen,1):
		try:
			abbrCharPos = str.index(abbr[char])
			hashtable[char] = abbrCharPos
		except:
			return False

	if ((hashtable.values())==(sorted(hashtable.values()))):
		return True
	else:
		return False

def tests():
	print isAbbr("acl", "achal")
	print isAbbr("m", "ken")
	print isAbbr("bbe", "barbie")


if __name__ == '__main__':
	tests()