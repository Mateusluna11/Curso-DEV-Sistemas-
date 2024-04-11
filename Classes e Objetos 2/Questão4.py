#4-) Crie uma classe para representar um horario (hora, minuto e segundo).
#Implemente os metodos para fazer as operacoes de incremento (de segundos) no horario e diferença entre dois horarios.

class Horario:
    def __init__(self, hora, minuto, segundo):
        self.hora = hora
        self.minuto = minuto
        self.segundo = segundo

    def incrementar(self, segundos):
        self.segundo += segundos
        self.minuto += self.segundo // 60
        self.segundo %= 60
        self.hora += self.minuto // 60
        self.minuto %= 60

    def diferenca(self, outro_horario):
        segundos_self = self.hora * 3600 + self.minuto * 60 + self.segundo
        segundos_outro = outro_horario.hora * 3600 + outro_horario.minuto * 60 + outro_horario.segundo
        return segundos_self - segundos_outro

horario1 = Horario(10, 30, 0)
horario2 = Horario(11, 0, 0)

horario1.incrementar(3600)
diferenca = horario1.diferenca(horario2)

print(f"Horario 1: {horario1.hora}:{horario1.minuto}:{horario1.segundo}")
print(f"Horario 2: {horario2.hora}:{horario2.minuto}:{horario2.segundo}")
print(f"Diferença: {diferenca} segundos")
