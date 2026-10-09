# LLM-assisted interpretation (Section 2.9 of the manuscript)

This folder holds the materials of the auxiliary interpretation step: the notebook that called the OpenAI API, the texts sent to the model, the data files from which the input text was built, and the raw output.

The notebook sent two requests on 9 October 2026. The first was refused by the API because the account had no credit, and produced no output. The second (21:43 JST; `gpt-5.2-2025-12-11`, reasoning effort none, temperature 0) returned the output in `outputs/`. Both requests are listed in `RUN.md`.

- `code/llm_interpretation.ipynb` – the notebook. It reads `data/terms120.csv`, `data/network_nodes.csv`, `data/network_edges.csv` and `data/ca_characteristic_terms_monkin_ja.txt` at commit `1166178`, checks them against the numbers reported in the manuscript, builds the prompt and sends one request to the OpenAI Responses API.
- `prompts/` – the instructions and the input text, exactly as sent
- `inputs/` – the data files from which the input text was built, unchanged
- `outputs/` – the response body as received (`response_raw.json`) and the text of the response, unedited (`output.md`)
- `RUN.md`, `run_log.jsonl` – date and time, model, parameters, token counts and SHA-256 checksums of every request sent

The model output was used only as supplementary information; the interpretation reported in the manuscript was decided by the authors after cross-checking against the KH Coder outputs.
