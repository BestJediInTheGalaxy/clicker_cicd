import streamlit as st
import threading
import time

if "total" not in st.session_state:
        st.session_state.total = 0
if "click" not in st.session_state:
        st.session_state.click = 1
if "double_click" not in st.session_state:
        st.session_state.double_click = False
if "triple_click" not in st.session_state:
        st.session_state.triple_click = False
if "passive1" not in st.session_state:
        st.session_state.passive1 = False
if "passive2" not in st.session_state:
        st.session_state.passive2 = False


total = "$" + str(st.session_state.total)
st.write(total)

def passive1():
        print("Thread started")
        st.session_state.total += 1
        time.sleep(0.5)
        print("Thread ok")
        st.rerun()

def passive2():
        st.session_state.total += 10
        time.sleep(0.5)
        st.rerun()

if st.button("CLICK", use_container_width=True):
        st.session_state.total += st.session_state.click
        st.rerun()

st.write("---")

col0, col1, col2, col3, col4 = st.columns([0.5, 1, 0.5, 1, 0.5])

with col1:
        if st.button("Double  click  income     $10", use_container_width=True, disabled=st.session_state.double_click) and st.session_state.total >= 10:
                st.session_state.double_click = True
                st.session_state.total -= 10
                st.session_state.click *= 2
                st.rerun()
        if st.button("Triple  click  income     $100", use_container_width=True, disabled=st.session_state.triple_click) and st.session_state.total >= 100:
                st.session_state.triple_click = True
                st.session_state.total -= 100
                st.session_state.click *= 3
                st.rerun()

with col3:
        if st.button("Create passive income $500", use_container_width=True, disabled=st.session_state.passive1) and st.session_state.total >= 500:
                st.session_state.passive1 = True
                st.session_state.total -= 500
                thread = threading.Thread(target=passive1, daemon=True)
                thread.start()
                st.rerun()
        if st.button("Improve passive income $1000", use_container_width=True, disabled=st.session_state.passive2) and st.session_state.total >= 1000:
                st.session_state.passive2 = True
                st.session_state.total -= 1000
                thread = threading.Thread(target=passive2, daemon=True)
                thread.start()
                st.rerun()
