def increment_string(strng):
    head = strng.rstrip('0123456789')
    tail = strng[len(head):]
    if tail == "": return strng+"1"
    print(head + str(int(tail) + 1).zfill(len(tail)))

if __name__=='__main__':
	increment_string("foo")
	increment_string("foobar001")
	increment_string("foobar1")
	increment_string("foobar00")
	increment_string("foobar99")
	increment_string("")
