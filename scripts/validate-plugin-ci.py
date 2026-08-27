import json
from pathlib import Path
r=Path(__file__).resolve().parents[1];d=json.loads((r/'.codex-plugin/plugin.json').read_text(encoding='utf-8'));need={'name','version','description','author','homepage','repository','license','keywords','interface','mcpServers'};missing=sorted(need-d.keys())
if missing:raise SystemExit(f'missing: {missing}')
if d['mcpServers']!='./.mcp.json':raise SystemExit('bad mcpServers')
print(json.dumps({'ok':True,'plugin':d['name']}))
