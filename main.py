import requests
from chainlit import on_message, Message

def generate_qa_from_text(file_path, question, max_length=200):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            text_content = file.read()
    except FileNotFoundError:
        return f"Error: el archivo {file_path} no fue encontrado."
    except IOError:
        return f"Error: no se pudo leer el archivo {file_path}."

    prompt = f"Context: {text_content}\nQuestion: {question}"
    url = "http://localhost:11434/api/generate"  # Asegúrate de que esta URL y puerto sean correctos

    payload = {
        "model": "llama3",
        "prompt": prompt,
        "min_length": 300,
        "stream": False
    }
    headers = {'Content-Type': 'application/json'}

    response = requests.post(url, json=payload, headers=headers)
    if response.status_code == 200:
        response_data = response.json()
        return response_data.get('response', 'No response provided by the API.')
    else:
        return f"Error en la solicitud: {response.status_code}, {response.text}"

@on_message
async def handle_message(message: Message):
    file_path = 'data/autocodificadores.txt'
    question = message.content  # Accediendo al atributo content del objeto message
    print(f"Question received: {question}")  # Depuración
    
    # Enviar respuesta intermedia
    try:
        final_answer = await Message(content="Procesando tu pregunta, por favor espera...").send()
        print("Intermediate message sent.")  # Depuración
    except Exception as e:
        print(f"Error sending intermediate message: {e}")
    
    # Generar respuesta final
    try:
        answer = generate_qa_from_text(file_path, question)
        print(f"Answer generated: {answer}")  # Depuración
    except Exception as e:
        print(f"Error generating answer: {e}")
        answer = "Hubo un error al generar la respuesta."

    # Actualizar mensaje con la respuesta final
    try:
        final_answer.content = answer
        await final_answer.update()
        print("Final answer updated and sent.")  # Depuración
    except Exception as e:
        print(f"Error updating final answer: {e}")
