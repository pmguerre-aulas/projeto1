from utils import *

if __name__ == '__main__':
	aluno = get_string("Nome: ")
	nota1 = get_float("Nota 1: ")
	nota2 = get_float("Nota 2: ")

	media = (nota1 + nota2)/2

	print(f"{aluno} - {media}")
