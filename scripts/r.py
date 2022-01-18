# encoding: utf8

import re
import os
import os.path

t = r"https://zhuanlan.zhihu.com/p/\d*"

with open(u"软件架构设计.html", "r") as rfile:
	body = rfile.read()

s = set()

for m in re.finditer(t, body):
	link = m.string[m.start():m.end()]
	s.add(link.strip())

print "link amount", len(s)


done = set()

for name in os.listdir(u"软件架构设计"):
	with open(os.path.join(u"软件架构设计", name), "r") as rfile:
		for line in rfile:
			if " url: https://zhuanlan.zhihu.com" in line:
				link = line.split()[-1].strip()
				done.add(link)
				break
		else:
			raise "cannot find %s" % name

print "done amount", len(done)
for link in s:
	if link not in done:
		print "todo", link
