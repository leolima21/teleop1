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
    
    
    while not rospy.is_shutdown():
        # Print de como usar o robo para  usuario
        print('Digite W, S, A ou D e tecle enter para comandar os movimentos do robo')
        
        # Input da direcao 
        comando = input('Digite a direcao do movimento:')
    
        # publicacao da info no topico
        rospy.loginfo(comando)    
        pub.publish(comando)

        # Esperar 2 segundos
        time.sleep(2)


# Funcao main
if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException: pass
