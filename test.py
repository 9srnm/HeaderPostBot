'''
For testing different things outside the main code
'''


def delete_the_beginning(message: str):
    message_list = list(map(str.strip, message.split('\n')))
    for row in range(len(message_list)):
        for symbol in range(len(message_list[row])):
            if message_list[row][symbol] == ')':
                message_list[row] = message_list[row][symbol + 1:]
                message_list[row] = message_list[row].strip()
                break
    return '\n'.join(message_list)


print(delete_the_beginning(input()))
