from brownie import AdvancedCollectible, accounts, config
from scripts.helpful_scripts import get_breed
import time

STATIC_SEED = 123

def main():
    #obtenemos cuenta de desarrollo desde la clave privada
    dev = accounts.add(config['wallets']['from_key'])
    #obtenemos el contrato mas reciente
    advanced_collectible = AdvancedCollectible[len(AdvancedCollectible) - 1]
    
    #se crea la transaccion llamando la funcion createCollectible de el contrato AdvanceCollectible.sol
    transaction = advanced_collectible.createCollectible(
         STATIC_SEED, "None", {"from": dev})
    transaction.wait(1)
    time.sleep(180)
    requestId = transaction.events['requestedCollectible']['requestId']
    print(requestId)
    token_Id = advanced_collectible.requestIdToTokenId(requestId)
    print(token_Id)
    breed = get_breed(advanced_collectible.tokenIdToBreed(token_Id))
    print('la raza de perro del tokenId {} es {}'.format(token_Id, breed))

