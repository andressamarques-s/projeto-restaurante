class Restaurante:
    restaurantes = []

    def __init__(self, nome, categoria):
        self._nome = nome.title()
        self._categoria = categoria.upper()
        self._ativo = False
        self._avaliacoes = []
        Restaurante.restaurantes.append(self)

    def __str__(self):
        return f"{self._nome} | {self._categoria}"

    @classmethod
    def listar_restaurantes(cls):
        print(
            f"{'Nome do Restaurante'.ljust(25)} | "
            f"{'Categoria'.ljust(15)} | "
            f"{'Média'.ljust(10)} | "
            f"{'Status'}"
        )

        for restaurante in cls.restaurantes:
            print(
                f"{restaurante._nome.ljust(25)} | "
                f"{restaurante._categoria.ljust(15)} | "
                f"{str(restaurante.media_avaliacoes).ljust(10)} | "
                f"{restaurante.ativo}"
            )

    @property
    def ativo(self):
        return "☑" if self._ativo else "☐"

    def alternar_status(self):
        self._ativo = not self._ativo

    def adicionar_avaliacao(self, nota, comentario):
        if 0 < nota <= 5:
            Avaliacao(nota, comentario, self)

    @property
    def media_avaliacoes(self):
        if not self._avaliacoes:
            return "--"

        soma = sum(av.nota for av in self._avaliacoes)
        return round(soma / len(self._avaliacoes), 1)


class Avaliacao:
    def __init__(self, nota, comentario, restaurante):
        self._nota = nota
        self._comentario = comentario
        self._restaurante = restaurante
        restaurante._avaliacoes.append(self)

    @property
    def nota(self):
        return self._nota


if __name__ == "__main__":

    restaurante_praca = Restaurante("Praça", "Fast food")
    restaurante_praca.alternar_status()

    restaurante_praca.adicionar_avaliacao(5, "Muito bom")
    restaurante_praca.adicionar_avaliacao(4, "Bom atendimento")

    Restaurante.listar_restaurantes()
