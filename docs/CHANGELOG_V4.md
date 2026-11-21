# KINETIC v4 — live deployment and widget reliability

- Rebuilt Welcome with native Streamlit columns and a self-contained animated
  SVG asset. No nested `<svg>` inside `st.markdown()`; content stays legible
  if an SVG animation is unsupported.
- Uses `st.html(CSS)` for direct style insertion.
- Expanded `.streamlit/config.toml` to set native dark green controls, borders,
  and light/dark override palettes.
- Added more resilient CSS for BaseWeb select menus, dropdown popovers,
  text areas, text fields, numeric and date widgets, including selected options.
- Kept navigation, the three-area menu, synthetic data and scoring behaviour.
- Added guard tests to prevent returning to fragile SVG-in-Markdown design.
- Local preview screenshots cannot guarantee a hosted app matches exactly;
  deployment needs a browser test on its actual URL.
