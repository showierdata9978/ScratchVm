from __future__ import annotations

from dataclasses import dataclass

from .Block import Block


@dataclass
class Sprite:
  IsStage: bool
  name:str
  broadcasts:dict[str] #only needed if IsStage is True 
  variables:dict[list]
  lists:dict[list[str, list[any]]]
  blocks: dict[Block]
  TopBlocks: list[Block]
  currentCostume: int
  costumes: list[dict[str, int]]
  sounds: list
  volume: int
  layerOrder: int
  visible: bool
  x: int
  y: int
  size: int
  direction: int
  draggable: bool
  rotationStyle: str

  