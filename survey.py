# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
"""
“Have you ever been diagnosed with diabetes?” is a screening question that would be asked to evaluate for the eligibility criteria “Patients must have a diagnosis of diabetes.”
“Are you between the ages of 18 and 75?” is a screening question that would be asked to evaluate for the eligibility criteria “Patients must be between the ages of 18 and 75”.
"""
"""
QuestionType
    - stmt
    - id

RangeQuestionType
    - min
    - max
    - scoring_method

StringQuestionType
    - scoring_method
"""
class Question:
    def __init__(self, id, question_statement, correct_response):
        self.__question_statement = question_statement
        self.__id = id
        self.__correct_response = correct_response

    def get_question_statement(self):
        return self.__question_statement

    def get_id(self):
        return self.__id

    def get_correct_response(self):
        return self.__correct_response


#######################################


class GenericQuestion:
    def __init__(self, id, question_statement):
        self.__question_statement = question_statement
        self.__id = id

    def get_question_statement(self):
        return self.__question_statement

    def get_id(self):
        return self.__id

class RangeQuestion(GenericQuestion):
    def __init__(self, id, question_statement, min, max):
        super().__init__(id, question_statement)
        self.__min = min
        self.__max = max

    def get_min(self):
        return self.__min

    def get_max(self):
        return self.__max

class BooleanQuestion(GenericQuestion):
    def __init__(self, id, question_statement, correct_response):
        super().__init__(id, question_statement)
        self.__correct_response = correct_response

    def get_correct_response(self):
        return self.__correct_response

# class QuestionSet:
#     def __init__(self):
#         self.__

class UserResponse:
    def __init__(self, question_id, response):
        self.__question_id = question_id
        self.__response = response

    def get_response(self):
        return self.__response

    def get_question_id(self):
        return self.__question_id


class Survery:
    def __init__(self, questions_list = []):
        self.__questions_list = questions_list
        self.__result = 'Fail'

    def add_question(self, question):
        self.__questions_list.append(question)

    def get_survey_questions(self):
        return self.__questions_list

    def get_result(self):
        return self.__result

    def verify_response(self, user_response):
        for response in user_response:
            question_id = response.get_question_id()
            questtion_response = response.get_response()
            for question in self.__questions_list:
                if question.get_id() == question_id:
                    if isinstance(question, BooleanQuestion) and question.get_correct_response() != questtion_response:
                        self.__result = 'Fail'
                        return
                    elif isinstance(question, RangeQuestion):
                        if question.get_min() > questtion_response or question.get_max() < questtion_response:
                            self.__result = 'Fail'
                            return

        self.__result = 'Pass'


def main():
    survey = Survery()
    question_list = []
    question_list.append(BooleanQuestion(1, "Have you ever been diagnosed with diabetes?”", "Yes"))
    question_list.append(RangeQuestion(2, "Are you between the ages of 18 and 75?”", 18, 75))
    # survey.add_question(1, "Have you ever been diagnosed with diabetes?”", "Yes")
    # survey.add_question(2, "Are you between the ages of 18 and 75?”", "No")

    for question in question_list:
        survey.add_question(question)

    question_list = survey.get_survey_questions()

    for question in question_list:
        print(question.get_question_statement())

    user_response = []
    user_response.append(UserResponse(1, "Yes"))
    user_response.append(UserResponse(2, 25))
    survey.verify_response(user_response)

    result = survey.get_result()

    print('Result = {}'.format(result))



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
