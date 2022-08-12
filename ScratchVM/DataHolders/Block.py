from __future__ import annotations

from dataclasses import dataclass

from typing import Any as any


@dataclass
class Block:
  ID: str #random letters generated on block creation on scratch
  opcode: str
  inputs: dict
  fields: dict[list[any, int]]
  topLevel: bool

  next: str
  parent: str

  