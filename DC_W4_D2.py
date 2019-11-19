
#input("What is your birthdate (in format : DD/MM/YYYY) ? : ")


str_today = input("Today date is (in format : DD/MM/YYYY) ? : ")#"18/11/2019"

l = list(str_today)
l.remove(l[2])
l.remove(l[4])

l2 = [l[0]+l[1],l[2]+l[3],l[4]+l[5]+l[6]+l[7]]
str_today = l2


str_birth = input("What is your birthdate (in format : DD/MM/YYYY) ? : ") #"21/04/1980"

l3 = list(str_birth)
l3.remove(l3[2])
l3.remove(l3[4])


l4 = [l3[0]+l3[1],l3[2]+l3[3],l3[4]+l3[5]+l3[6]+l3[7]]
str_birth = l4

age = int(str_today[2]) - int(str_birth[2]) + (int(str_today[1]) - int(str_birth[1]))/12 + int((int(str_today[0]) - int(str_birth[0]))/365)
int_age = int(age)

l = list(str(int_age))
nb_candles = l[len(l)-1]

i_cake = 'i' * nb_candles
space = " "
cake_str = space*4 + """__""" + i_cake + """__\n""" + space*3 +"" 
cake_str+= """|:H:a:p:p:y:|\n""" + space*1 +""
cake_str+= """__|___________|__ \n""" + space*0 +"" 
cake_str+= """|^^^^^^^^^^^^^^^^^|\n""" + space*0 +""
cake_str+= """|: B:i:r:t:h:d:a:y| \n""" +""
cake_str+= space*0 + """~~~~~~~~~~~~~~~~~~~"""

print(cake_str)