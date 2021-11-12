from brownie import AdvancedCollectible, network, accounts, config
from scripts.helpful_scripts import get_breed

dog_metadata_dic = {
    "PUG": "https://ipfs.io/ipfs/Qmd9MCGtdVz2miNumBHDbvj8bigSgTwnr4SbyH6DNnpWdt?filename=0-PUG.json",
    "SHIBA_INU": "https://ipfs.io/ipfs/QmdryoExpgEQQQgJPoruwGJyZmz6SqV4FRTX1i73CT3iXn?filename=1-SHIBA_INU.json",
    "ST_BERNARD": "https://ipfs.io/ipfs/QmbBnUjyHHN7Ytq9xDsYF9sucZdDJLRkWz7vnZfrjMXMxs?filename=2-ST_BERNARD.json",
    "MASK_SQUARE": "https://ipfs.io/ipfs/Qmb4e93zcXQ7oya25jfhfDJnkfVb56eiNdKuXnw76AnFod?filename=0-MASK_SQUARE.json",
    "MASK": "https://ipfs.io/ipfs/QmawzGQdhSrkdQE85RNLTRG5F9HsTzqTnAj61Ai87sTT7q?filename=0-MASK.json",
}

OPENSEA_FORMAT = "https://testnets.opensea.io/assets/{}/{}"

def main():
    print("Trabajando en la red " + network.show_active())
    advanced_collectible = AdvancedCollectible[len(AdvancedCollectible) - 1]
    number_of_advanced_collectibles = advanced_collectible.tokenCounter()
    print("El numero de tokens que has desplegado es: " + str(number_of_advanced_collectibles))
    
    for token_id in range(number_of_advanced_collectibles):
        breed = get_breed(advanced_collectible.tokenIdToBreed(token_id))
        #verificamos que no se haya asignado un tokenURI
        if not advanced_collectible.tokenURI(token_id).startswith("https://"):
            print("Configurando el tokenURI de {}".format(token_id))
            set_tokenURI(token_id, advanced_collectible, dog_metadata_dic[breed])
        else:
            print("Omitiendo {}, ya esta configurado el tokenURI".format(token_id))

def set_tokenURI(token_id, nft_contract, tokenURI):
    dev = accounts.add(config["wallets"]["from_key"])
    nft_contract.setTokenURI(token_id, tokenURI, {"from": dev})
    print(
        "Genial! ahora podras ver tu NFT en {}".format(OPENSEA_FORMAT.format(nft_contract.address, token_id))
    )
    print(
        "Por favor espera almenos 20 minutos y selecciona el boton 'refresca metadatos'"
    )