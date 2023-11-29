#!/usr/bin/env python3

class MyString:
    def __init__(self, value=""):
        self.value = value

    def get_value(self):
        return self._value

    def set_value(self,value):
        if type(value) == str:
            self._value = value
        else:
            print("The value must be a string.")
        
    value = property(get_value,set_value)

    def is_sentence(self):
        return (self.value).endswith(".")

    def is_question(self):
        return(self.value).endswith("?")

    def is_exclamation(self):
        return(self.value).endswith("!")

    def count_sentences(self):
        if self.value != "" :
            changed_sentence = (self.value).replace("?",".")
            final_sentence = changed_sentence.replace("!",".")
            sentence_fragments = (final_sentence).split(".")
            sentences = []
            for fragment in sentence_fragments:
                if fragment != "":
                    sentences.append(fragment)
            return len(sentences)
        else:
            return 0