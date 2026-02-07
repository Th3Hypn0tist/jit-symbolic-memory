# store.py
import sqlite3
from typing import Optional, List, Dict, Any

DB_PATH = "records.db"

def _conn():
    return sqlite3.connect(DB_PATH)

def init_db():
    with _conn() as c:
        c.execute("""
        CREATE TABLE IF NOT EXISTS records (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            key TEXT UNIQUE NOT NULL,
            value TEXT NOT NULL,
            meta TEXT DEFAULT '',
            updated_at TEXT DEFAULT (datetime('now'))
        );
        """)
        c.commit()

def add_record(key: str, value: str, meta: str = "") -> Dict[str, Any]:
    with _conn() as c:
        c.execute(
            "INSERT INTO records(key,value,meta,updated_at) VALUES(?,?,?,datetime('now'))",
            (key, value, meta),
        )
        c.commit()
        return {"key": key, "value": value, "meta": meta}

def get_record(key: str) -> Optional[Dict[str, Any]]:
    with _conn() as c:
        row = c.execute(
            "SELECT key,value,meta,updated_at FROM records WHERE key=?",
            (key,),
        ).fetchone()
        if not row:
            return None
        return {"key": row[0], "value": row[1], "meta": row[2], "updated_at": row[3]}

def update_record(key: str, value: Optional[str] = None, meta: Optional[str] = None) -> Optional[Dict[str, Any]]:
    cur = get_record(key)
    if not cur:
        return None
    new_value = value if value is not None else cur["value"]
    new_meta = meta if meta is not None else cur["meta"]
    with _conn() as c:
        c.execute(
            "UPDATE records SET value=?, meta=?, updated_at=datetime('now') WHERE key=?",
            (new_value, new_meta, key),
        )
        c.commit()
    return get_record(key)

def list_records(limit: int = 50) -> List[Dict[str, Any]]:
    with _conn() as c:
        rows = c.execute(
            "SELECT key,value,meta,updated_at FROM records ORDER BY updated_at DESC LIMIT ?",
            (limit,),
        ).fetchall()
        return [{"key": r[0], "value": r[1], "meta": r[2], "updated_at": r[3]} for r in rows]
