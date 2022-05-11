import bottle
import model

vislice=model.Vislice()

@bottle.get("/img/<file>")
def staticne_slike(file):
    return bottle.static_file(file, root="img")

@bottle.get("/")
def prikazi_osnovno_stran():
    return bottle.template('index')

@bottle.post("/igra/")
def nova_igra():
    novi_id = vislice.nova_igra()
    return bottle.redirect(f"/igra/{novi_id}")

@bottle.get("/igra/<id_igre:int>")
def pokazi_igro(id_igre):
    return bottle.template("igra", igra=vislice.igre[id_igre][0])

 def preveri_vnos()

@bottle.post("/igra/<id_igre:int>")
def ugibaj(id_igre):
    crka=bottle.request.forms.getunicode('crka').upper()
    if preveri_vnos(crka):
        vislice.ugibaj(id_igre, crka)
        return pokazi_igro(id_igre)
    else:
        return 





#to je na dnu
bottle.run(reloader=True, debug=True)