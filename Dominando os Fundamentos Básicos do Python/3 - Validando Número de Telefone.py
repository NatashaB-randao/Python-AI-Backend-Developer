# Desafio
# Imagine que você trabalha para uma empresa de telecomunicações e é responsável por validar se um número de telefone fornecido pelo cliente está em um formato correto. Para garantir a precisão dos registros, é essencial que os números de telefone estejam no formato padrão. Desenvolva uma função programa que valide se um número de telefone tem o formato correto.

# Formato esperado:
# O formato aceito para números de telefone é: (XX) 9XXXX-XXXX, onde X representa um dígito de 0 a 9. Lembre-se de respeitar os espaços entre os números quando preciso.

# Entrada
# Uma string representando o número de telefone.

# Saída
# Uma mensagem indicando se o número de telefone é válido ou inválido.

# Conheça mais sobre o Regex: https://docs.python.org/pt-br/3.8/howto/regex.html
# Conheça mais sobre o 're' do python: https://docs.python.org/pt-br/3/library/re.html

# Módulo 're' que fornece operações com expressões regulares.
import re

# Função para validar o número de telefone
def validate_numero_telefone(phone_number):
    # Define o padrão de expressão regular (regex) para validar números de telefone no formato (XX) 9XXXX-XXXX
    pattern = r"\(\d{2}\) 9\d{4}-\d{4}"
    
    # Verifica se o padrão definido corresponde ao número de telefone fornecido
    if re.match(pattern, phone_number):
        return "Número de telefone válido."
    else:
        return "Número de telefone inválido."

# Solicita ao usuário que insira um número de telefone e armazena o valor fornecido na variável 'phone_number'.
phone_number = input()  

# Chama a função 'validate_numero_telefone()' com o número de telefone fornecido como argumento e armazena o resultado retornado na variável 'result'.
result = validate_numero_telefone(phone_number)

# Imprime o resultado
print(result)

