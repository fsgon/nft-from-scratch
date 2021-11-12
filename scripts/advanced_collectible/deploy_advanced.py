from brownie import AdvancedCollectible, accounts, network, config
from scripts.helpful_scripts import fund_advaced_collectible

def main():
    #se le da la direccion de villetera
    dev = accounts.add(config['wallets']['from_key'])
    print(network.show_active())
    publish_source= False
    #se crea un nuevo contrato con parametros vrf_coordinator, link_token, keyhash
    advanced_collectible = AdvancedCollectible.deploy(
        #parametros para el constructor del contrato
        #vrf_coordinator
        config['networks'][network.show_active()]['vrf_coordinator'],
        #link_token
        config['networks'][network.show_active()]['link_token'],
        #keyhash
        config['networks'][network.show_active()]['keyhash'],
        {"from": dev},
        publish_source= publish_source
    )
    #se financia el contrato con un enlace
    fund_advaced_collectible(advanced_collectible)
    return advanced_collectible