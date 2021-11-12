from brownie import AdvancedCollectible, accounts, config, interface, network

#funcion para obtener la raza del perro
def get_breed(breed_number):
    switch = {0: 'PUG', 1: 'SHIBA_INU', 2: 'ST_BERNARD', 3: 'MASK', 4: 'MASK_SQUARE'}
    return switch[breed_number]


#funcion que financia contratos
def fund_advaced_collectible(nft_contract):
    #configuracion de cuenta para financiar desde esta direccion
    dev = accounts.add(config['wallets']['from_key'])
    #enviar el token para financiar
    #ABI define la forma de interactuar con un smart contract --se define en interfaces
    link_token = interface.LinkTokenInterface(
        config['networks'][network.show_active()]['link_token']
        )

    #usamos la funcion transfer de la interface
    link_token.transfer(nft_contract, 100000000000000000, {'from': dev} )