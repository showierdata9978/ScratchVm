from .DataHolders import Block, Sprite

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
      
        return op1 + op2

    def op_default_subtract(vm, sprite:Sprite, block:Block):
        opt1, opt2 = BlockDefinions._option_get(vm, block, sprite)

        return opt1 - opt2

    def _op_default_multiply(vm , sprite:Sprite, block:Block):
      opt1, opt2 = BlockDefinions._option_get(vm, block, sprite)

      return opt1 * opt2