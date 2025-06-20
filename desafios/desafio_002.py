val = input('Digite um valor: ') #função input sempre retorna uma string
print ('o tipo primitivo dela é', type (val))
print ('esse valor é numerico: ',val.isnumeric()) #verifica se todos os digitos são numericos
print('esse valor é alfabetico:', val.isalpha()) #verifica se todos os digitos são letras
print (' esse valor tem numeros e letras misturados:',val.isalnum()) #verifica se tem letras e numeros misturados
print('ele é composto só de espaços', val.isspace())