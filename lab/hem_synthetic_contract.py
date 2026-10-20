"""Synthetic HEM stop-recovery contract: no real question IDs or private imports."""
from dataclasses import dataclass

@dataclass(frozen=True)
class Evidence:
    semantic: bool = False
    scope: bool = False
    integrity: bool = False
    lineage: bool = False
    federation: bool = False
    normative: bool = False

@dataclass(frozen=True)
class Proposal:
    decision: str
    missing_proofs: tuple[str, ...]
    graph_write_authorized: bool = False
    db_write_authorized: bool = False
    merge_authorized: bool = False
    deploy_authorized: bool = False
    delivery_authorized: bool = False

def evaluate(e: Evidence) -> Proposal:
    checks = (("SEMANTIC_MATCH", e.semantic), ("DESTINATION_SCOPE", e.scope),
              ("SOURCE_INTEGRITY", e.integrity), ("GRAPH_LINEAGE", e.lineage),
              ("FEDERATION_SAFETY", e.federation), ("NORMATIVE_CURRENCY", e.normative))
    return Proposal("EVIDENCE_REQUIRED", tuple("UNVERIFIED_" + name for name, ok in checks if not ok))
