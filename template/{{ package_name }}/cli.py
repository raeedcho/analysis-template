"""Shared CLI argument parsing for DVC pipeline scripts.

Usage in a script:
    from src.cli import parse_args  # or whatever package_name is
    args = parse_args(description="My stage", extra_args=[...])

This module centralizes the boilerplate of reading params.yaml-style
arguments so each script doesn't have to redefine --dataset, --loglevel, etc.
"""
import argparse
from pathlib import Path
import logging


def add_dir_structure_args(parser: argparse.ArgumentParser) -> None:
    """Add standard directory structure arguments matching params.yaml."""
    parser.add_argument("--raw_data_dir", type=Path)
    parser.add_argument("--trialframe_dir", type=Path, default=Path("data/trialframe"))
    parser.add_argument("--config_dir", type=Path, default=Path("conf"))
    parser.add_argument("--log_dir", type=Path, default=Path("logs"))
    parser.add_argument("--results_dir", type=Path, default=Path("results"))


def add_logging_args(parser: argparse.ArgumentParser) -> None:
    """Add standard logging arguments."""
    parser.add_argument("--loglevel", default="INFO")


def parse_args(
    description: str,
    extra_args: list | None = None,
) -> argparse.Namespace:
    """Parse CLI arguments with standard project conventions.

    Parameters
    ----------
    description : str
        Script description for --help.
    extra_args : list, optional
        List of (name, kwargs) tuples for additional arguments.
        Example: [("--bin_size", {"default": "10ms"})]
    """
    parser = argparse.ArgumentParser(description=description)
    parser.add_argument("--dataset", required=True, help="Dataset name (e.g. Prez_2022-07-21)")
    add_dir_structure_args(parser)
    add_logging_args(parser)

    for name, kwargs in (extra_args or []):
        parser.add_argument(name, **kwargs)

    return parser.parse_args()


def setup_logging(args: argparse.Namespace, stage_name: str) -> logging.Logger:
    """Configure logging for a pipeline stage."""
    log_dir = Path(args.log_dir) / stage_name
    log_dir.mkdir(parents=True, exist_ok=True)

    logging.basicConfig(
        filename=log_dir / f"{args.dataset}.log",
        level=getattr(logging, args.loglevel.upper(), logging.INFO),
        format="%(asctime)s %(name)s %(levelname)s: %(message)s",
    )
    return logging.getLogger(stage_name)
