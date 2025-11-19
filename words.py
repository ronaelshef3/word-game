# # Write your python code here:
# word = input("Please enter a string:")
# w = word[0]
# if len(word) < 1:
#     pass
# else:
#     word2 = word[1:]
#     word2=word2.replace(w,'e')
#
#     print(w+word2)
# Write your python code here:
word = input('enter word ')
l = (len (word)//2)

first= word [0:l]
end= word[l:]
first = first.lower()
end = end.upper()
print (first+end)