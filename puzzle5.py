def test(str1):
    return str1[len(str1)-2] in str1[len(str1)-1] and str1[len(str1)-2]!=str[len(str1)-1]
str=["a","abb","sfs","00","de","sfde"]
print("original list")
print(str)
print("check the nth-1 string is a proper substring of nth string of the said list of string s")
print(test(str))