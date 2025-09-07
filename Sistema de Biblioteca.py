
class Livros:
    def __init__(self,titulo,autor,ano):
        self.titulo = titulo
        self.autor = autor
        self.ano = ano
        self.emprestado = False

    def __repr__(self):
        status = "Emprestado" if self.emprestado else "Disponível"
        return f"{status} {self.titulo}  ({self.autor}) [{self.ano}]"

class Biblioteca:
    def __init__(self):
        self.catalogo = []

    def adicionar(self,titulo,autor,ano):
        if any(l.titulo.lower() == titulo.lower() for l in self.catalogo):
            print(f"Ja existe {titulo} no catalogo!")
            return
        self.catalogo.append(Livros(titulo, autor ,ano))
        print(f"Livro adicionado com sucesso! {titulo} no catalogo!")

    def listar(self, somente_disponiveis=False):
        livros = self.disponiveis() if somente_disponiveis else self.catalogo
        if not livros:
            print("Nenhum livro encontrado.")
            return
        for i, l in enumerate(livros, start=1):
            print(f"{i}. {l}")

    def disponiveis(self):
        return [l for l in self.catalogo if not l.emprestado]

    def buscar_por_titulo(self, titulo):
        for l in self.catalogo:
            if l.titulo.lower() == titulo.lower():
                return l
        return None
    def emprestar(self, titulo):
        l = self.buscar_por_titulo(titulo)
        if not l:
            print(f"{titulo} não está no catálogo.")
        elif l.emprestado:
            print(f"{titulo} já está emprestado.")
        else:
            print(f"{titulo}Você emprestou")
    def devolver(self, titulo):
        l = self.buscar_por_titulo(titulo)
        if not l:
            print(f"{titulo} não está no catálogo")
        elif not l.emprestado:
            print(f"{titulo} já está disponível.")
        else:
            l.emprestado = True
            print(f"Devolução {titulo} registrada com sucesso!")


bib = Biblioteca()
bib.adicionar("O Senhor dos Anéis", "J. R. R. Tolkien", 1954)
bib.listar()
bib.emprestar("O Senhor dos Anéis")
bib.listar(somente_disponiveis=True)
bib.devolver("O Senhor dos Anéis")
