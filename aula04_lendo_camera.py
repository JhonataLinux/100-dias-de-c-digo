import cv2
import numpy as np # Para manipulação de arrays (usado internamente pelo OpenCV)
from flask import Flask, Response # Framework web para criar o servidor # Response: Para criar respostas HTTP personalizadas

app = Flask(__name__) #Cria uma instância da aplicação Flask__name__ é uma variável especial que representa o nome do módulo atual

#Função que gera os frames da câmera
def generate_frames():
    cap = cv2.VideoCapture(0)
    
    while True:
        success, frame = cap.read()
        if not success:
            break
        
        # Codifica o frame em JPEG
        ret, buffer = cv2.imencode('.jpg', frame)
        frame = buffer.tobytes()
        #Converte o buffer NumPy para bytes puros
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/video')
def video_feed():
    return Response(generate_frames(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

#o exemplo a cima é com um simulandor de webcan

#codigo a baixo se tiver webcan plugada na porta usb ou for em um notbook parametro que deve ser usando (0,1)

#import cv2
#import numbers as py

#objeto a ser capturado

#cap = cv2.VideoCapture(1)

while True:
    #coletar o frame
    _, frame = cap.read()

    cv2.imshow('grava tela', frame)

    # e adicionar a opção do usuario sair do loop
    if cv2.waitKey(20) & 0xFF==ord('d'):
        break