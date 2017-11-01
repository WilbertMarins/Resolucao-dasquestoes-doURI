Multiplicação com ponto flutuante
1.Some os expoentes com peso dos dois números,subtraindo o valor do peso da soma para obter o novo expoente.
2.Multiplique as mantissas.
3.Normalize se necessário,caso ocorra ajuste o expoente.
4.Verifique se houve overflow ou underflow ,caso aconteça considere exceção.
5.Verifique se está normalizado,senã estiver retorne ao passo (3).
6.Ponha o sinal,se ambos tiverem o mesmo sinal,considera-se positivo,caso contrário ,será negativo.
