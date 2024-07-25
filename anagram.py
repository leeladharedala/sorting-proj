def anagram(str1,str2):
    count1 = {}
    count2 = {}
    for i in str1:
        if i in count1:
            count1[i] += 1
        else:
            count1[i] = 1
    for j in str2:
        if j in count2:
            count2[j] += 1
        else:
            count2[j] = 1
    print(str(count1))
    print(str(count2))

    if count1 == count2:
        return "Anagram"
    else:
        return "Not an Anagram"

print(anagram("triangle","integral"))
print(anagram("banana","apple"))