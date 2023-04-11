from typing import Optional

class Thermocouple:
    def __init__(
        self,
        forward_polynomials: list["Polynomial"],
        inverse_polynomials: list["Polynomial"],
        exponential_term: Optional[list[float]] = ...,
    ) -> None: ...
    def celsius_to_mv(self, temperature): ...
    def mv_to_celsius(self, voltage): ...

class Polynomial:
    applicable_range: "Range"
    def __init__(self, applicable_range: "Range", coefficients: list[float]) -> None: ...
    def within_range(self, value): ...
    def apply(self, x): ...

class Range:
    start: float
    end: float
    def __init__(self, start: float, end: float) -> None: ...
    def within_range(self, value): ...

type_b: Thermocouple
type_e: Thermocouple
type_j: Thermocouple
type_k: Thermocouple
type_n: Thermocouple
type_r: Thermocouple
type_s: Thermocouple
type_t: Thermocouple
