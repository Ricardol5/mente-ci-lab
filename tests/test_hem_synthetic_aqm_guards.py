"""Synthetic AQM invariants: not original SQL, not a PostgreSQL execution."""
from dataclasses import dataclass

@dataclass(frozen=True)
class Mapping:
    area: str = "SYNTHETIC_AREA"
    cargo: str = "synthetic_cargo"
    eligibility: str = "AREA_BLOCKED"

def validate_mapping(m: Mapping) -> bool:
    return (m.area == "SYNTHETIC_AREA" and
            m.cargo == "synthetic_cargo" and
            m.eligibility == "AREA_BLOCKED")

def test_default_is_blocked():
    assert validate_mapping(Mapping())

def test_cross_area_rejected():
    assert not validate_mapping(Mapping(area="OTHER_AREA"))

def test_cross_cargo_rejected():
    assert not validate_mapping(Mapping(cargo="other_cargo"))

def test_eligibility_promotion_rejected():
    assert not validate_mapping(Mapping(eligibility="AREA_ELIGIBLE"))
