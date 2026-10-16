from typing import TypedDict, Annotated, Sequence
import operator

class AgentState(TypedDict):
    input_text: str
    parsed_query: str
    tool_results: list
    final_output: str

def query_analyzer_node(state: AgentState):
    """Analiza la consulta y extrae parametros para ejecucion."""
    return {"parsed_query": f"Extracted: {state['input_text']}"}

def tool_execution_node(state: AgentState):
    """Simula llamada a herramientas seguras (SQL Read-Only / API externa)."""
    return {"tool_results": ["Record 101: Validated"]}

def generator_node(state: AgentState):
    """Genera la respuesta final basada en el estado acumulado."""
    return {"final_output": f"Resultado validado: {state['tool_results']}"}