# MCP Infinity Agentic Loop

Dieses Modul erweitert den MCP-Microservice um ein einfaches Agenten-Loop-Skript.
Es liest eine YAML-Spezifikation ein und startet mehrere parallele Aufrufe an das
hinterlegte LLM. Die Antworten werden je Welle in Textdateien gespeichert.

## Beispielaufruf

```bash
python -m infinity.loop specs/sample_spec.yaml
```

## Spezifikationsformat

```yaml
prompt: "Entwerfe ein neues UI-Konzept f\u00fcr das Modul Lagerverwaltung."
model: "gpt-3.5-turbo"
max_tokens: 300
parallel_agents: 2
count: 3
output_dir: "agent_outputs"
```

Damit werden drei Wellen mit jeweils zwei parallelen Agenten ausgef\u00fchrt. Die
Antworten landen in `agent_outputs/wave_<nummer>_agent_<index>.txt`.
