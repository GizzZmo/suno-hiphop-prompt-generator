#!/usr/bin/env python3
"""
Suno Prompt Generator for Hip-Hop
Based on the Systematic Linguistic Analysis and Generative Modeling of the OHHLA proposal.
Generates ready-to-paste Suno v5.5 Custom Mode prompts following the Harmonic Prompt Crafter guidelines.
Incorporates era-specific styles, regional vernaculars, rhyme density concepts, flow types,
AAVE authenticity, and sophisticated harmonic steering (circle of fifths + tritones).
"""

import textwrap
from typing import Dict, List, Optional

class HipHopSunoGenerator:
    def __init__(self):
        self.eras = {
            "80s_oldschool": {
                "bpm": "100-110",
                "instruments": "classic boom bap drums, vinyl crackle, simple drum machine patterns, horn stabs",
                "mood": "raw, energetic, party-oriented",
                "harmonic": "straightforward progressions with bluesy tritone accents in basslines",
                "vocal": "aggressive, clear delivery, rhythmic chanting"
            },
            "90s_boombap": {
                "bpm": "90",
                "instruments": "dusty boom bap drums (hard kick, snappy snare, crisp hi-hats), chopped jazz and soul samples, warm bass",
                "mood": "gritty, introspective or boastful, street-wise",
                "harmonic": "sophisticated harmonic movement following the circle of fifths with descending fifths basslines and strategically placed tritone tensions from jazz samples",
                "vocal": "precise multi-syllabic flow, AAVE-inflected delivery"
            },
            "westcoast_gfunk": {
                "bpm": "95",
                "instruments": "smooth G-Funk synthesizers (Moog-style leads), deep 808-inspired bass, laid-back drum patterns, funky guitar licks",
                "mood": "laid-back, sunny yet menacing, cruising",
                "harmonic": "smooth circle-of-fifths progressions with minor pentatonic and tritone-colored melodic hooks",
                "vocal": "melodic, syncopated delivery, conversational tone"
            },
            "southern_trap": {
                "bpm": "140",
                "instruments": "heavy 808 sub-bass, rapid hi-hat rolls, dark synth melodies, sparse drums",
                "mood": "dark, aggressive or hedonistic, high energy",
                "harmonic": "ominous tritone-laden synth riffs resolving with power, minimal harmonic movement with heavy low-end",
                "vocal": "triplet-heavy cadence, ad-libs, melodic auto-tune optional"
            },
            "modern_trap": {
                "bpm": "140-150",
                "instruments": "modern 808s, atmospheric pads, trap drums with rolls, melodic synths",
                "mood": "introspective, emotional or flexing",
                "harmonic": "dark harmonic color from tritones balanced with consonant resolution, sparse progressions",
                "vocal": "melodic rap, mumble or clear, high or low energy"
            }
        }

        self.regions = {
            "east_coast": "dense multi-syllabic rhyme schemes, complex internal rhymes, high rhyme density",
            "west_coast": "melodic, syncopated flows, smoother delivery",
            "south": "triplet-heavy cadence, rhythmic bounce, Southern drawl phonetics",
            "midwest": "fast technical flows or storytelling, varied"
        }

        self.flows = {
            "chopper": "high syllables-per-beat, dense packing, rapid-fire delivery",
            "standard": "balanced flow, clear articulation",
            "mumble_vibe": "low syllables-per-beat, stretched syllables, atmospheric rests, vibe-oriented"
        }

    def generate_style_prompt(self, era: str, region: str, flow: str, mood: str, theme_hint: str = "") -> str:
        era_data = self.eras.get(era, self.eras["90s_boombap"])
        region_desc = self.regions.get(region, self.regions["east_coast"])
        flow_desc = self.flows.get(flow, self.flows["standard"])

        # Clean era name for display
        era_display = era.replace("_", " ").replace("boombap", "Boom Bap").replace("gfunk", "G-Funk")
        if era_display.startswith("90s"):
            era_display = "90s Boom Bap"
        elif era_display.startswith("80s"):
            era_display = "80s Old School"
        elif "westcoast" in era_display.lower():
            era_display = "West Coast G-Funk"
        elif "southern" in era_display.lower():
            era_display = "Southern Trap"
        elif "modern" in era_display.lower():
            era_display = "Modern Trap"

        style_parts = [
            f"{era_display} hip-hop",
            f"{mood} energy",
            era_data["instruments"],
            f"male rap vocals with {flow_desc}, {region_desc}",
            era_data["vocal"],
            f"{era_data['bpm']} BPM",
            era_data["harmonic"],
            "crisp mix with punchy low end and clear midrange for vocals",
            "-muddy low end -generic pop drums -overly bright synths -auto-tune excessive"
        ]
        # Optionally weave theme lightly if short
        if theme_hint and len(theme_hint) < 40:
            style_parts.insert(2, f"thematic focus on {theme_hint}")

        style = ", ".join(style_parts)
        if len(style) > 950:
            style = style[:950] + "..."
        return style

    def generate_lyrics(self, theme: str, era: str, region: str, flow: str, rhyme_density: str = "high") -> str:
        # Structured lyrics with AAVE-friendly phrasing, era-appropriate density, harmonic cues
        # Theme is woven throughout; high rhyme density emphasizes multi-syllabic and internal rhymes

        sections = []

        sections.append("[Instrumental Intro: boom bap / trap drums with descending fifths bass motif and subtle tritone tension]")

        # Dynamic Verse 1
        if "east" in region or era == "90s_boombap":
            verse1 = f"""[Verse 1]
Concrete and code, {theme} in the cipher we hold
Multi-syllabic structures stacking stories untold
Midnight sessions, the density of the rhyme controlled
From the Bronx oral tradition to the data we mold
AAVE in the syntax, no correction of the flow
Phonetic precision, the vernacular we know
Tension in the tritone sample, then the fifths let it go
Bars engineered for the ear, not just the next-token show"""
        elif "south" in region or "trap" in era:
            verse1 = f"""[Verse 1]
{theme.capitalize()} bouncing on the triplet and the 808
Southern cadence carrying the weight of the day
Rhyme density flexing when the beat start to sway
Opp watching, but the flow don't fade away
Drawl in the delivery, authentic to the core
Tritone shadows in the synth, then the resolution pours"""
        else:
            verse1 = f"""[Verse 1]
{theme.capitalize()} moving through the nighttime air
Rhyme schemes locking in with technical flair
Flow matching the regional character we share
From analysis to generation, the archive's care
Preserving the nuances the models often miss
Descending fifths drive the narrative to this"""

        sections.append(verse1)

        chorus = f"""[Chorus]
{theme.capitalize()} — quantified and brought to life
Rhyme density, vocabulary, the linguistic knife
Cutting through the noise with authentic AAVE
East to West to South, the styles that we convey
Circle of fifths in the harmony, tritone for the edge
DeepFlow engine turning data into the pledge"""

        sections.append(chorus)

        verse2 = """[Verse 2]
Second verse diving into the metrics of the art
Syllables per beat, syncopation from the start
Vocabulary entropy mapping every part
Of the evolution, from boom bap to the modern heart
Reverse-order generation anchoring the end
Then building forward, the structural trend
Cultural insiders in the feedback loop we send
Avoiding caricature, authenticity we defend"""

        sections.append(verse2)

        sections.append("""[Bridge: stronger tritone tension before circle-of-fifths resolution]
When the solver proxy navigates the archive deep
Anubis challenges, but the data we keep
Normalization preserving every phonetic leap
So the model can generate with genuine heat

[Outro: resolving harmonic movement]
From OHHLA's raw transcriptions to the trained machine
The oral tradition quantified, the future we have seen""")

        lyrics = "\n\n".join(sections)
        if len(lyrics) > 4500:
            lyrics = lyrics[:4500] + "\n[...]"
        return lyrics

    def generate_full_prompt(self, era: str = "90s_boombap", region: str = "east_coast",
                             flow: str = "standard", mood: str = "gritty and focused",
                             theme: str = "the preservation of oral tradition through data",
                             rhyme_density: str = "high") -> str:
        style = self.generate_style_prompt(era, region, flow, mood)
        lyrics = self.generate_lyrics(theme, era, region, flow, rhyme_density)

        full = f"""### STYLE PROMPT
{style}

### LYRICS + DIRECTIONS
{lyrics}"""
        return full

    def interactive(self):
        print("=== Hip-Hop Suno Prompt Generator ===")
        print("Based on OHHLA Linguistic Analysis & Generative Modeling Proposal\n")
        print("Available eras:", list(self.eras.keys()))
        print("Available regions:", list(self.regions.keys()))
        print("Available flows:", list(self.flows.keys()))
        print()

        era = input("Era (default 90s_boombap): ").strip() or "90s_boombap"
        region = input("Region (default east_coast): ").strip() or "east_coast"
        flow = input("Flow (default standard): ").strip() or "standard"
        mood = input("Mood (default gritty and focused): ").strip() or "gritty and focused"
        theme = input("Theme (default: the preservation of oral tradition through data): ").strip() or "the preservation of oral tradition through data"
        rhyme_density = input("Rhyme density (high/medium/low, default high): ").strip() or "high"

        print("\n" + "="*50)
        print(self.generate_full_prompt(era, region, flow, mood, theme, rhyme_density))
        print("="*50)

if __name__ == "__main__":
    gen = HipHopSunoGenerator()
    # Example generation
    print("EXAMPLE PROMPT (90s East Coast Boom Bap, high rhyme density):\n")
    print(gen.generate_full_prompt())
    print("\n\nTo run interactively: python suno_hiphop_prompt_generator.py --interactive")
    # Uncomment for interactive:
    # gen.interactive()
