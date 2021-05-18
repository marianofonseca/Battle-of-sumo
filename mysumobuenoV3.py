#RobotName: GrupoPython2

#Aca importo la libreria

from RobotRL import RobotRL

robot = RobotRL()


#Sensor Izquierdo
di = 0
#Sensor Derecho
dd = 0

#Que es ir recto


def recto():
    robot.setVI(100)
    robot.setVD(100)

#Que es retroceder
def retroceder():
    robot.setVI(-100)
    robot.setVD(-100)

#Que es ir izquierda
def irIzquierda():
    robot.setVI(-40)
    robot.setVD(40)

#Que es ir derecha
def irDerecha():
    robot.setVI(40)
    robot.setVD(-40)

#Que es parar
def parar():
    robot.setVI(0)
    robot.setVD(0)

#Como buscar al otro robot
def buscar():
    global di, dd
    di = robot.getDI()
    dd = robot.getDD()

    #Si esta en frente
    if ((di < 100) and (dd < 100)):
        recto()
        return
    #Si viene por derecha
    if ((di == 100) and (dd < 100)):
        irDerecha()
        return
    #Si viene izquierda
    if ((di < 100) and (dd == 100)):
        irIzquierda()
        return



#Al chocar
def Chocando():
    global ci, cd 
    ci = robot.getBI()
    cd = robot.getBD()

    if((ci==True)):
        robot.setVI(-50)
        robot.setVD(100)
        
    if((cd==True)):
        robot.setVI(100)
        robot.setVD(-50)

    
#Por si lo estan tirando    
def MeTiran():
    ci = robot.getBI()
    cd = robot.getBD()
    vi = robot.getVI()
    vd = robot.getVD()

    rectouno = vi *-1
    rectodos = vd *-1
    
    if((robot.getColorPiso() > 90)):
        robot.setVI(rectouno)
        robot.setVD(rectodos)
        print("Its doit iz")
        return


#si me empujan
def MeEmpujan():
    ci = robot.getBI()
    cd = robot.getBD()
    vi = robot.getVI()
    vd = robot.getVD()

    if((ci==True) and (cd==True)):
        robot.setVI(100)
        robot.setVD(100)
        print("They pumped me derecho")
    
    elif((ci==True) and (cd==False)):
        robot.setVI(-100)
        robot.setVD(100)
        print("They pumped me izq")
    
    elif((ci==False) and (cd==True)):
        robot.setVI(100)
        robot.setVD(-100)
        print("they pumped me derecha")
    else:
        buscar() 
        print("buscando")



#Para no caer





while robot.step():
    robot.setVI(20)
    robot.setVD(-20)
    
    buscar()
    Chocando()
    MeTiran()
    MeEmpujan()