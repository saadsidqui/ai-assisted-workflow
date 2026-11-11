# From card to lesson

Where each part of a module card goes in the lesson built from `templates/lesson.md`.

| Card field | Lesson part | How |
|---|---|---|
| Header: Who | Front matter `track`, and the audience the examples address | Track value from `module-map.md` |
| Header: Delivery | Nothing on the page; it decides which deck the slides join | See `module-map.md` |
| Header: Time | Front matter `minutes` and the timing table total | Core: the card's figure plus the S-01 checkpoint row; other modules: the card's figure (decision 0017) |
| Rationale paragraph | Learner introduction under the title | Rewritten in French, in one or two sentences |
| Outcomes | Objectifs | One item per outcome, in the same order; each continues « vous serez en mesure » |
| Required topics | One unit per idea (example slide, then concept slide) | Every bullet is covered; closely linked bullets may share a unit |
| Recommended topics | Pour aller plus loin | Reference text; not taught in the session |
| Optional topics | Pour aller plus loin, after the recommended ones | One line each, with a link where one exists |
| Checkpoint | Point de contrôle | The question as written, with the protocol and a transition |
| Practice | Pratique | Same task, on synthetic material, with minutes and expected result |
| Presenter notes | Speaker notes of the slides they concern | Turned into things to say or stage directions, never pasted as a list |
| Re-verify before each delivery | À revérifier avant chaque prestation | Same items, each with the date it was last checked |
| Read more | Pour aller plus loin | Links to the matching section of R-01 and its sources |

Session and track context:

- **Core modules.** S-01 gives the segment, the 90-minute version and what to cut. Write the matching « Si vous êtes en retard » markers.
- **Track modules.** The track page gives the session the module belongs to and its practice slot.
- **Overlays.** The lesson must work inside any of the sessions listed in `module-map.md`.
