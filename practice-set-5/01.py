'''
12/03/26
Write a program to create a dictionary of Hindi words with values as their English 
translation. Provide user with an option to look it up! 
'''
hindi_to_English = {
    "madad" : "help",
    "khush" : "happy",
    "billi" : "cat"
}

word = input("Enter the word to find: ")
print(hindi_to_English[word])