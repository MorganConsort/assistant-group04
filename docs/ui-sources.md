# Source Display Design

This document defines how the Study Assistant will show supporting sources directly below each answer. The examples are UI mockups; source metadata will be supplied by the backend when the interactive Streamlit page is implemented.

## Design rules

- Place sources immediately below the answer they support.
- Number sources in the order they are referenced: `[1]`, `[2]`, and so on.
- Show a short source title and a specific record or section.
- Keep the source area visually secondary to the answer.
- Use the visible heading `Sources` so screen-reader and keyboard users can find it.
- Do not invent a citation when the backend provides no source metadata.

## Example 1: One source

**Question**

> Where is the Computational Thinking theory class?

**Answer**

> It is at room I.11B on every Thursday. [1]

**Sources**

1. **Computational Thinking Course Schedule** — theory class location and weekly timetable.

```text
+----------------------------------------------------------+
|                                             You [U]      |
|       Where is the Computational Thinking theory class?  |
|                                                          |
| [A] Assistant                                            |
|     It is at room I.11B on every Thursday. [1]           |
|                                                          |
|     Sources                                              |
|     [1] Computational Thinking Course Schedule           |
|         Theory class location and weekly timetable       |
+----------------------------------------------------------+
```

## Example 2: Multiple sources

**Question**

> When are the Training Office and Student Affairs open?

**Answer**

> The Training Office is open Monday-Friday, 07:30-16:30 [1]. Student Affairs is open Monday-Friday, 08:00-16:00 [2].

**Sources**

1. **University Office Directory** — `data/offices.csv`, Training Office record.
2. **University Office Directory** — `data/offices.csv`, Student Affairs record.

```text
+----------------------------------------------------------+
|                                             You [U]      |
|   When are Training Office and Student Affairs open?     |
|                                                          |
| [A] Assistant                                            |
|     Training Office: Mon-Fri, 07:30-16:30 [1].           |
|     Student Affairs: Mon-Fri, 08:00-16:00 [2].           |
|                                                          |
|     Sources                                              |
|     [1] University Office Directory - Training Office    |
|     [2] University Office Directory - Student Affairs    |
+----------------------------------------------------------+
```

## Planned data flow

1. The UI sends the user's question to the backend.
2. The backend returns the answer together with source metadata.
3. The UI renders the answer first.
4. The UI renders the associated sources immediately below that answer.

The UI should not inspect `data/offices.csv` itself. Reading data and selecting sources remain backend responsibilities.

## Accessibility

- Use a heading for each source section rather than relying on color alone.
- Use numbered lists so citations have a clear reading order.
- Give links descriptive text instead of labels such as "click here."
- Preserve sufficient color contrast and visible keyboard focus.
- Indicate when an external link opens in a new browser tab.
