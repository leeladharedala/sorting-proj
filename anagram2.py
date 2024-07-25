def anagram(str1,str2):
    lst1 = []
    lst2 = []
    len1 = len(str1)
    len2 = len(str2)
    for i in range(0,len1):
        lst1.append(str1[i])
    for i in range(0,len2):
        lst2.append(str2[i])
    # print(lst1)
    # print(lst2)
    for i in range(0,len1):
        for j in range(i,len1):
            if lst1[i] < lst1[j]:
                temp = lst1[i]
                lst1[i] = lst1[j]
                lst1[j] = temp
    for i in range(0,len2):
        for j in range(i,len2):
            if lst2[i] < lst2[j]:
                temp = lst2[i]
                lst2[i] = lst2[j]
                lst2[j] = temp
    srt1 = ""
    srt2 = ""
    for i in range(0,len1):
        srt1 = srt1+lst1[i]
    for i in range(0,len2):
        srt2 = srt2+lst2[i]
    print(srt1)
    print(srt2)
    if(srt1 == srt2):
        return "Anagram"
    else:
        return "Not an Anagram"

print(anagram("triangle","integral"))
print("\n")
print(anagram("banana","apple"))