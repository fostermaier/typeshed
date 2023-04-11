from _typeshed import Incomplete
from typing import Any

import numpy as np

log: Incomplete
RAW_DATA_INPUT_SOURCE: int
VOLTAGE_EXCITATION: int
CURRENT_EXCITATION: int

class NoOpScaling:
    input_source: str
    def __init__(self, input_source: str) -> None: ...
    @staticmethod
    def from_properties(properties, scale_index, scale_name): ...
    def scale(self, data): ...

class LinearScaling:
    intercept: float
    slope: float
    input_source: str
    def __init__(self, intercept: float, slope: float, input_source: str) -> None: ...
    @staticmethod
    def from_properties(properties, scale_index): ...
    def scale(self, data): ...

class PolynomialScaling:
    coefficients: list[float]
    input_source: str
    def __init__(self, coefficients: list[float], input_source: str) -> None: ...
    @staticmethod
    def from_properties(properties, scale_index): ...
    def scale(self, data): ...

class RtdScaling:
    current_excitation: float
    r0_nominal_resistance: float
    a: float
    b: float
    c: float
    lead_wire_resistance: float
    resistance_configuration: int
    input_source: str
    def __init__(
        self,
        current_excitation: float,
        r0_nominal_resistance: float,
        a: float,
        b: float,
        c: float,
        lead_wire_resistance: float,
        resistance_configuration: int,
        input_source: str,
    ) -> None: ...
    @staticmethod
    def from_properties(properties, scale_index): ...
    def scale(self, data): ...

class StrainScaling:
    configuration: Incomplete
    poisson_ratio: Incomplete
    gage_resistance: Incomplete
    lead_wire_resistance: Incomplete
    initial_bridge_voltage: Incomplete
    gage_factor: Incomplete
    gain_adjustment: Incomplete
    voltage_excitation: Incomplete
    input_source: Incomplete
    def __init__(
        self,
        configuration: int,
        poisson_ratio: float,
        gage_resistance: float,
        lead_wire_resistance: float,
        initial_bridge_voltage: float,
        gage_factor: float,
        gain_adjustment: float,
        voltage_excitation: float,
        input_source: str,
    ) -> None: ...
    @staticmethod
    def from_properties(properties, scale_index): ...
    def scale(self, data): ...
    FULL_BRIDGE_1: int
    FULL_BRIDGE_2: int
    FULL_BRIDGE_3: int
    HALF_BRIDGE_1: int
    HALF_BRIDGE_2: int
    QUARTER_BRIDGE_1: int
    QUARTER_BRIDGE_2: int

class TableScaling:
    input_values: Incomplete
    output_values: Incomplete
    input_source: Incomplete
    def __init__(
        self, pre_scaled_values: np.ndarray[Any, Any], scaled_values: np.ndarray[Any, Any], input_source: str
    ) -> None: ...
    @staticmethod
    def from_properties(properties, scale_index): ...
    def scale(self, data): ...

class ThermistorScaling:
    excitation_type: Incomplete
    excitation_value: Incomplete
    resistance_configuration: Incomplete
    r1_reference_resistance: Incomplete
    lead_wire_resistance: Incomplete
    a: Incomplete
    b: Incomplete
    c: Incomplete
    temperature_offset: Incomplete
    input_source: Incomplete
    def __init__(
        self,
        excitation_type: int,
        excitation_value: float,
        resistance_configuration: int,
        r1_reference_resistance: float,
        lead_wire_resistance: float,
        a: float,
        b: float,
        c: float,
        temperature_offset: float,
        input_source: str,
    ) -> None: ...
    @staticmethod
    def from_properties(properties, scale_index): ...
    def scale(self, data): ...

class ThermocoupleScaling:
    thermocouple: Incomplete
    scaling_direction: Incomplete
    input_source: Incomplete
    def __init__(self, type_code: int, scaling_direction: int, input_source: str) -> None: ...
    @staticmethod
    def from_properties(properties, scale_index): ...
    def scale(self, data): ...

class AddScaling:
    left_input_source: Incomplete
    right_input_source: Incomplete
    def __init__(self, left_input_source: str, right_input_source: str) -> None: ...
    @staticmethod
    def from_properties(properties, scale_index): ...
    def scale(self, left_data, right_data): ...

class SubtractScaling:
    left_input_source: Incomplete
    right_input_source: Incomplete
    def __init__(self, left_input_source: str, right_input_source: str) -> None: ...
    @staticmethod
    def from_properties(properties, scale_index): ...
    def scale(self, left_data, right_data): ...

class DaqMxScalerScaling:
    scale_id: Incomplete
    def __init__(self, scale_id: int) -> None: ...
    def scale_daqmx(self, scaler_data): ...

class MultiScaling:
    scalings: Incomplete
    def __init__(self, scalings: list[int]) -> None: ...
    def scale(self, raw_channel_data): ...
    def get_dtype(self, raw_data_type, scaler_data_types): ...

def get_scaling(channel_properties, group_properties, file_properties): ...
