def output_fun(available_characters, dictionary, output_str):
  user_input = input('Please enter some text: ')
  print(user_input)

  for char in user_input:
    if not char.upper() in available_characters:
      print("ERROR: CHARACTER {} IS NOT AVAILABLE!!!".format(char))
      break
    else:
      morse_code = dictionary[char.upper()]
      output_str += morse_code

  print(output_str)