class Veiculo():
	def __init__(self):
		self.nivel_tanque = 0

	def abastecer(self, litros):
		self.nivel_tanque = litros


class Carro(Veiculo):
	def __init__(self):
		super().__init__()


if __name__ == "__main__":
	palio = Carro("Clebinho")
	palio.abastecer(20)
