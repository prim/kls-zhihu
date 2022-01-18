# encoding: utf8

import os

def u(s):
	for encoding in ["utf8", "gbk", "gb2312"]:
		try:
			return s.decode(encoding);
		except:
			pass
	return unicode(s)

for old in os.listdir("."):
	old = u(old)
	new = old.replace(u"备份-2022-01-18-", "")
	new = new.replace(u"- 知乎", "")
	os.rename(old, new)
