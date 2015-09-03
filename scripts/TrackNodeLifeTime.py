
import pymjin2

class TrackNodeLifeTime:
    def __init__(self, sceneName, nodeName, scene):
        print "TrackNodeLifeTime.__init__. scene: {0} node: {1}".format(sceneName, nodeName)
    def __del__(self):
        print "TrackNodeLifeTime.__del__"

def SCRIPT_CREATE(sceneName, nodeName, scene):
    return TrackNodeLifeTime(sceneName, nodeName, scene)

def SCRIPT_DESTROY(instance):
    del instance

