# 0012. Program title and French names of its parts

- Date: 2026-11-10
- Status: accepted
- Supersedes: none

## Context

The README, the program map, the decks and the textbooks need names that readers see: a title for the hub, and French names for the common core, the three tracks and the overlays. The specification names these parts in English only.

## Decision

1. **Title.** English: "Working with AI", subtitle "Training and coaching hub". French: « Travailler avec l’IA », subtitle « Formation et accompagnement ».
2. **French names of the parts:**

| English (specification) | French |
|---|---|
| Common core | Tronc commun |
| Engineering track | Parcours Génie logiciel |
| Product and experience track | Parcours Produit et expérience |
| Business and people track | Parcours Gestion et affaires |
| Overlays | Modules transversaux |

"Génie logiciel" is the preferred term for software engineering in the Grand dictionnaire terminologique (https://vitrinelinguistique.oqlf.gouv.qc.ca/fiche-gdt/fiche/8373430/genie-logiciel, checked on 2026-11-10).

## Consequences

- Every French deliverable uses these names.
- The glossary (R-02) lists them when it is built.
- File and directory names keep the English track identifiers: `engineering`, `product-experience`, `business-people`.
