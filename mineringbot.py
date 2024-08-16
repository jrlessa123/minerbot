import pyautogui
import time
import os
import math

def move_mouse_in_circle(radius=10, duration=0.1):
    center_x, center_y = pyautogui.position()
    steps = int(duration * 100)
    angle_step = 2 * math.pi / steps
    for step in range(steps):
        x = center_x + radius * math.cos(step * angle_step)
        y = center_y + radius * math.sin(step * angle_step)
        pyautogui.moveTo(x, y)
        time.sleep(duration / steps)

def move_mouse_smoothly(x, y, duration=0.5):
    current_x, current_y = pyautogui.position()
    distance_x = x - current_x
    distance_y = y - current_y
    steps = int(duration * 100)
    for step in range(steps):
        intermediate_x = current_x + (distance_x * step / steps)
        intermediate_y = current_y + (distance_y * step / steps)
        pyautogui.moveTo(intermediate_x, intermediate_y)
        time.sleep(duration / steps)

def search_and_click_image(image_path):
    try:
        qdd_icon = pyautogui.locateCenterOnScreen(image_path, confidence=0.8)
        if qdd_icon:
            print('Imagem encontrada em:', qdd_icon)
            move_mouse_smoothly(qdd_icon[0], qdd_icon[1])
            pyautogui.click(qdd_icon[0], qdd_icon[1], clicks=1, interval=0.1, button='left')
            while pyautogui.locateCenterOnScreen(image_path, confidence=0.8):  # Continua clicando enquanto a imagem estiver visível
                pyautogui.mouseDown(button='left')
                time.sleep(0.1)  # Intervalo para segurar o clique
                pyautogui.mouseUp(button='left')
                print('Clicou na imagem em:', qdd_icon)
                time.sleep(0.5)  # Intervalo entre cliques
            print('A imagem desapareceu. Procurando próxima...')
        else:
            print('Imagem não encontrada.')
    except pyautogui.ImageNotFoundException:
        print('Imagem não encontrada ou confiança insuficiente.')

def new_func():
    pasta_imagens = './images/'
    
    if not os.path.exists(pasta_imagens):
        print("A pasta de imagens não foi encontrada.")
        return
    
    while True:
        print("Procurando imagens...")
        move_mouse_in_circle()

        imagens = os.listdir(pasta_imagens)
        for imagem in imagens:
            imagem_path = os.path.join(pasta_imagens, imagem)
            print("Procurando imagem:", imagem)
            search_and_click_image(imagem_path)
        
        print('Ciclo de busca completado. Reiniciando...')
        time.sleep(2)

new_func()