questions = ('What is the basic unit of life?', 
                      'Which organelle is known as the “powerhouse of  cell”?', 
                      'Which of the following is responsible for photosynthesis?', 
                      'Which gas is released during photosynthesis?', 
                      'What is the main function of red blood cells?')
 
options = (('A. Tissue', 'B. Organ', 'C. Cell', 'D. System'),
                  ('A. Nucleus', 'B. Ribosome', 'C. Mitochondrion', 'D. Vacuole'),
                  ('A. Chloroplast', 'B. Mitochondrion', 'C. Lysosome', 'D. Nucleus'),
                  ('A. Carbon dioxide', 'B. Oxygen', 'C. Nitrogen', 'D. Hydrogen'),
                  ('A. Fight infection', 'B. Digest food', 'C. Carry oxygen', 'D. Produce hormones')) 
                  
answers = ('C', 'C', 'A', 'B', 'C')

user_answers = []    
score = 0

for i in range(len(questions)):
    print()
    print(f'Q{i + 1}: {questions[i]}') 
    for option in options[i]:
        print(option) 
        
    
    user_answer = input('Choose an answer from A,B,C,D: ').upper()
    
      
    user_answers.append(user_answer)  
    
    if user_answer == answers[i]:
        score += 1
    else:
        print(f'Wrong! the correct answer is {answers[i]}')   
        
total_questions = len(questions) 
percent = (score / total_questions)  * 100       

print("\n========== QUIZ RESULT ==========")

for j in answers:
    print(j, end=' ' )
print()    
for z in user_answers:
    print(z, end=' ' )         
print()       
print(f'You scored: {percent:.2f}%')                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           