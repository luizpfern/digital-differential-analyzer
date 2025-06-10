
def dda(x0, y0, x1, y1):
    # Calcula a diferença entre os pontos finais
    dx = x1 - x0  # diferença em X
    dy = y1 - y0  # diferença em Y

    # Decide quantos passos são necessários (escolhe o maior deslocamento)
    if abs(dx) > abs(dy):
        steps = abs(dx)
    else:
        steps = abs(dy)

    # Calcula o quanto deve ser incrementado em cada passo
    x_inc = dx / steps  # quanto aumenta o X a cada passo
    y_inc = dy / steps  # quanto aumenta o Y a cada passo

    # Começa a partir do ponto inicial
    x = x0
    y = y0

    # Para cada passo calcula o próximo ponto e imprime
    for i in range(int(steps) + 1):
        print("Ponto:", round(x), round(y))  # imprime o ponto atual
        x = x + x_inc  # soma o incremento ao X
        y = y + y_inc  # soma o incremento ao Y

# Exemplo de uso:
dda(2,3,8,5)

