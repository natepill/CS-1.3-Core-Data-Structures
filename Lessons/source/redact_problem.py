

class Redact():

    def redact_words(self, text, banned_words):
        """
        Return new array of words from the text that that are not in the text
        O(N) + M
        """
        banned_words = set(banned_words)

        new_text = list()

        for word in text:
            try:
                if word in banned_words:
                    pass
                else:
                    new_text.append(word)
            except:
                raise ValueError("The value in the array caused an issue")

        return new_text
