# Specification

What the program teaches, to whom, and how each deliverable is judged. The specification is in English. The deliverables built from it are in Canadian French.

## Contents

| File | What it holds |
|---|---|
| [`curriculum/`](curriculum/README.md) | The curriculum outline: 36 module cards with required, recommended and optional topics per role, the design of the common session and its workshop (S-01, S-02), and resources (R-01 to R-03). Start at its index |
| [`module-map.md`](module-map.md) | Every module ID with its card, its lesson path, its session deck and the textbooks that include it |
| [`deliverables.md`](deliverables.md) | Each type of deliverable: source, location, format, language and definition of done |
| [`build-order.md`](build-order.md) | The order in which deliverables are produced |
| [`open-decisions.md`](open-decisions.md) | Content and program decisions not yet taken, each with a proposal |
| [`suggestions.md`](suggestions.md) | A backlog of proposals. An item binds only when a card reflects it or the author accepts it in `open-decisions.md` |

## Reading a module card

A card has a header (where it sits, who, delivery, time), a short rationale, outcomes, topics sorted into three tiers, a checkpoint, and usually practice, presenter notes, a "re-verify before each delivery" list and further reading. The [curriculum index](curriculum/README.md) explains the tiers, the role tables and the conventions, including stable module IDs.

## Precedence inside the specification

- For a module's content, its card wins over its track page, and the track page wins over the curriculum index.
- For the program as a whole, the curriculum index and its conventions apply.
- Where the specification disagrees with a decision record or with `DESIGN.md`, the order in `AGENTS.md` applies, and the disagreement goes to the author.

## Origin and changes

The specification began as planning input in `.ai/project/seed/` and moved here during initialization. Seven sentences that referred to documents outside the repository were reworded so that each stands alone (decision 0009). One explanatory sentence was removed from suggestion D.5 (decision 0013). No other text of the planning input changed. The other files in this folder were added during initialization.

Once the stage is `build`, every file in this folder is locked. A change needs the author's approval (`AGENTS.md`, lifecycle and lock).
