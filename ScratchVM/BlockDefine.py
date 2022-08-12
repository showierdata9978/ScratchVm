from .DataHolders import Block, Sprite
import random


class BlockDefinions:
  def _option_get(vm, block, sprite):

    args = []
    
    for impt in block.inputs.values():
      if type(impt[1]) is str:
        _, _, op = vm.run_block(impt[1], sprite.name)
      else:
        op = impt[1][1]
      args.append(op)
      
    return args
  class Operators:

  
    def op_default_equals(vm, sprite:Sprite, block:Block):
        op1, op2 = BlockDefinions._option_get(vm, block, sprite)
        return op1 == op2
    
    def op_default_add(vm, sprite:Sprite, block:Block):
        op1, op2 = BlockDefinions._option_get(vm, block, sprite)
      
        return int(op1) + int(op2)

    def op_default_subtract(vm, sprite:Sprite, block:Block):
        opt1, opt2 = BlockDefinions._option_get(vm, block, sprite)

        return int(opt1)- int(opt2)

    def op_default_multiply(vm , sprite:Sprite, block:Block):
      opt1, opt2 = BlockDefinions._option_get(vm, block, sprite)

      return opt1 * opt2
    
    #implement all of the cmds defined in opCodes.json

    def op_default_random(vm, sprite:Sprite, block:Block):
      _from, to = BlockDefinions._option_get(vm, block, sprite)

      return random.randint(_from, to)