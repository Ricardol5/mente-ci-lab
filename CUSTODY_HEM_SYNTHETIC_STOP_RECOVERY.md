# HEM TRT8_04 — Public Synthetic Stop Recovery Custody

CASE: HEM_TRT8_04_PUBLIC_CI_STOP_RECOVERY_02W
MODE: PUBLIC_SYNTHETIC_ONLY / READ_ONLY_ORIGINAL / NO_PRODUCTION_AUTHORITY

## Private source anchors (not published here)
Repository: Ricardol5/plataforma-manager (private)
Branch: mente/hem-question-inheritance-micro-mvo-01w
Historical STOP HEAD: 7cb47fe0c1657fd2965b9a64ffc5b053315f4db3
Original blob SHAs:
- app/pem_v2/hem_question_inheritance.py: cf00160ecdc89af63946ef76479fedd7802ce983
- app/pem_v2/hem_trt8_birth_contract.py: 44fdab5daae4d28e31f20ba782895c64812d77f8
- app/pem_v2/trt8_identity.py: 637d89008c6fcc70a98647b743c7db28922a03e2
- tests/test_hem_trt8_birth_contract.py: 05976bef944fe77be915e10db910d2d8a4fb6929
- db/patches/hem_trt8_04_aqm_candidate.sql: 96715784c7eb92026c3aa9790f336488ab27198d
- tests/test_hem_trt8_aqm_candidate_static.py: 3948f077944614f7ac387b4641811693fe1e59c7

## Public material
- lab/hem_synthetic_contract.py
- tests/test_hem_synthetic_stop_recovery.py
- .github/workflows/hem-synthetic-stop-recovery.yml

This is an independently authored, intentionally simplified synthetic analogue.
It does not reproduce original code, real question/concept IDs, source provenance,
original identity catalog, SQL DDL, database schemas or production data.

## Evidence limits
- Passing public tests proves only synthetic fail-closed invariants.
- It does NOT prove that the private focal tests passed under pytest.
- It does NOT prove SQL constraints, rollback, concurrency or production behavior.
- The private PR #395 remains draft; TRT8 C remains PARKED.
- No Graph/DB mutation, ADI admission, merge or deploy is authorized.

## Next gate
Confirm public workflow success and inspect pytest step logs.
A separately approved, exposure-reviewed transport would be required for exact
private-test parity. Do not infer parity from matching test counts.
