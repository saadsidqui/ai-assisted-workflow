---
name: lesson-writing
description: Write or revise a French lesson in lessons/ from its module card, with slides and full speaker notes for a presenter who is new to teaching. Use when drafting a lesson, adding or reworking a unit, writing or fixing speaker notes, or checking a lesson against its card. Not for building decks or textbooks (publish), editing the specification, or a typography-only check (canadian-french).
---

# Lesson writing

Turns one module card into one French lesson. A novice presenter who speaks slowly can deliver it, and a learner can study it from the textbook.

## Inputs

- **The module ID.** Its row in `.ai/project/spec/module-map.md` gives the card path and the lesson path.
- **The card**, its track page, and the conventions in the curriculum index.
- **The template and the design:** `templates/lesson.md`, and `DESIGN.md` sections 4.2 (slide types, word limits), 7 (voice, speaker notes), 8 (pedagogical patterns) and 9 (French typography).
- **The glossary:** `resources/R-02-glossary.md`. Until it exists, use the candidates in the spec's R-02 card and mark each as unconfirmed.
- **The running example:** `resources/fictional-engagement.md`. If it does not exist yet, stop and ask before inventing one (OD-11).

## Procedure

1. **Locate.** Read the module-map row, the card and, if it exists, the current lesson. Read [card-to-lesson.md](references/card-to-lesson.md).
2. **Plan, and show the plan before writing a new lesson.**
   - List the card's outcomes and required topics.
   - Plan one unit per idea, and map every required topic to a unit.
   - Take the minutes from decision 0017: for a core module, the card's Time line plus its S-01 checkpoint row; otherwise the card's Time line. Budget the notes at about 110 words per planned minute of talk, which means the minutes minus the checkpoint and practice rows, where the room does the talking.
   - Count about one slide per two minutes of talk.
3. **Write in template order:** front matter, short learner introduction, section slide, Objectifs, Déroulement, units, Point de contrôle, Pratique, Récapitulatif, Pour aller plus loin, À revérifier avant chaque prestation.
4. **Units.** Each unit runs:
   1. learner text giving the concrete example;
   2. an `example` slide;
   3. learner text that names the idea;
   4. a `concept` slide.

   Use the running example wherever it fits. Follow [pedagogy.md](references/pedagogy.md).
5. **Speaker notes.** Every slide region gets a notes block. Follow [speaker-notes.md](references/speaker-notes.md).
6. **Checkpoint.** Use the card's question word for word, the protocol in `DESIGN.md` section 8, and a transition written out in full.
7. **Practice.** Use the card's practice, on synthetic material, with its minutes and its expected result.
8. **Pour aller plus loin.** The card's recommended and optional topics go here as reference text, with links to further reading. They are not taught in the session.
9. **À revérifier.** The card's re-verify list, plus every product name or version used in the lesson, each with the date it was checked.
10. **Language.** Write in French from the start; never translate an English draft sentence by sentence. Then run the `canadian-french` check and the `slop-check` text pass on the lesson.
11. **Clean up.** Delete every `GUIDE` comment and keep the slide markers. Set `status` (`draft`, or `review` when you hand the lesson over), `native_review: pending` and the `glossary` list.
12. **Check and report**, using the acceptance check below.

## Rules that are easy to miss

- **Card only.** Teach what the card says. A topic that is not in the card goes to the author as a question, not into the lesson.
- **Sources.** No invented facts, statistics, quotations, testimonials or sources. A claim that needs a source either gets one you opened or comes out.
- **Product names** appear only where the card's topics need them. Versions and dated behaviour appear only in the re-verify list.
- **Examples** and practice material are fictional and organization-neutral.
- **Slides show, notes tell.** The notes add to the slide and never read it aloud.
- **Titles.** The lesson title and the slide headings carry no module ID. The ID lives in the front matter and in the stop map.

## Acceptance check

Report each line as pass or fail, with evidence:

- [ ] Every outcome of the card is in Objectifs, and every required topic is taught in a unit.
- [ ] Each unit has an example before its concept, and each slide holds one idea. Slide types and word limits follow `DESIGN.md` section 4.2.
- [ ] Every slide region has a `###` heading and a notes block that starts with a timing mark.
- [ ] The spoken words in all notes blocks are within 15 % of 110 × the talk minutes (`minutes` minus the checkpoint and practice rows). Stage directions in brackets are not counted. Report the count.
- [ ] The timing table adds up to `minutes`, the checkpoint has its own row, and the timing marks in the notes add up to the same total.
- [ ] The checkpoint uses the card's question, with the written transition and the protocol.
- [ ] Recommended and optional topics appear only in "Pour aller plus loin".
- [ ] No version numbers outside the re-verify list, and no invented facts.
- [ ] The `canadian-french` and `slop-check` results are reported.
- [ ] No `GUIDE` comment is left, and the front matter is complete.

When `tools/check_lesson.py` exists, run it for the counts and the slide-region checks above.
