from fastapi import FastAPI
from pyswip import Prolog

app = FastAPI()

prolog = Prolog()
prolog.consult("base-integracao.pl") #ok

# GET Listar sintomas do paciente (prolog-fatos)
@app.get("/sintomas/{paciente}")
def get_sintomas(paciente: str):
    sintomas = list(prolog.query(f"sintoma({paciente}, Sintoma)")) # Buscar sintomas na base Prolog
    return {"sintomas": [s["Sintoma"] for s in sintomas]} # Retornar os sintomas "JSON"}

# GET Listar todas as doencas e seus sintomas de acordo com a base de conhecimento (prolog-fatos)
@app.get("/doencas/")
def get_doencas():
    doencas = list(prolog.query("doenca(Doenca, Sintoma)")) # Buscar doencas na base Prolog
    return {"doencas": [{"doenca": d["Doenca"], "sintomas": d["Sintoma"]} for d in doencas]} # Retornar as doencas "JSON"

# GET Verificar possíveis doenças de um paciente de acordo com os sintomas informados (prolog-regra)
@app.get("/possivel_diagnostico/{paciente}")
def get_possiveis_doencas(paciente: str):
    possivel_doencas = list(prolog.query(f"possivel_doenca({paciente}, Doenca)"))
    return {"possiveis_doencas": [d["Doenca"] for d in possivel_doencas]}









