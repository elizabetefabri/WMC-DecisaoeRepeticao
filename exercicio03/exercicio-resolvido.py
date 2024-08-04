'''
3. Faça um programa que peça uma nota, entre zero e dez. Mostre uma
mensagem caso o valor seja inválido e continue pedindo até que o usuário
informe um valor válido.
'''
## In the following block, the grade validation loop is started according to the value entered by the user
while True: 
    grade = float(input('Please, enter a grade between 0 and 10: '))

#In the next block, the validation of the entered grade is displayed, along with whether the loop should continue or not.
    if grade >= 0 and grade <= 10:
     print('It is a valid grade.')
     break
    else:
        print('It is an invalid grade. Grade must contain a value between 0 and 10.')    
