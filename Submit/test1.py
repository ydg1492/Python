with open('Submit/scores.csv', 'r', encoding='UTF-8') as f:

    kor_scores = []
    eng_scores = []
    math_scores = []

    for line in f:
        name, kor, eng, math = line.strip().split(',')

        if kor.isdigit():
            kor_scores.append(int(kor))

        if eng.isdigit():
            eng_scores.append(int(eng))

        if math.isdigit():
            math_scores.append(int(math))

print(
    f'국어 평균:{round(sum(kor_scores)/len(kor_scores),2)}, 최고점:{max(kor_scores)}, 최저점:{min(kor_scores)}\n'
    f'영어 평균:{round(sum(eng_scores)/len(eng_scores),2)}, 최고점:{max(eng_scores)}, 최저점:{min(eng_scores)}\n'
    f'수학 평균:{round(sum(math_scores)/len(math_scores),2)}, 최고점:{max(math_scores)}, 최저점:{min(math_scores)}'
)

with open('Submit/scores.csv', 'r', encoding='UTF-8') as f:

    kor_scores = []
    eng_scores = []
    math_scores = []

    result = []

    for line in f:
        name, kor, eng, math = line.strip().split(',')
 
       
        if kor.isdigit():
            kor_scores.append(kor)

        if eng.isdigit():
            eng_scores.append(eng)

        if math.isdigit():
            math_scores.append(math)
            
            kor = int(kor)
            eng = int(eng)
            math = int(math)
            
            total = kor + eng + math
            avg = total/3

            if avg.is_integer():
               avg = int(avg)
            else:
                avg = round(avg, 2)


            
            result.append(f'{name},{total},{avg}')


with open('Submit/result.csv', 'w', encoding='UTF-8') as f:
    f.write('이름,총점,평균\n')

    for r in result:
        f.write(",".join(result))


print(result)