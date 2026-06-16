import streamlit as st

USERS = {

    # Admin Account
    "admin": "admin123",

    # Recruiter Account
    "recruiter": "recruit123",

    # Demo Account
    "demo": "demo123",

    # Portfolio Demo
    "varun_demo": "varun123"
}


def login():

    st.sidebar.title("🔐 Login")

    st.sidebar.info(
        """
Demo Credentials

Username: demo
Password: demo123
        """
    )

    username = st.sidebar.text_input(
        "Username"
    )

    password = st.sidebar.text_input(
        "Password",
        type="password"
    )

    login_btn = st.sidebar.button(
        "Login"
    )

    if login_btn:

        if (
            username in USERS
            and
            USERS[username] == password
        ):

            st.session_state[
                "authenticated"
            ] = True

            st.session_state[
                "username"
            ] = username

            st.success(
                f"Welcome {username}"
            )

            st.rerun()

        else:

            st.error(
                "Invalid Credentials"
            )


def logout():

    st.sidebar.markdown("---")

    st.sidebar.write(
        f"Logged in as: "
        f"{st.session_state.get('username', 'Unknown')}"
    )

    if st.sidebar.button(
        "Logout"
    ):

        st.session_state.clear()

        st.rerun()


def is_authenticated():

    return st.session_state.get(
        "authenticated",
        False
    )