calls = 0


def count_calls():
    global calls
    calls += 1


def string_info(string):
    count_calls()
    string_list = list()
    string_list.append(len(string))
    string_list.append(string.lower())
    string_list.append(string.upper())
    return tuple(string_list)


def is_contains(string, input_list):
    count_calls()

    if string in input_list:
        return True
    else:
        return False

print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches
print(calls)