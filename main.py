print("welcome the quiz game!")
score = 0
q1 = str(input("what's the capital of america: "))
if q1 == "Washington, D.C.":
    print("correct ans!")
    print("score +1")
    score += 1
else:
    print("wrong ans, try again.")
q2 = str(input("in which year did suez canal open: "))
if q2 == "1869":
    print("correct ans!")
    print("score +1")
    score += 1
else:
    print("wrong ans, try again")
q2 = str(input("which is the largest democratic country: "))
if q2 == "India":
    print("correct ans!")
    print("score +1")
    score += 1
else:
    print("wrong ans, try again")

print("you got " + str(score) + " questions correct")
print("your score is " + str(score))
