def concatenate(*words, **more_words):
    final_word = "".join(words)
    for key, value in more_words.items():
        final_word = final_word.replace(key, value)

    return final_word

print(concatenate("Soft", "UNI", "Is", "Grate", "!", UNI="Uni", Grate="Great"))
print(concatenate("I", " ", "Love", " ", "Cythons", C="P", s="", java='Java'))