def give_options(x, y, z):
    print("a):", x)
    print("b):", y)
    print("c):", z)

print("Hello! Welcome to my Quiz" "\n" "All Questions carries 10 marks each")
ans = input("Are you ready to play (yes/no): ")
a = "Note: write option number! do not write anything else."
score = 0
total_questions = 9

#correct_ans = ["python", "steve jobs", "artificial intelligence", "bitcoin", "-32768 to 32767", "The opening parenthesis should immediately follow the macro name. ", " "]
correct_ans = ["1", "3", "2", "3", "2", "1", "1", "2", "2"]

if ans.lower() == "yes":
    print(a)
    print("Question- What is the best Programming Language? ")
    give_options("Python", "C", "Java")
    ans = input(">>>")
    if ans.lower() == correct_ans[0]:
        score = score + 1
        print("Correct")
    else:
        print("Incorrect")
    print(a)
    print("Question- Who is the Founder of Apple Inc? ")
    give_options("Mark Zuckerberg", "Warren Buffet", "Steve jobs")
    ans = input(">>>")
    if ans.lower() == correct_ans[1]:
        score = score + 1
        print("Correct")
    else:
        print("Incorrect")
    print(a)
    print("Question- What is more better among these? ")
    give_options("Data Science", "Artificial Intelligence", "Digital Marketing")
    ans = input(">>>")
    if ans.lower() == correct_ans[2]:
        score = score + 1
        print("Correct")
    else:
        print("Incorrect")
    print(a)
    print("Question- What is the best Investment? ")
    give_options("Share Capital", "Mutual Funds", "Bitcoin")
    ans = input(">>>")
    if ans.lower() == correct_ans[3]:
        score = score + 1
        print("Correct")
    else:
        print("Incorrect")
    print(a)
    print("Question- What is the 16-bit compiler allowable range for integer constants? ")
    give_options("-3.4e38 to 3.4e38", "-32768 to 32767", "-32767 to 32768")
    ans = input(">>>")
    if ans.lower() == correct_ans[4]:
        score = score + 1
        print("Correct")
    else:
        print("Incorrect")
    print(a)
    print("Question-  Which of the following comment is correct when a macro definition includes arguments? ")
    give_options("The opening parenthesis should immediately follow the macro name.", " There should be only one blank between the macro name and the opening parenthesis.", "All of the above is correct")
    ans = input(">>>")
    if ans.lower() == correct_ans[5]:
        score = score + 1
        print("Correct")
    else:
        print("Incorrect")

    print(a)
    print("Question- What is a lint? ")
    give_options("Analyzing tool", "Interactive debugger", "C compiler")
    ans = input(">>>")
    if ans.lower() == correct_ans[6]:
        score = score + 1
        print("Correct")
    else:
        print("Incorrect")

    print(a)
    print("Question-  What is the output of this statement printf(%d,(a++) )? ")
    give_options("The value of (a + 1)", "Error message", "The current value of a")
    ans = input(">>>")
    if ans.lower() == correct_ans[7]:
        score = score + 1
        print("Correct")
    else:
        print("Incorrect")

    print(a)
    print("Question- In the C language, the constant is defined _______. ")
    give_options("Before main", "It increases code size.", "It reduces code size.")
    ans = input(">>>")
    if ans.lower() == correct_ans[8]:
        score = score + 1
        print("Correct")
    else:
        print("Incorrect")
    '''
 print(a)
 print("Question- Who is the Founder of Apple Inc? ")
 give_options("Mark Zuckerberg", "Warren Buffet", "Steve jobs")
 ans = input(">>>")
 print(a)
 print("Question- What is the best Programming Language? ")
 give_options("Python", "C", "Java")
 ans = input(">>>")
 if ans.lower() == correct_ans[5]:
     score = score + 1
     print("Correct")
 else:
     print("Incorrect")
 print(a)
 print("Question- Who is the Founder of Apple Inc? ")
 give_options("Mark Zuckerberg", "Warren Buffet", "Steve jobs")
 ans = input(">>>")
 print(a)
 print("Question- What is the best Programming Language? ")
 give_options("Python", "C", "Java")
 ans = input(">>>")
 if ans.lower() == correct_ans[6]:
     score = score + 1
     print("Correct")
 else:
     print("Incorrect")
 print(a)
 print("Question- Who is the Founder of Apple Inc? ")
 give_options("Mark Zuckerberg", "Warren Buffet", "Steve jobs")
 ans = input(">>>")
 print(a)
 print("Question- What is the best Programming Language? ")
 give_options("Python", "C", "Java")
 ans = input(">>>")
 if ans.lower() == correct_ans[7]:
     score = score + 1
     print("Correct")
 else:
     print("Incorrect")
 print(a)
 print("Question- Who is the Founder of Apple Inc? ")
 give_options("Mark Zuckerberg", "Warren Buffet", "Steve jobs")
 ans = input(">>>")
 '''
i = score * 10
if i < 50:
    print("Ouch, your score is", i, "/ 90 better luck next time.")
elif i == 60:
    print("Nice! you scored", i, "/ 90 Work hard.")
elif i == 70:
    print("Nice! you scored", i, "/ 90 you are quite smart.")
else:
    print("Congratulations! it's a perfect", i, "/ 90 you are Intelligent.")
