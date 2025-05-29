
import duckdb
from .base import StorageBackend
import os

class DuckDBStorage(StorageBackend):
    def __init__(self, db_path="data/articles.duckdb"):
        os.makedirs(os.path.dirname(db_path), exist_ok=True)
        self.conn = duckdb.connect(db_path)

        self.conn.execute("""
            CREATE TABLE IF NOT EXISTS articles (
                pmcid TEXT PRIMARY KEY,
                title TEXT,
                journal TEXT,
                abstract TEXT,
                authors TEXT
            )
        """)

        self.conn.execute("""
            CREATE TABLE IF NOT EXISTS figures (
                pmcid TEXT,
                figure_label TEXT,
                figure_caption TEXT,
                figure_image_url TEXT,
                figure_key_entities TEXT
            )
        """)

    def save(self, data: dict):
        self.conn.execute("""
            INSERT OR REPLACE INTO articles
            (pmcid, title, journal, abstract, authors)
            VALUES (?, ?, ?, ?, ?)
        """, (
            data["pmcid"],
            data.get("title"),
            data.get("journal"),
            data.get("abstract"),
            ", ".join(data.get("authors", []))
        ))

        self.conn.execute("DELETE FROM figures WHERE pmcid = ?", (data["pmcid"],))

        for fig in data.get("figures", []):
            self.conn.execute("""
                INSERT INTO figures
                (pmcid, figure_label, figure_caption, figure_image_url, figure_key_entities)
                VALUES (?, ?, ?, ?, ?)
            """, (
                data["pmcid"],
                fig.get("label", ""),
                fig.get("caption", ""),
                fig.get("image_url", ""),
                ", ".join([ent.get("text", "") for ent in fig.get("key_entities", [])])
            ))

    def query_all(self) -> list:
        return self.conn.execute("""
            SELECT 
                a.pmcid,
                a.title,
                a.abstract,
                f.figure_label,
                f.figure_caption,
                f.figure_image_url,
                f.figure_key_entities
            FROM articles a
            LEFT JOIN figures f ON a.pmcid = f.pmcid
        """).fetchall()

    def clear(self):
        self.conn.execute("DELETE FROM figures")
        self.conn.execute("DELETE FROM articles")
