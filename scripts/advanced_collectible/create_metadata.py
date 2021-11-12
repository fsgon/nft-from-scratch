from brownie import AdvancedCollectible, network
from metadata import sample_metadata
from scripts.helpful_scripts import get_breed
from pathlib import Path
import os
import requests
import json


breed_to_image_uri = {
    "PUG": "https://ipfs.io/ipfs/QmSsYRx3LpDAb1GZQm7zZ1AuHZjfbPkD6J7s9r41xu1mf8?filename=pug.png",
    "SHIBA_INU": "https://ipfs.io/ipfs/QmYx6GsYAKnNzZ9A6NvEKV9nf1VaDzJrqDR23Y8YSkebLU?filename=shiba-inu.png",
    "ST_BERNARD": "https://ipfs.io/ipfs/QmUPjADFGEKmfohdTaNcWhp7VGk26h5jXDA7v3VtTnTLcW?filename=st-bernard.png",
}

def main():
    print("trabajando en la red "+ network.show_active())
    advanced_collectible = AdvancedCollectible[len(AdvancedCollectible) -1]
    number_of_tokens = advanced_collectible.tokenCounter()
    print("El numero de tokens que ha implementado es {}".format(number_of_tokens))
    write_metadata(number_of_tokens, advanced_collectible)

def write_metadata(number_of_tokens , nft_contract):
    for token_id in range(number_of_tokens):
        collectible_metadata = sample_metadata.metadata_template
        breed = get_breed(nft_contract.tokenIdToBreed(token_id))
        #se crea un archivo con el nombre
        #./metadata/rinkeby/0-PUG.json
        metadata_file_name = (
            "./metadata/{}/".format(network.show_active()) + str(token_id)
            + "-" + breed + ".json"
        )
        #verifica si ya existe el archivo sino lo crea
        if Path(metadata_file_name).exists():
            print("{} ya existe!".format(metadata_file_name))
        else:
            print("creando el archivo metadata {}".format(metadata_file_name))
            collectible_metadata["name"] = breed
            collectible_metadata["description"] = "Un adorable {} cachorro!".format(breed)
            print(collectible_metadata)
            image_to_upload = None
            #poner variable de entorno verdadera 
            #export UPLOAD_IPFS=true
            if os.getenv("UPLOAD_IPFS") == "true":
                #se define la ruta donde esta la imagen para subir a ipfs
                image_path = "./img/{}.png".format(breed.lower().replace("_" , "-"))
                #ejectuta la funcion para subir archivos a ipfs para subir la imagen
                image_to_upload = upload_to_ipfs(image_path)

            #image_to_upload = breed_to_image_uri[breed] if not image_to_upload
            #else image_to_upload
            
            collectible_metadata["image"] = image_to_upload

            #crea el archivo metadatos de manera local en la ruta especificada
            with open(metadata_file_name, "w") as file:
                json.dump(collectible_metadata, file)
            if os.getenv("UPLOAD_IPFS") == "true":
                #ejectuta la funcion para subir archivos a ipfs para subir la metadata
                upload_to_ipfs(metadata_file_name)






# http://127.0.0.1:5001
# curl -X POST -F file=@img/pug.png http:/localhost:5001/api/v0/add

#subir imagenes y metadata .JSON a IPFS
def upload_to_ipfs(filepath):
    with Path(filepath).open("rb") as fp:
        image_binary = fp.read()
        #tiene que estar levantado el nodo ipfs local
        ipfs_url = "http://localhost:5001"
        response = requests.post(
            ipfs_url + "/api/v0/add", files={"file": image_binary})

        ipfs_hash = response.json()["Hash"]
        filename = filepath.split("/")[-1:][0]
        uri = "https://ipfs.io/ipfs/{}?filename={}".format(ipfs_hash, filename)
        print(uri)
        return uri
    return None