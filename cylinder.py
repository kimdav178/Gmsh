import sys
import gmsh

gmsh.initialize()
gmsh.model.add("t3")
lc = 1e-2

gmsh.model.geo.addPoint(0, 0, 0, lc, 1)
gmsh.model.geo.addPoint(.1, 0, 0, lc, 2)
gmsh.model.geo.addPoint(0, 0.1, 0, lc, 3)
gmsh.model.geo.addPoint(-.1, 0, 0, lc, 4)
gmsh.model.geo.addPoint(0, -.1, 0, lc, 5)

gmsh.model.geo.addCircleArc(2, 1, 3)
gmsh.model.geo.addCircleArc(3, 1, 4)
gmsh.model.geo.addCircleArc(4, 1, 5)
gmsh.model.geo.addCircleArc(5, 1, 2)
gmsh.model.geo.addCurveLoop([1, 2, 3, 4], 1)
gmsh.model.geo.addPlaneSurface([1], 1)

gmsh.model.geo.addPoint(0, 0, 0.5, lc, 6)
gmsh.model.geo.addPoint(.1, 0, 0.5, lc, 7)
gmsh.model.geo.addPoint(0, 0.1, 0.5, lc, 8)
gmsh.model.geo.addPoint(-.1, 0, 0.5, lc, 9)
gmsh.model.geo.addPoint(0, -.1, 0.5, lc, 10)

gmsh.model.geo.addCircleArc(7, 6, 8)
gmsh.model.geo.addCircleArc(8, 6, 9)
gmsh.model.geo.addCircleArc(9, 6, 10)
gmsh.model.geo.addCircleArc(10, 6, 7)
gmsh.model.geo.addCurveLoop([5, 6, 7, 8], 2)
gmsh.model.geo.addPlaneSurface([2], 2)

gmsh.model.geo.addLine(2, 7, 9)
gmsh.model.geo.addLine(3, 8, 10)
gmsh.model.geo.addLine(4, 9, 11)
gmsh.model.geo.addLine(5, 10, 12)

gmsh.model.geo.addCurveLoop([1, 10, -5, -9], 3)
gmsh.model.geo.addSurfaceFilling([3], 3)
gmsh.model.geo.addCurveLoop([2, 11, -6, -10], 4)
gmsh.model.geo.addSurfaceFilling([4], 4)
gmsh.model.geo.addCurveLoop([3, 12, -7, -11], 5)
gmsh.model.geo.addSurfaceFilling([5], 5)
gmsh.model.geo.addCurveLoop([4, 9, -8, -12], 6)
gmsh.model.geo.addSurfaceFilling([6], 6)

l = gmsh.model.geo.addSurfaceLoop([i + 1 for i in range(6)])
gmsh.model.geo.addVolume([l])

gmsh.model.geo.synchronize()
gmsh.model.mesh.generate(3)

#gmsh.write("t3.msh")
#gmsh.write("t3.geo_unrolled")

if '-nopopup' not in sys.argv:
    gmsh.fltk.run()

gmsh.finalize()
