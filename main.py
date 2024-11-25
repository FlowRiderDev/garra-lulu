from hand import *
from camera import *
import time

# Inicializar o banco de dados
init_db()

# Capturar vídeo
cap = capture_video()

# Tempo de iteração
iterate = 3
movement = [0,0,30]
claw = False
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                
for frame in cap:
    # Exibir vídeo com crosshair
    display_video_with_crosshair([frame])

    numerate_pixels(frame)
    map_pixels_to_quadrants_and_store(frame)

    # Pausa no loop
    time.sleep(1)
    print("centralize sua mão")
    # Verificar se 'q' foi pressionado
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break



# Loop principal
for frame in cap:
    # Exibir vídeo com crosshair
    display_video_with_crosshair([frame])  # Enviar o frame como uma lista para iterar

    # Verificar as mãos
    if is_left_hand_in_frame(frame):
        print("Left hand detected")
    elif is_right_hand_in_frame(frame):
        movement = get_right_hand_landmark_0_coordinates_with_z(frame)
        claw = is_right_hand_open(frame)
        print(movement)
        print(claw)

    else:
        print("No hands detected")

    # Pausa no loop
    time.sleep(iterate)

    # Verificar se 'q' foi pressionado
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Liberar a câmera e destruir as janelas
cv2.destroyAllWindows()
