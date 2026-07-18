import streamlit as st
import database_handling
import pandas_work


database_handling.init_db()
st.title("Dotti & Donát Esküvője")
st.subheader("Vendéglista Regisztráció")

with st.form("registration_form", clear_on_submit=True):
    first_name = st.text_input("Add meg a vezetékneved", key="f_name").capitalize().strip()
    second_name = st.text_input("Add meg a keresztneved", key="s_name").capitalize().strip()
    guests = st.selectbox(
        "Kérlek, jelöld be egyedül hányan jöttök:",
        options=[1, 2],
        index=0
    )

    submitted = st.form_submit_button("Regisztráció")

    if submitted:
        if first_name.strip() != "" and second_name.strip() != "":
            database_handling.add_guest(second_name, first_name, guests)
            st.success("Regisztráció sikeres!")
        else:
            st.error("Kérlek töltsd ki a név mezőt!")

df = pandas_work.create_df()
guest_count = pandas_work.summ_guests(df)
guests = df["first_name"] + " " + df["second_name"]
guest_list_html = "<br>".join(guests.tolist())


st.markdown(
    f"""
    <div style="text-align: center;">
        <h1>Idáig ennyien jeleztétek, hogy jöttök!</h1>
        <h1>{guest_count}</h1>
    </div>
    """,
    unsafe_allow_html=True
)


st.markdown(
    f"""
    <div style="text-align: center;">
        <h1>Résztvevők listája</h1>
        <h1>{guest_list_html}</h1>
    </div>
    """,
    unsafe_allow_html=True
)
