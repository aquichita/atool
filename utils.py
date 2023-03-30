import warnings
from pathlib import Path
from typing import List
import pandas as pd
from jinja2 import Environment, FileSystemLoader


pd.set_option("display.notebook_repr_html", False)


def _format_row(row: str) -> List[str]:
    lines = []
    if pd.isna(row) or not row.strip():
        return lines
    if row.count("\n") and row[:1].isdigit():
        for row in row.split("\n"):
            lines.append(row.strip())
    else:
        lines.append(row.strip())
    return lines


def _contents(file: bytes) -> dict:
    with warnings.catch_warnings(record=True):
        warnings.simplefilter("always")
        data = pd.read_excel(io=file, engine="openpyxl", sheet_name=None)
        assert len(data) > 0, data
        for name, content in data.items():
            columns, rows = content.columns, content.values
            steps = []
            for row in content.values:
                row = dict(zip(columns, row))
                row[row.get("角色")] = _format_row(row.get(row.get("角色")))
                steps.append(row)
            return {"name": name, "steps": steps}


statics = Path.cwd().joinpath("statics")
env = Environment(loader=FileSystemLoader(statics))


def case_template(file: bytes):
    case = env.get_template("case.tpl")
    return case.render(case=_contents(file))
