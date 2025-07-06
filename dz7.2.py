import string
def correct_sentence(string1: str) ->str:
    string1 = string1[0].upper() + string1[1:]
    if string1[-1] == ".":
        return string1
    else:
        return (string1 + '.')
assert correct_sentence("greetings, friends") == "Greetings, friends.", 'Test1'
assert correct_sentence("hello") == "Hello.", 'Test2'
assert correct_sentence("Greetings. Friends") == "Greetings. Friends.", 'Test3'
assert correct_sentence("Greetings, friends.") == "Greetings, friends.", 'Test4'
assert correct_sentence("greetings, friends.") == "Greetings, friends.", 'Test5'
print('ОК')