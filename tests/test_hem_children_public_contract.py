"""Public synthetic contract: HEM-Children; no private checkout."""
from lab.hem_children_public_contract import (
    Candidate, CAPABILITY_ID, STATE, AUTHORITY, partition,
)

def candidate(identifier, **overrides):
    values = dict(semantic_approved=True, graph_approved=True, identity_valid=True,
                  rmd_ready=True, production_authorized=True)
    values.update(overrides)
    return Candidate(identifier, **values)

def test_conditional_capability_never_grants_authority():
    assert CAPABILITY_ID == "HEM_CHILDREN_INDEPENDENT_LEGITIMATE_PROGRESSION_08"
    assert STATE == "AVAILABLE_CONDITIONAL"
    assert AUTHORITY == "NONE_OF_ITS_OWN"

def test_42_and_8_synthetic_partial_delivery():
    items = [candidate(str(i)) for i in range(42)] + [
        candidate(str(i), graph_approved=False) for i in range(42,50)]
    eligible, quarantine = partition(items)
    assert len(eligible) == 42
    assert len(quarantine) == 8

def test_39_and_11_synthetic_graph_partition():
    items = [candidate(str(i)) for i in range(39)] + [
        candidate(str(i), graph_approved=False) for i in range(39,50)]
    assert tuple(map(len,partition(items))) == (39,11)

def test_failure_isolated_without_promoting_dependents():
    eligible, quarantine = partition([candidate("good"),candidate("bad",rmd_ready=False)])
    assert eligible == ["good"]
    assert quarantine == ["bad"]

def test_each_gate_fails_closed():
    for field in ("semantic_approved","graph_approved","identity_valid","rmd_ready","production_authorized"):
        assert partition([candidate(field,**{field:False})]) == ([],[field])

def test_quarantine_can_be_reassessed_without_auto_promotion():
    assert partition([candidate("q",semantic_approved=False)]) == ([],["q"])
    assert partition([candidate("q")]) == (["q"],[])
