##TODO 13 实现你的算法
import math
class point(object):


env_data = [
    [3,2,2,2,2,2,2,2,1],
    [0,0,2,2,2,2,2,0,0],
    [2,0,0,2,2,2,0,0,2],
    [2,2,0,0,2,0,0,2,2],
    [2,2,2,0,0,0,2,2,2]]

class Point(object):
    """
    代表一个点
    """
    def __init__(self, x,y):
        self.x = x
        self.y = y
    def __eq__(self,other):
        if self.x == other.x and self.y == other.y:
            return True
        else:
            return False
    def __str__(self):
        return "x:{},y:{}".format(self.x,self.y)
class AStar(object):
    """
    A*算法类
    """
    class Node:
        """
        节点类
        """
        def __init__(self,point,endPoint,g=0):
            self.point = point
            self.g = g
            self.parent = None
            self.h = (abs(point.x - endPoint.x)+abs(point.y - endPoint.y))*10
    def __init__(self,env_data,startPoint,endPoint,pass = 0):
        self.env_data = env_data #地图二维表
        self.startPoint = startPoint #起点位置
        self.endPoint = endPoint    #终点位置
        self.pass = pass    #可通过标识
        self.openList = []  #开表
        self.closeList = [] #闭表
    def getMinNode(self):
        """
        获取f值最小的节点
        """
        currentNode = self.openList[0]
        for node in openList:
            if node.g + node.h < currentNode.g + currentNode.h:
                currentNode = Node
        return currentNode
    def pointInOpenList(self,point):
        """
        判断点是否在openList里
        """
        return point in self.openList
class Node:
    """
    节点类
    """
    def __init__(self,point,endPoint,g=0):
        self.point = point
        self.endPoint = endPoint
        self.g = g
        self.parent = None
        self.h = (abs(point.x - endPoint.x)+abs(point.y - endPoint.y))*10
    def __str__(self):
        return "x:{},y:{}".format(self.point,self.endPoint)
openList = []
closeList = []
endPoint = Point(0,0)
def getMinNode():
    """
    获取f值最小的节点
    """
    currentNode = openList[0]
    for node in openList:
        if node.g + node.h < currentNode.g + currentNode.h:
            currentNode = node
    return currentNode
def pointInOpenList(point):
    """
    判断点是否在openList里
    """
    for node in openList:
        if node.point == point:
            return node
    return None
def pointInCloseList(point):
    """
    判断点是否在closeList里
    """
    for node in closeList:
        if node.point == point:
            return True
        else:
            return False

def endPointInCloseList():
    """
    判断终点是否在闭表里
    """
    for node in closeList:
        if node.point==endPoint:
            return node
    return None
def searchNear(minF,optinX,optinY):
    """
    寻找附近的点
    """
    #进行越界检测
    if minF.point.x + optinX < 0 or minF.point.x + optinX > len(env_data) - 1 or minF.point.y + optinY < 0 or minF.point.y + optinY > len(env_data[0]) -1:
        return
    #进行障碍检测
    if env_data[minF.point.x + optinX][minF.point.y + optinY] != 0 and env_data[minF.point.x + optinX][minF.point.y + optinY] != 3:
        return
        #进行闭表检测
    if pointInCloseList(Point(minF.point.x + optinX,minF.point.y + optinY)):
        return
    if optinX == 0 or optinY == 0:
        step = 10
    else:
        step = 14
    #不在开表中，则加入开表
    currentNode = pointInOpenList(Point(minF.point.x + optinX,minF.point.y + optinY))
    if not currentNode:
        currentNode=Node(Point(minF.point.x+optinX,minF.point.y+optinY),endPoint,g=minF.g+step)
        currentNode.parent=minF
        openList.append(currentNode)
        return
    #如果在openList中，判断minF到当前点的G是否更小
    if minF.h<currentNode.h: #如果更小，就重新计算g值，并且改变parent
        currentNode.h=minF.h
        currentNode.parent=minF
def star():
    startNode=Node(Point(0,8),Point(0,0))
    openList.append(startNode)
    #2.主循环逻辑
    while True:
        #找到F值最小的点
        minF=getMinNode()
        #把这个点加入closeList中，并且在openList中删除它
        closeList.append(minF)
        #print(minF)
        openList.remove(minF)
        #判断这个节点的上下左右节点
        searchNear(minF,0,-1)
        searchNear(minF, 0, 1)
        searchNear(minF, -1, 0)
        searchNear(minF, 1, 0)
        #判断是否终止
        point=endPointInCloseList()
        if point:  #如果终点在关闭表中，就返回结果
            # print("关闭表中")
            cPoint=point
            pathList=[]
            while True:
                if cPoint.parent:
                    pathList.append(cPoint.point)
                    cPoint=cPoint.parent
                else:
                    #print(pathList)
                    for x in list(reversed(pathList)):
                        print(x)
                    return
                    # print(pathList.reverse())
                    #return list(reversed(pathList))
        if len(openList)==0:
            print("失败了")
            return None
star()