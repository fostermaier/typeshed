from typing import Any, Optional, Self
from datetime import datetime

import numpy as np

EPOCH: np.datetime64

class TdmsTimestamp:
    seconds: int
    second_fractions: float
    def __init__(self, seconds: int, second_fractions: float) -> None: ...
    def as_datetime64(self, resolution: str = ...) -> np.datetime64: ...
    def as_datetime(self) -> datetime: ...

class TimestampArray(np.ndarray):
    def __new__(cls, input_array: np.ndarray[Any, np.dtype[np.int_]]) -> Self: ...
    def __array_finalize__(self, obj: Optional[np.ndarray[Any, Any]]) -> None: ...
    def __getitem__(self, item) -> Any: ...
    @property
    def seconds(self) -> np.ndarray[Any, np.dtype[np.int_]]: ...
    @property
    def second_fractions(self) -> np.ndarray[Any, np.dtype[np.int_]]: ...
    def as_datetime64(self, resolution: str = ...) -> np.datetime64: ...
