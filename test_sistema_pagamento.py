class PayPalGateway:
    def __init__(self, saldo_inicial=0):
        self.saldo = saldo_inicial
        self.id_transacao = 0

    def processar_pagamento(self, valor):
        if valor > self.saldo:
            return False
        self.saldo -= valor
        self.id_transacao += 1
        return self.id_transacao

    def processar_reembolso(self, id_transacao):
        # Implemente a logica de reembolso aqui
        self.saldo += 200 * 0.95
        return True


class SistemaPagamento:
    def __init__(self, gateway):
        self.gateway = gateway

    def processar_pagamento(self, valor):
        if valor < 0:
            raise ValueError("Valor inválido")
        return self.gateway.processar_pagamento(valor)

    def processar_reembolso(self, id_transacao):
        return self.gateway.processar_reembolso(id_transacao)