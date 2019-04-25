from typing import List, Set, Iterable, Tuple, Dict, TYPE_CHECKING

from eth_utils import to_bytes, to_dict, to_list, to_ordered_dict, to_set, to_tuple
from eth_utils.curried import (
    apply_formatter_at_index,
    apply_formatter_if,
    apply_formatters_to_dict,
    apply_formatters_to_sequence,
    apply_formatter_to_array,
    apply_key_map,
    apply_one_of_formatters,
    from_wei,
    hexstr_if_str,
    is_same_address,
    text_if_str,
    to_wei,
)


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

to_dict_formatter = apply_formatters_to_dict({"a": int})

to_sequence_formatter = apply_formatters_to_sequence((int,))

to_array_formatter = apply_formatter_to_array(len)

key_map = apply_key_map({"key": "KEY"})

one_of_formatter = apply_one_of_formatters(((bool, int),))

wei_to_ether = from_wei(unit="ether")
from_100_wei = from_wei(100)

from_hex_to_bytes = hexstr_if_str(to_bytes)

is_zero_address = is_same_address("0x" + "00" * 20)

from_text_to_bytes = text_if_str(to_bytes)

ether_to_wei = to_wei(unit="ether")
wei_from_100_units = to_wei(100)
