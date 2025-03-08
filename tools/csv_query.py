from collections.abc import Generator
from typing import Any

import pandas as pd
from sqlalchemy import create_engine
from dify_plugin import Tool
from dify_plugin.entities.tool import ToolInvokeMessage


class CSVQueryTool(Tool):
    def _invoke(self, tool_parameters: dict[str, Any]) -> Generator[ToolInvokeMessage]:
        file = tool_parameters.get("file")
        df = pd.read_csv(file)
        
        engine = create_engine("sqlite:///csv.db")
        df.to_sql("csv", engine, index=False)

