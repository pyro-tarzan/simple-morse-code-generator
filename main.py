plain_characters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s",
                    "t", "u", "v", "w", "x", "y", "z", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", " "]
morse_characters = [".-",
                    "-...",
                    "-.-.",
                    "-..",
                    ".",
                    ".._.",
                    "--.",
                    "....",
                    "..",
                    ".---",
                    "-.-",
                    ".-..",
                    "--",
                    "-.",
                    "---",
                    ".--.",
                    "--.-",
                    ".-.",
                    "...",
                    "-",
                    "..-",
                    "...-",
                    ".--",
                    "-..-",
                    "-.--",
                    "--..",
                    "-----",
                    ".----",
                    "..---",
                    "...--",
                    "....-",
                    ".....",
                    "-....",
                    "--...",
                    "---..",
                    "----.",
                    "/"]

print("Consider a scenario like Cooper. You want to convey a meessage to your lovely daughter \"Murphy Cooper\" in"
      " morse code.")

message_1 = input("Hey, I am TARS. I can help you to convert plain text into morse code: ")


def text_to_morse(plain_text):
    print("Roger that.")
    morse_text = ""
    plain_text = plain_text.lower()

    for char_index in range(0, len(plain_text)):
        for char in range(len(plain_characters)):
            if plain_text[char_index] == plain_characters[char]:
                morse_text += morse_characters[char] + " "
    return f"your morse code: {morse_text}"


if message_1:
    print(text_to_morse(message_1))
else:
    print("TARS can't convert empty value.")
