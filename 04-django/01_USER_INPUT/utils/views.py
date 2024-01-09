from django.shortcuts import render


def bmi_in(request):
    # <form> HTML 제공
    return render(request, 'utils/bmi_in.html')


def bmi_out(request):
    # bmi_in 에서 넘어온 데이터로
    # BMI 를 계산하여 사용자에게 보여줌
    height = float(request.GET['height'])
    weight = float(request.GET['weight'])

    bmi = weight / (height / 100) ** 2
    bmi = round(bmi, 2)

    if bmi < 18.5:
        status = '저체중'
    elif bmi < 23:
        status = '정상'
    elif bmi < 25:
        status = '과체중'
    else:
        status = '비만'

    return render(request, 'utils/bmi_out.html', {
        'bmi': bmi,
        'status': status,
    })