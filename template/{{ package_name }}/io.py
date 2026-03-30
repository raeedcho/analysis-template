"""Data I/O utilities for loading and saving trialframe parquet files."""
import pandas as pd
from pathlib import Path


def load_signal(
    trialframe_dir: Path,
    dataset_name: str,
    signal_name: str,
) -> pd.DataFrame:
    """Load a signal-specific parquet file for a session.

    Parameters
    ----------
    trialframe_dir : Path
        Base directory for trialframe data.
    dataset_name : str
        Session identifier (e.g. "Prez_2022-07-21").
    signal_name : str
        Signal file suffix (e.g. "meta", "neural-spikes-binned").

    Returns
    -------
    pd.DataFrame
    """
    path = trialframe_dir / dataset_name / f"{dataset_name}_{signal_name}.parquet"
    return pd.read_parquet(path)


def save_signal(
    df: pd.DataFrame,
    trialframe_dir: Path,
    dataset_name: str,
    signal_name: str,
) -> Path:
    """Save a DataFrame as a signal-specific parquet file."""
    out_dir = trialframe_dir / dataset_name
    out_dir.mkdir(parents=True, exist_ok=True)
    path = out_dir / f"{dataset_name}_{signal_name}.parquet"
    df.to_parquet(path)
    return path
