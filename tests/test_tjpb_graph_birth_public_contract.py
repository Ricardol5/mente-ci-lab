"""Public synthetic TJ-PB Graph Birth guards; no private source or credentials."""
import json
from pathlib import Path

RECEIPT = Path(__file__).resolve().parents[1] / 'receipts' / 'tjpb-graph-birth-pr397.json'


def test_receipt_schema_and_custody():
    data = json.loads(RECEIPT.read_text(encoding='utf-8'))
    assert data['case'] == 'TJPB_GRAPH_BIRTH_PAPAI_OBM_01W'
    assert data['private_repository'] == 'Ricardol5/plataforma-manager'
    assert data['private_pr'] == 397
    assert len(data['private_head_sha']) == 40
    assert data['private_code_in_public_repo'] is False
    assert data['verification_class'] == 'PUBLIC_SYNTHETIC_AND_METADATA_ONLY'


def test_one_link_preserves_origin():
    link = json.loads(RECEIPT.read_text(encoding='utf-8'))['minimal_link']
    assert link['axis_target'] == 'tjpb'
    assert link['official_subitem'] == '5.4'
    assert link['concept_id'] == '90e48763-3434-4ede-b02e-912d2faed530'
    assert link['source_axis'] == 'linguagem'
    assert link['target_axis_does_not_own_source_concept'] is True


def test_no_false_operational_claims():
    data = json.loads(RECEIPT.read_text(encoding='utf-8'))
    assert data['private_ci_status'] == 'NOT_PROVEN'
    assert data['graph_link_persisted'] is False
    assert data['runtime_activated'] is False
    assert data['production_observed'] is False


def test_public_lab_is_not_private_runtime():
    data = json.loads(RECEIPT.read_text(encoding='utf-8'))
    assert data['b3_authority_persisted'] is False
    assert data['rmd_adi_admitted'] is False
    assert data['sessions_released'] is False
