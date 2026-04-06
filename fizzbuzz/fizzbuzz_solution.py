## solution
def fizzbuzz(n:int):
    answer = []
    for i in range(i, n+i):
        if i % 15 == 0:
            answer.append('FizzBuzz')
        elif i % 3 == 0:
            answer.append('Fizz')
        elif i % 5 == 0:
            answer.append('Buzz')
        else:
            answer.append(str(i))
    return answer

## applied
def performance(dataset):
    grade = []
    for i in range(len(dataset)):
        each_row = dataset.iloc[i]
        result = each_row['score']/each_row['target'] * 100
        if result >= 80:
            grade.append("A")
        elif result >= 60:
            grade.append("B")
        elif result >= 40:
            grade.append("C")
        else:
            grade.append("F")
    return grade                   
        

                    