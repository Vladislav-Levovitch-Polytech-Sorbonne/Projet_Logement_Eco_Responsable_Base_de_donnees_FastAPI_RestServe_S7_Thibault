from fastapi import FastAPI
#from pydantic #Ouf pour les setter, getter, creation json, exploitation json
app = FastAPI()

#http://localhost:8000/docs
#http://localhost:8000/docs#
# Voir les Post 
# Voir les template from fastapi import FastAPI, Request

@app.get("/")
async def root():
    return {"message": "Hello World"}

#@app.get("/etudiants/{id}/nom/")
#async def nom_etu( id : int ):
#    return "Test" #Equ de la recherhce dans la base 

#@app.get("/etu/")
#async def nom_etu( id : int=1, nom: str="" ):
#    return "etudiant num "+str(id) + nom #Equ de la recherhce dans la base 


