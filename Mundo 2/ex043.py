altura = float(input('Por favor informe sua altura: '))
peso = float(input('Agora informe seu peso: '))
imc = peso / (altura ** 2)
if imc < 18.5:
    print(f'Atenção! Seu IMC é de {imc:.1f} e você está ABAIXO do peso ideal.')
elif imc >= 18.5 and imc <= 25:
    print(f'Parabéns! Seu IMC é de {imc:.1f} e você está no peso IDEAL.')
elif imc >= 25.1 and imc <= 30:
    print(f'Atenção! Seu IMC é de {imc:.1f} e você está com SOBREPESO.')
elif imc >= 30.1 and imc <= 40:
    print(f'Cuidado! Seu IMC é de {imc:.1f} e você está com OBESIDADE.')
elif imc > 40:
    print(f'Cuidado! Seu IMC é de {imc:.1f} e você está com OBESIDADE MÓRBIDA.')
