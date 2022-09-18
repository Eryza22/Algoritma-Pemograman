#get user input
answer = input("greetings: ")

new_answer = answer.lower().strip()

#check if the answer has 'hello', print 0
if 'hello' in new_answer:
    print("$0")

#check if the answer starts with 'h', print 20
elif 'h' in new_answer[0]:
    print("$20")

#otherwise, print 100
else:
    print("$100")