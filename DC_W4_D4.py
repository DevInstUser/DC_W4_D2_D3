matrix = [

['7','','3'],
['T','s','i'],
['h','%','x'],
['i','','#'],
['s','M',''],
['$','a',''],
['#','t','%'],
['i','r','!']

]
special_char = """!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""
sp_char_list = list(special_char)
print(sp_char_list)



mat_list_tuple = list(zip(*matrix))
mat_list = [list(ele) for ele in mat_list_tuple]

print(mat_list)

v=['%']
for i in range(len(mat_list)):
  v+= mat_list[i][1:]
v.pop(0)


for a in range(len(v)):
  for b in v:
    if b in sp_char_list:
      v.remove(b)

str=" "
print(str.join(v))