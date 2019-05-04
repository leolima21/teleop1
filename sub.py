#!/usr/bin/env python

# Bibliotecas necessarias
import rospy
from std_msgs.msg import String
from std_msgs.msg import Int32
import RPi.GPIO as GPIO
import time

# Modo de operacao do GPIO
GPIO.setmode(GPIO.BOARD)

# Desabilitar mensagens de erro
GPIO.setwarnings(False)

# Configuracao dos pinos da placa
GPIO.setup(11, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)
GPIO.setup(15, GPIO.OUT)
GPIO.setup(16, GPIO.OUT)

# Setup do PWM com 100Hz de frequencia
left_forward = GPIO.PWM(16, 100)
right_forward = GPIO.PWM(15, 100)
left_back = GPIO.PWM(13, 100)
right_back = GPIO.PWM(11, 100)

# Inicio do PWM com 0
left_forward.start(0)
right_forward.start(0)
left_back.start(0)
right_back.start(0)


# Funcao q ira executar o movimento do robo
def callback(data):
    direcao = data.data
    if (direcao == 'w'):
        # Andar para a frente por 2 segundos
        print("Frente")
        left_forward.ChangeDutyCycle(20)
        right_forward.ChangeDutyCycle(20)

        time.sleep(2)

        left_forward.ChangeDutyCycle(0)
        right_forward.ChangeDutyCycle(0)      

    elif (direcao == 's'):
        # Andar para tras por 2 segundos
        print("Tras")
        left_back.ChangeDutyCycle(20)
        right_back.ChangeDutyCycle(20)

        time.sleep(2)

        left_back.ChangeDutyCycle(0)
        right_back.ChangeDutyCycle(0)

    elif (direcao == 'a'):
        # Girar para a esquerda
        print("Esquerda")
        left_back.ChangeDutyCycle(40)
        right_forward.ChangeDutyCycle(40)

        time.sleep(0.5)

        left_back.ChangeDutyCycle(0)
        right_forward.ChangeDutyCycle(0)

    elif (direcao == 'd'):
        # Girar para a direita
        print("Direita")
        right_back.ChangeDutyCycle(40)
        left_forward.ChangeDutyCycle(40)

        time.sleep(0.5)

        right_back.ChangeDutyCycle(0)
        left_forward.ChangeDutyCycle(0)

    else:
        # ERRO
        print('ERRO: Digite apenas as teclas WASD')
        left_forward.ChangeDutyCycle(0)
        right_forward.ChangeDutyCycle(0)
        left_back.ChangeDutyCycle(0)
        right_back.ChangeDutyCycle(0)
    
    # Limpar os dados do GPIO
    # GPIO.cleanup() (linha desativada pois estava atrapalhando o funcionamento do robo) 
 

def listener():
    # Inicio do node teleop_sub
    rospy.init_node('teleop_sub', anonymous=True)

    # Inscricao no topico e definicao da callback como funcao a ser executada
    rospy.Subscriber("teleop_topic", String, callback)

    # Mantem o python funcionando apos o encerramendo do node
    rospy.spin()


# Funcao main
if __name__ == '__main__':
    print("Funcionando")
    listener()
