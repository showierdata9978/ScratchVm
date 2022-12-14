import shutil
from pathlib import Path

from json import load

from .DataHolders import Block, Sprite
from .BlockDefine import BlockDefinions


def make_sprites(json):

    sprites = {}
    top_blocks = {}

    for sprite in self.project_data["targets"]:
        blocks = {}
        topBlocks = []
        for id, block in sprite["blocks"].items():
          if block["topLevel"]:
            block = Block(id, block["opcode"], block["inputs"], block["fields"],block["topLevel"], block["next"], block["parent"])
            topBlocks[id] = block
            if block["opcode"] in top_blocks:
              top_blocks[block["opcode"]].append({"id": id, "next": block["next"], "SpriteName": sprite["name"], "Block": block })
            else:
              top_blocks[block["opcode"]] = [{"id": id, "next": block["next"], "SpriteName": sprite["name"] }]
          else:
            blocks.append(Block(id, block["opcode"], block["inputs"], block["fields"],block["topLevel"],  block["next"], block["parent"]))
      
    sprites[sprite["name"]] = Sprite(
        sprite["isStage"], 
        sprite["name"], 
        sprite["broadcasts"], 
        sprite["variables"], 
        sprite["lists"], 
        blocks, 
        top_blocks,
        sprite["currentCostume"], 
        sprite["costumes"], 
        sprite["sounds"],
        sprite["volume"], 
        sprite["layerOrder"],
        sprite["visible"],
        sprite["x"],
        sprite["y"],
        sprite["size"],
        sprite["direction"],
        sprite["draggable"],
        sprite["rotationStyle"]
      )

    return sprites, top_blocks

class VM:
  def __init__(self, sb3):
    pth_to = Path("./temp/project").mkdir(parents=True, exist_ok=False)
    shutil.unpack_archive(sb3, pth_to , format="zip")
    with open(f"{str(pth_to)}/project.json") as f:
      self.project_data = load(f)

    self.sprites, self.top_blocks = make_sprites(self.project_data)
    
    

  def call_top_block(self, opcode, msg = None):
    if opcode in self.top_blocks:
      for hat in self.top_blocks[opcode]:
          if opcode == "event_whenbroadcastreceived":
              if hat["Block"].fields["BROADCAST_OPTION"][0] == msg:
                  
                  HasNext, next = self.run_block(hat["next"], hat["SpriteName"])
                  while HasNext:
                    HasNext, next, Block_return = self.run_block(next, hat["SpriteName"])
          else:
            self.run_block(hat["next"]) #stuff like on flag clicked lmao


  def run_block(self, block_id, Sprite_name):
    sprite:Sprite = self.sprites[Sprite_name]
    block:Block = sprite.blocks[block_id]
    opcode = block.opcode
    ret = ""
    # Dont Worry about hats, they should be taken care of by calling function

    if opcode.startswith("operator_"):
      ret = BlockDefinions.Operators.do(vm, sprite, block)

    if block.next is None:
      return False, None, ret
    else:
      return True, block.next, ret