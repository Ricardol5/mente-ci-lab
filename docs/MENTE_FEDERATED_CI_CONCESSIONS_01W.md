# MENTE — CI Federado / Matriz de Concessões 01W

CASE = MENTE_FEDERATED_CI_CONCESSIONS_01W
DRIVER = MENTE
AUTHORITY = H / MENTE
MODE = DOCUMENTATION_ONLY / LAC / CLS / OBM / PCC_STRICT
TARGET = Ricardol5/plataforma-manager PR #396
STATE = PARTIAL_EVIDENCE / NO_AUTHORITY_BRIDGE

## 1. Princípio

O local de execução não transfere autoridade de integração. Nenhum check privado obrigatório é satisfeito automaticamente por um workflow de outro repositório. Nunca afirmar PASS para código privado a partir de recibo de metadados.

## 2. Concessões

| Classe | Executor | Evidência admissível | Limite |
| --- | --- | --- | --- |
| P0 — Schema de receipt, checkout, integridade sintática de metadados | `mente-ci-lab` público | Run SUCCESS + commit público + SHA privado declarado | Não verifica bytes privados nem testes privados |
| P1 — Testes sintéticos com fixtures públicas sem material proprietário | `mente-ci-lab` público | Run SUCCESS + teste/fixture públicos + commit | Não extrapolar para produção privada |
| V0 — Diff, escopo, Git blob, SHA do head e revisão da PR | `plataforma-manager` privado / leitura autenticada | Compare/patch/commit privados | Não equivale a CI runtime |
| V1 — Compile, pytest, contratos runtime e PostgreSQL isolado privados | `plataforma-manager` privado ou executor autorizado com acesso privado protegido | Logs/testes realmente executados contra SHA exato | Sem código privado em repositório público; sem token de escrita ou segredos em jobs não confiáveis |
| A0 — Branch protection, required checks, review, merge | GitHub do repositório privado | Estado de proteção e decisão do próprio GitHub | Receipt externo não substitui required checks |
| D0 — Deploy, health e readback | Render e endpoints de produção autorizados | Deploy id + SHA + health + readback | Não comprova invocação funcional nem nascimento Graph |

## 3. Regra de fronteira

Se a ponte GitHub público ↔ privado não for autorizada ou não for tecnicamente comprovada: manter trilhos independentes; registrar `BRIDGE_NOT_PROVEN`, manter checks privados `NOT_PROVEN`, bloquear promoção de evidência e merge enquanto requisitos obrigatórios não forem satisfeitos.

Alternativas legítimas, somente após decisão explícita e análise de risco: runner self-hosted sob custódia privada, GitHub App com permissões mínimas e execução em ref confiável, ou execução isolada privada fora do Actions com atestação verificável. Não instalar tokens, publicar código, remover branch protection ou fabricar status checks.

## 4. PR #396 — checkpoint

PRIVATE_HEAD = f31cf491cd4f86c5a284a8e2213f4d96545bb168
PRIVATE_BLOB_SHA1 = eb3f79a3464ffadde03e571e1284726af57d4fcb
PUBLIC_RECEIPT = receipts/tjpb-c-pr396.json
PUBLIC_CI = SUCCESS observed by human screenshot for run #2 and #3; metadata-only
PRIVATE_CI = FAILURE observed; cause not independently proven
PRIVATE_REQUIRED_CHECKS = UNKNOWN
MERGE = HOLD
DEPLOY = HOLD
GRAPH_DB = READ_ONLY
WAGON_C = OPEN

## 5. Próximo NGH

1. Obter regras de proteção e checks requeridos na PR privada.
2. Para cada check, identificar se exige código privado e qual runner autorizado pode executá-lo.
3. Reconciliar SHA exato e resultado de execução antes de promover qualquer gate.
4. Se uma proteção obrigatória não puder ser satisfeita, STOP documentado; nenhuma alteração de proteção implícita.
