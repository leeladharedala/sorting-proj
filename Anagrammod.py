def string_to_char_list(s):
    lst = []
    for char in s:
        lst.append(char)
    return lst

def sort_char_list(lst):
    len_lst = len(lst)
    for i in range(len_lst):
        for j in range(i, len_lst):
            if lst[i] < lst[j]:
                temp = lst[i]
                lst[i] = lst[j]
                lst[j] = temp
    return lst

def char_list_to_string(lst):
    s = ""
    for char in lst:
        s += char
    return s

def anagram(str1, str2):
    lst1 = string_to_char_list(str1)
    lst2 = string_to_char_list(str2)

    lst1 = sort_char_list(lst1)
    lst2 = sort_char_list(lst2)

    srt1 = char_list_to_string(lst1)
    srt2 = char_list_to_string(lst2)

    # print(srt1)
    # print(srt2)

    if srt1 == srt2:
        return "Anagram"
    else:
        return "Not an Anagram"


