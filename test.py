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
