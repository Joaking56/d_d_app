import psycopg2
import streamlit as st

DB_URL = st.secrets["DB_URL"]


def init_connection():
    return psycopg2.connect(DB_URL)


def init_db():
    conn = init_connection()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS guests (
            id SERIAL PRIMARY KEY,
            first_name TEXT NOT NULL,
            second_name TEXT NOT NULL,
            guests INTEGER NOT NULL
        )
    """)
    conn.commit()
    cursor.close()
    conn.close()


def add_guest(first_name, second_name, guests):
    conn = init_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO guests (first_name, second_name, guests) VALUES (%s, %s, %s)",
        (first_name, second_name, guests)
    )
    conn.commit()
    cursor.close()
    conn.close()


def get_all_guests():
    conn = init_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, first_name, second_name, guests FROM guests")
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    return rows