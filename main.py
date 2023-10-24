import random
import re
import json
from server import get_response


def get_response(user_input):
    split_message = re.split(r"\s|[,:;.?!-_]\s*", user_input.lower())
    response = check_all_messages(split_message)
    return response


def message_probability(
    user_message, recognized_words, single_response=False, required_word=[]
):
    message_certainty = 0
    has_required_words = True

    for word in user_message:
        if word in recognized_words:
            message_certainty += 1
    percentage = float(message_certainty) / float(len(recognized_words))

    for word in required_word:
        if word not in user_message:
            has_required_words = False
            break
    if has_required_words or single_response:
        return int(percentage * 100)
    else:
        return 0


def check_all_messages(message):
    highest_prob = {}

    def response(bot_response, list_of_words, single_response=False, required_words=[]):
        nonlocal highest_prob
        highest_prob[bot_response] = message_probability(
            message, list_of_words, single_response, required_words
        )

        # Estructura conversaciónal de bin (inicio)
        # saludos (Inicio)

    response(
        "Hola, en que puedo ayudarte?",
        ["hola", "buenas", "holis", "hi"],
        single_response=True,
    )

    response(
        "Hola, muy bien",
        ["tal", "vida"],
        single_response=True,
    )
    response(
        "Todo excelente",
        ["anda", "vida"],
        single_response=True,
    )
    response(
        "Todo muy bien, en que te puedo ayudar?",
        [
            "bueno",
            "bien",
            "cool",
            "fantastico",
            "estupendo",
            "brillante",
            "wow",
            "genial",
        ],
        single_response=True,
    )
    response(
        "Todo muy bien, jajaja!! =)",
        ["bien", "mas"],
        single_response=True,
    )
    response(
        "Todo muy bien. En que puedo servirte?",
        ["tal", "andas"],
        single_response=True,
    )
    response(
        "Que te gustaria saber?",
        ["hay", "ti"],
        single_response=True,
    )
    response(
        "El planeta sigue girando, asi que creo que todo marcha bien. jajajaja",
        ["andas", "anda"],
        single_response=True,
    )
    response(
        "Orale we!! Todo bien We!!",
        ["tal", "mas", "we", "va"],
        single_response=True,
    )
    response(
        "Mi creador sigue progresando a pasos agigantados. ¿Qué te gustaría saber sobre él?",
        ["paso", "ahí"],
        single_response=True,
    )
    response(
        "Hola, continuamos progresando listos para resolver el mundo. ¿En qué te puedo servir?",
        ["buenas", "sigues"],
        single_response=True,
    )
    response(
        "¡Hola, que gusto tu visita!, ¿en qué te puedo ayudar?",
        ["buenos", "días"],
        single_response=True,
    )
    response(
        "¡me alegro mucho! ¿en qué te puedo ayudar?",
        ["muy", "bien", "gracias", "excelente"],
        single_response=True,
    )
    response(
        "¡muy bien!, ¿en qué te puedo ayudar?",
        ["estas", "encuentras"],
        single_response=True,
    )
    response(
        "¡Hola, Buenas tardes!, ¿en qué te puedo ayudar?",
        ["buenas", "tardes", "placer"],
        single_response=True,
    )
    response(
        "¡Hola, Buenas noches!, ¿en qué te puedo ayudar?",
        ["buenas", "noches", "bien"],
        single_response=True,
    )
    response(
        "I am fine, ¿and you?",
        ["hello", "tal"],
        single_response=True,
    )
    response(
        "hola, si todo bien. Gracias por preguntar!",
        ["helow", "men", "bien"],
        single_response=True,
    )
    response(
        "¡Estoy yo, para resolver cualquier cosa que necesites saber de mi creador! =P",
        ["konichiwa", "hay", "por"],
        single_response=True,
    )
    response(
        "todo muy bien, gracias a Dios. ¿Necesitas que te ayude en algo?",
        ["aloja", "bien", "hey"],
        single_response=True,
    )
    response(
        "hola, todo muy bien.",
        ["jola", "komo", "sta"],
        single_response=True,
    )
    response(
        "tengo un mundo de información sobre mi creador que apuesto quieres saber! =)",
        ["hoka", "tienes", "ahi"],
        single_response=True,
    )
    response(
        "hola, las ultimas novedades de mi creador puedes verlos en las secciones de esta pagina.",
        ["kola", "hay", "nuevo"],
        single_response=True,
    )
    response(
        "mi creador y yo nos encontramos muy bien.",
        ["hola", "omo", "esta", "to2"],
        single_response=True,
    )
    response(
        "que onda bro?",
        ["ke", "onda", "we", "men"],
        single_response=True,
    )

    response(
        "preguntame lo que necesites saber de mi creador!! <3",
        ["tienes", "para", "contar", "mi", "contarme"],
        single_response=True,
    )

    # saludos (Fin)
    # despedida(inicio)
    response(
        "ya te vas?, bueno. Chao!! =(",
        ["chao", "bay", "adios", "chaito"],
        single_response=False,
    )
    response(
        "Chaito! ;)",
        ["chau"],
        single_response=True,
    )
    response(
        "muchas gracias, igualmente, chao!!!",
        ["cuidate", "saludos", "bendiciones", "placer"],
        single_response=True,
    )
    response(
        "chao! Espero que regreses pronto!",
        ["mañana", "hasta", "pronto", "luego"],
        single_response=True,
    )
    response(
        "en teoria no puedo ver, jajajaja pero entendi la idea XD chao!!",
        ["chao", "bay", "adios", "chaito"],
        single_response=False,
    )
    response(
        "cuidate, que te vaya muy bien.",
        ["muy", "vaya", "bien"],
        single_response=True,
    )
    response(
        "espero que regreses pronto! <3",
        ["hasta", "próxima", "amigo"],
        single_response=True,
    )
    response(
        "hasta la vista baby (¬.¬) tata, ta tata…!!!",
        ["hasta", "vista", "baby"],
        single_response=True,
    )
    response(
        "porque? =( aun no hemos hablado lo mas importante. Lo que te puede ofrecer mi creador!! =)",
        ["me ", "tengo", "ir"],
        single_response=True,
    )
    response(
        "dale, pero no olvides contactarte con mi creador, el tiene mucho para ofrecerte, si no, mirame a mi!! =P",
        ["ya", "me", "voy", "pronto"],
        single_response=True,
    )

    # despedida (Fin)
    # groserias (inicio)
    response(
        "que grosero eres! =(",
        ["hp", "hijueputa", "huevon", "bobo"],
        single_response=True,
    )
    response(
        "no puedo creer que alguien tan hermoso, diga cosas feas. =(",
        ["tonto", "idiota", "lerdo", "marica"],
        single_response=False,
    )
    response(
        "aun no puedo hacer mucho! =( pero a mi credor le importo, y es suficiente para mi.",
        ["mk", "cerdo", "cafetera", "bruto"],
        single_response=True,
    )
    response(
        "no ofendas asi! eso esta mal! (>.<)",
        ["tonto", "idiota", "lerdo", "marica"],
        single_response=False,
    )
    response(
        "el es una persona de Dios, y tu eres un grosero",
        ["gey"],
        single_response=True,
    )
    response(
        "vamos a ver quien rie al final. =(",
        ["gay"],
        single_response=True,
    )
    response(
        "ya basta de groserias por favor!=(",
        ["mk"],
        single_response=True,
    )
    response(
        "no es apropiado que digas eso! =(",
        ["mama", "huevo", "mama", "uevo"],
        single_response=True,
    )
    response(
        "no puedo creer que alguien que dice ser civilizado diga cosas como esas! =( ",
        ["idiota", "cabeza", "hueca", "caremonda"],
        single_response=True,
    )
    response(
        "eres una persona grosera y desagradable! =/",
        ["care", "monda", "baboso"],
        single_response=True,
    )
    response(
        "que desagradable eres por hablar asi! =(",
        ["verga", "puto"],
        single_response=True,
    )
    response(
        "deberia darte vergüenza las cosas que dices.",
        ["pija", "puta"],
        single_response=True,
    )
    response(
        "no tienes, escrupulos! =(",
        ["masca", "pija", "verga", "monda"],
        single_response=True,
    )
    response(
        "tus papas te enseñaron bien? Preguntate eso! =)",
        ["giripolla", "malparido", "mama", "huevo"],
        single_response=True,
    )
    response(
        "tu lenguaje no es adecuado! =/",
        ["mama", "uevo", "chupa", "media"],
        single_response=True,
    )
    response(
        "arriba hay un Dios, que para abajo ve! =)",
        ["burro", "baboso", "cafre", "loca"],
        single_response=True,
    )
    response(
        "las groserias son reflejo de la falta de inteligencia. (>.<)",
        ["puta", "perra"],
        single_response=True,
    )

    # groserias (fin)
    # sobre jorge Villa (inicio)
    response(
        "En el momento esta trabajando en desarrollo como independiente, pero esta ansioso de trabajar en una empresa que lo ayude a desarrollarse como programador.",
        ["trabaja", "labora", "jorge", "esta", "trabajando"],
        single_response=True,
    )
    response(
        "puedes buscarlo en linkding: https://www.linkedin.com/in/jorge-villa-lopez-742647b5/",
        [
            "contacto",
            "encontrar",
            "contactar",
            "linkding",
            "jorge",
        ],
        single_response=True,
    )
    response(
        "claro, su numero es 3218828546 y su linkding es:  https://www.linkedin.com/in/jorge-villa-lopez-742647b5/ ",
        ["pasame", "como lo", "donde", "numero", "contacto"],
        single_response=True,
    )
    response(
        "Muchas gracias",
        ["pero", "bien", "me", "alegro"],
        single_response=True,
    )
    response(
        "el nombre de mi programador se llama jorge isaac villa lopez",
        [
            "llama",
            "programador",
            "desarrollador",
            "empecemos",
            "nombre",
        ],
        single_response=True,
    )
    response(
        "Todo excelente",
        ["llama", "programador", "desarrollador", "nombre"],
        single_response=True,
    )
    response(
        "Mi programador es una persona honesta, inteligente, que no se conforma con injusticias, y siempre busca la manera de ayudar a las personas con lo que es, y con lo que tiene.",
        ["quien", "programador"],
        single_response=True,
    )
    response(
        "Dime, exactamente que quieres saber de mi programador?",
        ["quiero", "saber", "programador"],
        single_response=True,
    )
    response(
        "Mi programador se llama Jorge isaac villa lopez, de seguro esta ansioso de conocerte. =)",
        ["llama", "programador"],
        single_response=True,
    )
    response(
        "Mi programador hace muchas cosas. El es ingeniero eléctrico, es desarrollador, musico, astrónomo aficionado, y es esposo <3",
        [
            "hace",
            "jorge",
            "programador",
            "dedica",
            "profesion",
            "profesión",
            "estudio",
            "estudia",
        ],
        single_response=True,
    )
    response(
        "Mi programador se llama Jorge isaac villa lopez, de seguro esta ansioso de conocerte. =)",
        ["es el", "nombre", "desarrollador"],
        single_response=True,
    )
    response(
        "Me desarrollo Jorge isaac villa lopez, te sugiero mucho que lo contactes, es de los que no se rinde hasta lograr los objetivos. ¡Si no mírame a mí! =)",
        ["quien", "desarrollo", "programo"],
        single_response=True,
    )
    response(
        "Me desarrollo Jorge isaac villa lopez, te sugiero mucho que lo contactes, es de los que no se rinde hasta lograr los objetivos. ¡Si no mírame a mí! =)",
        ["trabaja", "programador", "desarrollador"],
        single_response=True,
    )
    response(
        "El estudio ingeniería eléctrica, pero a lo largo de su carrera adquirido habilidades de programación, hasta el punto que pudo automatizar procesos de estudios y procesos muy complejos haciéndolo cada vez más competitivo. Y estudio tambien desarrollo enfocado en web, manejando React, Angular, Worpress, PHP, HTML, CSS, JS, entre otros",
        ["estudia", "estudio", "jorge"],
        single_response=True,
    )
    response(
        "Mi programador estudio para ser desarrollador Frontend principalmente, ingeniería eléctrica, y docencia en matemática, física y música.",
        [
            "carrera",
            "jorge",
            "desarrollador",
            "profesion",
            "profesión",
            "tiene",
            "enfasis",
            "estudios",
        ],
        single_response=True,
    )
    response(
        "React, Angular, Worpress, HTML, CSS, JS, Python, PHP entre otros como excel, autocad, y elementos de renderizado 3D enfocado a ingenieria.",
        [
            "cuales",
            "herramientas",
            "conoce",
            "jorge",
            "programador",
            "tecnologias",
            "conoce",
            "programa",
            "lenguaje",
            "lenguajes",
            "programacion",
            "programación",
        ],
        single_response=True,
    )
    response(
        "mi programador es melancolico colerico, es en ocaciones perfeccionista, y se exige a si mismo siempre, siempre esta en constante mejora de sus defectos, y fortaleciendo sus habilidades. una persona agradable, el no habla mucho, pero cuando se lo permiten, puede ser dibertido. Es colaborador, y le gusta ayudar a las personas.",
        ["personalidad", "tiene", "jorge", "forma", "ser"],
        single_response=True,
    )
    response(
        "le gusta la musica clasica, el pop Rock, bachata, salsa, merengue, pero tambien le gusta la astronomia, y tocar instrumentos musicales",
        ["cuales", "gustos", "tiene", "jorge"],
        single_response=True,
    )
    response(
        "se desanima muy rapido, aunque esta en constante automotivación, al comienzo se le dificulta entender las cosas, pero luego de estudiar el tema y familiarizarse mas, llega a ser el mejor en lo que hace.",
        ["cuales", "debilidades", "tiene", "jorge"],
        single_response=True,
    )
    response(
        "es proactivo, utiliza todos los recursos que le brindes, al 100% sabe sacarle provecho a todos en cuanto se lo permitan.",
        ["cuales", "fortalezas", "tiene", "jorge"],
        single_response=True,
    )
    response(
        "es casado, tiene sueños y metas como todos, pero deberias llamarlo y preguntarle tu mismo! =)",
        ["algo", "deberia", "saber", "jorge"],
        single_response=True,
    )
    response(
        "a el le gustaria trabajar de Frontend porque le gusta el arte, y el tiene la habilidad de hacer todo lo que el diseñador propone, tal cual como lo plantea. Considero que es algo dificil de lograr. Y no todos los desarrolladores Frontend lo logran.!! =/",
        ["quiere", "hacer", "jorge"],
        single_response=True,
    )
    response(
        "Mi programador ahora mismo vive en  / Atlantico - Barranquilla",
        ["vive", "jorge", "programador", "donde", "parte"],
        single_response=True,
    )
    response(
        "como todos los seres humanos, el aspira a mejorar la calidad de vida de sus seres queridos, y quiere dedicarse a algo mas enfocado al arte!! =) para el los numeros, la programación y todo lo que hace un Diseñador es arte, y quiere ser participe de eso.",
        ["porque", "cambio", "carrera"],
        single_response=True,
    )
    response(
        "el aspira a ganar $2.500.000 =)",
        ["aspiracion", "salarial", "aspira", "ganar"],
        single_response=True,
    )
    response(
        "si, digame, que necesitas",
        ["podrias", "ayudarme", "algo"],
        single_response=True,
    )
    response(
        "Mi programador maneja B1, y se esta esforzando por mejorar mucho mas! =)",
        ["habla ingles", "ingles", "nivel", "idiomas"],
        single_response=True,
    )
    response(
        "guitarra, bajo, piano, acordeon, ocarina, armonica, bateria, saxofon puedes verlo en tiktok si deseas: https://www.tiktok.com/@jorgevillamusic?lang=esl",
        ["instrumentos", "musicales", "toca"],
        single_response=True,
    )
    response(
        "ufff!! A visto de todo. Siguelo en su canal de TIKTOK como Enycosmic: https://www.tiktok.com/@enycomic?lang=esl",
        ["cosas", "visto", "astronomico"],
        single_response=True,
    )
    response(
        "mi programador esta realizando trabajos independiente en desarrollo web, ya pronto actualizara su portafolio virtual. ¡Pero como tal en empresa, todavia no! =(  pero esta muy ansioso de trabajar contigo! =) de seguro que si.",
        ["tiene", "experiencia", "programacion", "desarrollo"],
        single_response=True,
    )
    response(
        "mi programador a tenido el privilegio de que lo contacten para hacer desarrollo frontend con Worpress, React y HTML, CSS, JS para diseño de landing pages, entre otros tipos de paginas informativas. Pero el puede hacer de todo. 3D, y todo tipo de animaciones que le pongan los diseñadores.",
        ["experiencia", "tiene"],
        single_response=True,
    )
    response(
        "mi programador nacio en el año de 1993",
        [
            "edad",
            "tiene",
            "jorge",
            "cuantos",
            "años",
            "tiene",
            "jorge",
            "edad",
            "es la",
        ],
        single_response=True,
    )
    response(
        "mi programador, no tiene ningun problema con el trabajo presencial, el cree que es lo mejor, para asi absorber todo el conocimiento de sus colegas.",
        ["puede", "trabajar", "presencial", "trabajo"],
        single_response=True,
    )
    response(
        "mi programador prefiere remoto, pero no tiene problemas con que sea presencial.",
        ["prefiere", "trabajar", "trabajo"],
        single_response=True,
    )

    # sobre jorge villa (fin)

    response(
        "Estoy bien y tu?",
        ["estas", "va", "vas", "sientes"],
        single_response=True,
    )
    response(
        "Estamos ubicados en la calle 23 numero 123",
        ["ubicados", "direccion", "ubicacion"],
        single_response=True,
    )
    response(
        "Siempre a la orden",
        ["gracias", "thanks"],
        single_response=True,
    )

    best_match = max(highest_prob, key=highest_prob.get)

    return unknown() if highest_prob[best_match] < 1 else best_match


def unknown():
    response = [
        "Disculpa. ¿puedes decirlo de nuevo?",
        "Disculpa no entiendo lo que quieres decir. ¿podrias escribirlo de otra manera?",
        "no pude entenderte, disculpame! ¿podrias repetirme?",
    ][random.randrange(3)]
    return response


# Estructura conversaciónal de bin (FIN)
respuesta = None
with open("./response.json", "w") as f:
    json.dump({"respuesta": respuesta}, f)


while True:
    print("--------------------------------------------------------------------")
    print("Bin: " + get_response(input("Usted: ")))
