#!/usr/bin/env python3
"""
╔══════════════════════════════════════════════════════════╗
║       🎭  TEAM MYSTERIOUS - File Hosting Bot  🎭        ║
║       Force Join + Menu + File Hosting                  ║
║       Owner: SCARY 👻  |  Developer: LILXGOD ⚡         ║
╚══════════════════════════════════════════════════════════╝
"""

import sys
import os
import subprocess
import importlib.util
from pathlib import Path

# ═══════════════════════════════════════════════════════════
#  🎯  SETUP ZONE — SIRF YAHAN VALUES BHARO
# ═══════════════════════════════════════════════════════════
#
#  1️⃣  BOT_TOKEN      →  @BotFather se lo
#  2️⃣  OWNER_ID       →  @userinfobot se lo (apni Telegram ID)
#  3️⃣  CHANNEL_USERNAME →  apna channel @username (force join)
#  4️⃣  ADMIN_IDS      →  extra admins ki IDs (comma se separate)
#  5️⃣  PORT           →  HTTP server port (default 8080)
#  6️⃣  BASE_URL       →  public URL (blank = localhost)
#
# ───────────────────────────────────────────────────────────

BOT_TOKEN = os.getenv("BOT_TOKEN", "").strip()
OWNER_ID = int(os.getenv("OWNER_ID", "0") or 0)
CHANNEL_USERNAME = os.getenv("CHANNEL_USERNAME", "").strip()
ADMIN_IDS = [int(x.strip()) for x in os.getenv("ADMIN_IDS", "").split(",") if x.strip().isdigit()]
PORT = int(os.getenv("PORT", "8080") or 8080)
BASE_URL = os.getenv("BASE_URL", "").strip()