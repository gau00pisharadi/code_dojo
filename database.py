import sqlite3
import ast

DB_NAME = "data.db"


def get_connection():
    return sqlite3.connect(DB_NAME)


def create_tables():
    conn = get_connection()
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS problems (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            topic TEXT NOT NULL,
            difficulty TEXT NOT NULL,
            description TEXT NOT NULL,
            starter_code TEXT,
            solution TEXT NOT NULL,
            hint TEXT,
            solved INTEGER NOT NULL DEFAULT 0
        )
    """)

    cur.execute("PRAGMA table_info(problems)")
    columns = [row["name"] for row in cur.fetchall()]

    if "solved" not in columns:
        cur.execute(
            "ALTER TABLE problems ADD COLUMN solved INTEGER NOT NULL DEFAULT 0"
        )

    conn.commit()
    conn.close()


def add_problem(
    title,
    topic,
    difficulty,
    description,
    starter_code,
    solution,
    hint,
):
    conn = get_connection()
    cur = conn.cursor()

    # Prevent duplicate imports
    cur.execute(
        """
        SELECT id
        FROM problems
        WHERE title = ?
        """,
        (title,),
    )

    if cur.fetchone() is not None:
        conn.close()
        return False

    cur.execute(
        """
        INSERT INTO problems
        (
            title,
            topic,
            difficulty,
            description,
            starter_code,
            solution,
            hint
        )
        VALUES (?, ?, ?, ?, ?, ?, ?)
        """,
        (
            title,
            topic,
            difficulty,
            description,
            starter_code,
            solution,
            hint,
        ),
    )

    conn.commit()
    conn.close()

    return True


def update_problem(
    problem_id,
    title,
    topic,
    difficulty,
    description,
    starter_code,
    solution,
    hint,
):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        """
        UPDATE problems
        SET
            title=?,
            topic=?,
            difficulty=?,
            description=?,
            starter_code=?,
            solution=?,
            hint=?
        WHERE id=?
        """,
        (
            title,
            topic,
            difficulty,
            description,
            starter_code,
            solution,
            hint,
            problem_id,
        ),
    )

    conn.commit()
    conn.close()


def update_problem_status(problem_id, solved):
    conn = get_connection()

    conn.execute(
        """
        UPDATE problems
        SET solved=?
        WHERE id=?
        """,
        (int(solved), problem_id),
    )

    conn.commit()
    conn.close()


def delete_problem(problem_id):
    conn = get_connection()

    conn.execute(
        "DELETE FROM problems WHERE id=?",
        (problem_id,),
    )

    conn.commit()
    conn.close()


def get_all_problems():
    conn = get_connection()
    conn.row_factory = sqlite3.Row

    rows = conn.execute(
        """
        SELECT *
        FROM problems
        ORDER BY id
        """
    ).fetchall()

    conn.close()

    return rows


def get_problem(problem_id):
    conn = get_connection()
    conn.row_factory = sqlite3.Row

    row = conn.execute(
        """
        SELECT *
        FROM problems
        WHERE id=?
        """,
        (problem_id,),
    ).fetchone()

    conn.close()

    return row


def search_problems(search_text="", topic="All", difficulty="All"):
    conn = get_connection()
    conn.row_factory = sqlite3.Row

    query = """
        SELECT *
        FROM problems
        WHERE title LIKE ?
    """

    params = [f"%{search_text}%"]

    if topic != "All":
        query += " AND topic=?"
        params.append(topic)

    if difficulty != "All":
        query += " AND difficulty=?"
        params.append(difficulty)

    query += " ORDER BY id"

    rows = conn.execute(query, params).fetchall()

    conn.close()

    return rows


def get_topics():
    conn = get_connection()

    rows = conn.execute(
        """
        SELECT DISTINCT topic
        FROM problems
        ORDER BY topic
        """
    ).fetchall()

    conn.close()

    return [row[0] for row in rows]


def get_counts():
    conn = get_connection()

    total = conn.execute(
        "SELECT COUNT(*) FROM problems"
    ).fetchone()[0]

    easy = conn.execute(
        "SELECT COUNT(*) FROM problems WHERE difficulty='Easy'"
    ).fetchone()[0]

    medium = conn.execute(
        "SELECT COUNT(*) FROM problems WHERE difficulty='Medium'"
    ).fetchone()[0]

    hard = conn.execute(
        "SELECT COUNT(*) FROM problems WHERE difficulty='Hard'"
    ).fetchone()[0]

    conn.close()

    return total, easy, medium, hard


def get_solved_count():
    conn = get_connection()

    solved = conn.execute(
        """
        SELECT COUNT(*)
        FROM problems
        WHERE solved=1
        """
    ).fetchone()[0]

    conn.close()

    return solved


def normalize_code(code):
    """
    Compare code using Python's AST so formatting differences
    (spacing, blank lines, etc.) are ignored.
    """
    try:
        return ast.dump(ast.parse(code))
    except SyntaxError:
        return None

def clear_problems():
    conn = get_connection()

    conn.execute("DELETE FROM problems")

    conn.commit()
    conn.close()
