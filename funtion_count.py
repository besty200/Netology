def function_count(spisok, letter):
    count=0
    for word in spisok:
        if letter in word:
            count+=1
    return count

spisok = ['python', 'c++', 'c', 'scala', 'java']
print(function_count(spisok,'c'))