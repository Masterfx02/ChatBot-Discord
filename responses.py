import random 

def get_response(message: str) -> str:
    p_message = message.lower() 

    if p_message == 'hola':
        return '¡Que rollo!'
    
    if message == 'creadores':
        return 'Ariel Humberto Valle Escoto y Yeshua Neftali Espinoza González'
    
    if message == 'real hasta la muerte':
        return 'BRRRRRRR! BEBECITA'
    
    if message == 'existen los aliens?':
        return '¿No conoces a wisin y yandel?'
    
    if message == 'roll':
        return str(random.randint(1, 10))
    
    if p_message == '!ayuda':
        return 'que onda pa, ¿te puedo ayudar en algo?'
    
    return 'no entiendo lo que quisiste decir. intenta escribir "!ayuda".' 