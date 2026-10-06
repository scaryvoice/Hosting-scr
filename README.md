# TEAM MYSTERIOUS — Railway-ready Telegram File Hosting Bot

## Files
- `scaryhost1.py` — bot + HTTP file server
- `requirements.txt` — compatible Python dependencies
- `Procfile` — Railway start command
- `railway.toml` — Railway deploy configuration
- `.env.example` — variables template
- `.gitignore` — keeps secrets and hosted files out of Git

## Railway Variables
Set these in Railway → Service → Variables:
- `BOT_TOKEN`
- `OWNER_ID`
- `CHANNEL_USERNAME`
- `ADMIN_IDS` (optional)
- `BASE_URL` (optional)

Important: do NOT put the real bot token in GitHub.

## Railway deploy
1. Push all files to the GitHub repository.
2. Railway → Deploy from GitHub Repo → select the repository.
3. Add the Variables above.
4. Deploy/redeploy.
5. For direct file links, generate a public Railway domain. If `BASE_URL` is blank, the bot uses `https://RAILWAY_PUBLIC_DOMAIN` automatically when available.

## Local / Termux
```bash
python -m pip install -r requirements.txt
export BOT_TOKEN="YOUR_TOKEN"
export OWNER_ID="YOUR_ID"
export CHANNEL_USERNAME="@teamxmysterious"
python scaryhost1.py
```

Windows PowerShell:
```powershell
py -m pip install -r requirements.txt
$env:BOT_TOKEN="YOUR_TOKEN"
$env:OWNER_ID="YOUR_ID"
$env:CHANNEL_USERNAME="@teamxmysterious"
py scaryhost1.py
```
