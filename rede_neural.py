import math

input = 1
weight = 0.5
output_desire = 0
learning_rate = 0.1
error = math.inf

aux = 0

def activation(sum):
    if sum > 0:
        return 1
    else:
        return 0
    
while error != 0:
    aux += 1

    print("iteracao", aux)
    print('peso', weight)


    sum = input * weight

    output = activation(sum)
    print("saida", output)

    error = output_desire - output
    print("erro", error)

    if not error == 0:
        weight = weight + (learning_rate * error * input) # peso igual a peso mais taxa de aprendizado vezes erro vezes entrada

print("A REDE APRENDEU!")