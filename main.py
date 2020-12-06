def csRemoveTheVowels(input_str):
    new_input = input_str
    v = ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U')
    for letter in input_str:
        if letter in v:
            new_input = new_input.replace(letter, "")
    return new_input
    