import os 
import json
import random 
from Q import Questions

Question_file = "Q&A.json"

def Loadata():
    if os.path.exists(Question_file):
        with open(Question_file,"r") as f:
            return json.load(f)
    else: 
        print("The File is not Exist!")
        return {}
def save_data():
    with open(Question_file,"w") as f:
        json.dump(Questions,f,indent = 4)
MyQuestions = Loadata()


class question:
    def __init__(self, questions, options, answers):
        self.questions = questions
        self.options = options
        self.answers = answers
        
    def Display_Questions(self):
        self.question_list = []
        
        for q in Questions:
            obj = question (
                q["Question"],
                q["Options"],
                q["Answer"]
            )
            self.question_list.append(obj)
        random.shuffle(self.question_list)
            
        return self.question_list

Object = question(None,None,None)

def percentage(Score):
    Total_Score = len(Questions)
    percent = (Score/Total_Score)*100
    return percent
def Grade(Score):
    p = percentage(Score)
    if p > 95:
        grade = "A+ Grade"
    elif p > 85:
        grade = "A Grade"
    elif p > 75:
        grade = "B+ Grade"
    elif p > 65:
        grade = "B Grade"
    elif p > 55:
        grade = "C+ Grade"
    elif p > 50:
        grade = "C Grade"
    elif p > 45:
        grade = "D+ Grade"
    elif p > 40:
        grade = "D Grade"
    elif p > 35: 
        grade = "E Grade"
    elif p < 33:
        grade = "F Grade"
    return grade 
    


def Code_runner():
    print("==== Select Your Options ====")
    print("Create your Account -->  1")
    print("Start The Game      -->  2")
    print("Check Your Result   -->  3")
    print("Exit                -->  4")
    
    while True:
       try:
        choice = int(input("Enter your Option: "))
       except:
           print("Enter the Valid Option!!")
           continue
        
       if choice == 1:
            Name = input("Enter the Name of the Participant: ")
            Player_ID = str(random.randint(10000, 99999))
            print('Your Player ID is this', Player_ID)

            MyQuestions[Player_ID] = {
              "Name" : Name,
              "Score" : 0,
              "Grade" : "Nothing",
              "Percentage" : "Nothing"
            }
            save_data()
       elif choice == 2:
            score = 0 
            Player_ID = input("Enter Your Player ID: ")
            if Player_ID in MyQuestions:
                all_questions = Object.Display_Questions()
                for i, q_data in enumerate(all_questions, 1):
                    print(f"\nQuestion {i}: {q_data.questions}")
                    print(f"Options: {q_data.options}")
                    answer = input("Your Answer: ")
                    if answer == q_data.answers:
                        print("Correct Answer!!")
                        score +=1
                    else:
                        print("Incorrect answer")
                MyQuestions[Player_ID]["Score"] = score

            save_data()
            
       elif choice == 3:
            Player_ID = input("Enter Your Player ID: ")
            if Player_ID in MyQuestions:
                score = MyQuestions[Player_ID]["Score"]
                MyQuestions[Player_ID]["Grade"] = Grade(score)           #updating and doing entry in the json file 
                MyQuestions[Player_ID]["Percentage"] = percentage(score)
                print('Your Score is: ',score)
                print('Your Grade is: ',MyQuestions[Player_ID]["Grade"])
                print("Your Percentage is: ",MyQuestions[Player_ID]["Percentage"])  # showing the result
            save_data()
               
       elif choice == 4:
            print("Exiting")
            break
        
        

Code_runner()
