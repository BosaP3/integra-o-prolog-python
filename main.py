from fastapi import FastAPI, HTTPException
from pyswip import Prolog

app = FastAPI()

prolog = Prolog()
prolog.consult("base-integracao.pl")

# Função para verificar se o paciente existe na base de dados Prolog
def paciente_existe(paciente: str) -> bool:
    return bool(list(prolog.query(f"paciente({paciente})")))

# GET Listar sintomas do paciente (prolog-fatos)
@app.get("/sintomas/{paciente}")
def get_sintomas(paciente: str):
    
    if not paciente_existe(paciente):  
        raise HTTPException(status_code=404, detail=f"Paciente '{paciente}' não encontrado.")
    
    sintomas = list(prolog.query(f"sintoma({paciente}, Sintoma)"))  
    return {"sintomas": [s["Sintoma"] for s in sintomas]}   

# GET Listar todas as doenças e seus sintomas de acordo com a base de conhecimento (prolog-fatos)
@app.get("/doencas/")
def get_doencas():
    doencas = list(prolog.query("doenca(Doenca, Sintomas)")) 

    if not doencas:  # Verificar se não foram encontradas doenças
        raise HTTPException(status_code=404, detail="Nenhuma doença encontrada na base de conhecimento.")
    
    return {"doencas": [{"doenca": d["Doenca"], "sintomas": d["Sintomas"]} for d in doencas]} 

# GET Verificar possíveis doenças de um paciente de acordo com os sintomas informados (prolog-regra)
@app.get("/possivel_diagnostico/{paciente}")
def get_possiveis_doencas(paciente: str):

    if not paciente_existe(paciente):  
        raise HTTPException(status_code=404, detail=f"Paciente '{paciente}' não encontrado.")
    
    possivel_doencas = list(prolog.query(f"possivel_doenca({paciente}, Doenca)"))

    if not possivel_doencas:  # Verificar se não foram encontradas possíveis doenças
        raise HTTPException(status_code=404, detail=f"Nenhuma possível doença encontrada para o paciente '{paciente}'.")
    
    return {"possiveis_doencas": [d["Doenca"] for d in possivel_doencas]}
