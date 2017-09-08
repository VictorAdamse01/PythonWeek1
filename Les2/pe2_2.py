cijferICOR = 7.0
cijferPROG = 8.5
cijferCSN = 7.5
gemiddelde = (cijferCSN + cijferICOR + cijferPROG) / 3
beloning = (cijferCSN + cijferICOR + cijferPROG) * 30
overzicht = 'Mijn cijfers (gemiddeld een ' + str(round(gemiddelde,1)) + ') leveren een beloning van € ' + str(beloning) + ' op!'
print(overzicht)