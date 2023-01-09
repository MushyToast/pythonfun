import time

def typing_test(sentence):
    start_time = time.time()
    user_input = input(f"Type the following sentence:\n{sentence}\n")
    end_time = time.time()
    elapsed_time = end_time - start_time
    if user_input == sentence:
        print("Correct!")
    else:
        print("Incorrect!")
    wpm = len(sentence.split()) / (elapsed_time / 60)
    print(f"You typed at a speed of {wpm:.2f} words per minute.")

typing_test("The quick brown fox jumps over the lazy dog")