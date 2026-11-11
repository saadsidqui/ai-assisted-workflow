# Vendor pages

How the vendor pages behind the landscape snapshot (C-02) respond to automated reading. Useful for each refresh of its re-verify list.

- 2026-11-11: openai.com pages (ChatGPT overview, Codex page) return HTTP 403 to automated reads, including with a generic browser user agent. help.openai.com also returned 403 to a web-fetch tool; it was not retried with a browser user agent. Source: observed.
- 2026-11-11: OpenAI's product documentation for ChatGPT and Codex is at learn.chatgpt.com. developers.openai.com/codex redirects there. Its pages load with a generic browser user agent, and appending `.md` to a page URL returns a Markdown version; the index is `https://learn.chatgpt.com/llms.txt`. Source: observed.
- 2026-11-11: the Microsoft 365 Copilot product page on microsoft.com timed out; the Microsoft Learn pages for Copilot load. Source: observed.
- 2026-11-11: Microsoft's documentation states that "The Microsoft 365 Copilot app is now called Microsoft Copilot". Source: https://learn.microsoft.com/en-us/copilot/microsoft-365/copilot-overview
- 2026-11-11: the Zoom AI assistant product page presents the assistant as "ZoomMate". Source: https://www.zoom.com/en/products/ai-assistant/
- 2026-11-11: the Perplexity FAQ at `/hub/faq` returns 404; the help centre article "How does Perplexity work" loads. Source: observed.
