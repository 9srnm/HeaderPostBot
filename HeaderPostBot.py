import telebot


def delete_the_beginning(message: str):
    message_list = list(map(str.strip, message.split('\n')))
    for row in range(len(message_list)):
        for symbol in range(len(message_list[row])):
            if message_list[row][symbol] == ')':
                message_list[row] = message_list[row][symbol + 1:]
                message_list[row] = message_list[row].strip()
                break
    return '\n'.join(message_list)


bot = telebot.TeleBot(token='')


@bot.message_handler(content_types=['text'])
def change_results_of_matches(message):
    bot.send_message(message.from_user.id, delete_the_beginning(message.text))


bot.polling(none_stop=True, interval=0)
