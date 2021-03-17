#predifined character set

from re import *
pattern='[ab]'   #either a or b
pattern='[a-z]'   #checking for lowercase alphabets
pattern='[A-Z]'   #" uppercase
pattern='[a-zA-Z]' #checking both lower&uppercase
pattern='[0-9]'   #checking for digits
pattern='[^0-9]' # ^ (except)

#predifined characters

pattern="\s"   # space
pattern="\d"   # 0-9 digits
pattern="\D"   # ^0-9 (except digits)
pattern="\w"   # all words (0-9,a-z,A-Z) including _
pattern="\W"   #spcl characters,excluding _

