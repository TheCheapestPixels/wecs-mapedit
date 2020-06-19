from wecs.core import Component
from wecs.core import System
from wecs.core import and_filter
from wecs.core import UID

from wecs.aspects import Aspect
from wecs.panda3d import aspects
from wecs import panda3d as wp3d

from wecs.panda3d import Model
from wecs.panda3d import CharacterController

from .creation import Creator

@Component()
class CursorMovement:
    move_snap: int = 2
    move_speed: float = 10.0
    rot_speed: float = 180.0
    rot_snap: float = 90.0
    snapping: bool = True


# Move horizontally and possibly snap to a grid.
class Cursoring(System):
    entity_filters = {
        'cursor' : and_filter([
            CursorMovement,
            CharacterController,
            Model
        ]),
    }

    def update(self, entities_by_filter):
        for entity in entities_by_filter['cursor']:
            cursor = entity[CursorMovement]
            model = entity[Model]
            char = entity[CharacterController]
            char.translation *= cursor.move_speed
            char.rotation *= cursor.rot_speed
            char.rotation[1] = 0
            if cursor.snapping:
                if char.move.x == 0 and char.move.y == 0 and char.move.z == 0:
                    if char.heading == 0:
                        np = model.node
                        np.set_pos(snap_vector(np.get_pos(), cursor.move_snap))
                        np.set_hpr(snap_vector(np.get_hpr(), cursor.rot_snap))


cursor = Aspect(
    [
        aspects.character,
        wp3d.Input,
        CursorMovement,
        #wp3d.camera.ThirdPersonCamera,
        #wp3d.camera.TurntableCamera,
        Creator,
    ],
)
