# To use this code, make sure you
#
#     import json
#
# and then, to convert JSON from a string, do
#
#     result = json_parser_from_dict(json.loads(json_string))

from dataclasses import dataclass
from typing import Any, List, Dict, TypeVar, Callable, Type, cast


T = TypeVar("T")


def from_int(x: Any) -> int:
    assert isinstance(x, int) and not isinstance(x, bool)
    return x


def from_str(x: Any) -> str:
    assert isinstance(x, str)
    return x


def from_list(f: Callable[[Any], T], x: Any) -> List[T]:
    assert isinstance(x, list)
    return [f(y) for y in x]


def from_dict(f: Callable[[Any], T], x: Any) -> Dict[str, T]:
    assert isinstance(x, dict)
    return { k: f(v) for (k, v) in x.items() }


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


@dataclass
class Userdatum:
    role_id: int
    role_status: str
    name: str
    username: str
    password: str

    @staticmethod
    def from_dict(obj: Any) -> 'Userdatum':
        assert isinstance(obj, dict)
        role_id = from_int(obj.get("role_id"))
        role_status = from_str(obj.get("role_status"))
        name = from_str(obj.get("name"))
        username = from_str(obj.get("username"))
        password = from_str(obj.get("password"))
        return Userdatum(role_id, role_status, name, username, password)

    def to_dict(self) -> dict:
        result: dict = {}
        result["role_id"] = from_int(self.role_id)
        result["role_status"] = from_str(self.role_status)
        result["name"] = from_str(self.name)
        result["username"] = from_str(self.username)
        result["password"] = from_str(self.password)
        return result


@dataclass
class JSONParser:
    userdata: List[Dict[str, Userdatum]]

    @staticmethod
    def from_dict(obj: Any) -> 'JSONParser':
        assert isinstance(obj, dict)
        userdata = from_list(lambda x: from_dict(Userdatum.from_dict, x), obj.get("userdata"))
        return JSONParser(userdata)

    def to_dict(self) -> dict:
        result: dict = {}
        result["userdata"] = from_list(lambda x: from_dict(lambda x: to_class(Userdatum, x), x), self.userdata)
        return result


def json_parser_from_dict(s: Any) -> JSONParser:
    return JSONParser.from_dict(s)


def json_parser_to_dict(x: JSONParser) -> Any:
    return to_class(JSONParser, x)
