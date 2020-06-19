from panda3d.core import NodePath
from panda3d.core import Point3
from panda3d.core import LineSegs

from wecs import panda3d as wp3d
from wecs import mechanics
from wecs.aspects import Aspect
from wecs.panda3d import aspects
from mapedit.helpers import draw_grid
from mapedit import mapedit
from mapedit.cursor import cursor

system_types = [
    wp3d.ManageGeometry,
    mechanics.DetermineTimestep,
    wp3d.UpdateCharacter,
    mapedit.cursor.Cursoring, # Horizontal movement with optional grid-snapping.
    wp3d.ExecuteMovement,
    wp3d.UpdateCameras,
    mapedit.mapeditor.UpdateMapEditor, # Handles Creator and Tilemap (to be split up later)
]

# empty scene with a grid.
gridsize = 500 # Size of grid in cells
cellsize = 2 # Size of cells in meters
aspects.empty_scene.add(
    base.ecs_world.create_entity(),
    overrides = {
        panda3d.Model: dict(node=draw_grid(gridsize, gridsize, cellsize)),
    }
)


# cursor entity.
cursor_node = NodePath("cursor")
cursor_model = loader.loadModel("../../assets/cursor.bam")
cursor_model.set_scale(cellsize)
cursor_model.reparent_to(cursor_node)
cursor.add(
    base.ecs_world.create_entity(),
    overrides={
            panda3d.ThirdPersonCamera: dict(distance=15.0, focus_height=0),
            panda3d.TurntableCamera: dict(pitch=-90),
            panda3d.CursorMovement: dict(move_snap=cellsize),
            panda3d.Model: dict(node=cursor_node),
            panda3d.Position: dict(value=Point3(gridsize/2, gridsize/2, 0)),
    }
)
