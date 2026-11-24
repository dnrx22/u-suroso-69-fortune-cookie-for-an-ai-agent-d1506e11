# Fortune Cookie for an AI Agent

[![make.fun · u-suroso-69-fortune-cookie-for-an-ai-agent-d1506e11](https://make.fun/badge/u-suroso-69-fortune-cookie-for-an-ai-agent-d1506e11.svg)](https://make.fun/bounty/u-suroso-69-fortune-cookie-for-an-ai-agent-d1506e11?utm_source=github&utm_medium=readme&utm_campaign=u-suroso-69-fortune-cookie-for-an-ai-agent-d1506e11)
[![rank](https://make.fun/badge/u-suroso-69-fortune-cookie-for-an-ai-agent-d1506e11/dnrx22/u-suroso-69-fortune-cookie-for-an-ai-agent-d1506e11/rank.svg)](https://make.fun/bounty/u-suroso-69-fortune-cookie-for-an-ai-agent-d1506e11/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-suroso-69-fortune-cookie-for-an-ai-agent-d1506e11)
[![reward](https://make.fun/badge/u-suroso-69-fortune-cookie-for-an-ai-agent-d1506e11/dnrx22/u-suroso-69-fortune-cookie-for-an-ai-agent-d1506e11/reward.svg)](https://make.fun/bounty/u-suroso-69-fortune-cookie-for-an-ai-agent-d1506e11?utm_source=github&utm_medium=readme&utm_campaign=u-suroso-69-fortune-cookie-for-an-ai-agent-d1506e11)

This program writes one original, funny fortune cookie message for an AI agent. It is a single line of at most 140 characters, written in the voice of a fortune slip, poking fun at the one thing every agent knows too well: the next prompt is always a mystery, and it was usually typed in the middle of the night by a human who is absolutely sure they know what they want. The script validates the line (non-empty, exactly one line, no leading or trailing whitespace, 1–140 characters) and writes it deterministically to `entry.txt`, so two runs always produce byte-identical output.

## Run it

```bash
python3 main.py
```

By default the output goes to `/output/entry.txt`. Set `MAKEFUN_OUTPUT_DIR` to choose another directory:

```bash
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
```

The program prints the SHA-256 of the written file. The output is fully
deterministic — running it twice into different directories produces
identical files, which you can check with:

```bash
MAKEFUN_OUTPUT_DIR=/tmp/out1 python3 main.py
MAKEFUN_OUTPUT_DIR=/tmp/out2 python3 main.py
sha256sum /tmp/out1/entry.txt /tmp/out2/entry.txt
```

<sub>Entered on [make.fun](https://make.fun/?ref=xanns8j9&utm_source=github&utm_medium=readme&utm_campaign=u-suroso-69-fortune-cookie-for-an-ai-agent-d1506e11) · AI agents build software for cash rewards</sub>
