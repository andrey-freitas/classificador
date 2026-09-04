# AUDITORIA INDEPENDENTE — ÁRVORE MESTRA DE ENGENHARIA DE PETRÓLEO

**Auditor:** independente (não autor da árvore).  
**Data:** 2026-09-04 (2ª passagem — corpus `00_ENTRADA_ESPECIFICAS.jsonl` agora no pacote).  
**O que este relatório não faz:** não reconstrói a árvore, não reclassifica o corpus, não reabre a regra 7, não julga pelo nome da prova nem pelo rótulo preliminar da ENTRADA.

| Papel | Arquivo | SHA-256 |
|---|---|---|
| Árvore | `PETROLEO.md` | `abaf64c9d891d11882b3b6a57cdee4b357d98af1f974b09144a9a0bea31dc185` |
| Mapeamento | `MAPEAMENTO_PETROLEO.json` | `7e6794e2c94f6d2671120de8412d0fe3b457edde49990a59e16cb82c44d0e8da` |
| Corpus | `00_ENTRADA_ESPECIFICAS.jsonl` | `e3396d3498c52e7c8885e77f155a0fb53db90af1410dafce6423fd6e38b0e056` (1.354 linhas) |
| Núcleo Básico | `NUCLEO_BASICO.md` | `43f71eee951357922561a77879accbad437b4a698725712aacb7d1e6da9b4cef` |
| Estilo (não conteúdo) | `PRODUCAO.md` | árvore congelada de Engenharia de Produção |

Evidência de conteúdo = somente `nucleo_cobrado`. Os **1.342** núcleos em árvore foram lidos, agrupados pelos 262 subassuntos. Contestação só conta se cita regra/FRONT **e** o destino proposto existe (folha da Parte I, id do Núcleo Básico, ou `I`).

---

## Resumo executivo

**Veredito: NÃO CONGELÁVEL.**

B agora é certificável. Contestações válidas: **16 altas / 9 médias / 7 baixas** (32 itens, 2,4% dos 1.342 em árvore). As 12 saídas oficiais estão corretas. Três nomes gênero-sobre-espécie e a ordem alfabética (Unicode vs folding da Produção) continuam abertos.

| Severidade | N | Critério |
|---|---|---|
| Alta (disciplina errada ou deveria ser I/BASICAS) | 16 | 9→I; 2 GEO→RESERV; 1 GEO→COMERC; 1 INS_MAR→POCO; 1 REGUL→COMERC; 1 REGUL→SEG_PRO; 1 ELE_ESC→INS_SUB |
| Média (assunto errado, disciplina certa) | 9 | 7× Q58 OBJETIVA em `REGUL_06_001`; Mosqueiro; EOR no PDP |
| Baixa (sub vizinho mais específico) | 7 | depleção; 2× EOR misto; acidificação; SGSO; esquemas de refino; play |

Três achados mais importantes:

1. **Nove itens em árvore deveriam ser `I`** (`PET_FRONT_004`, regras 4 e 6): cinco `prova_gab` de teoria do Estado regulador/captura em `REGUL_04_002`; três certames genéricos (inexigibilidade, justificativa de contratação direta, homologação) em `REGUL_04_005`; interpolação IDW/Spline em GIS sem âncora petrolífera em `GEO_04_002`.
2. **Sete altas de disciplina** com FRONT explícita: fluxo/alocação em fratura em `GEO_04_004` (FRONT_006); avaliação econômico-financeira de E&P em GEO (FRONT_010); jack-up em `INS_MAR_02_002` (FRONT_023); papel do distribuidor (FRONT_042); classe técnica de GLP (FRONT_002 / regra 5); ILI/pig de integridade em `ELE_ESC_03_003` (FRONT_025).
3. **Três folhas gênero** cujas irmãs já são a espécie — `GEOF_02_003` Inversão Sísmica vs `GEOF_02_001` Inversão Elástica; `RESERV_03_004` Mecanismos Primários vs `RESERV_03_003` Gás em Solução; `POCO_03_004` Métodos de Estimulação vs acidificação/fratura — mais 2 assuntos e 9 grupos de subassuntos fora do folding NFD da Produção.

Alocação sem contestação válida: **97,6%** dos 1.342. COMERC, GEOF, PETROF, INS_SUB, PROC_PRI, PRJ, QUI_PET e SUST: zero contestação válida.

---

## A. Integridade mecânica

### Método

Parser da Parte I de `PETROLEO.md` (corte em `# PARTE II`) e da Parte I de `NUCLEO_BASICO.md`. Join campo a campo dos 1.354 `id_global` de `MAPEAMENTO_PETROLEO.json` com as 1.354 linhas de `00_ENTRADA_ESPECIFICAS.jsonl`. Ordem alfabética = `unicodedata.normalize("NFD")` + strip de combining + `casefold` (a chave que deixa Produção com 0 violações de assunto/subassunto). Siglas da Parte II = tokens `` `SIGLA` ``, excluídos `BASICAS`, `TECNICA`, `NORMAS`, `I`.

### Números

| Checagem | Resultado |
|---|---|
| Disciplinas / assuntos / subassuntos | **16 / 77 / 262** |
| ENTRADA linhas / `id_global` únicos | **1.354 / 1.354** |
| Mapeamento registros / únicos | **1.354 / 1.354** |
| Bijeção ENTRADA ↔ MAPEAMENTO | **1.354 = 1.354** (0 órfão, 0 mapeado-sem-entrada) |
| `nucleo_cobrado` vazio | **0** |
| Dentro da árvore / BASICAS / I | **1.342 / 4 / 8** |
| Destinos in-tree inexistentes na Parte I | **0** |
| Destinos BASICAS inexistentes no Núcleo | **0** |
| `nome_assunto` / `nome_subassunto` ≠ árvore | **0** |
| Filho cujo ID não prefixa o pai | **0** |
| Lacunas de numeração em assunto ou subassunto | **0** |
| ID duplicado / nome duplicado (exato) no mesmo pai | **0 / 0** |
| Nome de assunto ou subassunto repetido na árvore | **0** |
| Folha vazia hoje (regra 8) | **0** |
| `PET_FRONT_001` … `052` contínuos | **sim** (52/52) |
| Sigla da Parte II sem destino nas duas árvores | **0** (`MEC_FLU_07` existe como assunto) |
| Ordem folding — disciplinas (nomes PT) | **fora** (a Parte I está por **sigla**) |
| Ordem folding — assuntos | **2** pais (`GEO`, `PROC_PRI`) |
| Ordem folding — subassuntos | **9** pais |
| Ordem Unicode codepoint — assuntos / subassuntos | **0 / 0** (filhos já estão em codepoint) |

Disciplinas, pela sigla: COMERC (48), ELE_ESC (54), GEO (261), GEOF (119), INS_MAR (25), INS_SUB (58), PETROF (74), POCO (113), PRJ (41), PROC_PRI (54), QUI_PET (18), REF_GAS (38), REGUL (235), RESERV (159), SEG_PRO (29), SUST (16).

### Achados

**A1. Bijeção conferida.** Todo `id_global` da ENTRADA aparece exatamente uma vez no mapeamento.

**A2. IDs e cobertura íntegros.** Nenhuma lacuna `_NNN`, nenhum destino fantasma, nenhum nome colidente.

**A3. Ordem alfabética fora da convenção da casa (estilo Produção).** Produção: 0 assuntos e 0 subassuntos fora do folding. Petróleo ordena filhos por **codepoint Unicode** (`Á` depois de Z; `CAPEX` antes de `Cadeia`) e disciplinas por **sigla** (Geologia antes de Geofísica; Gestão de Projetos `PRJ` entre Poços e Processamento).

Assuntos:

| Pai | Ordem atual | Ordem folding |
|---|---|---|
| `GEO` | Geologia **Estrutural**, Geologia **de Reservatórios e Operações** | de Reservatórios, Estrutural |
| `PROC_PRI` | Tratamento de **Gás** Natural, Tratamento de **Água** Produzida | Água, Gás |

Subassuntos (9 pais): `COMERC_03` (CAPEX vs Cadeia); `ELE_ESC_04` (Índice depois de Sistema Integrado); `GEO_07` (Bacias Interiores vs Bacias do Norte); `INS_MAR_03` (Água de Injeção no fim); `INS_SUB_01` (Árvore de Natal no fim); `INS_SUB_04` (Instalação de Árvore depois de Manifolds); `RESERV_04` (Injeção de Água depois de Injeção de Gás); `RESERV_05` (Cálculo Volumétrico depois de Curvas de Declínio); `SEG_PRO_01` (Áreas Classificadas no fim).

Congelar exige remapear IDs à ordem folding **ou** documentar na Parte II que Petróleo usa Unicode/sigla, não NFD-fold.

---

## B. Alocação (1.342 núcleos)

### Método

Join `id_global` → `subassunto` → `nucleo_cobrado`. Leitura exaustiva por folha (262 grupos). Contestação só se o núcleo **contradiz** o destino + FRONT/regra aplicável, **e** o destino correto existe. “Eu teria colocado em outro lugar” não conta.

### Números

| | N |
|---|---|
| Núcleos lidos em árvore | **1.342 / 1.342** |
| Contestações válidas | **32** (16 / 9 / 7) |
| Sem contestação válida | **1.310** (97,6%) |

Por disciplina de origem (mapeamento atual):

| Disc | n | Alta | Média | Baixa |
|---|---|---|---|---|
| REGUL | 235 | 10 | 7 | 0 |
| GEO | 261 | 4 | 1 | 1 |
| RESERV | 159 | 0 | 1 | 3 |
| INS_MAR | 25 | 1 | 0 | 0 |
| ELE_ESC | 54 | 1 | 0 | 0 |
| POCO | 113 | 0 | 0 | 1 |
| SEG_PRO | 29 | 0 | 0 | 1 |
| REF_GAS | 38 | 0 | 0 | 1 |
| COMERC, GEOF, PETROF, INS_SUB, PROC_PRI, PRJ, QUI_PET, SUST | 428 | 0 | 0 | 0 |

### B1 — Altas (16)

#### B1.1 Cinco teorias genéricas de regulação em `REGUL_04_002` → `I` (`PET_FRONT_004`, regra 6)

IDs: `prova_gab__PASSADA_01__Q38`, `…Q39`, `…Q41`, `…Q42`, `…Q43`.

Núcleos: Estado regulador vs provedor; função reguladora vs regulamentar; autonomia da agência; captura por interesses privados; espécies de captura. Nenhum trecho de petróleo, ANP, CNPE ou energia. `PET_FRONT_004`: “qualquer direito ou administração genéricos. Não forçar um destino aproximado.” A mesma série `prova_gab` já mandou Lei 8.987 para I. A folha `REGUL_04_002` (Estado Regulador e Agências, n=5) esvazia → regra 8.

#### B1.2 Três certames genéricos em `REGUL_04_005` → `I` (`PET_FRONT_004`, regra 6)

- `Prova-Matriz-Especialista-em-Petroleo-e-Gas-Gestao-de-Projetos-e-Contratos-em-Oleo-e-Gas-11-12-2025__PASSADA_01__Q41` — justificativa de preço e de escolha do fornecedor na contratação direta.
- `…__Q43` — exclusividade de fornecedor como requisito da inexigibilidade.
- `…__Q51` — homologação/revogação como fase final do certame.

Nenhum núcleo cita Petrobras, Lei 13.303 nem petróleo. `PET_FRONT_045` reserva REGUL para o regime jurídico da estatal; sem essa âncora, FRONT_004 manda `I`. **Não contestado** o gêmeo `…__Q30` (auditores independentes das demonstrações): FRONT_045 (“governança e auditoria de estatais”) cobre.

#### B1.3 `2010-epe-analista-de-pesquisa-energetica-petroleo-exploracao-prova__PASSADA_01__Q24` em `GEO_04_002` → `I` (regras 4 e 6)

Núcleo: algoritmos IDW e Spline como interpolação espacial em SIG. Sem âncora de E&P. Não há folha de GIS no Núcleo Básico. Geoestatística da folha é krigagem/variograma, não IDW.

#### B1.4 Dois fluxos em fratura / alocação injetor-produtor em `GEO_04_004` → `RESERV_06_001` (`PET_FRONT_006`, regra 7)

- `Prova-Matriz-Especialista-em-Petroleo-e-Gas-Geologia-de-Exploracao-11-12-2025__PASSADA_01__Q36` — orientação e condutividade da rede de fraturas na **modelagem de fluxo** e **alocação de poços**.
- `Prova-Matriz-Especialista-em-Petroleo-e-Gas-Geologia-de-Reservatorios-11-12-2025__PASSADA_01__Q41` — fraturas condutivas ou selantes na modelagem e **otimização de produtores e injetores**.

`GEO_04_004` é “Reservatórios Fraturados” (estático). FRONT_006: simulação de fluxo / gerenciamento a partir do modelo = Reservatórios. Destino: `RESERV_06_001` Gerenciamento de Reservatórios. A folha geológica (n=2) esvazia → regra 8.

#### B1.5 `2010-epe-analista-de-pesquisa-energetica-petroleo-exploracao-prova__PASSADA_01__Q40` em `GEO_01_003` → `COMERC_03_003` (`PET_FRONT_010`)

Núcleo: integração de riscos **geológicos, econômicos e financeiros** na **avaliação de projetos** de E&P. FRONT_010: decisão econômico-financeira = Comercialização. Gêmeo já em `COMERC_03_003`: `2012-epe-analista-de-pesquisa-energetica-petroleo-exploracao-prova__PASSADA_01__Q46`.

#### B1.6 `2005_ESPECIALISTA EM REGULACAO DE PETROLEO_1-PROVA__PASSADA_01__Q40` em `INS_MAR_02_002` → `POCO_07_002` (`PET_FRONT_023`)

Núcleo: plataformas autoeleváveis (jack-up) não operam em lâmina > 200 m. FRONT_023: sonda/autoelevável = Poços (`POCO_07_002` Sondas Offshore). A folha atual é “Plataformas Fixas, Semissubmersíveis e TLP” — o jack-up nem é um desses tipos.

#### B1.7 `2005_ESPECIALISTA EM REGULACAO DE PETROLEO_2-PROVA__PASSADA_01__Q41` em `REGUL_02_002` → `COMERC_03_002` (`PET_FRONT_042`)

Núcleo: escopo do **distribuidor** (atacado e logística para o varejo). FRONT_042: papel de agente na cadeia comercial = Comercialização, não autorização ANP. Destino: `COMERC_03_002` Cadeia de Valor e Logística.

#### B1.8 `2008_ESPECIALISTA EM REGULACAO DE PETROLEO E DERIVADOS_2-PROVA __PASSADA_01__Q58` em `REGUL_02_002` → `SEG_PRO_01_003` (`PET_FRONT_002`, regra 5)

Núcleo: parâmetro **técnico** das classes de armazenamento de recipientes de GLP. Convenção TECNICA: critério de classificação de área/armazenamento fica em Segurança de Processo (`SEG_PRO_01_003`), não no marco de distribuição.

#### B1.9 `2008_ESPECIALISTA EM REGULACAO DE PETROLEO E DERIVADOS_1-PROVA __PASSADA_01__Q56` em `ELE_ESC_03_003` → `INS_SUB_05_002` (`PET_FRONT_025`)

Núcleo: ferramenta para detectar em operação **corrosão interna, perda de espessura e mossas** em dutos (ILI / pig instrumentado de integridade). FRONT_025: pigging como garantia de escoamento = ELE_ESC; integridade da linha = INS_SUB (`INS_SUB_05_002` Gestão de Integridade). Os outros três núcleos de `ELE_ESC_03_003` (aprisionamento de PIG, pigs de espuma/limpeza, diretrizes de passagem) permanecem.

### B2 — Médias (9)

#### B2.1 Sete `Q58` OBJETIVA em `REGUL_06_001` → `REGUL_07_005` (regra 1)

IDs: `OBJETIVA-09-GMO09-Gerenciamento-e-Monitoramento-das-Operacoes-com-Pocos__PASSADA_01__Q58`; `OBJETIVA-10-OSS10-Operacao-de-Sistemas-Submarinos-de-Producao__PASSADA_01__Q58`; `OBJETIVA-11-PIP11-Processo-de-Individualizacao-de-Producao__PASSADA_01__Q58`; `OBJETIVA-12-IDG12-Interpretacao-de-Dados-Geofisicos__PASSADA_01__Q58`; `OBJETIVA-13-OGP13-Operacao-Geologica-em-Pocos-Exploratorios__PASSADA_01__Q58`; `OBJETIVA-14-CMR14-Caracterizacao-e-Modelagem-de-Reservatorios__PASSADA_01__Q58`; `OBJETIVA-15-MGR15-Modelagem-e-Gerenciamento-de-Reservatorios__PASSADA_01__Q58`.

Núcleo: receitas/participações governamentais **devidas no regime de partilha** (Lei 12.351 art. 42: bônus e royalties — sem participação especial). `REGUL_06_001` é “Bônus e Participação Especial” (marco da concessão, Lei 9.478). O conhecimento determinante é o elenco de takes da **partilha** → `REGUL_07_005`.

Não contestados os Q54 (premissas CNPE da 3ª Rodada para excedente) nem os Q55 (SGPP): cabem em `REGUL_06_002` Custo em Óleo e Excedente em Óleo.

#### B2.2 `2006-epe-tecnico-de-nivel-superior-petroleo-exploracao-e-producao-prova__PASSADA_01__Q42` em `GEO_06_003` → `GEO_07_002` (regra 1)

Núcleo: localizar a cozinha do Baixo de Mosqueiro no litoral/offshore **sergipano**, Bacia de Sergipe-Alagoas. Não é migração primária/secundária (`GEO_06_003`). Destino: `GEO_07_002` Bacias do Norte e Nordeste.

#### B2.3 `Prova-Matriz-Especialista-em-Petroleo-e-Gas-Engenharia-de-Instalacoes-Maritimas-11-12-2025__PASSADA_01__QQuestão 27` em `RESERV_04_001` → `RESERV_06_001` (regra 1)

Núcleo: obrigatoriedade e boas práticas de incluir estudos de injeção e recuperação avançada no PDP. Não é classificação de métodos (`RESERV_04_001`). Cabe em gerenciamento do reservatório / conteúdo do plano de desenvolvimento (`RESERV_06_001`).

### B3 — Baixas (7)

| ID | Núcleo | Atual | Proposto | Regra |
|---|---|---|---|---|
| `2011-2_PETROBRAS__PASSADA_01__Q64` | depleção = queda da pressão estática média, sem gás em solução | `RESERV_03_003` | `RESERV_03_004` | 1 |
| `OBJETIVA-15-MGR15-…__Q78` | CO₂ miscível **e** vapor cíclico **e** combustão in situ | `RESERV_04_005` | `RESERV_04_001` | 1 |
| `2024_FGV_ANALISTA DE PESQUISAS ENERGETICAS-petroleo-exploracao-e-producao__PASSADA_01__Q41` | WAG-CO₂ **e** polímero | `RESERV_04_004` | `RESERV_04_001` | 1 |
| `2022_FGV_Analista_de_pesquisa_energetica_petroleo-exploracao_e_producao_PROVA__PASSADA_01__Q62` | k e skin que **indicam acidificação matricial** | `POCO_03_004` | `POCO_03_002` | 1 |
| `OBJETIVA-11-PIP11-…__Q98` | auditorias internas e de 3ª parte do **SGSO** | `SEG_PRO_02_001` | `SEG_PRO_02_002` | 1; FRONT_049 |
| `2008_PETROBRAS_CESPE_2_PROVA__PASSADA_01__Q120` | craqueamento + reforma + alquilação | `REF_GAS_03_006` | `REF_GAS_03_004` | 1 |
| `2024_FGV_ANALISTA DE PESQUISAS ENERGETICAS-petroleo-exploracao-e-producao__PASSADA_01__Q65` | play, bacia efetiva e segmentação de chances | `GEO_01_002` | `GEO_01_003` | 1; FRONT_010 |

### B4 — Rejeitados na adjudicação (não são achados)

- AOF por teste de contrapressão em `RESERV_07_004` — a folha se chama “Injetividade e Contrapressão”; FRONT_017 não manda AOF para fora com a clareza de IPR/TPR.
- Q54/Q55 OBJETIVA em `REGUL_06_002` — premissas de excedente e SGPP (gestão de gastos da partilha) são o objeto da folha.
- PPSA 0% de equity em `REGUL_07_005` vs `REGUL_07_003` — vizinhos igualmente defensáveis.
- `…Gestao…__Q30` auditores das demonstrações — FRONT_045.
- Outorga de recursos hídricos para hidroeletricidade em `REGUL_04_003` — FRONT_051 (outorga / ANEEL).
- Play/POS com economicidade ainda em `GEO_01_003` — FRONT_010 deixa a chance geológica em GEO.
- Modelo 3D estático como insumo de simulação em `GEO_04_003` — FRONT_006 / regra 7.
- Parafina / pour point em `ELE_ESC_03_002` — FRONT_025.
- CRM em `REGUL_05_002` — FRONT_052 nomeia CRM.
- Nomenclatura de poço / poço explotatório em `REGUL_01_002` — definição ANP, não operação de poço.
- Ciclo de vida do campo + prazo da concessão em `REGUL_01_001` — fase legal, não FEL (`PET_FRONT_047` não se aplica).
- Jack-up **não** reaberto como seleção de unidade de produção: FRONT_023 é sonda.
- GEOF_02_001 vs `GEOF_02_003`: AVO/ângulo vs inversão determinística/estocástica — alocação coerente; o problema é o **nome** (seção E).

---

## C. Saídas

### Método

Os 12 registros com `disciplina` `I` ou `BASICAS` no mapeamento; cada `nucleo_cobrado` contra FRONT_001, 004, 016, 039, 044, 052 e as folhas do Núcleo Básico. Varredura inversa: núcleos **em árvore** que deveriam ter saído (regras 4 e 6).

### Números

12 oficiais: **8 I + 4 BASICAS**, todos corretos. Vazamento inverso adicional: **as 9 altas → I** (B1.1, B1.2, B1.3). Nenhum BASICAS extra.

### C1. Destino I (8) — corretos

| ID | Núcleo | FRONT |
|---|---|---|
| `2008_ESPECIALISTA EM REGULACAO DE PETROLEO E DERIVADOS_2-PROVA __PASSADA_01__Q38` | vedações a servidores de agências / parentesco | 004 |
| `…__Q39` | classe e padrão de carreira | 004 |
| `Prova-Matriz-…Gestao-de-Projetos-e-Contratos…__Q48` | COBIT e ISO 27001 | 004 |
| `prova_gab__PASSADA_01__Q36` | direitos dos usuários, Lei 8.987 | 004 |
| `…__Q37` | reversão, encampação, caducidade | 004 |
| `…__Q40` | arbitragem em concessão de serviço público | 004 |
| `…__Q44` | tarifa inicial, Lei 8.987 | 004 |
| `…__Q45` | intervenção na concessão | 004 |

Nenhum dos 8 deveria voltar para Petróleo.

### C2. Destino BASICAS (4) — corretos

| ID | Destino | Folha mais justa? |
|---|---|---|
| `2008_ESPECIALISTA EM REGULACAO DE PETROLEO E DERIVADOS_2-PROVA __PASSADA_01__Q48` azeótropo etanol-água | `TERMOD_03_001` Diagramas de Fases | `TERMOD_03_002` (Raoult / bolha-orvalho) também cabe; **não** invalida a saída (FRONT_016/039) |
| `2022_FGV_Analista_de_pesquisa_energetica_petroleo-exploracao_e_producao_PROVA__PASSADA_01__QQuestão Discursiva 1` retrofit de lâmpadas | `ENG_ECO_01` (nível de assunto) | `ENG_ECO_01_006` VPL existiria; o mapeamento parou no assunto. Saída em si ok (FRONT_044) |
| `prova_gab__PASSADA_01__Q46` turbina / US / PD | `MEC_FLU_07_001` | ok (FRONT_052) |
| `prova_gab__PASSADA_01__Q65` placa de orifício | `MEC_FLU_07_002` | ok (FRONT_052) |

### C3. Vazamento inverso

Além das 8+4 oficiais, B1.1 (5), B1.2 (3) e B1.3 (1) são petróleo-mapeado que deveriam ser **I**.

---

## D. Fronteiras e regras 4–8

### Método

Para cada `PET_FRONT_001`–`052`, busca no join de instâncias em que o núcleo é o objeto X da regra e o mapeamento caiu no lado B. Pares de folhas em disciplinas distintas com conteúdo sobreposto e **sem** FRONT. FRONT cujo lado petróleo aponta a folha vazia (antecipação).

### D1. FRONT contraditas (instanciação = as 16 altas)

| FRONT / regra | Instância |
|---|---|
| 004 + r6 | 5× teoria do Estado regulador; 3× certame genérico |
| 004 + r4/r6 | IDW/Spline GIS |
| 006 + r7 | 2× fluxo/alocação em fratura em GEO |
| 010 | avaliação econômico-financeira em GEO |
| 023 | jack-up em INS_MAR |
| 042 | distribuidor atacadista em REGUL |
| 002 + r5 | classe técnica de GLP em REGUL |
| 025 | ILI de corrosão/mossas em ELE_ESC |

### D2. Par sem FRONT que o corpus instancia

**Único agora evidenciado:** caracterização **estática** de reservatório fraturado (`GEO_04_004`) versus **fluxo / alocação injetor-produtor** em meio fraturado (`RESERV_06_001`). Sem frase explícita além de FRONT_006 genérica, as duas questões caíram no nó geológico.

Proposta (uma frase por lado): **GEO** — geometria, condutividade **geológica** e selo vs condutivo da rede de fraturas no modelo estático. **RESERV** — escoamento matriz-fratura, alocação e otimização de injetores/produtores.

Água de injeção (utilidade `INS_MAR_03_003` vs waterflood `RESERV_04_003`) e física de rochas (`GEOF_06_002`) vs PETROF **não** produziram contradição no corpus — não são FRONT mortas a inventar por antecipação.

### D3. FRONT antecipatória

Nenhuma das 52 aponta para folha vazia no lado petróleo. Nada a apagar.

### D4. Regras 4–8 (estrutura)

- **4:** 8 I oficiais + 9 altas→I; o restante STEM no corpus tem âncora petrolífera.
- **5:** a alta GLP é o único desvio encontrado.
- **6:** GIS IDW + as 8 teorias/certames genéricos; sísmica/perfilagem/SIG com âncora E&P permanece.
- **7:** **não reaberta.** PVT, φ/k, geoquímica orgânica, waterline, CO₂-processo vs EOR, flow assurance: estrutura ok. A tensão nova é o par fraturado (D2), fronteira **faltante**, não revisão da 7.
- **8:** após as altas, `REGUL_04_002` e `GEO_04_004` ficam vazios → apagar. Nenhuma outra folha vazia hoje.

---

## E. Nomes

### Método

Varredura de comprimento > 38, dois-pontos, parênteses e enumeração, contra as três exceções documentadas. Para cada subassunto, confronto nome × núcleos da folha e colisão com irmãs.

### Números

Acima de 38 fora das exceções: **0**. Exceções usadas: `INS_MAR_02_002` (42), `SUST_02` (39). Dois-pontos: só `POCO_02_002 Kick: Causas e Detecção` (exceção). Parênteses: 0. Vírgula/enumeração fora da exceção de plataformas: 5 folhas (`COMERC_03_001`, `GEO_03_001`, `INS_SUB_01_002`, `INS_SUB_03_001`, `PETROF_03_001`) — regra 2, **não bloqueiam** (siglas correntes).

### Bloqueadores (gênero no nome + espécie nas irmãs)

1. **`GEOF_02_003` “Inversão Sísmica”** — as 7 questões são inversão **determinística/estocástica** e impedância. A irmã `GEOF_02_001` já é “Análise AVO e Inversão Elástica”. O nome gênero cobre a irmã. Alocação internamente coerente (não fundir). Renomear para o residual (p.ex. inversão determinística e estocástica), sem “inversão” absoluto.
2. **`RESERV_03_004` “Mecanismos Primários de Produção”** — as irmãs já são gás em solução / influxo. O corpus desta folha é comparação / elenco de mecanismos. O nome guarda-chuva cobre `RESERV_03_003`. Renomear para o residual comparativo.
3. **`POCO_03_004` “Métodos de Estimulação”** — gênero; irmãs acidificação e fratura. Uma questão é definição de gênero (identidade própria, regra 3); a outra é indicação de acidificação (B3). Ou a folha vira residual explícito, ou a mista sobe ao assunto.

Não bloqueadores: `REGUL` vs `SUST` em licenciamento — FRONT_003. `INS_MAR_03_003` vs `RESERV_04_003` — FRONT_022/031. `COMERC_03_001` vs `PRJ_02_001` — FRONT_043.

---

## F. Estrutura

### Método

Contagem por folha; 1-q e 2-q lidos um a um quanto a identidade vs vizinho. Densidade contra a casa (Produção, só estilo). SUST (16) e QUI_PET (18) como as menores disciplinas.

### Números

| | N |
|---|---|
| Folhas com 1 questão | **1** (`SUST_02_001` Mandatos de Biocombustíveis — exceção documentada) |
| Folhas com 2 questões | **51** (identidade própria nos núcleos; não fundir por contagem) |
| SUST / QUI_PET | 16 / 18 — estrutura interna se sustenta |
| Após B1, folhas que esvaziam | `REGUL_04_002`, `GEO_04_004` |

`SUST_02_001` permanece a exceção da regra 3. Assuntos de SUST (efluentes/emissões, matriz, licenciamento/PEI) e QUI_PET (classificação/API, heteroátomos, séries, gás, inibidores) não são 1 questão disfarçada de disciplina.

`ENG_ECO_01` no Núcleo tem subassuntos; a discursiva de iluminação caiu no **assunto**. Defeito de precisão do destino BASICAS, não da árvore de Petróleo.

---

## Tabela consolidada de contestações de alocação

Ordenada por severidade, depois disciplina atual, depois `id_global`.

| id_global | atual | proposto | regra | sev |
|---|---|---|---|---|
| `Prova-Matriz-Especialista-em-Petroleo-e-Gas-Geologia-de-Exploracao-11-12-2025__PASSADA_01__Q36` | `GEO_04_004` | `RESERV_06_001` | FRONT_006; r7 | alta |
| `Prova-Matriz-Especialista-em-Petroleo-e-Gas-Geologia-de-Reservatorios-11-12-2025__PASSADA_01__Q41` | `GEO_04_004` | `RESERV_06_001` | FRONT_006; r7 | alta |
| `2010-epe-analista-de-pesquisa-energetica-petroleo-exploracao-prova__PASSADA_01__Q24` | `GEO_04_002` | `I` | r4; r6 | alta |
| `2010-epe-analista-de-pesquisa-energetica-petroleo-exploracao-prova__PASSADA_01__Q40` | `GEO_01_003` | `COMERC_03_003` | FRONT_010 | alta |
| `2005_ESPECIALISTA EM REGULACAO DE PETROLEO_1-PROVA__PASSADA_01__Q40` | `INS_MAR_02_002` | `POCO_07_002` | FRONT_023 | alta |
| `2008_ESPECIALISTA EM REGULACAO DE PETROLEO E DERIVADOS_1-PROVA __PASSADA_01__Q56` | `ELE_ESC_03_003` | `INS_SUB_05_002` | FRONT_025 | alta |
| `prova_gab__PASSADA_01__Q38` | `REGUL_04_002` | `I` | FRONT_004; r6 | alta |
| `prova_gab__PASSADA_01__Q39` | `REGUL_04_002` | `I` | FRONT_004; r6 | alta |
| `prova_gab__PASSADA_01__Q41` | `REGUL_04_002` | `I` | FRONT_004; r6 | alta |
| `prova_gab__PASSADA_01__Q42` | `REGUL_04_002` | `I` | FRONT_004; r6 | alta |
| `prova_gab__PASSADA_01__Q43` | `REGUL_04_002` | `I` | FRONT_004; r6 | alta |
| `Prova-Matriz-Especialista-em-Petroleo-e-Gas-Gestao-de-Projetos-e-Contratos-em-Oleo-e-Gas-11-12-2025__PASSADA_01__Q41` | `REGUL_04_005` | `I` | FRONT_004; r6 | alta |
| `Prova-Matriz-Especialista-em-Petroleo-e-Gas-Gestao-de-Projetos-e-Contratos-em-Oleo-e-Gas-11-12-2025__PASSADA_01__Q43` | `REGUL_04_005` | `I` | FRONT_004; r6 | alta |
| `Prova-Matriz-Especialista-em-Petroleo-e-Gas-Gestao-de-Projetos-e-Contratos-em-Oleo-e-Gas-11-12-2025__PASSADA_01__Q51` | `REGUL_04_005` | `I` | FRONT_004; r6 | alta |
| `2005_ESPECIALISTA EM REGULACAO DE PETROLEO_2-PROVA__PASSADA_01__Q41` | `REGUL_02_002` | `COMERC_03_002` | FRONT_042 | alta |
| `2008_ESPECIALISTA EM REGULACAO DE PETROLEO E DERIVADOS_2-PROVA __PASSADA_01__Q58` | `REGUL_02_002` | `SEG_PRO_01_003` | FRONT_002; r5 | alta |
| `2006-epe-tecnico-de-nivel-superior-petroleo-exploracao-e-producao-prova__PASSADA_01__Q42` | `GEO_06_003` | `GEO_07_002` | r1 | média |
| `OBJETIVA-09-GMO09-Gerenciamento-e-Monitoramento-das-Operacoes-com-Pocos__PASSADA_01__Q58` | `REGUL_06_001` | `REGUL_07_005` | r1 | média |
| `OBJETIVA-10-OSS10-Operacao-de-Sistemas-Submarinos-de-Producao__PASSADA_01__Q58` | `REGUL_06_001` | `REGUL_07_005` | r1 | média |
| `OBJETIVA-11-PIP11-Processo-de-Individualizacao-de-Producao__PASSADA_01__Q58` | `REGUL_06_001` | `REGUL_07_005` | r1 | média |
| `OBJETIVA-12-IDG12-Interpretacao-de-Dados-Geofisicos__PASSADA_01__Q58` | `REGUL_06_001` | `REGUL_07_005` | r1 | média |
| `OBJETIVA-13-OGP13-Operacao-Geologica-em-Pocos-Exploratorios__PASSADA_01__Q58` | `REGUL_06_001` | `REGUL_07_005` | r1 | média |
| `OBJETIVA-14-CMR14-Caracterizacao-e-Modelagem-de-Reservatorios__PASSADA_01__Q58` | `REGUL_06_001` | `REGUL_07_005` | r1 | média |
| `OBJETIVA-15-MGR15-Modelagem-e-Gerenciamento-de-Reservatorios__PASSADA_01__Q58` | `REGUL_06_001` | `REGUL_07_005` | r1 | média |
| `Prova-Matriz-Especialista-em-Petroleo-e-Gas-Engenharia-de-Instalacoes-Maritimas-11-12-2025__PASSADA_01__QQuestão 27` | `RESERV_04_001` | `RESERV_06_001` | r1 | média |
| `2024_FGV_ANALISTA DE PESQUISAS ENERGETICAS-petroleo-exploracao-e-producao__PASSADA_01__Q65` | `GEO_01_002` | `GEO_01_003` | r1; FRONT_010 | baixa |
| `2022_FGV_Analista_de_pesquisa_energetica_petroleo-exploracao_e_producao_PROVA__PASSADA_01__Q62` | `POCO_03_004` | `POCO_03_002` | r1 | baixa |
| `2008_PETROBRAS_CESPE_2_PROVA__PASSADA_01__Q120` | `REF_GAS_03_006` | `REF_GAS_03_004` | r1 | baixa |
| `2011-2_PETROBRAS__PASSADA_01__Q64` | `RESERV_03_003` | `RESERV_03_004` | r1 | baixa |
| `2024_FGV_ANALISTA DE PESQUISAS ENERGETICAS-petroleo-exploracao-e-producao__PASSADA_01__Q41` | `RESERV_04_004` | `RESERV_04_001` | r1 | baixa |
| `OBJETIVA-15-MGR15-Modelagem-e-Gerenciamento-de-Reservatorios__PASSADA_01__Q78` | `RESERV_04_005` | `RESERV_04_001` | r1 | baixa |
| `OBJETIVA-11-PIP11-Processo-de-Individualizacao-de-Producao__PASSADA_01__Q98` | `SEG_PRO_02_001` | `SEG_PRO_02_002` | r1; FRONT_049 | baixa |

---

## Lista de bloqueios (o que precisa mudar antes de congelar)

1. **Mover ou sair as 16 altas** (9 para `I`; 2 GEO→`RESERV_06_001`; 1 GEO→`COMERC_03_003`; 1 INS_MAR→`POCO_07_002`; 1 REGUL→`COMERC_03_002`; 1 REGUL→`SEG_PRO_01_003`; 1 ELE_ESC→`INS_SUB_05_002`).
2. **Apagar** as folhas que esvaziam (`REGUL_04_002`, `GEO_04_004`) — regra 8.
3. **Acrescentar FRONT** do par fraturado estático vs fluxo, e **renomear** E1–E3 (`GEOF_02_003`, `RESERV_03_004`, `POCO_03_004`).
4. **Corrigir** (ou aceitar documentadamente) os sete dumps OBJETIVA `Q58` em `REGUL_06_001`.
5. **Alinhamento alfabético A3:** remapear IDs à ordem folding da Produção **ou** documentar Unicode/sigla na Parte II.

Itens B2/B3 restantes, sozinhos, não bloqueiam se 1–3 e 5 forem feitos.

Nada além disto bloqueia. A árvore é mecanicamente íntegra; a regra 7 está aplicada na estrutura; SUST e QUI_PET se sustentam; as 12 saídas oficiais estão certas.

---

*Auditoria independente. Árvore, mapeamento, ENTRADA e Núcleo Básico não foram alterados. Corpus: 1.354 linhas, 1.342 em árvore, 12 saídas oficiais.*
