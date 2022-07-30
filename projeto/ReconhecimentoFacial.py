import cv2 
import mediapipe as mp 

webcam = cv2.VideoCapture(0) # python conecta na webcam.

reconhecimento_facial = mp.solutions.face_detection # reconhecimento de rosto
draw = mp.solutions.drawing_utils #desenho
detector = reconhecimento_facial.FaceDetection() #reconhece os rostos

while webcam.isOpened():
    true, frame = webcam.read() # lê a imagem da webcam
    if not true:
        break
    img = frame
    rosto = detector.process(img) # cria uma lista com os rostos 
    
    if rosto.detections: # rosto reconhecido
        for rosto in rosto.detections: 
            draw.draw_detection(img, rosto) # contorna o rosto 
    
    cv2.imshow("Reconhecimento Facial com python", img) # mostra o video da webcam 
    if cv2.waitKey(5) == 27: # ESC para parar
        break
webcam.relzease() # encerra a conexão com a webcam



