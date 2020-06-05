def change(st):
    return "".join("1" if char in st.lower() else "0" for char in "abcdefghijklmnopqrstuvwxyz")
