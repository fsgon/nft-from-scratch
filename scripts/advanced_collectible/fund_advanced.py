from brownie import AdvancedCollectible
from scripts.helpful_scripts import fund_advaced_collectible

#financiador de contratos inteligentes
def main():
    #con esta linea se obtiene el smart contract implementado mas recientemente
    advanced_collectible = AdvancedCollectible[len(AdvancedCollectible) - 1]
    #se llama la funcion de helpful para financiar contratos y se envia como parametro el ultimo contrato
    fund_advaced_collectible(advanced_collectible)
