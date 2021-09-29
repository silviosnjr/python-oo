class Conta:

    #método construtor ao criar um objeto deve-se enviar
    #os parametros deste método
    def __init__(self, numero, titular, saldo, limite):
        #print("Construindo objeto ... {}".format(self))
        #abaixo são os atributos (privados) da classe que recebe o parametros
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    #abaixo temos os métodos/comportamentos da classe
    def extrato(self):
        print("Saldo de {} do titular {}".format(self.__saldo, self.__titular))

    def deposita(self, valor):
        if (self.__verifica_valor_negativo(valor)):
            self.__saldo += valor

    #método criado a mais para validar se o valor da operação não está sendo enviado como negativo.
    def __verifica_valor_negativo(self, valor):
        if (valor < 0):
            print("Esse valor é negativo, não foi possível realizar sua operação!")
            return False;
        else :
            return True;

    def __pode_sacar(self, valor_a_sacar):
        valor_disponivel_a_sacar = self.__saldo + self.__limite
        return valor_a_sacar <= valor_disponivel_a_sacar

    def saca(self, valor):
        if (self.__verifica_valor_negativo(valor)):
            if(self.__pode_sacar(valor)):
                self.__saldo -= valor
            else:
                print("Não foi possível sacar! O valor {} passou o limite".format(valor))

    def transfere(self, valor, destino):
        if (self.__verifica_valor_negativo(valor)):
            self.saca(valor)
            destino.deposita(valor)

    #métodos que são propriedade para acessar os atributos
    @property
    def saldo(self):
        return self.__saldo

    @property
    def titular(self):
        return self.__titular

    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self, limite):
        self.__limite = limite

    #métodos da classe ou melhor estáticos
    @staticmethod
    def codigo_banco():
        return "001"

    @staticmethod
    def codigos_bancos():
        return {'BB':'001', 'Caixa':'104', 'Bradesco':'237'}