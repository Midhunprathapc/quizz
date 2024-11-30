def project():
    count=0
    timelimit=15
    import time
    startinngtimme=time.time()
    print("""quiz competition
    question 1
    SELECT THE STRING EXAMPLE
    1.""  
    2.[]
    3.()  
    4.{' """)
    a=int(input("enter your choice\n"))
    if time.time()-startinngtimme>timelimit:
        print("time out")
    elif a==1:
        print("correct answer")
        count+=1
    else:
        print("wrong answer")

    print("""2nd question
    choose the list 
    1.(1,2,3)
    2[1,2,3]
    3.("2") 
    4.["midhun]""")
    a=int(input("enter your choice\n"))
    if time.time()-startinngtimme>timelimit:
        print("time out")
    elif a==2:
        print("correct answer")
        count+=1
    else:
        print("wrong answer")
        
    print("""question 3
    which year is python released?
    1.1898 
    2.1789
    3.1991
    4.1990""")
    a=int(input("enter your choice\n"))
    if time.time()-startinngtimme>timelimit:
        print("time out")
    elif a==3:
        print("correct answer")
        count+=1
    else:
        print("wrong answer")

    print("""question 4
    Which of the following is a valid variable name in Python?

    1) 1st_name
    2) first-name
    3) first_name
    4) first name""") 
    a=int(input("enter your choice\n"))
    if time.time()-startinngtimme>timelimit:
        print("time out")
    elif a==3:
        print("correct answer")
        count+=1  
    else:
        print("wrong answer")
    
    print("""question 5
    What will be the output of the following code?
    x=5
    y=10
    print(x+y)  

    1) 5
    2) 10
    3) 15
    4) 50 """)
    a=int(input("enter your choice\n"))
    if time.time()-startinngtimme>timelimit:
        print("time out")
    elif a==3:
        print("correct answer")
        count+=1
    else:
        print("wrong answer")

    print(f"you got {count} mark")
try:
    project()
except ValueError:
    print("invalid input.choose the option ")
    project()