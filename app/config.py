from pathlib import Path
import tempfile
import traceback
import json
import sys
import os


try:
    port = int(os.environ.get("PORT", "8080"))
except Exception as e:
    print(e)
    port = -1
if not 1 <= port <= 65535:
    print(
        "Please make sure the PORT environment variable is an integer between 1 and 65535"
    )
    sys.exit(1)

try:
    api_id = 4106161
    api_hash = "bf05f7a4f0a6ac3bc75afb4c89c44be6"
except (KeyError, ValueError):
    traceback.print_exc()
    print("\n\nPlease set the API_ID and API_HASH environment variables correctly")
    print("You can get your own API keys at https://my.telegram.org/apps")
    sys.exit(1)

try:
    index_settings_str = """{
  "index_all": true,
  "index_private": false,
  "index_group": false,
  "index_channel": true,
  "exclude_chats": [],
  "include_chats": []
}""".strip()
    
    index_settings = json.loads(index_settings_str)
except Exception:
    traceback.print_exc()
    print("\n\nPlease set the INDEX_SETTINGS environment variable correctly")
    sys.exit(1)

try:
    session_string = "1AZWarzgBu7qodE-dSdkZL4x7uAW7H9BVz26BuWHRSvtf6zOiZgZMoaW6RDN3TVfAcBahPe5Bt5nGxMHLWWGZOdIogCtSgCNe4-lvwypHAVUYCTYzIoDwIoDUbDlDtiNPwzf-pW0OADdG76yp70MoQrvCRZRT7uJnG-wI6-QFqwbCS0W8NsxQNYJYBFQpB4y9Qt18Zf0xH6OvMwy4_7l2uQYavrFSDACQpIHYlQoyPiQRGN8X15h4QYTHxRfzgdBv3-NXa-K87rV_11mk8vKjebkhErpzUEL3hY-lrhOXR_Zb64GRbPj7_ATKS21rYsnytlwG8lOqNruTgxez8OZbpCLcT26jGwY="
except (KeyError, ValueError):
    traceback.print_exc()
    print("\n\nPlease set the SESSION_STRING environment variable correctly")
    sys.exit(1)

host = os.environ.get("HOST", "0.0.0.0")
debug = bool(os.environ.get("DEBUG"))
block_downloads = bool(os.environ.get("BLOCK_DOWNLOADS"))
results_per_page = int(os.environ.get("RESULTS_PER_PAGE", "20"))
logo_folder = Path(os.path.join(tempfile.gettempdir(), "logo"))
logo_folder.mkdir(parents=True, exist_ok=True)
username = os.environ.get("TGINDEX_USERNAME", "")
password = os.environ.get("PASSWORD", "")
SHORT_URL_LEN = int(os.environ.get("SHORT_URL_LEN", 3))
authenticated = bool(username and password)
SESSION_COOKIE_LIFETIME = int(os.environ.get("SESSION_COOKIE_LIFETIME") or "60")
try:
    SECRET_KEY = os.environ["SECRET_KEY"]
    if len(SECRET_KEY) != 32:
        raise ValueError("SECRET_KEY should be exactly 32 charaters long")
except (KeyError, ValueError):
    if authenticated:
        traceback.print_exc()
        print("\n\nPlease set the SECRET_KEY environment variable correctly")
        sys.exit(1)
    else:
        SECRET_KEY = ""

SHORT_URL = False