choice = input("Hi there! Do you want to encrypt or decrypt ? (1: encrypt / 2 : decrypt)\n")
#message = "this is an unencrypted message" "qefp fp xk rkbkzovmqba jbppxdb"
message = input("enter your message : \n") or "this is an unencrypted message"
message_list = list(message)
abc_str = 'abcdefghijklmnopqrstuvwxyz'
abc_list = list(abc_str)


# ******* ENCRYPTION ********
if choice == "1":

  str1 = ""
  for j in range(len(abc_str)):
    for i in range(len(message)):
      if message[i] == abc_str[j]:
       message_list[i] = abc_list[j-3]

  print(str1.join(message_list))


#********* DECRYPTION *********

else:
  
  str1 = ""

  for j in range(len(abc_str)):
    for i in range(len(message)):
      if message[i] == abc_str[j]:
        diff = len(abc_str)-j
        if diff <= 3:
         message_list[i] = abc_list[abs(3)-diff]
        else:
         message_list[i] = abc_list[j+3]
      
  print(str1.join(message_list))