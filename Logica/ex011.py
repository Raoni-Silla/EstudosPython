n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2)/2
print('a sua média foi {:.2f}'.format(m))
if m >= 8:
    print('media boa')
elif m >= 6:
    print('media razoavel')
else:
    print('media ruim')