import sys

__author__ = "Colin"

f = open("some.txt", "r", encoding="utf-8")
f_new = open("some.txt.bak", "w", encoding="utf-8")

find_str = 'when'
replace_str = 'how'
for line in f:
    if find_str in line:
        line = line.replace(find_str, replace_str)
    f_new.write(line)
f.close()
f_new.close()