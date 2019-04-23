from typing import List, Set, Iterable, Tuple, Dict, TYPE_CHECKING

from eth_utils import (
    to_dict,
    to_list,
    to_ordered_dict,
    to_set,
    to_tuple,
    to_bytes,
    apply_formatter_at_index,
    apply_formatter_if,
)
from eth_utils.curried import hexstr_if_str


if TYPE_CHECKING:
    from collections import OrderedDict  # noqa: F401


@to_tuple
def typing_to_tuple() -> Iterable[int]:
    yield 1
    yield 2
    yield 3


v_tuple: Tuple[int, ...] = typing_to_tuple()


@to_list
def typing_to_list() -> Iterable[int]:
    yield 1
    yield 2
    yield 3


v_list: List[int] = typing_to_list()


@to_set
def typing_to_set() -> Iterable[int]:
    yield 1
    yield 2
    yield 3


v_set: Set[int] = typing_to_set()


@to_dict
def typing_to_dict() -> Iterable[Tuple[str, int]]:
    yield ("a", 1)
    yield ("b", 2)
    yield ("c", 3)


v_dict: Dict[str, int] = typing_to_dict()


@to_ordered_dict
def typing_to_ordered_dict() -> Iterable[Tuple[str, int]]:
    yield ("a", 1)
    yield ("b", 2)
    yield ("c", 3)


v_ordered_dict: "OrderedDict[str, int]" = typing_to_ordered_dict()


at_index_formatter_only_fn = apply_formatter_at_index(str)
at_index_formatter_fn_and_index = apply_formatter_at_index(str, 0)

if_formatter_only_condition = apply_formatter_if(bool)
if_formatter_condition_and_fn = apply_formatter_if(bool, str)


from_hex_to_bytes = hexstr_if_str(to_bytes)
