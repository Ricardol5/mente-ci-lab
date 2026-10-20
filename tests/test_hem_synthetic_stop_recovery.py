"""Independent synthetic HEM tests, not original private tests."""
from dataclasses import fields
from lab.hem_synthetic_contract import Evidence, evaluate

def test_evidence_required_and_six_gaps():
    p = evaluate(Evidence())
    assert p.decision == "EVIDENCE_REQUIRED"
    assert set(p.missing_proofs) == {
        "UNVERIFIED_SEMANTIC_MATCH", "UNVERIFIED_DESTINATION_SCOPE",
        "UNVERIFIED_SOURCE_INTEGRITY", "UNVERIFIED_GRAPH_LINEAGE",
        "UNVERIFIED_FEDERATION_SAFETY", "UNVERIFIED_NORMATIVE_CURRENCY",
    }

def test_no_authority():
    p = evaluate(Evidence())
    flags = [f.name for f in fields(p) if f.name.endswith("_authorized")]
    assert len(flags) == 5
    assert all(getattr(p, flag) is False for flag in flags)

def test_partial_evidence_stays_blocked():
    p = evaluate(Evidence(semantic=True, scope=True))
    assert p.decision == "EVIDENCE_REQUIRED"
    assert len(p.missing_proofs) == 4

def test_no_false_proof_promotion():
    p = evaluate(Evidence(lineage=True))
    assert "UNVERIFIED_SOURCE_INTEGRITY" in p.missing_proofs
    assert p.delivery_authorized is False
