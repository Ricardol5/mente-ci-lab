"""Synthetic HEM-Children Addendum 08 contract; no private source imported."""
from dataclasses import dataclass

CAPABILITY_ID = "HEM_CHILDREN_INDEPENDENT_LEGITIMATE_PROGRESSION_08"
STATE = "AVAILABLE_CONDITIONAL"
AUTHORITY = "NONE_OF_ITS_OWN"

@dataclass(frozen=True)
class Candidate:
    identifier: str
    semantic_approved: bool
    graph_approved: bool
    identity_valid: bool
    rmd_ready: bool
    production_authorized: bool

def partition(candidates):
    """Return independent eligible and quarantined IDs, never perform ingress."""
    eligible, quarantined = [], []
    for candidate in candidates:
        gates = (
            candidate.semantic_approved,
            candidate.graph_approved,
            candidate.identity_valid,
            candidate.rmd_ready,
            candidate.production_authorized,
        )
        (eligible if all(gates) else quarantined).append(candidate.identifier)
    return eligible, quarantined
