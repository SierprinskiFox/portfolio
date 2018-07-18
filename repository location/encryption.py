"""
Sample Python/Pygame Programs
Simpson College Computer Science
http://programarcadegames.com/
http://simpson.edu/computer-science/
Explanation video: http://youtu.be/sxFIxD8Gd3A
"""
#pylint: disable=redefined-builtin

def printme(str):
    "This prints a passed string into this function"
    print str
    return

PLAIN_TEXT = "This is a test. ABC abc"

ENCRYPTED_TEXT = ""
for c in PLAIN_TEXT:
    x = ord(c)
    x = x + 1
    c2 = chr(x)
    ENCRYPTED_TEXT = ENCRYPTED_TEXT + c2
print ENCRYPTED_TEXT
