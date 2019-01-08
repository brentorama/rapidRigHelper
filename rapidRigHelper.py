import maya.cmds as cmd
import maya.mel as mel

origs = cmd.ls(sl=True)
obs = cmd.ls(sl=True)
froms = cmd.ls(sl=True)
cmd.select(hi = True)
fromPre = 'Body_texturing_0001_'
for one in origs:
    #print (fromPre + one, one+'ShapeOrig')
    try:
        cmd.select(fromPre + one, one)
        cmd.transferAttributes(transferPositions = 0, transferNormals = 0, transferUVs = 2, transferColors = 0, sampleSpace = 4, sourceUvSpace = "map1", targetUvSpace = "map1", searchMethod = 3, flipUVs = 0, colorBorders = 1)
    except:
        pass
    for att in ['RRARigName', 'RRARigConnection']:
        exists = cmd.attributeQuery (att, node = one, ex = True)
        if exists:
            trash = (one+'.'+att)
            cmd.setAttr(trash, l = False)
            cmd.deleteAttr(one+'.'+att)
    
for one in obs:    
    cmd.setAttr (one + '.intermediateObject', 1)
    
cmd.select(obs)

joints = cmd.skinCluster(q=True, inf=True)
cmd.select('head_BND')
