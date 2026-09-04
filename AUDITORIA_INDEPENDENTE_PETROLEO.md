# AUDITORIA INDEPENDENTE — ÁRVORE MESTRA DE ENGENHARIA DE PETRÓLEO

**Auditor:** independente (não autor da árvore).  
**Data:** 2026-09-04.  
**Objetos auditados:** `PETROLEO.md` (Parte I + 52 `PET_FRONT`) e `MAPEAMENTO_PETROLEO.json` (1.354 registros).  
**Referências carregadas:** `NUCLEO_BASICO.md` (PR #2, `arvores/NUCLEO_BASICO_CORRIGIDO_ETAPA2.md`) e `ENGENHARIA_PRODUCAO.md` (PR #3, só estilo/convenção da Parte II).  
**Não carregado:** `00_ENTRADA_ESPECIFICAS.jsonl` — o arquivo não estava no pacote da auditoria (anexos efetivos: árvore + mapeamento). Sem `nucleo_cobrado` a seção B não é certificável.

**O que este relatório não faz:** não reconstrói a árvore, não reclassifica o corpus, não reabre as decisões da regra 7, não julga pelo nome da prova nem pelo rótulo preliminar.

---

## Resumo executivo

**Veredito: NÃO CONGELÁVEL.**

Não se congela uma árvore de classificação cuja alocação (a parte que importa) não pôde ser lida contra o `nucleo_cobrado`. O mapeamento é mecanicamente coerente com a Parte I, as 12 saídas batem com os exemplos da Parte II, e as decisões de escopo da regra 7 estão *estruturalmente* aplicadas. Isso não substitui B.

Achados por severidade (só o que viola regra citada, com evidência):

| Severidade | N | O que conta |
|---|---|---|
| Alta (disciplina errada) | 0 | Nenhuma contestação de alocação certificável |
| Média (assunto/subassunto guarda-chuva ou colisão de nome) | 3 | `GEOF_02_003`, `RESERV_03_004`, `POCO_03_004` |
| Baixa (mecânica / granularidade / fronteira faltante) | 15 | 11 grupos fora da ordem alfabética da casa; 1 destino BASICAS em nível de assunto; 3 pares sem `PET_FRONT` |

Três achados mais importantes:

1. **B não executado.** `00_ENTRADA_ESPECIFICAS.jsonl` ausente. Contestações válidas de alocação = 0, não porque a alocação esteja aprovada, mas porque a regra do auditor (“só o `nucleo_cobrado` é evidência”) não tem o que ler. Congelar agora seria assinar um corpus não visto.
2. **Três subassuntos guarda-chuva na mesma família do vizinho** (regra 1 e regra 2): `GEOF_02_003` Inversão Sísmica colide com `GEOF_02_001` Análise AVO e Inversão Elástica; `RESERV_03_004` Mecanismos Primários de Produção cobre o irmão `RESERV_03_003` Mecanismo de Gás em Solução; `POCO_03_004` Métodos de Estimulação cobre Acidificação e Fraturamento.
3. **Ordem alfabética** (checagem A): 2 assuntos e 9 grupos de subassuntos ordenados por *codepoint Unicode* (Á/Í no fim, “CAPEX” antes de “Cadeia”). A árvore congelada de Produção usa folding de acentos e case-insensitive e está 0/0. Ou se reordena com de-para de IDs, ou se documenta a chave Unicode na Parte II.

**O que já está sólido:** 16 / 77 / 262 como anunciado; 1.354 IDs únicos no mapeamento; 1.342 destinos existem na árvore; 4 destinos BASICAS existem no Núcleo Básico; 0 lacuna de numeração; 0 nome repetido; `PET_FRONT_001`–`052` contínuos; siglas da Parte II resolvem nas duas árvores; 0 subassunto vazio (regra 8); regra 7 visível na estrutura; SUST (16) e QUI_PET (18) se sustentam; as 8 saídas `I` repetem os três exemplos de `PET_FRONT_004`.

---

## A. Integridade mecânica

### Método

Parser da Parte I de `PETROLEO.md` (corte em `# PARTE II`) e da Parte I de `NUCLEO_BASICO.md`. Cruzamento campo a campo com os 1.354 registros de `MAPEAMENTO_PETROLEO.json`. Ordem alfabética = folding NFD + `casefold` (a mesma chave que deixa Produção com 0 violações). Siglas da Parte II = todos os tokens `` `SIGLA` ``, excluídos os rótulos auxiliares `BASICAS`, `TECNICA`, `NORMAS`, `I`.

`00_ENTRADA_ESPECIFICAS.jsonl` não estava no pacote: a bijeção ENTRADA ↔ MAPEAMENTO **não** foi conferida. Conferiu-se só a consistência interna do mapeamento.

### Números

| Checagem | Resultado |
|---|---|
| Disciplinas / assuntos / subassuntos na Parte I | **16 / 77 / 262** (bate com o anunciado) |
| Registros no mapeamento | **1.354** (`meta.quantidade` = 1.354) |
| `id_global` únicos | **1.354** (0 duplicata) |
| Bijeção com ENTRADA | **não conferida** (arquivo ausente) |
| Dentro da árvore / BASICAS / I | **1.342 / 4 / 8** |
| Destinos in-tree inexistentes na Parte I | **0** |
| Destinos BASICAS inexistentes no Núcleo Básico | **0** |
| Nome de assunto/subassunto no mapeamento ≠ árvore | **0** |
| Filho cujo ID não prefixa o pai | **0** |
| Lacunas de numeração em assunto ou subassunto | **0** |
| Nome de assunto ou subassunto repetido (exato ou folded) | **0** |
| Ordem alfabética (folding) — assuntos | **2** disciplinas |
| Ordem alfabética (folding) — subassuntos | **9** pais |
| `PET_FRONT_001` … `052` contínuos, sem duplicata | **sim** (52/52) |
| Sigla da Parte II sem destino nas duas árvores | **0** (`MEC_FLU_07` existe como assunto) |

Disciplinas, pela sigla: COMERC, ELE_ESC, GEO, GEOF, INS_MAR, INS_SUB, PETROF, POCO, PRJ, PROC_PRI, QUI_PET, REF_GAS, REGUL, RESERV, SEG_PRO, SUST.

### Achados

**A1. Bijeção com ENTRADA não conferida.**  
Evidência: o pacote da auditoria continha `PETROLEO.md` e `MAPEAMENTO_PETROLEO.json`. Sem o JSONL, não há como afirmar que todo `id_global` da ENTRADA aparece exatamente uma vez. O mapeamento, *por si*, tem 1.354 IDs únicos e nenhum órfão interno.

**A2. Ordem alfabética fora da convenção da casa (regra A / estilo PRODUCAO).**  
Produção: 0 assuntos e 0 subassuntos fora do folding. Petróleo usou ordenação Unicode (`Á` depois de Z; `A` maiúsculo antes de `a`).

Assuntos:

| Pai | Ordem atual | Ordem folding |
|---|---|---|
| `GEO` | … Geologia **Estrutural**, Geologia **de Reservatórios** … | Geologia **de Reservatórios**, Geologia **Estrutural** |
| `PROC_PRI` | … Tratamento de **Gás** Natural, Tratamento de **Água** Produzida … | Tratamento de **Água** Produzida, Tratamento de **Gás** Natural |

Subassuntos:

| Pai | Sintoma |
|---|---|
| `COMERC_03` | `CAPEX, OPEX e Lifting Cost` antes de `Cadeia de Valor e Logística` |
| `ELE_ESC_04` | `Sistema Integrado de Produção` antes de `Índice de Produtividade` |
| `GEO_07` | `Bacias Interiores Paleozoicas` antes de `Bacias do Norte e Nordeste` |
| `INS_MAR_03` | `Água de Injeção` por último |
| `INS_SUB_01` | `Árvore de Natal Molhada` por último |
| `INS_SUB_04` | `Instalação de Manifolds` antes de `Instalação de Árvore de Natal Molhada` |
| `RESERV_04` | `Injeção de Gás e WAG` antes de `Injeção de Água` |
| `RESERV_05` | `Classificação de Reservas e Recursos` antes de `Cálculo Volumétrico` |
| `SEG_PRO_01` | `Áreas Classificadas e Contenção` por último |

Não é preferência estética: a checagem A pede ordem alfabética dentro do pai, e a árvore de referência a cumpre com folding.

**A3. Destino BASICAS em nível de assunto, não de subassunto.**  
`2022_FGV_Analista_de_pesquisa_energetica_petroleo-exploracao_e_producao_PROVA__PASSADA_01__QQuestão Discursiva 1` → `ENG_ECO_01` (assunto “Análise de Investimentos”). Os outros três BASICAS apontam subassunto (`TERMOD_03_001`, `MEC_FLU_07_001`, `MEC_FLU_07_002`). `ENG_ECO_01` *existe* no Núcleo Básico; a checagem “destino existe” passa. A Parte II exige id canônico, não exige folha. Inconsistência de granularidade, não id órfão.

---

## B. Alocação de questões

### Método

O protocolo pedia: para cada uma das 1.342 questões in-tree, ler o `nucleo_cobrado` e testar o subassunto contra as regras 1, 4, 5 e 7. Sem amostra.

**Arquivo `00_ENTRADA_ESPECIFICAS.jsonl` não foi fornecido.** O mapeamento não carrega `nucleo_cobrado` (chaves: `id_global`, `disciplina`, `assunto`, `subassunto`, `nome_assunto`, `nome_subassunto`). Julgar pelo `id_global` (nome da prova) ou pelo rótulo preliminar é proibido. “Eu teria colocado em outro lugar” não é achado.

### Números

| Métrica | Valor |
|---|---|
| Questões in-tree | 1.342 |
| `nucleo_cobrado` lidos | **0** |
| Contestações válidas (alta / média / baixa) | **0 / 0 / 0** |
| Contestações por disciplina | — |

### Achados

**B1. Seção B não certificada.**  
Não há contestação válida porque não há evidência lícita. Isso **não** é aprovação da alocação. Qualquer lista de “erros prováveis” a partir do nome da prova ou do nome do nó seria violação da regra do auditor e foi omitida.

A tabela consolidada de contestações ao final está vazia de propósito.

---

## C. Saídas (12 fora da árvore) e vazamentos

### Método

As 12 saídas trazem, em `nome_subassunto`, um rótulo de conteúdo escrito pelo mapeador. Isso **não** é `nucleo_cobrado`; é a melhor evidência disponível *sobre as saídas*. Confrontou-se esse rótulo com `PET_FRONT_001`, `004`, `016`, `039`, `044`, `052` e com os IDs do Núcleo Básico. Para vazamento inverso (in-tree que deveria ter saído), sem `nucleo_cobrado` não há contestação válida — só inspeção estrutural da regra 7.

### Números

| Classe | N | Destinos |
|---|---|---|
| `I` | 8 | rótulo `I` |
| `BASICAS` | 4 | `TERMOD_03_001`, `ENG_ECO_01`, `MEC_FLU_07_001`, `MEC_FLU_07_002` |
| Saídas cujo rótulo contradiz `PET_FRONT_004` / `001` | **0** |
| Questões in-tree contestadas para BASICAS ou I | **0** (B não executado) |

### As 8 saídas I — corretas pelo rótulo

Todas repetem os três exemplos canônicos de `PET_FRONT_004`. Não se forçou destino aproximado (regra 6).

| id_global | rótulo no mapeamento | Regra |
|---|---|---|
| `2008_ESPECIALISTA EM REGULACAO DE PETROLEO E DERIVADOS_2-PROVA __PASSADA_01__Q38` | regime de servidores de agências | `PET_FRONT_004` |
| `2008_ESPECIALISTA EM REGULACAO DE PETROLEO E DERIVADOS_2-PROVA __PASSADA_01__Q39` | regime de servidores de agências | `PET_FRONT_004` |
| `Prova-Matriz-Especialista-em-Petroleo-e-Gas-Gestao-de-Projetos-e-Contratos-em-Oleo-e-Gas-11-12-2025__PASSADA_01__Q48` | governança de TI | `PET_FRONT_004` |
| `prova_gab__PASSADA_01__Q36` | Lei de Concessões de serviços públicos (8.987) | `PET_FRONT_004` |
| `prova_gab__PASSADA_01__Q37` | idem | `PET_FRONT_004` |
| `prova_gab__PASSADA_01__Q40` | idem | `PET_FRONT_004` |
| `prova_gab__PASSADA_01__Q44` | idem | `PET_FRONT_004` |
| `prova_gab__PASSADA_01__Q45` | idem | `PET_FRONT_004` |

Nenhuma das oito deveria entrar na árvore de Petróleo com o rótulo que o mapeamento declara.

### As 4 saídas BASICAS — saída correta; um destino interno discutível

| id_global | Destino | Rótulo | Saída para Básicas? | Nota |
|---|---|---|---|---|
| `2008_…_Q48` | `TERMOD_03_001` Diagramas de Fases | equilíbrio de fases: azeótropo etanol-água | **Sim** (`PET_FRONT_016` / `039`: azeótropo sem contexto de refino/reservatório → `TERMOD`) | Dentro das Básicas, `TERMOD_03_002` Lei de Raoult e Pontos de Bolha e Orvalho é o vizinho mais específico do azeótropo. Observação de folha, não de árvore de Petróleo. |
| `2022_FGV_…_QQuestão Discursiva 1` | `ENG_ECO_01` | Análise de Investimentos | **Sim** (`PET_FRONT_044`: VPL/TIR sem risco geológico → `ENG_ECO`) | Destino = assunto, não folha (A3). |
| `prova_gab__PASSADA_01__Q46` | `MEC_FLU_07_001` | Outros Medidores de Vazão | **Sim, se o objeto é o princípio físico** (`PET_FRONT_052`) | Se o `nucleo_cobrado` (não lido) for RTM/ponto fiscal, o destino seria `REGUL_05`. Sem `nucleo_cobrado`, não se contesta. |
| `prova_gab__PASSADA_01__Q65` | `MEC_FLU_07_002` | Placa de Orifício | idem | idem |

### Vazamento inverso (in-tree → Básicas ou I)

**Nenhuma contestação válida.** Inspeção estrutural (não é achado de alocação): a árvore *reserva* nós para fenômenos que as Básicas também têm, exatamente como `PET_FRONT_001` manda — `RESERV_02_003` Lei de Darcy (9 questões), `GEOF_03_001` Cinemática da Reflexão (6), `POCO_04_003` Janela Operacional e Geopressões (7), `RESERV_05_001` Análise de Incertezas (contexto de reservas). Isso é aplicação da regra 4/7, não vazamento.

---

## D. Fronteiras

### Método

1. Contradição instanciada: regra diz X→A e o mapeamento põe questão X em B. Exige `nucleo_cobrado`. Não executado no nível da questão.
2. Contradição estrutural: a *árvore* põe o tema da regra 7 no lado errado. Executado por inspeção dos IDs.
3. Pares de subassuntos em disciplinas diferentes com sobreposição de nome/objeto e sem `PET_FRONT` cobrindo o par. Executado.
4. `PET_FRONT` sem nó de Petróleo com questão. Executado (contagem por ID citado).

### Números

| Checagem | Resultado |
|---|---|
| Contradições instanciadas (questão × texto da regra) | **não executado** (sem `nucleo_cobrado`) |
| Decisões da regra 7 aplicadas na estrutura | **6/6** |
| `PET_FRONT` cujo lado de Petróleo tem 0 questões | **0 / 52** |
| Pares sobrepostos sem regra na Parte II | **3** (propostos abaixo) |

### D1. Regra 7 — aplicação estrutural (não reabrir; auditar se foi aplicada)

| Decisão | Onde caiu na árvore | Status |
|---|---|---|
| Geoquímica orgânica em Geologia, não em Química do Petróleo | `GEO_06` Sistema Petrolífero e Geoquímica (`GEO_06_002` Geoquímica e Biomarcadores, 7 q.; `GEO_06_004` Origem e Maturação, 10 q.). QUI_PET não tem querogênio/COT/Rock-Eval | Aplicada |
| PVT e fases em Reservatórios | `RESERV_01` Comportamento de Fases e PVT (10 q.) | Aplicada |
| Propriedade da rocha em Petrofísica; rocha-fluido em Reservatórios | `PETROF_04` Porosidade (9) + Permeabilidade Absoluta (3); `RESERV_02` Molhabilidade e Pressão Capilar (8) + Permeabilidade Efetiva e Relativa (5) | Aplicada |
| Modelo estático em Geologia; dinâmico em Reservatórios | `GEO_04_002` Geoestatística (8), `GEO_04_003` Modelagem Geológica 3D (9); `RESERV_06_003` Simulação e Ajuste de Histórico (2) | Aplicada |
| CO₂/CCUS/descarbonização como processo na disciplina técnica, nunca em SUST | `PROC_PRI_01_003` Reinjeção de Gás e CO₂ (4), `PROC_PRI_03_004` Remoção de CO₂ por Membranas (2), `RESERV_04_002` Injeção de Gás e WAG (4), `INS_SUB_02_001` Separação e Bombeio Submarino (4). SUST não tem nó de CCUS | Aplicada |
| Garantia de Escoamento como assunto de Elevação e Escoamento | `ELE_ESC_03` (10 q.: hidratos, parafinas, pigging) | Aplicada |
| Linha d'água: INS_SUB abaixo, INS_MAR acima | Assuntos INS_SUB = equipamentos/risers/instalação/integridade; INS_MAR = casco/unidades/utilidades/offloading. Risers ficam em INS_SUB (`INS_SUB_03_002`, `PET_FRONT_029`) | Aplicada |

### D2. Contradições instanciadas

Nenhuma listável. Sem `nucleo_cobrado` não se demonstra “a regra manda A e a questão X foi para B”.

### D3. Pares sobrepostos sem `PET_FRONT`

Cada par tem questões nos dois lados (contagens abaixo). A Parte II não despacha o par.

**Par 1 — `INS_MAR_03_003` Água de Injeção (2) × `RESERV_04_003` Injeção de Água (6).**  
`PET_FRONT_031` despacha água de injeção como *utilidade da unidade* versus tratamento de água *produzida* em `PROC_PRI`, não versus waterflood em Reservatórios.

- `INS_MAR`: qualidade e condicionamento da água de injeção como utilidade (dessulfatação, filtração, biocida).
- `RESERV`: injeção de água como método de recuperação (arranjos, varrido, preenchimento).

**Par 2 — `GEOF_06_002` Física de Rochas (2) × `PETROF_04` / `PETROF_01` (propriedade da rocha e saturação).**  
`PET_FRONT_011` despacha sônico de poço versus well-tie, não Gassmann/substituição de fluidos versus petrofísica de laboratório.

- `GEOF`: velocidades, impedância e substituição de fluidos para sísmica (AVO/4D).
- `PETROF`: porosidade, saturação e k medidas no poço ou no testemunho.

**Par 3 — `GEO_04_004` Reservatórios Fraturados (2) × `RESERV_02` Escoamento em Meios Porosos.**  
Não há `PET_FRONT` para fratura como objeto geológico versus como meio de fluxo.

- `GEO`: caracterização da rede de fraturas no modelo estático.
- `RESERV`: escoamento em meio fraturado (dupla porosidade, permeabilidade de fratura).

Outros pares com nome parecido **já** têm regra: `PETROF_05` Testes de Formação × `RESERV_07_005` (`PET_FRONT_014`); `COMERC_02_003` × `REGUL_02_003` (`PET_FRONT_042`); `QUI_PET_02` × `RESERV_01` (`PET_FRONT_016`); `POCO_03_001` Abandono × norma (`PET_FRONT_002`); `PROC_PRI_04` × `SUST_01` (`PET_FRONT_003`).

### D4. Regras escritas por antecipação

Nenhum `PET_FRONT` aponta um lado de Petróleo com zero questões. Os nós que as regras citam têm carga, por exemplo: BCS 4 (`PET_FRONT_028`), fadiga de riser 6 (`034`), SGSS 5 (`033`), RTM 11 (`052`), POS 11 (`010`), PEI 2 (`048`), mandatos 1 (`040`), HISEP/separação submarina 4 (`030`/`050`), 4D 10 (`012`).

Não se prova antecipação. Algumas regras (`013` Snell, `024` Stevin, `028` afinidade, `034` S-N, `039` azeótropo) são higiene de classificador contra as Básicas; o lado de Petróleo existe no corpus.

---

## E. Nomes

### Método

Varredura de todos os 77 assuntos e 262 subassuntos: comprimento, `:`, `()`, enumeração tipo “a, b, c, d”. Exceções documentadas aplicadas. Colisão = nome que descreve o irmão ou o pai. Correspondência nome × questões: só é certificável com `nucleo_cobrado`; aqui restringe-se a colisão *onômica* (o nome, sozinho, não individualiza o conhecimento).

### Números

| Checagem | Resultado |
|---|---|
| Subassuntos > 38 caracteres fora das exceções | **0** |
| `Plataformas Fixas, Semissubmersíveis e TLP` | 42 — exceção documentada |
| `Energias Renováveis e Matriz Energética` | 39 — exceção documentada (assunto `SUST_02`) |
| Dois-pontos fora de `Kick: Causas e Detecção` | **0** |
| Parênteses explicativos | **0** |
| Subassuntos exatamente no teto (38) | 2: `GEOF_04_003` Indicadores Diretos de Hidrocarbonetos; `POCO_01_001` Arquitetura e Sequência de Completação |
| Colisões de nome / guarda-chuva (regra 1 e 2) | **3** |

Siglas nos nomes (`PVT`, `WAG`, `TLD`, `PPSA`, `FEL`, `ESD`, `FID`, `GNL`, `FPSO`, `AVO`, `LWD`, `MWD`, `BOP`, `ECD`, `HAZOP`, `SGSO`, `SGSS`, `ANP`, `UPGN`, `API`, `PLET`, `PLEM`, `ROV`, `SP`, `TLP`, `EAP`, `CO₂`) são nome corrente de área. A lista entre parênteses na regra 2 é exemplificativa, não numerus clausus. Não se pede rename por gosto.

### Achados

**E1. `GEOF_02_003` Inversão Sísmica (7 q.) colide com `GEOF_02_001` Análise AVO e Inversão Elástica (7 q.).**  
Regra 2: o nome não diz o conceito que o irmão já não cubra. “Inversão Sísmica” é o gênero; o irmão já nomeia uma espécie (inversão elástica). Rename só se o conteúdo for outra inversão (p.ex. acústica / impedância). Sem `nucleo_cobrado` não se move questão; o *nome* já viola a regra 2.

**E2. `RESERV_03_004` Mecanismos Primários de Produção (9 q.) é guarda-chuva do irmão `RESERV_03_003` Mecanismo de Gás em Solução (4 q.).**  
Regra 1: um subassunto por conhecimento determinante. Gás em solução *é* mecanismo primário. O nome do _004 não omite o que o assunto já diz (`RESERV_03` já se chama Mecanismos e Balanço de Materiais); ele reengloba o irmão. Se as 9 questões forem os *outros* mecanismos (água, capa, compactação), o nome está errado (regra 2). Se forem a classificação geral, funde-se com o assunto ou com o _003.

**E3. `POCO_03_004` Métodos de Estimulação (2 q.) é guarda-chuva dos irmãos `POCO_03_002` Acidificação Matricial (2) e `POCO_03_003` Fraturamento Hidráulico (2).**  
Mesma regra 1. Identidade própria só se as 2 questões forem seleção/classificação de métodos (análogo a `ELE_ESC_01_005` Seleção de Métodos de Elevação, que convive com BCS/gas lift porque o conhecimento determinante é a *seleção*). O nome atual não diz “seleção”; diz o gênero. Rename para o conceito real ou fusão, depois de ler o `nucleo_cobrado`.

Não são achados (não violaram regra 2 / não são rename por gosto): `CAPEX, OPEX e Lifting Cost`; `Manifolds, PLET e PLEM`; `Falhas, Dobras e Tensões`; `Dutos Flexíveis, Rígidos e Umbilicais` — nomes correntes de um objeto composto, não ementa.

---

## F. Estrutura

### Método

Contagem de questões por nó. Subassuntos com 1–2 questões: identidade própria versus vizinho natural do *mesmo conhecimento* (não fusão por contagem). Assuntos/disciplinas grandes ou pequenos: SUST e QUI_PET lidos por inteiro, como pedido. Regra 8: nó sem questão.

### Números

| Métrica | Valor |
|---|---|
| Subassuntos com 0 questão | **0** (regra 8 cumprida) |
| Subassuntos com 1 questão | **1** (`SUST_02_001` Mandatos de Biocombustíveis — exceção documentada) |
| Subassuntos com 2 questões | **51** |
| Questões / disciplina (min–max) | SUST 16 … GEO 261 |
| Assunto mais carregado | `REGUL_07` Regimes de E&P (94 q., 6 subassuntos distintos) |
| Subassunto mais carregado | `REGUL_07_003` PPSA (40 q.) |

Carga por disciplina (in-tree): GEO 261, REGUL 235, RESERV 159, GEOF 119, POCO 113, PETROF 74, INS_SUB 58, ELE_ESC 54, PROC_PRI 54, COMERC 48, PRJ 41, REF_GAS 38, SEG_PRO 29, INS_MAR 25, QUI_PET 18, SUST 16.

### F1. Subassuntos de 1–2 questões — identidade

Não se sugere fusão só pela contagem. Amostra do critério:

| Nó | q. | Veredito |
|---|---|---|
| `SUST_02_001` Mandatos de Biocombustíveis | 1 | Identidade própria (política de mistura ≠ matriz). Exceção documentada. Manter. |
| `INS_MAR_02_001` FPSO | 2 | Identidade própria (produção+armazenamento+offloading). Não fundir em `INS_MAR_02_002`. |
| `GEO_03_002` Seções Balanceadas | 2 | Técnica distinta de “Falhas, Dobras e Tensões”. Manter. |
| `GEOF_03_005` Velocidades Sísmicas | 2 | Conceito próprio (Dix, NMO, modelo de v). Manter. |
| `GEOF_05_003` Modelo Convolucional e Wavelet | 2 | Fundamento de processamento, não é o irmão Migração. Manter. |
| `GEOF_06_002` Física de Rochas | 2 | Identidade própria; o problema é o *pai* (ver F3) e a fronteira com PETROF (D3 par 2). Não fundir com 4D. |
| `GEO_04_004` Reservatórios Fraturados | 2 | Identidade geológica; falta FRONT com RESERV (D3 par 3). Não fundir em Modelagem 3D. |
| `PETROF_02_002/003/004` perfis específicos | 2+2+2 | Física distinta por ferramenta. Manter. O irmão `PETROF_02_005` Princípios e Classificação (8) é o overview, não o mesmo conhecimento. |
| `PETROF_05_001` Comparação de Testes | 2 | Identidade se o determinante for DST vs cabo. Manter até o `nucleo_cobrado`. |
| `ELE_ESC_04_001` Análise Nodal | 2 | Conceito próprio, não é Índice de Produtividade. Manter. |
| `ELE_ESC_02_001` Escoamento Multifásico | 2 | Fenômeno ≠ simulação (`_002`, 4). Manter. |
| `REF_GAS_03_001` / `_002` craqueamentos | 2+2 | Processos distintos. Manter. |
| `QUI_PET_03_001` Inibidores e Sequestrantes | 2 | Identidade exigida por `PET_FRONT_027`/`036` (produto × técnica). Manter. |
| `POCO_03_002/003` Acidificação / Fraturamento | 2+2 | Identidade própria. O problema é o irmão guarda-chuva `POCO_03_004` (E3). |
| `RESERV_06_003` Simulação e Ajuste de Histórico | 2 | É o lado dinâmico da regra 7. Pouca carga, identidade máxima. Manter. |
| `PRJ_01_002` Long Lead Items | 2 | Jargão próprio de suprimentos de UEP. Manter. |
| `SUST_03_002` PEI | 2 | `PET_FRONT_048` existe justamente para não fundir com SEG_PRO. Manter. |

Os demais nós de 2 questões (ancoragem, hidratos já estão em 3, etc.) têm nome de objeto técnico reconhecível e não têm vizinho que seja o *mesmo* conhecimento. Sem `nucleo_cobrado`, não se funde nenhum além dos três guarda-chuva da seção E.

### F2. SUST (16) e QUI_PET (18) — a estrutura interna se sustenta?

**SUST — sim.** Três assuntos, seis subassuntos, carga 2+2 / 1+5 / 4+2. Cada folha corresponde a um lado de fronteira já escrito (`PET_FRONT_003` efluente×planta, `040` mandato×produto, `048` PEI×processo, `050` política×CCUS, `051` matriz×instituição). Fundir as seis folhas destruiria essas fronteiras. Não é disciplina pequena demais: é disciplina *estreita por desenho* (regra 7: técnica não entra aqui).

**QUI_PET — sim.** Três assuntos, seis subassuntos, carga 4+4+3 / 3+2 / 2. É o lado “o que é a molécula” de `PET_FRONT_008`, `016`, `027`, `036`, `037`, `041`. Sem esta disciplina, composição/°API/Wobbe/inibidor-como-produto não têm destino canônico e cairiam em GEO, RESERV, REF_GAS ou ELE_ESC — exatamente o que as fronteiras proíbem. `QUI_PET_03` com um único subassunto é pequeno, mas é o suporte estrutural de `PET_FRONT_027`/`036`. Manter.

### F3. Assuntos grandes ou híbridos (não é achado por contagem)

**Não é problema por ser grande:** `REGUL_07` (94) tem seis folhas com objetos distintos (concessão, partilha, PPSA, cessão onerosa, conteúdo local, vigentes/extintos). `GEO_06` (59) são os elementos do sistema petrolífero. Contagem alta de prova ANP não viola regra.

**F3a. `POCO_03` Estimulação e Abandono** junta P&A (4 q.) com estimulação (6 q.). Não é o mesmo conhecimento determinante. As *folhas* já separam; o nome do assunto é que é híbrido. Severidade baixa: organização, não classificação. Cindir o assunto só se se for reordenar IDs por outra razão (A2).

**F3b. `GEOF_06` Sísmica 4D e Física de Rochas** põe física de rochas (insumo de AVO **e** de 4D) debaixo de 4D. A folha `GEOF_06_002` tem identidade; o pai sugere dependência falsa. `PET_FRONT_012` trata 4D GEOF×RESERV, não física de rochas×AVO. Observação de rótulo de assunto, não fusão da folha.

**F3c. `INS_SUB_01_004` Tecnologias Submarinas do Pré-Sal (3 q.).** Nome de pacote, não de conhecimento. Risco de colidir com `INS_SUB_02_001` (HISEP/VASPS estão em `PET_FRONT_030`/`050`). Sem `nucleo_cobrado` não se move; o nome é genérico demais para a regra 2 se as 3 questões forem um equipamento já nomeado no irmão. Watch item, não contestação.

---

## Tabela consolidada de contestações de alocação

Ordenada por severidade e disciplina. **Vazia:** nenhuma contestação satisfaz a regra do auditor (citar a regra violada **e** o `nucleo_cobrado`).

| id_global | atual | proposto | regra | severidade |
|---|---|---|---|---|
| — | — | — | — | — |

Itens que **não** entram nesta tabela (não são alocação de questão in-tree):

- as 12 saídas (seção C) — corretas pelo rótulo do mapeamento;
- A2 ordem alfabética, E1–E3 nomes, D3 pares sem FRONT, A3 granularidade `ENG_ECO_01`.

---

## Lista de bloqueios

O que precisa mudar **antes** de congelar:

1. **Entregar `00_ENTRADA_ESPECIFICAS.jsonl` e reexecutar B** sobre as 1.342 questões. Sem isso a alocação não é certificável. Este é o bloqueio principal.
2. **Resolver E1–E3** (rename ou fusão, com de-para se o ID mudar): `GEOF_02_003`, `RESERV_03_004`, `POCO_03_004`. A regra 1/2 já está violada pelo nome, independentemente do corpus.
3. **Ordem alfabética (A2):** ou reordenar com de-para de IDs na chave folding (como Produção), ou escrever na Parte II a chave efetivamente usada (codepoint Unicode). Do jeito que está, a checagem A falha contra a convenção da casa.
4. **Escrever os três `PET_FRONT` de D3** (água de injeção utilidade×waterflood; física de rochas×petrofísica; reservatório fraturado estático×fluxo). Não são bloqueio de alocação já vista; são buraco do classificador na próxima questão limítrofe.

O que **não** bloqueia:

- SUST e QUI_PET pequenos — estrutura interna se sustenta.
- `SUST_02_001` com 1 questão — exceção documentada, identidade própria.
- 51 subassuntos com 2 questões — identidade própria na inspeção onômica.
- 0 nós vazios, 0 lacunas, 0 nomes duplicados, 52 fronteiras contínuas, regra 7 estruturalmente aplicada, 8×`I` e 4×BASICAS coerentes com a Parte II *pelos rótulos do mapeamento*.
- `ENG_ECO_01` como id de assunto — canônico; só uniformizar granularidade se o contrato do classificador exigir folha.
- Status `CONGELADO` já escrito na Parte II de `PETROLEO.md` — é pretensão, não fato desta auditoria.

**Nada disto autoriza reconstruir a árvore.** Os bloqueios 2–4 são correções pontuais. O bloqueio 1 é evidência, não remodelagem.

---

## Apêndice — evidência de arquivos

| Arquivo pedido | O que foi usado |
|---|---|
| `PETROLEO.md` | anexo `PETROLEO_6530.md` (1.171 linhas; 16/77/262; `PET_FRONT_001`–`052`) |
| `MAPEAMENTO_PETROLEO.json` | anexo `MAPEAMENTO_PETROLEO_3b1d.json` (`gerado_em`: 2026-09-04, 1.354) |
| `00_ENTRADA_ESPECIFICAS.jsonl` | **ausente** |
| `NUCLEO_BASICO.md` | PR #2 `arvores/NUCLEO_BASICO_CORRIGIDO_ETAPA2.md` (15 disciplinas, 98 assuntos, 361 subassuntos) |
| `PRODUCAO.md` | PR #3 `ENGENHARIA_PRODUCAO.md` (estilo; 20/67/227; ordem alfabética folding 0 violações) |

Nenhum arquivo de taxonomia foi alterado nesta auditoria.
