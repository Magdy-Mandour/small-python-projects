question = input("what's on your mind today? ")
def count_words(word):
    user_answer = len(question.split())
    if user_answer > 15:
        return f"Oh friend, you seems to have a lot on your mind, that was {user_answer} words!"
    else:
        return f"Oh nice, you just told me what's on your mind in {user_answer} words!"
print(count_words(question))
