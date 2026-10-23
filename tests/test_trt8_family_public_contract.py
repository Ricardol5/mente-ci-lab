"""Public synthetic contract only; does not import or checkout private code."""
import json
import re
from pathlib import Path

RECEIPT = Path(__file__).resolve().parents[1] / "receipts" / "trt8-family-pr409.json"


def receipt():
    return json.loads(RECEIPT.read_text(encoding="utf-8"))


def recognize(axis, area, slug):
    return axis == "trt8" and receipt()["expected_contract"]["valid_slug_by_area"].get(area) == slug


def test_receipt_custody_and_no_private_source():
    d = receipt()
    assert d["private_repository"] == "Ricardol5/plataforma-manager"
    assert d["private_pr"] == 409
    assert re.fullmatch(r"[0-9a-f]{40}", d["private_head_sha"])
    assert d["private_code_in_public_repo"] is False
    assert d["public_ci_class"] == "PUBLIC_SYNTHETIC_AND_METADATA_ONLY"


def test_valid_priority_composites_and_cross_axis_rejection():
    assert all(recognize("trt8", area, slug) for area, slug in receipt()["expected_contract"]["valid_slug_by_area"].items())
    assert not recognize("tjce", "TRT8_04", "analista_judiciario")
    assert not recognize("trt8", "TRT8_23", "analista_judiciario")
    assert not recognize("trt8", "TRT8_04", "tecnico_judiciario")


def test_synthetic_pre_insert_failure_response():
    c = receipt()["expected_contract"]
    assert c["invalid_composite_status"] == 422
    assert c["delivery_not_authorized_status"] == 409
    assert c["session_created"] is False
    assert c["cached_resume_allowed"] is False


def test_public_ci_never_certifies_private_runtime():
    d = receipt()
    assert d["private_runtime_verified"] is False
    assert d["session_created_observed"] is False
    assert d["graph_persisted"] is False
    assert d["production_observed"] is False
