from typing import TypedDict

class Filterd(TypedDict):
    obj: object
    name: str


def filter_magicmethod(obj: object) -> list[Filterd]:
    return [
        {"obj": obj, "name": property_name}
        for property_name in list(filter(lambda d: "_" not in d, dir(obj)))
    ]