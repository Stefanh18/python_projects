class Sentence:
    def __init__(self, sentence):
        self.sentence = sentence
        self.word_list = self.sentence.split()

    def get_first_word(self):
        return str(self.sentence.split()[0])

    def get_all_words(self):
        return self.word_list

    def replace(self, index = 0, new_word = ""):
        try:
            self.word_list[index] = new_word
            return self.word_list
        except:
            pass
