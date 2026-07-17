import sqlite3

DB_NAME = "data.db"


def get_connection():
    return sqlite3.connect(DB_NAME)


def create_tables():
    conn = get_connection()
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
            hint TEXT
        )
    """)

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
        VALUES (?,?,?,?,?,?,?)
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

    return [x[0] for x in rows]


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
