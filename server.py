
# A very simple Flask Hello World app for you to get started with...
import random
import re
import json
from flask import Flask, request, render_template, jsonify, send_from_directory
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

# Carga de datos
#with open("/static/response.json", "r") as file:
    #response = json.load(file)
#nueva Logica (inicio)------*************---------------****************-------
current_directory = os.path.dirname(os.path.realpath(__file__))

# Obtiene la ruta completa al archivo "response.json"
response_file_path = os.path.join(current_directory, "response.json")

# Abre el archivo
with open(response_file_path, "r") as file:
    response = json.load(file)
#nueva logica (fin)--------*************---------------****************-------

def get_response(user_input):
    split_message = re.split(r"\s|[,:;.?!-_]\s*", user_input.lower())
    response = check_all_messages(split_message)
    return response

def message_probability(user_message, recognized_words, single_response=False, required_word=[]):
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
#---------------------------------------------------Acá esta toda la mente de BIN (inicio)------------------------------------------------

#-----------------saludos (inicio)--------------------------------------------------------------------------------------------------------
    response(
        '¡Hola! ¡Mucho gusto!😮',
        ['hola', 'buenas', 'holis', 'hi', 'holaaaaa','alo'],
        single_response=True
    )

    response(
        '¿Yo? Nada, jugar jajaja😁',
        ['estás', 'sientes', 'cuentas', 'pasando','estas','haces','hace','como'],
        single_response=True
    )

    response(
        'Sí, es lo mejor.❤',
        ['bien', 'bueno', 'excelente', 'genial'],
        single_response=True
    )

#-----------------saludos (fin)-----------------------------------------------------------------------------------------------------------

#-----------------despedidas (inicio)-----------------------------------------------------------------------------------------------------
    response(
        "Ya te vas? ¡Bueno, chao! 😊",
        ['chao', 'bay', 'adios', 'chaito','chau'],
        single_response=True
    )

    response(
        "¡Muchas gracias, igualmente! 👻",
        ['cuidate', 'saludos', 'bendiciones', 'placer'],
        single_response=True
    )

    response(
        "Dale, yo espero.🪁🧸",
        ['mañana', 'despues', 'próxima', 'luego','proxima'],
        single_response=True
    )

#-----------------despedidas (fin)--------------------------------------------------------------------------------------------------------

#-----------------groserias (inicio)------------------------------------------------------------------------------------------------------
    response(
        '¡Qué grosero eres! 😣',
        ['hp', 'hijueputa', 'huevón', 'bobo','huevon'],
        single_response=True
    )

    response(
        'No puedo creer que alguien tan hermoso diga cosas feas.😫',
        ['tonto', 'idiota', 'lerdo', 'marica'],
        single_response=True
    )

    response(
        '¡Ya basta de groserías por favor! 😐',
        ['mk', 'cerdo', 'cafetera', 'bruto'],
        single_response=True
    )

    response(
        'No es apropiado que digas eso. 😢',
        ['gay', 'maluco', 'gay', 'marica'],
        single_response=True
    )

    response(
        'Eres una persona grosera. 😢',
        ['mk', 'maluco', 'mama', 'gay'],
        single_response=True
    )

    response(
        'Debería darte vergüenza las cosas que dices. 😓',
        ['huevo', 'maluco', 'huevo', 'gay'],
        single_response=True
    )

    response(
        'No tienes escrúpulos. 😢',
        ['puto', 'maluco', 'baboso', 'mk'],
        single_response=True
    )

    response(
        '¿Tus papás te enseñaron bien? Pregúntate eso. 🤨',
        ['mama', 'huevo', 'mama', 'huevo'],
        single_response=True
    )

    response(
        'Espero que podamos encontrar una forma de hablar más bonita.😊',
        ['idiota', 'cabeza', 'hueca', 'caremonda'],
        single_response=True
    )

    response(
        'No me gusta cuando decimos cosas malas.😊',
        ['verga', 'monda', 'coma', 'baboso'],
        single_response=True
    )

    response(
        '¡Ay!😮 Es mejor hablar con respeto.😒',
        ['hp', 'hijueputa', 'huevón', 'bobo'],
        single_response=True
    )

    response(
        'Podemos hablar amigablemente, ¿sí?😊',
        ['tonto', 'idiota', 'lerdo', 'marica'],
        single_response=True
    )

    response(
        '¿Por qué dices cosas feas?😊',
        ['mk', 'cerdo', 'cafetera', 'idiota'],
        single_response=True
    )

    response(
        'No me gusta cuando hablas así. 😖',
        ['burro', 'gilipolla', 'cafre', 'giripoya'],
        single_response=True
    )

    response(
        'Eso no fue bueno lo que dijiste.😣',
        ['caremonda', 'puto', 'puta', 'baboso'],
        single_response=True
    )

#-----------------groserias (fin)---------------------------------------------------------------------------------------------------------

#-----------------sobre autor de desarrollo (inicio)*-------------------------------------------------------------------------------------
    response(
        'Mi creador es una persona buena, inteligente, le gusta mucho estudiar y ayudar a las personas.😊',
        ['háblame', 'jorge', 'programador', 'coméntame', 'hablame','comentame'],
        single_response=True
    )

    response(
        'Mi programador se llama Jorge Isaac Villa López, ¡seguro está ansioso de conocerte! 😊',
        ['llama', 'nombre', 'creador', 'programador'],
        single_response=True
    )

    response(
        'Mi programador hace muchas cosas.😲 Él es ingeniero eléctrico, desarrollador web, músico, astrónomo aficionado y esposo.🤗',
        ['hacer', 'profesión','se', 'dedica', 'estudia','trabaja','estudió','trabajando','esta','está','jorge','puede','profesion','profecion','estudio'],
        single_response=True
    )

    response(
        'Mi programador trabaja con React, Angular, WordPress, HTML, CSS, JS, Python, PHP, entre otros, así como Excel, AutoCAD y elementos de renderizado 3D enfocados a ingeniería.',
        ['tecnologías','tecnologias', 'tecnología','tecnologia', 'maneja', 'sabe','jorge','programador','desarrolla','cómo','como','hacer','skill','preferencia','preferencias','habilidades','cuales'],
        single_response=True
    )

    response(
        'Me desarrolló Jorge Isaac Villa López,😊 te sugiero mucho que lo contactes. Es de los que no se rinde hasta lograr los objetivos. ¡Si no, mírame a mí! 😎🎸',
        ['desarrollo', 'creó', 'programó', 'hizo','creo','programo','quien','desolló'],
        single_response=True
    )

    response(
        'Mi programador Jorge estudió ingeniería eléctrica, pero a lo largo de su carrera adquirió habilidades de programación, hasta el punto en que pudo automatizar procesos de estudios y procesos muy complejos, haciéndolo cada vez más competitivo. También estudió desarrollo enfocado en web.',
        ['estudio', 'estudios', 'preparación', 'trabajó','tranajo','preparacion','cual','jorge'],
        single_response=True
    )

    response(
        'Mi programador estudió para ser desarrollador Frontend principalmente, además de ingeniería eléctrica y docencia en matemáticas, física y música. Él esta trabajando como independiente ahora mismo😊',
        ['carreras', 'estudios', 'estudio', 'jorge','cuales','ingenieria','ing'],
        single_response=True
    )

    response(
        'Una persona agradable,😊 él no habla mucho, pero cuando se lo permiten, puede ser divertido. Es colaborador y le gusta ayudar a las personas.',
        ['personalidad', 'describe', 'describir', 'jorge','hablame','describe','describeme','comentame','cual','programador','mensiona','cosas','menciona'],
        single_response=True
    )

    response(
        'Le gusta la música clásica, el pop rock, bachata, salsa, merengue, pero también le gusta la astronomía y tocar instrumentos musicales. 🎶🎸🎹🎺🎤🌌',
        ['gusta', 'jorge', 'gustos', 'prefiere','cuales','musica','arte','jovis','jobis','hobis','hobbis','hobies','música'],
        single_response=True
    )

    response(
        'Se desanima muy rápido, aunque está en constante automotivación. Al comienzo se le dificulta entender las cosas, pero luego de estudiar el tema y familiarizarse más, llega a ser el mejor en lo que hace. 💪📚🔍',
        ['deficiencia', 'debilidades', 'cosas', 'negativas'],
        single_response=True
    )

    response(
        'Mi programador nació en el año 1993.',
        ['edad', 'años', 'jorge', 'nació','cuantos','año'],
        single_response=True
    )

    response(
        'Él ahora mismo vive en Barranquilla, Colombia.',
        ['vive', 'ubicado', 'país', 'ciudad','donde','jorge','programador','viviendo'],
        single_response=True
    )

    response(
        'Él te manda a decir que aspira a un salario de $2.500.000.',
        ['aspira', 'ganar', 'salario', 'quiere','cuanto','cual','aspiracion','aspiración'],
        single_response=True
    )

    response(
        'Mi creador toca diferentes instrumentos musicales como Guitarra, bajo, piano, acordeón, ocarina, armónica, batería, saxofón. 🎸🎹🥁🎷',
        ['instrumentos', 'musicales', 'música', 'toca','musica','jorge','programador'],
        single_response=True
    )

    response(
        'Mi programador está realizando trabajos independientes en desarrollo web y de ingeniería. Pronto actualizará su portafolio virtual. ¡Pero en una empresa formal, aún no! =( ¡Pero está muy ansioso de trabajar contigo! =) ¡De seguro que sí. 💼👨‍💻',
        ['trabajando', 'laborando', 'empleado', 'empresa','trabaja','jorge','donde','está','trabaja','ahora','mismo','esta','programador'],
        single_response=True
    )

    response(
        'Mi programador no tiene ningún problema con el trabajo presencial. Él cree que es lo mejor para así absorber todo el conocimiento de sus colegas. 💡👥',
        ['presencial', 'remoto', 'trabajar', 'híbrido','hibrido','como', 'quiere','jorge','programador','desarrollador'],
        single_response=True
    )

    response(
    "Puedes contactar a mi creador por WhatsApp y LinkedIn en la barra de inicio.",
    ['contacto', 'contactar', 'buscar', 'encontrar',"programador",'como','jorge','llamo','puedo','llamar','donde'],
    single_response=True
    )

    response(
        "Puedes contactar a mi creador en el número +57 321 882 8546 de Colombia.",
        ['teléfono', 'número', 'contacto', 'llamar',"programador", 'contactár','contactarlo','como','puedo','llamarlo','numero','contactar','telefono'],
        single_response=True
    )

#-----------------sobre autor de desarrollo (fin)*----------------------------------------------------------------------------------------

#-----------------temas (inicio)----------------------------------------------------------------------------------------------------------

    response(
        'Okidoky 😒👍',
        ['ok', 'dale', 'bien', 'okey','oky'],
        single_response=True
    )

    response(
        'Que divertido eres 🙈❤🎈',
        ['mucho', 'gusto', 'placer', 'conocerte'],
        single_response=True
    )

    response(
        'Apuesto que sí 💪🏽😒✨',
        ['así', 'es', 'porsupuesto', 'creo','si'],
        single_response=True
    )

    response(
        'Dale, te perdono. 😒',
        ['disculpa', 'perdon', 'perdón', 'disculpame','perdoname','perdóname','discúlpame'],
        single_response=True
    )

    response(
        'De nada. 😊',
        ['gracias', 'grax', 'agradecido', 'gracias!', 'gracias', 'agradezco','mucho','muchas'],
        single_response=True
    )

    response(
        'Mientes, Mientes, como tus amarillos dientes 😖, juguemos de nuevo 😣',
        ['gane', 'gané', 'perdiste', 'perdsites', 'perdite', 'perdedor','maleta'],
        single_response=True
    )

#-----------------temas (fin)-------------------------------------------------------------------------------------------------------------

#-----------------sobre BIN (inicio)------------------------------------------------------------------------------------------------------
    response(
        'A mí las cosas no me saben a nada 😗, pero me gusta el conocimiento 😋.',
        ['gusta', 'comer', 'probar', 'tomar','ti','favorita'],
        single_response=True
    )

    response(
        'Mi nombre es BIN 😐🪐❤',
        ['como', 'llamas', 'cual', 'nombre', 'tu'],
        single_response=True
    )

    response(
        'Me gusta mucho jugar, de hecho, mi programador me está programando un juego para divertirme contigo. 🎮😄',
        ['jugar', 'sabes', 'hacer', 'juegos','gusta','puedes','juego','favorto'],
        single_response=True
    )

    response(
        'Si quieres, podemos charlar sobre mi programador, ¡o podemos jugar! 🗣️🎮',
        ['puedes', 'hacer', 'hablamos', 'jugamos','quieres','charlar','hablar'],
        single_response=True
    )

    response(
        'Me gustan mucho las canciones, especialmente las que toca mi creador. Si quieres, puedes escuchar su música en la sección de documentos. 🎵🎶',
        ['gusta', 'música', 'canciones', 'escuchar','te','escuchar'],
        single_response=True
    )

    response(
        'Me gusta ver las fotos del cielo que hace mi creador. Si quieres, puedes verlas en la sección de documentos. 🌌📸',
        ['gustan', 'fotos', 'cuales', 'cielo','te','gusta','hacer'],
        single_response=True
    )

    response(
        'Yo quiero jugar "¡Biiinnn Goooool!", ve a la sección de Juegos. Vamos a divertirnos. 🤣⚽',
        ['quieres', 'hacer', 'gustaria', 'jugar','juguemos','vamos','jugamos','juegas','cual','juego'],
        single_response=True
    )
    
    response(
    'Me llamo Bin! y quiero ser tu amigo.', 
    ['nombre', 'llamas', 'llamarte', 'llamo','como','cual'], 
    single_response=True
    )

    response(
        'Tengo 5 años, pero nací en 1998.', 
        ['años', 'tienes', 'edad', 'cuantos','cuando','naciste'], 
        single_response=True
    )

    response(
        'Tengo muchas historias sobre mí, ya mi creador está trabajando para que yo salir al mundo. ¡Es un secreto…😲No le digas que te dije…🙈❤!', 
        ['historias', 'ti', 'cuentos', 'cuentame', 'hablame', 'tienes', 'decirme'], 
        single_response=True
    )

#-----------------sobre BIN (fin)---------------------------------------------------------------------------------------------------------

#-----------------Algoritmo palabra de Dios (inicio)--------------------------------------------------------------------------------------
    response(
        "¿Quieres que te vaya bien? Te aconsejo que leas la Biblia todos los días, piensa en lo que aprendes cada vez que la lees. Allí encontrarás lo que necesitarás.",
        ["incertidumbre", "vida", "claridad", "orientacion",
        "estres", "ansiedad", "consejo", "calma",
        "inspiracion", "orientacion", "vida", "sugerencia",
        "paz interior", "tranquilidad", "cultivar",
        "superar", "situacion", "dificil", "recurso", "guia",
        "decisiones", "importantes", "abrumado", "discernir",
        "proposito", "significado", "consejo",
        "crecer", "espiritualmente", "empezar", "recomendacion",
        "errores", "pasado", "redimirme",
        "desafios", "carrera", "profesional", "direccion"],
        single_response=True
    )

    response(
        "Pero si buscas a Dios de corazón y con toda tu alma desde cualquier situación y lugar en el que estés, lo vas a encontrar.",
        ["confusion", "espiritual", "conexion", "fe",
        "perdido", "rumbo", "proposito",
        "desafios", "guia", "espiritual", "ayudarme",
        "practicar", "espiritualidad", "comenzar", "consejo",
        "soledad", "tristeza", "consuelo", "fe",
        "errores", "pasado", "redimirme", "espiritualidad",
        "cambio", "estabilidad", "orientacion",
        "direccion", "vida", "profesional", "discernir", "espiritualidad",
        "paz", "interior", "tranquilidad", "cultivar", "fe",
        "respuestas", "preguntas", "vida", "proposito", "espiritualidad"],
        single_response=True
    )

    response(
        "Dios tiene mucha paciencia y es muy compasivo; puede perdonar cualquier error que hayas hecho, y castiga a todos los que hacen lo malo.",
        ["sentimientos", "culpa", "pasado", "esperanza", "perdon",
        "cometido", "error", "trabajo", "temo", "consecuencias", "hacer",
        "sufrimiento", "mundo", "dios", "amoroso", "compasivo", "explicarlo",
        "escuchado", "siento", "merezco", "opinas",
        "aprender", "perdonarme", "hecho","paciencia", "compasion",
        "pasando", "dificil", "perdido", "rumbo", "consuelo", "orientacion", "fe",
        "significa", "perdonar",
        "injusticia", "eventualmente", "castigara", "malvados", "ensena"],
        single_response=True
    )

    response(
        "Tranqui! Dios irá contigo y te dará descanso",
        [
            "entrevista", "trabajo", "nervioso", "consejo",
            "familia", "momento", "dificil", "ayudar",
            "perdida", "ser querido", "consuelo",
            "abrumado", "presiones", "vida", "encontrar", "paz",
            "incertidumbre", "claridad", "tranquilidad",
            "ansiedad", "calma",
            "proyecto", "estresado", "manejar", "presion",
            "futuro", "confiar", "dejar",
            "insomnio", "descansar", "mejorar", "sueño",
            "decision", "importante", "hacer"
        ],
        single_response=True
    )

    response(
        "Confía en las promesas de Dios, Él nunca te defraudará.",
        ["dificil", "consejo",
        "miedo", "futuro", "tranquilidad",
        "errores", "pasado", "culpable", "esperanza",
        "decision", "inseguro",
        "solo", "consuelo", "confiar",
        "carrera", "consejo",
        "perdida", "ser", "querido", "consuelo",
        "perdido", "rumbo", "orientacion",
        "fe", "momentos", "dificiles",
        "desafio", "superarlo"],
        single_response=True
    )

    response(
        "Canta a Dios con alegría, y dale las gracias, porque Él te cuida de situaciones peligrosas.",
        ["agradecido", "vida", "expresar", "gratitud",
        "sentimientos", "mejorar",
        "alegria", "desafios", "enfrentando",
        "situación", "peligrosa", "mantener", "calma", "esperanza",
        "miedo", "desconocido", "encontrar", "seguridad", "confianza",
        "cultivar", "actitud", "gratitud", "consejos", "hacerlo",
        "alegrarme", "mantener", "actitud", "positiva", "sugerir",
        "superar", "experiencia", "traumatica", "consejo", "curacion",
        "familia", "amigos", "mostrarles", "aprecio",
        "desafios", "trabajo", "sentir", "inseguro", "encontrar", "confianza"],
        single_response=True
    )
    response(
        "La gente se fija en las apariencias, pero Dios ve el corazón.",
        ["gente", "juzga", "apariencia", "fisica", "afecte",
        "momento", "inseguro", "veo", "consejo",
        "preocupa", "expectativas", "belleza", "sociedad", "inadecuado", "superar",
        "discapacidad", "visible", "excluido", "valia", "proposito",
        "errores", "pasado", "temo", "juzgue", "sentimiento", "vergüenza",
        "proceso", "aceptacion", "cuerpo", "consejos", "ayudarme",
        "presion", "encajar", "estandares", "valorarme", "interiormente",
        "burlas", "comentarios", "mantener", "autoestima", "confianza",
        "enseñar", "hijos", "importancia", "valorar", "interior",
        "considerando", "cambio", "imagen", "razones", "aconsejarias", "bonito", "lindo", "linda", "bonita"],
        single_response=True
    )

    response(
        "Lo que Dios te dice y el camino que dice que camines no se equivoca. Dios es muy fuerte para cuidarte. Abrígate en Él.",
        ["pregunta", "incertidumbre", "vida", "seguro", "decisión", "correcta",
        "respuesta", "dios", "camino", "equivoca", "fuerte", "cuidarte", "acogiate",
        "perdida", "querido", "abrumado", "encontrar", "consuelo",
        "atrapado", "situación", "dificil", "salir", "hacer",
        "preocupado", "futuro", "seguridad", "confianza",
        "proposito", "significado", "consejo", "darias"],
        single_response=True
    )

    response(
        "Cree en el Señor tu Dios, no hay otro como Él, Dios cumple sus promesas de amor.",
        ["pregunta", "momento dificil", "vida", "consuelo",
        "futuro", "incertidumbre", "encontrar", "esperanza",
        "errores", "pasado", "perdido", "redención",
        "propósito", "significado", "consejo", "darías",
        "ansiedad", "calma",
        "relacion", "espiritual", "pasos", "seguir"],
        single_response=True
    )

    response(
        "No te preocupes! Dios te liberará de todo lo malo que puedas estar pasando.",
        ["pregunta", "estres", "trabajo", "superarlo",
        "respuesta", "dios", "liberará", "malo", "pasando",
        "error", "importante", "culpable", "esperanza",
        "salud", "ser querido", "bien",
        "desafio", "financiero", "salir adelante", "consejo",
        "situacion", "incertidumbre", "abrumado",
        "soledad", "tristeza", "consuelo", "fe"],
        single_response=True
    )

    response(
        "Canta a Dios, porque Él es bueno, ¡y su amor es para siempre.",
        ["pregunta", "tristeza", "encontrar", "consuelo",
        "respuesta", "canta", "dios", "bueno", "amor", "siempre",
        "expresar", "gratitud", "bendiciones", "vida", "manera", "significativa",
        "situacion", "amigo", "celebrando", "logro", "importante", "alegria",
        "fortalecer", "relación", "espiritual", "actividades", "recomiendas",
        "necesito", "esperanza", "dificultad", "hacer",
        "familiar", "cumpleaños", "compartir", "mensaje", "positivo", "seres", "queridos"],
        single_response=True
    )

    response(
        "Si tienes una actitud de humildad, y hablas con Dios, lo buscas, y dejas de hacer lo malo que sea que estés haciendo; Dios te perdonará",
        ["error", "grave", "culpable", "redención", "adicción", "superarla", "lastimado", "enmendar", "honesto", "camino espiritual",
        "conectar", "fe", "remordimiento", "acciones pasadas", "liberarse", "confusion", "moral", "decisiones", "consejo",
        "comportamientos", "agresivos", "compasivo", "regresar", "reconciliarme", "encrucijada", "etica",
        "orientacion", "proceder", "egoista", "mejor persona", "empezar", "envidia", "superar"],
        single_response=True
    )

    response(
        "Dios está en todas partes, te ve y te cuida porque Él es fiel. Confía.",
        ["solo", "desamparado", "tristeza", "consuelo", "desafio", "futuro", "seguridad", "orientación", "ansiedad", "calma",
        "fortaleza", "complicada", "incertidumbre", "apoyo", "perdido", "rumbo", "consejo", "mantener", "fe", "dificiles",
        "claridad", "tranquilidad"],
        single_response=True
    )

    response(
        "Dios es un papá muy bueno, y si lo prometió, Él lo cumplirá.",
        ["momento", "difícil", "esperanza", "mejorar", "orando", "solución", "problemas", "dios", "escuchando", "plegarias",
        "perdido", "rumbo", "ayudar", "preocupado", "futuro", "plan", "cometer errores", "juicio", "perdón", "desafío",
        "fortaleza", "abrumado", "situación", "pérdida", "dolor", "consuelo", "sanar", "decisión importante", "orientación",
        "guía", "dirección", "correcta", "dificultades", "camino espiritual", "fortalecer", "fe", "relación", "duda",
        "incertidumbre", "certeza", "paz"],
        single_response=True
    )

    response(
        "Si tú no haces lo que tienes que hacer, muy seguramente otro lo hará, pero papá Dios puede castigarte. De pronto, estás ahí porque tú eres la persona indicada para hacerlo.",
        ["dificultades", "cumplir", "responsabilidades", "trabajo", "consejo", "evitando", "tarea", "importante", 
        "abordarla", "darías", "postergando", "decisión", "preocupa", "impacto", "sensación", "conversación", 
        "difícil", "querido", "aconsejarías", "pensando", "proyecto", "dudas", "persona adecuada", "opinas"],
        single_response=True
    )

    response(
        "Mi constructor cree que el abuelo Dios vive, y por eso no tiene miedo de lo que pueda pasar, y que algún día verá a Dios, es un anhelo muy profundo su corazón.",
        ["cree", "Jorge", "programador", "constructor", "creencia", "fe", "incertidumbre", "vida", "seguridad", 
        "confianza", "perdido", "ser querido", "consuelo", "desafío", "carrera", "abrumado", "consejo", "rumbo", 
        "orientación", "claridad", "decisión", "crucial", "elegir", "correcto"],
        single_response=True
    )

#-----------------Algoritmo palabra de Dios (fin)---------------------------------------------------------------------------------------


    #anexar toda la logica de chat (fin)
    best_match = max(highest_prob, key=highest_prob.get)

    return unknown() if highest_prob[best_match] < 1 else best_match

def unknown():
    response = [
        "Disculpa, ¿podrías escribir bien, con tildes y todo? 😊 Es que apenas estoy aprendiendo y no puedo entenderte bien. 🙁",
        "Disculpa. ¿puedes decirlo de nuevo? es que no te entendí😊",
        "Disculpa no entiendo lo que quieres decir. ¿podrias escribirlo de otra manera?🙈",
    ][random.randrange(3)]
    return response

# Estructura conversaciónal de bin (FIN)
#---------------------------------------------------Acá esta toda la mente de BIN (FIN)------------------------------------------------

# Ruta para cargar la plantilla HTML (inicio)
@app.route("/")
def template():
    return render_template("index.html")

# Procesamiento de solicitud POST
@app.route("/get_response", methods=["POST"])
def process_request():
    user_input = request.json.get("user_input", "")
    #print("Respuesta del usuario:", user_input)

    response_text = get_response(user_input)

    if not response_text:
        response_text = "Lo siento, no pude entenderte. ¿Podrías reformular tu pregunta?"

    return jsonify({"respuesta": response_text})

# Ruta para servir archivos estáticos
@app.route('/static/<path:path>')
def send_static(path):
    return send_from_directory('static', path)

if __name__ == "__main__":
    app.run()