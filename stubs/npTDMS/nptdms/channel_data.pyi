from _typeshed import Incomplete

log: Incomplete

def get_data_receiver(obj, num_values, raw_timestamps, memmap_dir: Incomplete | None = ...): ...

class ListDataReceiver:
    scaler_data: Incomplete
    def __init__(self, channel) -> None: ...
    def append_data(self, data) -> None: ...
    @property
    def data(self): ...

class NumpyDataReceiver:
    path: Incomplete
    data: Incomplete
    scaler_data: Incomplete
    def __init__(self, obj, num_values, memmap_dir: Incomplete | None = ...) -> None: ...
    def append_data(self, new_data) -> None: ...

class DaqmxDataReceiver:
    path: Incomplete
    data: Incomplete
    scaler_data: Incomplete
    def __init__(self, obj, num_values, memmap_dir: Incomplete | None = ...) -> None: ...
    def append_scaler_data(self, scale_id, new_data) -> None: ...

class TimestampDataReceiver:
    path: Incomplete
    data: Incomplete
    scaler_data: Incomplete
    def __init__(self, obj, num_values, raw_timestamps: bool = ..., memmap_dir: Incomplete | None = ...) -> None: ...
    def append_data(self, new_data) -> None: ...

class RawDataSlice:
    data: Incomplete
    scaler_data: Incomplete
    def __init__(self, data, scaler_data) -> None: ...

def slice_raw_data(raw_data, offset, length: Incomplete | None = ...): ...
