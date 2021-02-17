import sys
import gmsh

gmsh.initialize()
gmsh.model.add("t1")
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

gmsh.model.geo.synchronize()
gmsh.model.mesh.generate(2)

#gmsh.write("t1.msh")

if '-nopopup' not in sys.argv:
    gmsh.fltk.run()

gmsh.finalize()
