# Multi-Step Agentic Workflow using State Graphs
![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)
![LangGraph](https://img.shields.io/badge/LangGraph-StateGraph-orange.svg)
![LangChain](https://img.shields.io/badge/LangChain-v0.1+-green.svg)
![Pydantic v2](https://img.shields.io/badge/pydantic-v2-E92063.svg)
![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)

Implementacion de flujos de trabajo multi-agente deterministas utilizando grafos de estado (LangGraph). A diferencia de los bucles de agentes no restringidos, esta arquitectura modela las transiciones de forma explicita para evitar bucles infinitos y consumos imprevistos de tokens.

## Caracteristicas Principales
- Maquina de Estados Explicita: Control granular del ciclo de vida de la ejecucion y persistencia de memoria.
- Tool Calling con Validacion: Ejecucion controlada de herramientas externas bajo el principio de minimo privilegio.
- Mitigacion de Alucinaciones: Verificacion intermedia antes de emitir la respuesta final.

## Estructura del Flujo

```mermaid
graph TD
    Start([Inicio]) --> Analyzer[Nodo Analizador de Intencion]
    Analyzer --> Router{Requiere Herramienta}
    Router -- Si --> ToolExecution[Ejecucion de Herramienta Segura]
    ToolExecution --> Synthesizer[Sintesis y Validacion]
    Router -- No --> DirectAnswer[Generacion Directa]
    Synthesizer --> End([Respuesta Validada])
    DirectAnswer --> End
```
