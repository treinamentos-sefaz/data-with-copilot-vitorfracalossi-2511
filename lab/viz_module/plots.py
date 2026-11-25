"""Módulo 4 — Visualização de Dados.

Complete cada função com o apoio do GitHub Copilot. Cada função deve **gerar um
gráfico e salvá-lo** no caminho ``out_path`` (formato PNG). Use ``matplotlib`` e
``seaborn``. Em ambientes sem interface gráfica (CI), mantenha o backend "Agg".

Valide com:  ``python lab/check.py --module viz``
"""
from __future__ import annotations

from pathlib import Path

import matplotlib

matplotlib.use("Agg")  # backend sem interface gráfica (funciona no CI)
import matplotlib.pyplot as plt  # noqa: E402
import pandas as pd  # noqa: E402
import seaborn as sns  # noqa: E402


def plot_rating_distribution(df: pd.DataFrame, out_path: str):
    """Histograma da distribuição da coluna ``rating``. Inclua título e labels em
    português e salve a figura em ``out_path``."""
    # Prompt sugerido: "Crie um histograma da coluna rating com 20 bins, título e
    #  labels em português, e salve a figura em out_path."
    data = df.copy()
    ratings = pd.to_numeric(data["rating"], errors="coerce").dropna()

    fig, ax = plt.subplots(figsize=(8, 5))
    ax.hist(ratings, bins=20, color="#4C78A8", edgecolor="white")
    ax.set_title("Distribuição das notas dos vinhos")
    ax.set_xlabel("Nota")
    ax.set_ylabel("Quantidade")
    fig.tight_layout()

    output = Path(out_path)
    output.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(output, dpi=100, bbox_inches="tight")
    plt.close(fig)
    return fig


def plot_top_varieties(df: pd.DataFrame, out_path: str):
    """Gráfico de barras horizontais com as 10 variedades (``variety``) com maior
    quantidade de vinhos. Salve a figura em ``out_path``."""
    data = df.copy()
    counts = data["variety"].dropna().value_counts().head(10)

    fig, ax = plt.subplots(figsize=(9, 6))
    ax.barh(counts.index, counts.values, color="#4C78A8")
    ax.invert_yaxis()
    ax.set_title("10 variedades de vinho mais frequentes")
    ax.set_xlabel("Quantidade")
    ax.set_ylabel("Variedade")
    fig.tight_layout()

    output = Path(out_path)
    output.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(output, dpi=100, bbox_inches="tight")
    plt.close(fig)
    return fig


def plot_boxplot_by_variety(df: pd.DataFrame, out_path: str):
    """Boxplot de ``rating`` para as 5 variedades mais frequentes. Salve a figura
    em ``out_path``."""
    data = df.copy()
    top_varieties = data["variety"].dropna().value_counts().head(5).index.tolist()
    filtered = data[
        data["variety"].isin(top_varieties)
    ].copy()
    filtered["rating"] = pd.to_numeric(filtered["rating"], errors="coerce")
    filtered = filtered.dropna(subset=["rating", "variety"])

    fig, ax = plt.subplots(figsize=(10, 6))
    sns.boxplot(
        data=filtered,
        x="variety",
        y="rating",
        order=top_varieties,
        ax=ax,
        color="#72A7D4",
    )
    ax.set_title("Distribuição das notas das 5 variedades mais frequentes")
    ax.set_xlabel("Variedade")
    ax.set_ylabel("Nota")
    ax.tick_params(axis="x", rotation=30)
    fig.tight_layout()

    output = Path(out_path)
    output.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(output, dpi=100, bbox_inches="tight")
    plt.close(fig)
    return fig
