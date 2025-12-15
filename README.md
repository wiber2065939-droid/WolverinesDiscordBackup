# Wolverines Official - Discord Archive

A static Discord archive viewer for preserving and browsing historical channel data.

## Quick Start

1. Open `index.html` in a browser (for local use, you may need to serve it - see below)
2. Click on channels in the sidebar to view archived messages

## Updating with New Exports

### Step 1: Export from DiscordChatExporter
Export channels as JSON. Files will be named like:
```
Wolverines Official - Stock Market - stock-talk [940999329613754429].json
```

### Step 2: Strip the Channel IDs
Run the rename script to remove the ID numbers:

**Python (cross-platform):**
```bash
python rename_exports.py /path/to/exports/
```

This renames files to:
```
Wolverines Official - Stock Market - stock-talk.json
```

### Step 3: Copy to data/ folder
Move the renamed JSON files into the `data/` folder, overwriting placeholders.

### Step 4: Upload to GitHub
Push the updated files to your repository.

## File Naming Convention

Files follow the DiscordChatExporter format (minus the channel ID):
```
ServerName - CategoryName - channel-name.json
```

Examples:
- `Wolverines Official - Stock Market - stock-talk.json`
- `Wolverines Official - Family-Council - leadership-council-info.json`
- `Wolverines Official - TW War Hub - tw-primary-displays.json`

## Hosting on GitHub Pages

1. Create a new repository on GitHub
2. Upload all files (index.html, data folder, scripts)
3. Go to Settings → Pages
4. Select "Deploy from a branch" → main → / (root)
5. Your archive will be live at `https://username.github.io/repo-name/`

## Running Locally

Due to browser security (CORS), you can't just double-click the HTML file. Use one of these methods:

**Python 3:**
```bash
cd discord-archive
python -m http.server 8000
# Open http://localhost:8000
```

**Node.js:**
```bash
npx serve
```

**VS Code:**
Use the "Live Server" extension

## File Structure

```
discord-archive/
├── index.html              # Main application
├── README.md               # This file
├── rename_exports.py       # Python script to strip IDs from exports
└── data/                   # Channel JSON exports
    ├── Wolverines Official - Stock Market - stock-talk.json
    ├── Wolverines Official - Stock Market - stock-bot-readme.json
    └── ...
```

## Features

- Discord-like dark theme
- Collapsible categories
- Message search (searches current channel)
- Renders avatars, nicknames, role colours
- Displays attachments (images inline, files as links)
- Shows bot embeds
- Displays reactions
- Date dividers
- Formats code blocks, bold, italic, links

## Adding New Channels

If Discord adds new channels, you'll need to:

1. Export the channel from DiscordChatExporter
2. Run the rename script
3. Add an entry to `serverConfig.categories` in `index.html`:

```javascript
{ name: "new-channel", file: "data/Wolverines Official - CategoryName - new-channel.json" },
```

## Limitations

- Read-only (no posting/reacting)
- Images may expire if Discord CDN links become invalid
- No thread support (yet)
- Search is per-channel only

## Stats

- 22 categories
- 180 channels
- Files with actual data will show message counts when loaded
