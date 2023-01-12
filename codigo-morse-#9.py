
'''
 Reto #9
 * CÓDIGO MORSE
 * Dificultad: MEDIA
 *
 * Enunciado: Crea un programa que sea capaz de transformar texto natural a código morse y viceversa.

'''


morse_code_dict = {

    'A': '.-', 'B': '-...',
    'C': '-.-.', 'D': '-..', 'E': '.',
    'F': '..-.', 'G': '--.', 'H': '....',
    'I': '..', 'J': '.---', 'K': '-.-',
    'L': '.-..', 'M': '--', 'N': '-.',
    'O': '---', 'P': '.--.', 'Q': '--.-',
    'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--',
    'X': '-..-', 'Y': '-.--', 'Z': '--..',
    '1': '.----', '2': '..---', '3': '...--',
    '4': '....-', '5': '.....', '6': '-....',
    '7': '--...', '8': '---..', '9': '----.',
    '0': '-----', ', ': '--..--', '.': '.-.-.-',
    '?': '..--..', '/': '-..-.', '-': '-....-',
    '(': '-.--.', ')': '-.--.-'
}


def text_to_morse(text):

    result = ''

    for let in text.upper():

        if let == " ":
            result += " "

        else:
            result += morse_code_dict[let] + " "

    return result


def morse_to_text(morse):
    morse_code_dict_inverse = {v: k for k, v in morse_code_dict.items()}
    morse_text = ''

    words = morse.split()

    for let in words:
        if let in morse_code_dict_inverse:
            morse_text += morse_code_dict_inverse[let]

    return morse_text.lower()


if __name__ == '__main__':

    print(text_to_morse('kevin'))

    print(morse_to_text('-.- . ...- .. -. '))
