# To create this program, write a Question class to hold the data for the trivia question.
# The question class should have attributes for the following data:
# A trivia question
# Possible answer 1
# Possible answer 2
# Possible answer 3
# Possible answer 4
# The number of the correct answer (1, 2, 3, or 4)


class Question:
    def __init__(self, question, a1, a2, a3, a4, answer):
        self.__question = question
        self.__a1 = a1
        self.__a2 = a2
        self.__a3 = a3
        self.__a4 = a4
        self.__answer = answer

    # set methods
    def set_question(self, question):
        self.__question = question

    def set_a1(self, a1):
        self.__a1 = a1

    def set_a2(self, a2):
        self.__a2 = a2

    def set_a3(self, a3):
        self.__a3 = a3

    def set_a4(self, a4):
        self.__a4 = a4

    def set_answer(self, answer):
        self.__answer = answer

    # get methods
    def get_question(self):
        return self.__question

    def get_a1(self):
        return self.__a1

    def get_a2(self):
        return self.__a2

    def get_a3(self):
        return self.__a3

    def get_a4(self):
        return self.__a4

    def get_answer(self):
        return self.__answer

    def __str__(self):
        result = self.get_question() + '\n' + \
            'Option 1 - ' + self.get_a1() + '\n' + \
            'Option 2 - ' + self.get_a2() + '\n' + \
            'Option 3 - ' + self.get_a3() + '\n' + \
            'Option 4 - ' + self.get_a4()
        return result

    def right_answer(self, answer):
        return answer == self.get_answer()
