# Study Assistant UI Mockup

This document records the proposed layout for the Study Assistant chat page.

## Mockup

```text
+----------------------------------------------------------+
| Study Assistant                                          |
| Ask questions about university offices and services.     |
+----------------------------------------------------------+
|                                                          |
|  Assistant: Hello! Ask me where an office is or when     |
|             it opens.                                    |
|                                                          |
|                                                          |
+----------------------------------------------------------+
| Your question                                            |
| +-------------------------------------------+  +--------+ |
| | Where is the Training Office?             |  | Send   | |
| +-------------------------------------------+  +--------+ |
+----------------------------------------------------------+
```

## Planned interaction

1. The user types a question into the text input.
2. The user selects the Send button.
3. The UI passes the question to `assistant.rules.reply()`.
4. The returned answer appears in the conversation area.

## Current limitation

The page in `ui/index.html` is a visual placeholder only. Its Send button is disabled because the working Streamlit interface will be implemented in a later lab.

## Accessibility notes

- The question field has a visible label.
- The conversation area uses `aria-live="polite"` for future responses.
- Text and controls use high-contrast colors.
- The layout adapts to narrow screens.
- Keyboard focus is clearly visible on the input field.