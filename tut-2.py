str_1 = '    Demos Petsas   gioergjiorej   '
import re
str_2 = str_1.strip()
str_3 = re.sub(' +',' ',str_2)
print(str_3)
array_1 = str_3.split(' ')
# print(str_1)
# print(str_2)

print(array_1)