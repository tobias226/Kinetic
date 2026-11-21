# KINETIC v4 deployment checklist (non-technical)

Use **the v4 ZIP**, not v2 or v3. Unzip it and upload the **contents** directly
into your existing GitHub repo. The repo root must contain `app.py`,
`requirements.txt`, the `assets` folder, the `core` folder and `.streamlit/config.toml`.
Do **not** put the files inside a `kinetic-v4` directory within the repo.

**Important on macOS:** Folders beginning with a dot can be hidden. In Finder,
press `Command + Shift + .` to reveal `.streamlit` before uploading. Alternatively
create a file in GitHub using **Add file → Create new file** and name it exactly
`.streamlit/config.toml` then paste the contents of that file from this package.

In Streamlit Community Cloud, your existing deployment will redeploy after the
GitHub change. Open the app, expand the sidebar, and choose **Check Display
Settings**. It should say *KINETIC dark-green theme is loaded*. If it instead
warns the theme is missing, check `.streamlit/config.toml` is in GitHub at the
same level as `app.py`.

For the animated landing image, check `assets/kinetic-network.svg` exists in the
repo. The page is built with native columns and `st.image` rather than SVG inside
a Markdown block. The image remains legible when animations are disabled.

If the old page still appears, check the selected branch and main app path
(`app.py`) in Community Cloud and reload. If there is a runtime error, use
**Manage app → Logs** to find the message. You can share the URL or the error
message to pinpoint an installation-specific cause.

All records remain fictional. Do not add actual investor, counterparty or
confidential contact information to a public app.
