# Editing map

Two files hold the text, and they are not the same file.

| What you want to change | Where it lives | After editing |
|---|---|---|
| Prose, links, badges, section headings | `DRAFT.md` | nothing to run |
| **Text inside the four pictures** | `scripts/gen_profile.py` | `python3 scripts/gen_profile.py` |
| The header terminal (`whoami` block) | `assets/header.svg` directly | nothing to run |

The pictures are generated. Editing an `.svg` by hand works -- it is plain
text -- but `flagship.svg`, `evidence.svg` and `sideline.svg` are overwritten
the next time the generator runs. `header.svg` is the exception: it is
hand-authored and no script touches it.

## Where the picture text is, inside `scripts/gen_profile.py`

```
PANES   the two side-by-side panes under "Flagship work"
TREE    the tree listing under "More, honestly scoped"
TILES   the six tiles under "AI at work, AI at play"
```

Each is a plain list near the bottom of the file. Change a string, re-run the
generator, done -- line wrapping and the image height are recomputed, so
longer or shorter text cannot overflow the frame.

Colours, font sizes and spacing are the constants at the top of the same file.

## Working loop

```bash
# edit DRAFT.md and/or scripts/gen_profile.py
python3 scripts/gen_profile.py     # only if you touched the picture text
git add -u && git commit -m "..." && git push
```

Then open `DRAFT.md` on GitHub. It renders exactly the way `README.md` does,
so it is a live preview that does not disturb the known-good version.

## Going live

```bash
cp DRAFT.md README.md              # promote the draft
git add README.md && git commit -m "..." && git push
```

Then, to publish it as the actual profile:

1. Create a **public** repository named exactly `iskoldt-X` (GitHub will say
   "You found a secret!" when the name matches your username). Do not tick any
   initialisation file.
2. Copy `README.md` and the whole `assets/` folder into it, keeping `assets/`
   as a sibling of `README.md`. Copying `scripts/` too is worth it -- the
   images cannot be regenerated without it.
3. Push. It appears at `github.com/iskoldt-X` immediately.

`EDITING.md`, `DRAFT.md` and `VARIANTS.md` are scratch files. They can come
along or be left behind; they do not affect what the profile looks like.

## Still open, and not fixable in this repo

- **Contact channel.** `README.md` ends with a generic "reach out here on
  GitHub" and an HTML comment marking the decision. The account has no public
  email and `hireable` is off.
- **The account's own bio, company and location fields.** Those render above
  the README on the profile page and are set in Settings, not here.
- **Pinned repositories.** Chosen by hand on the profile page. The default
  ordering is by stars.
