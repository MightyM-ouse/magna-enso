# HTML Viewer Validation

Status: **HUMAN_REVIEW_PENDING**

Automated static checks verify 25 focused views, local viewer/SVG/Draw.io paths, no runtime network dependencies, JavaScript syntax/logic checks, search/filter/zoom implementation, and responsive CSS breakpoints. In a standalone extracted ZIP, all viewer artifact links resolve. The 26 source-Markdown links are separately classified as requiring the accepted sibling package and are visibly labelled; they are not claimed to resolve standalone.

Browser validation is intentionally not claimed. Human review must still test:

- Browser console on load and after interactions.
- Every diagram selection and focused-view link.
- Search by diagram ID, component ID, and component name.
- Each filter alone and representative combined filters.
- Zoom out, fit, zoom in, dense-diagram scrolling, and reset behavior.
- Desktop layout, 1100 px breakpoint, and mobile layout at/below 720 px.
- Keyboard focus/activation and readable labels at practical zoom levels.
- Source-link behavior both without and with the accepted sibling package.
