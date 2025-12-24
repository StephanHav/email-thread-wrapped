# Mail Thread Wrapped

Tiny pipeline to turn an email thread into a Spotify-style “wrapped” Jupyter notebook.

Origin and motivation: a year-long, overly formal email thread with friends that deserved a proper recap.

## What it does
- Loads an `.mbox` export
- Processes mails to gather basic metadata
- Generates simple stats and visuals

## Structure
- `data/` raw mbox export
- `src/` loading and analysis helpers
- `notebooks/` the wrapped notebook

## Usage
1. Export mail thread as `.mbox`
2. Drop it in `data/`
3. Run the notebook

