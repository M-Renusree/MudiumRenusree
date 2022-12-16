def test(str):
    return str[len(str)-2] in str[len(str)-1] and str[len(str)-2]!=str[len(str)-1]
str=["a","abb","sfs","00","de","sfde"]
print("original list")
print(str)
print("check the nth-1 string is a proper substring of nth string of the said list of string s")
print(test(str))