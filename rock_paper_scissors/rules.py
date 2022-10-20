from entity import Entity


RULES: dict[tuple[Entity, Entity], str] = {
    (Entity.PAPER, Entity.ROCK): "covers",
    (Entity.ROCK, Entity.SCISSORS): "crushes",
    (Entity.SCISSORS, Entity.PAPER): "cuts",
}


def get_winner(entity1: Entity, entity2: Entity) -> tuple[Entity | None, str]:
    if entity1 == entity2:
        return None, "It's a tie"
    elif (entity1, entity2) in RULES:
        return entity1, f"{entity1} {RULES[(entity1, entity2)]} {entity2}"
    elif (entity2, entity1) in RULES:
        return entity2, f"{entity2} {RULES[(entity2, entity1)]} {entity1}"
    else:
        raise KeyError("Some of the entities are invalid.")
    