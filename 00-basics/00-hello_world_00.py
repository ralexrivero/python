#!/usr/bin/python3
# if invoked in console, first two bytes are read, if these bytes are ASCII #!
# the shell assumes that the files is to be executed by an interpreter
# and that the files's first line specifies wich interpreter use
# this is the shebang or shell execute
# too can be called in the form #!/usr/bin/env python3
# the first form is used for Python programs that will be executed in a web server
# the second look in the shell's current environment
print("Hello", "World!")