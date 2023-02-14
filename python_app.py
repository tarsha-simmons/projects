#replace word in terminal
def replace_word():

  str = "Hi everyone, I am Tasha and hello hi hi"
  word_to_replace = input("Enter the word to replace: ")
  word_replacement = input("Enter the word replacement: ")
  print(str.replace(word_to_replace, word_replacement))

  replace_word()