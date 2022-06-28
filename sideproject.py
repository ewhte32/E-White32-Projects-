print('Hello welcome to trivia!')
ans = input('Are you ready to play (yes/no): ')
score = 0
total_q = 4 
if ans.lower() == 'yes':
    ans = input('1. What is the capital of america? ')
    if ans.lower() == 'washington':
        score += 1
        print('Correct')
    else:    
            print('Incorrect')


    ans = input('2. Who won the 2020 nba finals? ')
    if ans.lower() == 'lakers':
        score += 1
        print('Correct')
    else:
            print('Incorrect')


    ans = input('3. What is 2 + 8 + 9 -1 ? ')
    if ans == '18':
        score += 1
        print('Correct')
    else:
            print('Incorrect')


    ans = input('4. What year is it? ')
    if ans.lower() == '2022':
        score += 1
        print('Correct')
    else:
            print('Incorrect')
            
            
         print('Thank you for playing, you got', score, "questions correct.") 
    mark = (score/total_q) * 100

    print("Mark: ", str(mark) + '%')  
    print('Goodbye')      