#def revsrting(word):
#    if len(word) == 0 :  return ""
#    return revsrting(word[1:])+word[0]

#print(revsrting("Yesandu"))

def revers(number):
    if (number) == 0 : return 
    return revers(number[1:])+number[0]

print(revers(10223))