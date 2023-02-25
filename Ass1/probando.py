
#________________________________________________________________________________________________________________________
#FUNCIONA PERFECTO SI LLAMO EL FILE COMO: python probando.py -h O BIEN python probando.py --help
'''import argparse
parser = argparse.ArgumentParser()
#print(parser.parse_args())
parser.add_argument("echo", help="echoing whatever")
#print(parser.parse_args())
parser.add_argument("square", help="square of a num", type = int)
print(parser.parse_args())'''
#________________________________________________________________________________________________________________________





#______________________________
#ESTO FUNCIONA BIEN SI LO LLAMO: python probando.py 2 ---> OUTPUT: 4, LO PUEDO HACER CON CUALQUIER OTRO ENTERO TAMBIÉN
'''import argparse
parser = argparse.ArgumentParser()
parser.add_argument("square", help="square of a num", type = int)
args = parser.parse_args()
print(args.square**2)'''
#__________________________________________________________________________________________________________________________________________________________


#______________________________
#ESTO FUNCIONA BIEN SI LO LLAMO: python probando.py 123fool --->  OUTPUT: 123fool , REPITE CUALQUIER STRING O NUM QUE AÑADA AL FINAL DEL COMANDO en la cmd
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("echo", help="echoing whatever")
args = parser.parse_args()
print(args.echo)
#___________________________________________________________________________________________________________________________________________________________