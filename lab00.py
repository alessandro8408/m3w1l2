info    = []
eventi  = {
    0:  ('Terremoto', 1/30),
    1:  ('Incendio', 1/20),
    2:  ('Inondazione', 1/50),
}

def to_asset(asset: int):
    if (asset == 0):
        return "Edificio Primario".upper()
    if (asset == 1):
        return "Edificio Secondario".upper()
    if (asset == 2):
        return "Datacenter".upper()

def crea_dati(valore: int, percentuali: tuple):
    info.append(
        (
            valore,
            percentuali,
        )
    )

def perdita_annuale_frazionaria(evento: tuple, percentuale: int):
    return evento * percentuale

crea_dati(350000, (0.8, 0.6, 0.55))
crea_dati(150000, (0.8, 0.5, 0.4))
crea_dati(100000, (0.95, 0.6, 0.35))

risultato   = {}
titolo      = '\t\t\t'
for evento in eventi.keys():
    titolo  += eventi[evento][0] + '\t'

print(titolo)
for asset in range(len(info)):
    print(to_asset(asset), end='\t\t' if asset == 2 else '\t')
    for evento in eventi.keys():
        tmp         = int(info[asset][0] * info[asset][1][evento] * eventi[evento][1])
        asset_str   = to_asset(asset)
        evento_str  = eventi[evento][0]

        #risultato[(asset_str, evento_str)]  = tmp
        print(tmp, end='\t\t')
    print()
