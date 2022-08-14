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

        def do(vm, sprite, block):
            opcode = block.opcode


            if opcode == "operator_equals":
                ret = BlockDefinions.Operators.op_default_equals(
                    vm, sprite, block)

            elif opcode == "operator_add":
                ret = BlockDefinions.Operators.op_default_add(
                    vm, sprite, block)

            elif opcode == "operator_subtract":
                ret = BlockDefinions.Operators.op_default_subtract(
                    vm, sprite, block)

            elif opcode == "operator_multiply":
                ret = BlockDefinions.Operators.op_default_multiply(
                    vm, sprite, block)

            elif opcode == "operator_random":
                ret = BlockDefinions.Operators.op_default_random(
                    vm, sprite, block)

            elif opcode == "operator_gt":
                ret = BlockDefinions.Operators.op_default_gt(
                    vm, sprite, block)

            elif opcode == "operator_lt":
                ret = BlockDefinions.Operators.op_default_lt(
                    vm, sprite, block)

            elif opcode == "operator_letter_of":
                ret = BlockDefinions.Operators.op_default_get_letter(
                    vm, sprite, block)

            elif opcode == "operator_length":
                ret = BlockDefinions.Operators.op_default_length(vm, sprite, block)

            elif opcode == "operator_and":
                ret = BlockDefinions.Operators.op_default_and(vm, sprite, block)
            
            elif opcode == "operator_or":
                ret = BlockDefinions.Operators.op_default_or(vm, sprite, block)

            elif opcode == "operator_not":
                ret = BlockDefinions.Operators.op_default_not(vm, sprite, block)
            
            elif opcode == "operator_join":
                ret = BlockDefinions.Operators.op_default_join(vm, sprite, block)
            
            elif opcode == "operator_contains":
                ret = BlockDefinions.Operators.op_default_contains(vm, sprite, block)

            elif opcode == "operator_mod":
                ret = BlockDefinions.Operators.op_default_mod(vm, sprite, block)   

            elif opcode == "operator_round":
                ret = BlockDefinions.Operators.op_default_round(vm, sprite, block)
            
            elif opcode == "operator_mathop":
                raise NotImplementedError()
              
            
            return ret
        
        def op_default_equals(vm, sprite: Sprite, block: Block):
          op1, op2 = BlockDefinions._option_get(vm, block, sprite)
   
          return op1 == op2

        def op_default_add(vm, sprite: Sprite, block: Block):
            op1, op2 = BlockDefinions._option_get(vm, block, sprite)

            return int(op1) + int(op2)

        def op_default_subtract(vm, sprite: Sprite, block: Block):
            opt1, opt2 = BlockDefinions._option_get(vm, block, sprite)

            return int(opt1) - int(opt2)

        def op_default_multiply(vm, sprite: Sprite, block: Block):
            opt1, opt2 = BlockDefinions._option_get(vm, block, sprite)

            return opt1 * opt2

        # implement all of the cmds defined in opCodes.json

        def op_default_random(vm, sprite: Sprite, block: Block):
            _from, to = BlockDefinions._option_get(vm, block, sprite)

            return random.randint(_from, to)

        def op_default_gt(vm, sprite, block):
            args = BlockDefinions._option_get(vm, block, sprite)

            return args[0] > args[1]

        def op_default_lt(vm, sprite, block):
            args = BlockDefinions._option_get(vm, block, sprite)

            return args[0] < args[1]

        def op_default_get_letter(vm, sprite, block):
            args = BlockDefinions._option_get(vm, block, sprite)

            if len(args[1]) < int(args[0]):
                return None

            return args[1][int(args[0]) - 1]
        
        def op_default_length(vm, sprite, block):
            args = BlockDefinions._option_get(vm, block, sprite)

            return len(args[0])

        def op_default_and(vm, sprite, block):
            args = BlockDefinions._option_get(vm,block, sprite)

            return bool(args[0]) and bool(args[1])
        
        def op_default_or(vm, sprite, block):
          args = BlockDefinions._option_get(vm, block, sprite)

          return bool(args[0]) or bool(args[1])

        def op_default_not(vm, sprite, block):
          arggs = BlockDefinions._option_get(vm, block, sprite)

          return not bool(arggs[0])

        def op_default_join(vm, sprite, block):
          args = BlockDefinions._option_get(vm, block, sprite)

          return args[0] + args[1]

        def op_default_contains(vm, sprite, block):
          args = BlockDefinions._option_get(vm, block, sprite)

          return args[1] in args[0]
        
        def op_default_mod(vm, sprite, block):
          args = BlockDefinions._option_get(vm, block, sprite)

          return args[0] % args[1]

        def op_default_round(vm, sprite, block):
          args = BlockDefinions._option_get(vm, block, sprite)

          return round(int(args[0]))