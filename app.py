import streamlit as st
st.title("Our First Streamlit App")
st.header("Exploring different texts")
st.subheader("Even more examples")
st.text("Different ways")
st.write("Hello World")
st.markdown("""
            ### This is mardown heading
            We could use mardown to create
            -**Bold** and *Italic*
            - lists
            - links like [streamlit docs](https://docs.streamlit.io)
            - code blocks:
            ```python
            import streamlit as st
            
            st.write ("Hey there!")
            ```
            
            """)

st.markdown("""
|Header 1|header 2|header 3|
|--------|--------|--------|
|r1, c1|r1, c2|r1|c3
|r2, c1|r2, c2|r2|c3
            
            """)