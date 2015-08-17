import platform

if platform.python_version()[0] == "3":
    print("hello world")
elif platform.python_version()[0] == "2":
    print 'hello world'
