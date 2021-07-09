# Old intro scene
label sc00_main:
    $ quick_menu = False
    scene black
    with fade
    play music test
    $ renpy.pause (1, hard=False)

    # dialogue starts
    $ quick_menu = True
    # screen especial para definir el ambiente "Nueva York, 1928"
    show scene1_alley
    with Dissolve(2)
    # bg de basureros
    # sonido de sirenas y gente corriendo mientras pisa charcos
    "Policía" "¡Alto ahí! ¡No tienes a dónde huir!"
    # aparece el sprite del MC, las expresiones se pueden definir una por una
    mc "Argh, ¿qué demonios está pasando?"
    "No sé a dónde ir... ¿cómo llego a dar ese cadáver a mi apartamento?"
    "No tengo tiempo para decirles que soy inocente; pensarán que estoy loco..."
    "Este olor a basura es intolerable, tengo que huir de aquí."
    "... Creo que mi única opción es ir con mi hermano ABOGADO."
    "El es el mejor abogado que conozco. Si hay alguien que pueda ayudarme, es él!"
    $ quick_menu = False
    $ renpy.pause (2, hard=False)

    # cambio de escena a una calle, lloviendo
    $ quick_menu = True
    "Si mal no recuerdo, aún tengo su tarjeta de negocios en mi cartera."
    mc "...Justo lo que me faltaba; su oficina está hasta el otro lado de la ciudad."
    "Tendré que ser cuidadoso para que nadie me reconozca."
    "Policía" "Oye tú, ¡¿qué haces aquí?!"
    "¡Maldición! Está sosteniendo mi hombro con demasiada fuerza."
    "... Juré jamás volver a hacer esto, pero parece que no tengo alternativa."
    "Si me capturan tratando de huir de la escena del crimen será el fin para mí."
    "Policía" "¡Deja de resistir! ¡Quedas bajo arresto!"
    "Parece que no tengo opción. Vamos, ¡tengo que concentrarme!"
    # comienza mini juego para regresar al pasado (o el mini tutorial)
    # podría ser más bien una animación

    # la escena regresa a los basureros
    mc "Eso estuvo demasiado cerca."
    "De verdad que no había hecho esto en mucho tiempo."
    "No desde el último incidente que tuve con AMIGO..."
    mc "..."
    "Bueno, basta de eso. Tengo que encontrar a ABOGADO."

    # comienza el loop del cap1
    $ first_loop = True
    jump sc00_loop

label sc00_loop:
    if first_loop:
        mc "¿Cómo puedo escapar de este callejón sin que me atrapen?"
    else:
        mc "Argh, qué idiotez... tengo que pensar en algo mejor."
    menu:
        "Acercarse al oficial sigilosamente y noquearlo por atrás.":
            jump sc00_l1
        "Esperar a que el oficial se distraiga y se salga del callejón.":
            jump sc00_l2
        "Golpear al oficial con la tapa del basurero en la cabeza." if first_loop == False:
            jump sc00_w

label sc00_l1:
    $ first_loop = False
    "Intentaré noquear a ese oficial de ahí. No parece ser muy fuerte entonces será fácil."
    "Con... cuidado..."
    $ renpy.pause (1, hard=True)
    "Ya casi..."
    $ renpy.pause (1, hard=True)
    mc "¡Te tengo!"
    "Policía" "¡AH! ¡SUÉLTAME CRIMINAL!"
    # gun shot
    "Antes de que pudiera reaccionar, recibí un balazo en el pie."
    mc "¡M****A!"
    "Ese hombre no es nada fuerte, pero si que tiene buenos reflejos..."
    # transicion de viaje en el tiempo express wooosh
    jump sc00_loop

label sc00_l2:
    $ first_loop = False

    ## el MC se tropieza al tratar de salir de entre los basureros y hace ruido
    ## esto alerta al policía, haciendo que regrese al callejón y lo espose

    # transicion de viaje en el tiempo express wooosh
    jump sc00_loop

label sc00_w:
    $ first_loop = False

    ## El policía se acerca a donde estaban escondidos y el MC lo toma por sorpresa
    ## El golpe fue lo suficientemente duro como para noquearlo
    ## De ahí, hay una transición a la escena con el hermano/Abogado

    jump sc00_afterloop

label sc00_afterloop:
    ## diálogo con el hermano

    ## lo vuelven a atrapar y se muestra el titulo del juego al final (señalando el comienzo)

    return
