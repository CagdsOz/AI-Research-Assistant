from datetime import datetime
from typing import Dict, Any, Optional

class ReportFormatter:
    def __init__(self):
        """
        Aggregates and formats validated outputs into a structured academic report.
        """
        self.report_template = """# AI Research Assistant Report
**Date:** {date}
**Status:** {status}

---

## 1. Mathematical Analysis
{math_content}

---

## 2. Financial Data Analysis
{financial_content}

---
*Generated for RTU Engineering Research - Verified and Deterministic.*
"""

    def format_math_section(self, math_data: Dict[str, Any]) -> str:
        """Structures symbolic math engine output."""
        if math_data.get("success"):
            return (f"### Result (LaTeX):\n$${math_data['result_latex']}$$\n\n"
                    f"**Derivation:** {math_data['derivation']}\n"
                    f"**Raw Output:** `{math_data['raw_result']}`")
        return f"**Error in Math Engine:** {math_data.get('error', 'Unknown error')}"

    def format_financial_section(self, fin_data: Dict[str, Any]) -> str:
        """Structures financial data module output."""
        if fin_data.get("success"):
            return (f"### Market Data: {fin_data['id'].upper()}\n"
                    f"* **Current Price:** {fin_data['price']} {fin_data['currency']}\n"
                    f"* **24h Change:** {fin_data['change_24h']:.2f}%\n"
                    f"* **Market Cap:** {fin_data['market_cap']:,} {fin_data['currency']}")
        return f"**Error in Financial API:** {fin_data.get('error', 'Unknown error')}"

    def generate_markdown(self, math_result: Dict[str, Any], fin_result: Dict[str, Any]) -> str:
        """Generates the final .md content."""
        math_content = self.format_math_section(math_result)
        financial_content = self.format_financial_section(fin_result)
        
        return self.report_template.format(
            date=datetime.now().strftime("%Y-%m-%d %H:%M"),
            status="Success" if (math_result.get("success") and fin_result.get("success")) else "Partial Data",
            math_content=math_content,
            financial_content=financial_content
        )