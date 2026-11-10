# C-01 · Mental model and vocabulary

- **Where it sits:** Common core
- **Who:** Everyone: required
- **Delivery:** Core session, segment 1
- **Time:** 12 min

People misuse a tool they picture wrongly. Most first-time users treat an assistant as a search engine, a database, or a colleague who already knows the project. One accurate picture prevents most early mistakes.

## Outcomes

A participant can:

- Say in one sentence what a language model does.
- Tell apart a model, an application, a tool and an agent.
- Explain why a fluent answer can still be wrong.

## Topics

### Required

- Generative AI in one picture: a model trained on a very large amount of text produces a plausible continuation. Plausible is often true, and sometimes not.
- Four words that get mixed up: the **model** (the engine), the **application** (the product around it, such as a chat app or an IDE extension), a **tool** (something the application lets the model use: search, files, code execution), an **agent** (a model working in a loop with tools toward a goal).
- What the assistant knows: its training data up to a cutoff date, what is in the conversation, and what its tools fetch. It knows nothing about your project until you show it.
- The context window as working memory: it is finite, and everything the model considers has to fit in it. Tokens are the unit that both the limit and the bill are counted in.
- Wrong answers sound exactly like right ones. A confident tone carries no information.
- The same question can get different answers on two tries. That is normal behaviour.
- Input and output are no longer text only: images, files, audio, screens.

### Recommended

- Thinking effort is a setting: models can spend more or less effort on a task, and more is not always better.
- Using a model does not teach it. Whether your data is used for training is a product and plan setting (see [C-07](C-07-data-security-and-responsible-use.md)).
- Search and retrieval as "fetch first, then answer": why an answer with sources is checkable and one from memory is not.
- Same model, different products: behaviour depends on the application, the plan and the settings.

### Optional

- Embeddings and vector search.
- Fine-tuning versus prompting versus retrieval.
- Open-weight and local models.
- Benchmarks and why they predict your results poorly.
- Sampling and temperature.

## Checkpoint

> Name one thing the assistant cannot know about your current project unless you give it.

## Practice

Sort six cards (a chat app, an IDE extension, a model name, web search, a coding agent, a file upload) into model, application, tool or agent.

## Presenter notes

- Use one analogy and state where it breaks. "A very well-read new colleague who remembers nothing from yesterday" works; stacking three analogies does not.
- No mathematics and no architecture diagrams. If someone asks how transformers work, park it and point to the optional reading.
- Say "I don't know, I'll check" at least once on purpose. It models the behaviour the session teaches.

## Re-verify before each delivery

- Product and model names used as examples.
- What "memory" features do in each product.

## Read more

[Foundations](../resources/R-01-further-reading.md#foundations).

---

[Curriculum index](../README.md) · [C-02 Landscape snapshot](C-02-landscape-snapshot.md) →
