# Suno Hip-Hop Prompt Generator

Python tool that generates ready-to-paste **Suno v5.5 Custom Mode** prompts for hip-hop tracks.

It is based on concepts from the *Systematic Linguistic Analysis and Generative Modeling of the Original Hip-Hop Lyrics Archive (OHHLA)* proposal, including:

- Era-specific styles (80s Old School, 90s Boom Bap, West Coast G-Funk, Southern Trap, Modern Trap)
- Regional characteristics (East Coast multi-syllabic density, Southern triplet cadence, etc.)
- Flow types (Chopper / high SPB, Standard, Mumble/Vibe)
- AAVE preservation and authentic slang handling
- Harmonic steering using circle-of-fifths progressions and devil’s tritones (for tension and resolution)

## Usage

```bash
python suno_hiphop_prompt_generator.py
```

This prints an example 90s East Coast Boom Bap prompt.

### Programmatic use

```python
from suno_hiphop_prompt_generator import HipHopSunoGenerator

gen = HipHopSunoGenerator()
print(gen.generate_full_prompt(
    era="southern_trap",
    region="south",
    flow="chopper",
    mood="dark and aggressive",
    theme="rising from the bottom"
))
```

### Interactive mode

Uncomment the last line in the script or call `gen.interactive()`.

## Output format

Always produces:

```
### STYLE PROMPT
...

### LYRICS + DIRECTIONS
...
```

Ready to paste directly into Suno Custom Mode.

## Notes

- Style prompts stay under 1000 characters.
- Lyrics include section tags, performance notes, and harmonic directions.
- Negative prompts are included to avoid common Suno pitfalls.
- Default theme is meta (related to the OHHLA project). Change the `theme` parameter for your own subject.
