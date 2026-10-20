"""Public synthetic TJ-PB Graph Birth guards; no private source or credentials."""
import json
import re
from pathlib import Path

RECEIPT = Path(__file__).resolve().parents[1] / "receipts" / "tjpb-graph-birth-pr397.json"
SHA40 = re.compile(r"^[0-9a-f]{40}$")


def _receipt():
    return json.loads(RECEIPT.read_text(encoding="utf-8"))


def test_receipt_schema_and_custody():
    data = _receipt()
    assert data["case"] == "TJPB_GRAPH_BIRTH_PAPAI_OBM_01W"
    assert data["private_repository"] == "Ricardol5/plataforma-manager"
    assert data["private_pr"] == 397
    assert SHA40.fullmatch(data["private_head_sha"])
    assert data["private_code_in_public_repo"] is False
    assert data["verification_class"] == "PUBLIC_SYNTHETIC_AND_METADATA_ONLY"


def test_one_link_preserves_origin():
    link = _receipt()["minimal_link"]
    assert link["axis_target"] == "tjpb"
    assert link["official_subitem"] == "5.4"
    assert link["concept_id"] == "90e48763-3434-4ede-b02e-912d2faed530"
    assert link["source_axis"] == "linguagem"
    assert link["target_axis_does_not_own_source_concept"] is True


def test_no_false_operational_claims():
    data = _receipt()
    assert data["private_ci_status"] == "NOT_PROVEN"
    assert data["graph_link_persisted"] is False
    assert data["runtime_activated"] is False
    assert data["production_observed"] is False


def test_public_lab_is_not_private_runtime():
    data = _receipt()
    assert data["b3_authority_persisted"] is False
    assert data["rmd_adi_admitted"] is False
    assert data["sessions_released"] is False


def test_public_proof_has_exact_external_job_provenance():
    proof = _receipt()["public_ci_evidence"]
    assert proof["repository"] == "Ricardol5/mente-ci-lab"
    assert proof["run_id"] == 39505822311
    assert proof["job_id"] == 118914356803
    assert proof["checkout_sha"] == "e58ef994cc3558ff596fdc38bd1463581b09d40b"
    assert proof["pytest_result"] == "4 passed in 0.02s"
    assert proof["scope"] == "PUBLIC_SYNTHETIC_ONLY"


def test_public_ci_pass_does_not_imply_private_runtime_pass():
    data = _receipt()
    assert data["public_ci_evidence"]["pytest_result"].startswith("4 passed")
    assert data["private_ci_status"] == "NOT_PROVEN"
    assert data["graph_link_persisted"] is False
    assert data["production_observed"] is False
