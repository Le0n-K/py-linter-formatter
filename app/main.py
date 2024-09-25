from __future__ import annotations

from typing import Dict, List


def format_linter_error(error: dict) -> dict:
    return {
        "line": error.get("line_number"),
        "column": error["column_number"],
        "message": error["text"],
        "name": error["code"],
        "source": "flake8"
    }


def format_single_linter_file(file_path: str, errors: list) -> dict:
    return {
        "path": file_path,
        "status": "failed" if errors else "success",
        "errors": [format_linter_error(error) for error in errors]
   }


def format_linter_report(linter_report: dict) -> dict:
    return {
        "path": linter_report.get("path"),
        "status": "success" if not linter_report.get("errors") else "failed",
        "errors": [
            format_single_linter_file(file["path"], file["errors"])
            for file in linter_report.get("files", [])
        ]
    }