#!/usr/bin/env python

# Bibliotecas necessarias
import rospy
from std_msgs.msg import String
from std_msgs.msg import Int32
import time


# Funcao q ira publicar os comandos no topico
def talker():
    # Objeto q ira publicar no topico teleop_topic
    pub = rospy.Publisher('teleop_topic', String, queue_size=10)
    
    # Inicio do node teleop_pub
    rospy.init_node('teleop_pub', anonymous=True)
    
    # Prints de como usar o robo para  usuario
    print('Para movimentar o ROSBOT1 voce deve digitar a tecla correspondente ao movimento e apertar ENTER')
    print('Comandos disponiveis:')
    print('---------------------------')
    print('  W')
    print('A S D')
    print('---------------------------')

    while not rospy.is_shutdown():           
        # Input da direcao 
        comando = raw_input('Digite a tecla correspondente ao movimento e tecle ENTER:')
    
        # publicacao da info no topico
        rospy.loginfo(comando)    
        pub.publish(comando)

        # Esperar 2 segundos antes do priximo comando
        time.sleep(2)


# Funcao main
if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException: pass
