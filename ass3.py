import re 
def rem_vowel(string): 
    return (re.sub("[aeiouAEIOU]","",string))              
string =(input("enter the string"))
print(rem_vowel(string)) 
