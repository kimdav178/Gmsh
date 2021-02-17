import sys
import gmsh

gmsh.initialize()
gmsh.model.add("t4")
lc = 0.005

gmsh.model.geo.addPoint(0, 0, 0, lc, 1)
gmsh.model.geo.addPoint(0.1, 0, 0, lc, 2)
gmsh.model.geo.addPoint(0, 0.1, 0, lc, 3)
gmsh.model.geo.addPoint(0, 0.09, 0.01, lc, 4)
gmsh.model.geo.addPoint(0, 0.09, 0, lc, 5)
gmsh.model.geo.addPoint(0, 0, 0.01, lc, 6)
gmsh.model.geo.addPoint(0.09, 0, 0, lc, 7)
gmsh.model.geo.addPoint(0.09, 0, 0.01, lc, 8)

gmsh.model.geo.addCircleArc(2, 1, 3, 1)
gmsh.model.geo.addCircleArc(3, 5, 4, 2)
gmsh.model.geo.addCircleArc(4, 6, 8, 3)
gmsh.model.geo.addCircleArc(8, 7, 2, 4)

gmsh.model.geo.addCurveLoop([i+1 for i in range(4)], 1)
gmsh.model.geo.addSurfaceFilling([1], 1)


gmsh.model.geo.addPoint(0, 0.09, -0.01, lc, 14)
gmsh.model.geo.addPoint(0, 0, -0.01, lc, 16)
gmsh.model.geo.addPoint(0.09, 0, -0.01, lc, 18)

gmsh.model.geo.addCircleArc(2, 1, 3, 5)
gmsh.model.geo.addCircleArc(3, 5, 14, 6)
gmsh.model.geo.addCircleArc(14, 16, 18, 7)
gmsh.model.geo.addCircleArc(18, 7, 2, 8)

gmsh.model.geo.addCurveLoop([i+5 for i in range(4)], 2)
gmsh.model.geo.addSurfaceFilling([2], 2)


gmsh.model.geo.addPoint(0.08, 0, 0, lc, 22)
gmsh.model.geo.addPoint(0, 0.08, 0, lc, 23)

gmsh.model.geo.addCircleArc(22, 1, 23, 9)
gmsh.model.geo.addCircleArc(23, 5, 4, 10)
gmsh.model.geo.addCircleArc(4, 6, 8, 11)
gmsh.model.geo.addCircleArc(8, 7, 22, 12)

gmsh.model.geo.addCurveLoop([i+9 for i in range(4)], 3)
gmsh.model.geo.addSurfaceFilling([3], 3)

gmsh.model.geo.addCircleArc(22, 1, 23, 13)
gmsh.model.geo.addCircleArc(23, 5, 14, 14)
gmsh.model.geo.addCircleArc(14, 16, 18, 15)
gmsh.model.geo.addCircleArc(18, 7, 22, 16)

gmsh.model.geo.addCurveLoop([i+13 for i in range(4)], 4)
gmsh.model.geo.addSurfaceFilling([4], 4)

"""
gmsh.model.geo.addCurveLoop([4, -8, 16, -12], 114)
gmsh.model.geo.addPlaneSurface([114], 114)

gmsh.model.geo.addCurveLoop([2, -10, 14, -6], 116)
gmsh.model.geo.addPlaneSurface([116], 116)


l = gmsh.model.geo.addSurfaceLoop([1, 2, 3, 4, 114, 116])
gmsh.model.geo.addVolume([l])
"""

gmsh.model.geo.addPoint(0, 0, 0, lc, 111)
gmsh.model.geo.addPoint(-0.1, 0, 0, lc, 112)
gmsh.model.geo.addPoint(0, -0.1, 0, lc, 113)
gmsh.model.geo.addPoint(0, -0.09, 0.01, lc, 114)
gmsh.model.geo.addPoint(0, -0.09, 0, lc, 115)
gmsh.model.geo.addPoint(0, 0, 0.01, lc, 116)
gmsh.model.geo.addPoint(-0.09, 0, 0, lc, 117)
gmsh.model.geo.addPoint(-0.09, 0, 0.01, lc, 118)

gmsh.model.geo.addCircleArc(112, 111, 113, 17)
gmsh.model.geo.addCircleArc(113, 115, 114, 18)
gmsh.model.geo.addCircleArc(114, 116, 118, 19)
gmsh.model.geo.addCircleArc(118, 117, 112, 20)

gmsh.model.geo.addCurveLoop([i+17 for i in range(4)], 5)
gmsh.model.geo.addSurfaceFilling([5], 5)


gmsh.model.geo.addPoint(0, -0.09, -0.01, lc, 1114)
gmsh.model.geo.addPoint(0, 0, -0.01, lc, 1116)
gmsh.model.geo.addPoint(-0.09, 0, -0.01, lc, 1118)

gmsh.model.geo.addCircleArc(112, 111, 113, 21)
gmsh.model.geo.addCircleArc(113, 115, 1114, 22)
gmsh.model.geo.addCircleArc(1114, 1116, 1118, 23)
gmsh.model.geo.addCircleArc(1118, 117, 112, 24)

gmsh.model.geo.addCurveLoop([i+21 for i in range(4)], 6)
gmsh.model.geo.addSurfaceFilling([6], 6)


gmsh.model.geo.addPoint(-0.08, 0, 0, lc, 1122)
gmsh.model.geo.addPoint(0, -0.08, 0, lc, 1123)

gmsh.model.geo.addCircleArc(1122, 111, 1123, 25)
gmsh.model.geo.addCircleArc(1123, 115, 114, 26)
gmsh.model.geo.addCircleArc(114, 116, 118, 27)
gmsh.model.geo.addCircleArc(118, 117, 1122, 28)

gmsh.model.geo.addCurveLoop([i+25 for i in range(4)], 7)
gmsh.model.geo.addSurfaceFilling([7], 7)


gmsh.model.geo.addCircleArc(1122, 111, 1123, 29)
gmsh.model.geo.addCircleArc(1123, 115, 1114, 30)
gmsh.model.geo.addCircleArc(1114, 1116, 1118, 31)
gmsh.model.geo.addCircleArc(1118, 117, 1122, 32)

gmsh.model.geo.addCurveLoop([i+29 for i in range(4)], 8)
gmsh.model.geo.addSurfaceFilling([8], 8)



gmsh.model.geo.addPoint(0, 0, 0, lc, 221)
gmsh.model.geo.addPoint(-0.1, 0, 0, lc, 222)
gmsh.model.geo.addPoint(0, 0.1, 0, lc, 223)
gmsh.model.geo.addPoint(0, 0.09, 0.01, lc, 224)
gmsh.model.geo.addPoint(0, 0.09, 0, lc, 225)
gmsh.model.geo.addPoint(0, 0, 0.01, lc, 226)
gmsh.model.geo.addPoint(-0.09, 0, 0, lc, 227)
gmsh.model.geo.addPoint(-0.09, 0, 0.01, lc, 228)

gmsh.model.geo.addCircleArc(222, 221, 223, 33)
gmsh.model.geo.addCircleArc(223, 225, 224, 34)
gmsh.model.geo.addCircleArc(224, 226, 228, 35)
gmsh.model.geo.addCircleArc(228, 227, 222, 36)

gmsh.model.geo.addCurveLoop([i+33 for i in range(4)], 9)
gmsh.model.geo.addSurfaceFilling([9], 9)


gmsh.model.geo.addPoint(0, 0.09, -0.01, lc, 2214)
gmsh.model.geo.addPoint(0, 0, -0.01, lc, 2216)
gmsh.model.geo.addPoint(-0.09, 0, -0.01, lc, 2218)

gmsh.model.geo.addCircleArc(222, 221, 223, 37)
gmsh.model.geo.addCircleArc(223, 225, 2214, 38)
gmsh.model.geo.addCircleArc(2214, 2216, 2218, 39)
gmsh.model.geo.addCircleArc(2218, 227, 222, 40)

gmsh.model.geo.addCurveLoop([i+37 for i in range(4)], 10)
gmsh.model.geo.addSurfaceFilling([10], 10)


gmsh.model.geo.addPoint(-0.08, 0, 0, lc, 2222)
gmsh.model.geo.addPoint(0, 0.08, 0, lc, 2223)

gmsh.model.geo.addCircleArc(2222, 221, 2223, 41)
gmsh.model.geo.addCircleArc(2223, 225, 224, 42)
gmsh.model.geo.addCircleArc(224, 226, 228, 43)
gmsh.model.geo.addCircleArc(228, 227, 2222, 44)

gmsh.model.geo.addCurveLoop([i+41 for i in range(4)], 11)
gmsh.model.geo.addSurfaceFilling([11], 11)


gmsh.model.geo.addCircleArc(2222, 221, 2223, 45)
gmsh.model.geo.addCircleArc(2223, 225, 2214, 46)
gmsh.model.geo.addCircleArc(2214, 2216, 2218, 47)
gmsh.model.geo.addCircleArc(2218, 227, 2222, 48)

gmsh.model.geo.addCurveLoop([i+45 for i in range(4)], 12)
gmsh.model.geo.addSurfaceFilling([12], 12)



gmsh.model.geo.addPoint(0, 0, 0, lc, 1221)
gmsh.model.geo.addPoint(0.1, 0, 0, lc, 1222)
gmsh.model.geo.addPoint(0, -0.1, 0, lc, 1223)
gmsh.model.geo.addPoint(0, -0.09, 0.01, lc, 1224)
gmsh.model.geo.addPoint(0, -0.09, 0, lc, 1225)
gmsh.model.geo.addPoint(0, 0, 0.01, lc, 1226)
gmsh.model.geo.addPoint(0.09, 0, 0, lc, 1227)
gmsh.model.geo.addPoint(0.09, 0, 0.01, lc, 1228)

gmsh.model.geo.addCircleArc(1222, 1221, 1223, 49)
gmsh.model.geo.addCircleArc(1223, 1225, 1224, 50)
gmsh.model.geo.addCircleArc(1224, 1226, 1228, 51)
gmsh.model.geo.addCircleArc(1228, 1227, 1222, 52)

gmsh.model.geo.addCurveLoop([i+49 for i in range(4)], 13)
gmsh.model.geo.addSurfaceFilling([13], 13)


gmsh.model.geo.addPoint(0, -0.09, -0.01, lc, 12214)
gmsh.model.geo.addPoint(0, 0, -0.01, lc, 12216)
gmsh.model.geo.addPoint(0.09, 0, -0.01, lc, 12218)

gmsh.model.geo.addCircleArc(1222, 1221, 1223, 53)
gmsh.model.geo.addCircleArc(1223, 1225, 12214, 54)
gmsh.model.geo.addCircleArc(12214, 12216, 12218, 55)
gmsh.model.geo.addCircleArc(12218, 1227, 1222, 56)

gmsh.model.geo.addCurveLoop([i+53 for i in range(4)], 14)
gmsh.model.geo.addSurfaceFilling([14], 14)


gmsh.model.geo.addPoint(0.08, 0, 0, lc, 12222)
gmsh.model.geo.addPoint(0, -0.08, 0, lc, 12223)

gmsh.model.geo.addCircleArc(12222, 1221, 12223, 57)
gmsh.model.geo.addCircleArc(12223, 1225, 1224, 58)
gmsh.model.geo.addCircleArc(1224, 1226, 1228, 59)
gmsh.model.geo.addCircleArc(1228, 1227, 12222, 60)

gmsh.model.geo.addCurveLoop([i+57 for i in range(4)], 15)
gmsh.model.geo.addSurfaceFilling([15], 15)


gmsh.model.geo.addCircleArc(12222, 1221, 12223, 61)
gmsh.model.geo.addCircleArc(12223, 1225, 12214, 62)
gmsh.model.geo.addCircleArc(12214, 12216, 12218, 63)
gmsh.model.geo.addCircleArc(12218, 1227, 12222, 64)

gmsh.model.geo.addCurveLoop([i+61 for i in range(4)], 16)
gmsh.model.geo.addSurfaceFilling([16], 16)


gmsh.model.geo.synchronize()
gmsh.model.mesh.generate(3)

#gmsh.write("t4.msh")
#gmsh.write("t4.geo_unrolled")

if '-nopopup' not in sys.argv:
    gmsh.fltk.run()

gmsh.finalize()
