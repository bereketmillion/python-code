QUESTION_LIST = []

q1 = {"Question": "which one of the following allows nested function ?", "A": 'java', 'B': "c++", 'C': "python", "D": "None"}
QUESTION_LIST.append(q1)

q2 = {"Question": "which one of the following is not frontend language ?", "A": 'HTML', 'B': "CSS", 'C': "R", "D": "javascript"}
QUESTION_LIST.append(q2)

q3 = {"Question": "What does the range() function in Python return? ", "A": 'A list of numbers', 'B': "A generator object", 'C': "A tuple of numbers", "D": "A dictionary of numbers"}
QUESTION_LIST.append(q3)

q4 = {"Question": "What will the following code output?\n my_list = [1, 2, 3, 4, 5]\n print(my_list[-2])\n", "A": '2', 'B': "4", 'C': "3", "D": "5"}
QUESTION_LIST.append(q4)

q5 = {"Question": "Which of the following is a mutable data type in Python? ", "A": 'Tuple', 'B': "String", 'C': "Set", "D": "FrozenSet"}
QUESTION_LIST.append(q5)

correctAnswer = 0 
count = 1
answers = {1: "C", 2: "C", 3: "B", 4: "B", 5: "C"}

for question_index in range(len(QUESTION_LIST)):
    listofquestions = [count, "A", "B", "C", "D"]
    question_values = list(QUESTION_LIST[question_index].values())
    print("")
    for i in range(len(listofquestions)):
        print(listofquestions[i], ".", question_values[i])  # Skip first element which is the question itself

    x = (input(" Enter your answer : "))
    x=x.upper()

    if x == answers[count]:
        correctAnswer += 1
        print("correct answer")
    else:
        print("incorrect answer")
    count += 1

print(f"you got : {correctAnswer} / {len(QUESTION_LIST)}")
