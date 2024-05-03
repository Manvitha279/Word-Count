def count_words(text):
  '''Function to count the number of words in a text'''
  if not text: #check if the input text is empty
    return 0
  words = text.split() #Split the text into words using whitespace as the delimiter
  return len(words) #Return the number of words in the text

#Prompt the user to enter a text or sentence 
user_input = input("Hey there!! Please enter a text or sentence:")
#Call the count_words function to get the word count
word_count = count_words(user_input)
#Check if the word count is zero(empty input)
if word_count == 0:  
  print("Oopsss!! Looks like you didn't enter any text.")
else:
  #Print the word count to the console 
  print("The number of words in the text is:", word_count)
  