def separator(text):
    out = []
    text += " "  # to indicate end of text else the last word will not apend
    word = ""
    for letter in text:
        if letter != " ":
            word += letter
        else:
            out.append(word)
            word = ""

    return out

