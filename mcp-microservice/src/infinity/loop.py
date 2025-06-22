import asyncio
import os
from pathlib import Path
from typing import Any, Dict

import openai
import yaml


async def _call_openai(prompt: str, model: str, max_tokens: int) -> str:
    """Call OpenAI asynchronously and return the response text."""
    api_key = os.environ.get("OPENAI_API_KEY")
    if not api_key:
        raise RuntimeError("OPENAI_API_KEY not set")
    openai.api_key = api_key
    resp = await openai.ChatCompletion.acreate(
        model=model,
        messages=[{"role": "user", "content": prompt}],
        max_tokens=max_tokens,
    )
    return resp.choices[0].message["content"]


async def _run_wave(prompt: str, model: str, max_tokens: int, wave: int, parallel: int, out_dir: Path) -> None:
    """Run one wave of parallel agent calls."""
    tasks = []
    for i in range(parallel):
        tasks.append(_call_openai(prompt, model, max_tokens))
    results = await asyncio.gather(*tasks)
    for i, text in enumerate(results):
        outfile = out_dir / f"wave_{wave}_agent_{i}.txt"
        outfile.write_text(text)


async def run_infinite(spec: Dict[str, Any]) -> None:
    """Execute waves of agents based on the spec configuration."""
    prompt = spec["prompt"]
    model = spec.get("model", "gpt-3.5-turbo")
    max_tokens = spec.get("max_tokens", 200)
    parallel = spec.get("parallel_agents", 1)
    count = spec.get("count", 1)
    out_dir = Path(spec.get("output_dir", "agent_outputs"))
    out_dir.mkdir(parents=True, exist_ok=True)

    for wave in range(count):
        await _run_wave(prompt, model, max_tokens, wave, parallel, out_dir)


def main() -> None:
    import argparse

    parser = argparse.ArgumentParser(description="Run MCP infinity agentic loop")
    parser.add_argument("spec_file", help="Path to YAML specification file")
    args = parser.parse_args()

    with open(args.spec_file, "r", encoding="utf-8") as f:
        spec = yaml.safe_load(f)

    asyncio.run(run_infinite(spec))


if __name__ == "__main__":
    main()
