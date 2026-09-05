#!/usr/bin/env python3
"""Validador e inspetor do dataset de mapeamento de disciplinas.

Carrega um arquivo de mapeamento (por padrão ``mapeamento_disciplina.json``),
verifica a integridade estrutural e a consistência dos metadados e imprime um
resumo estatístico das disciplinas.

O código-fonte deste repositório é composto apenas por dados; esta ferramenta
funciona como a "aplicação" de referência para trabalhar com o dataset.
"""

from __future__ import annotations

import argparse
import json
import sys
from collections import Counter
from pathlib import Path


class ErroDeValidacao(Exception):
    """Levantada quando o dataset viola uma regra de integridade."""


def carregar(caminho: Path) -> dict:
    if not caminho.exists():
        raise ErroDeValidacao(f"arquivo não encontrado: {caminho}")
    try:
        with caminho.open(encoding="utf-8") as arquivo:
            return json.load(arquivo)
    except json.JSONDecodeError as exc:
        raise ErroDeValidacao(f"JSON inválido em {caminho}: {exc}") from exc


def validar(dados: dict) -> list[str]:
    """Retorna a lista de problemas encontrados (vazia quando o dataset é válido)."""

    problemas: list[str] = []

    if not isinstance(dados, dict):
        return ["o documento raiz deve ser um objeto JSON"]

    meta = dados.get("meta")
    mapeamentos = dados.get("mapeamentos")

    if not isinstance(meta, dict):
        problemas.append("campo 'meta' ausente ou não é um objeto")
        meta = {}
    if not isinstance(mapeamentos, list):
        problemas.append("campo 'mapeamentos' ausente ou não é uma lista")
        mapeamentos = []

    vistos: set[str] = set()
    for indice, item in enumerate(mapeamentos):
        if not isinstance(item, dict):
            problemas.append(f"mapeamentos[{indice}] não é um objeto")
            continue
        id_global = item.get("id_global")
        disciplina = item.get("disciplina_canonica")
        if not id_global or not isinstance(id_global, str):
            problemas.append(f"mapeamentos[{indice}] com 'id_global' ausente/vazio")
        elif id_global in vistos:
            problemas.append(f"'id_global' duplicado: {id_global}")
        else:
            vistos.add(id_global)
        if not disciplina or not isinstance(disciplina, str):
            problemas.append(
                f"mapeamentos[{indice}] ({id_global}) sem 'disciplina_canonica'"
            )

    quantidade_declarada = meta.get("quantidade_questoes")
    if isinstance(quantidade_declarada, int) and quantidade_declarada != len(mapeamentos):
        problemas.append(
            "meta.quantidade_questoes ("
            f"{quantidade_declarada}) difere do total real ({len(mapeamentos)})"
        )

    lotes = meta.get("lotes_origem")
    if isinstance(lotes, list):
        lotes_declarados = meta.get("quantidade_lotes")
        if isinstance(lotes_declarados, int) and lotes_declarados != len(lotes):
            problemas.append(
                "meta.quantidade_lotes ("
                f"{lotes_declarados}) difere do número de lotes ({len(lotes)})"
            )
        soma_lotes = sum(
            lote.get("quantidade_questoes", 0)
            for lote in lotes
            if isinstance(lote, dict)
        )
        if isinstance(quantidade_declarada, int) and soma_lotes != quantidade_declarada:
            problemas.append(
                "soma das questões dos lotes ("
                f"{soma_lotes}) difere de meta.quantidade_questoes ({quantidade_declarada})"
            )

    return problemas


def resumir(dados: dict) -> dict:
    meta = dados.get("meta", {}) if isinstance(dados, dict) else {}
    mapeamentos = dados.get("mapeamentos", []) if isinstance(dados, dict) else []
    contagem = Counter(
        item.get("disciplina_canonica", "(sem disciplina)")
        for item in mapeamentos
        if isinstance(item, dict)
    )
    return {
        "passada": meta.get("passada"),
        "etapa": meta.get("etapa"),
        "total_questoes": len(mapeamentos),
        "total_lotes": len(meta.get("lotes_origem", []) or []),
        "total_disciplinas": len(contagem),
        "disciplinas": contagem,
    }


def imprimir_relatorio(resumo: dict) -> None:
    print("=" * 60)
    print("  Dataset de mapeamento de disciplinas")
    print("=" * 60)
    print(f"  Passada .............: {resumo['passada']}")
    print(f"  Etapa ...............: {resumo['etapa']}")
    print(f"  Lotes de origem .....: {resumo['total_lotes']}")
    print(f"  Total de questões ...: {resumo['total_questoes']}")
    print(f"  Disciplinas distintas: {resumo['total_disciplinas']}")
    print("-" * 60)
    print("  Questões por disciplina (ordem decrescente):")
    for disciplina, quantidade in resumo["disciplinas"].most_common():
        print(f"    {quantidade:>5}  {disciplina}")
    print("=" * 60)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument(
        "arquivo",
        nargs="?",
        default="mapeamento_disciplina.json",
        type=Path,
        help="caminho do arquivo de mapeamento (padrão: mapeamento_disciplina.json)",
    )
    parser.add_argument(
        "--somente-validar",
        action="store_true",
        help="valida a integridade sem imprimir o resumo estatístico",
    )
    parser.add_argument(
        "--json",
        action="store_true",
        help="imprime o resumo em formato JSON",
    )
    args = parser.parse_args(argv)

    try:
        dados = carregar(args.arquivo)
    except ErroDeValidacao as exc:
        print(f"ERRO: {exc}", file=sys.stderr)
        return 2

    problemas = validar(dados)
    if problemas:
        print(f"Validação FALHOU: {len(problemas)} problema(s):", file=sys.stderr)
        for problema in problemas:
            print(f"  - {problema}", file=sys.stderr)
        return 1

    if not args.somente_validar:
        resumo = resumir(dados)
        if args.json:
            saida = {**resumo, "disciplinas": dict(resumo["disciplinas"])}
            print(json.dumps(saida, ensure_ascii=False, indent=2))
        else:
            imprimir_relatorio(resumo)

    print(f"\nOK: {args.arquivo} é válido.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
