# User Interface (UI) Plan

## Current scope

The Lab 2 UI is a static placeholder for the future Study Assistant chat page. A working Streamlit interface will be implemented in a later lab.

The placeholder demonstrates:

- A heading describing the application.
- A text input for the user's question.
- A Send button.
- An area where the assistant's response will appear.
- Accessible labels for interactive elements.

Open `ui/index.html` in a web browser to view the placeholder.

## Planned user flow

1. The user enters a study-related question.
2. The UI sends the question to the backend.
3. The backend processes the question.
4. The backend returns a text response.
5. The UI displays the response in the conversation area.

## Backend integration

The UI will use the existing backend function in `src/assistant/rules.py`:

```python
from assistant.rules import reply

answer = reply(user_message)
```

The UI must call `reply()` instead of reading the CSV data directly. This keeps presentation logic in the UI and response logic in the backend.

A future Streamlit implementation could use:

```python
import streamlit as st

from assistant.rules import reply

st.title("Study Assistant")

user_message = st.chat_input("Ask a study-related question")

if user_message:
    with st.chat_message("user"):
        st.write(user_message)

    with st.chat_message("assistant"):
        st.write(reply(user_message))
```

## Files

- `ui/index.html` — current static placeholder page.
- `ui/README.md` — UI architecture and integration plan.
- `docs/ui-chat-placeholder.md` — mockup and design notes.

## Future work

- Replace the static page with a Streamlit application.
- Add loading and error states.
- Add conversation history.
- Add automated tests for the interactive UI.