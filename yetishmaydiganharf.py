from  string import  ascii_lowercase


word = "abcdefgpqrstuvwxyz"
natija = ""
for i in ascii_lowercase:
    if word.islower():
        if  i not in word:
            natija+=i
    else:
            print("ERROR")



print(natija)