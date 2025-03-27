import streamlit as st
import re

def main():
  st.set_page_config(page_title="Text Analyzer",page_icon="🖹",layout="centered")
  
  st.markdown("""
              <style>
              .main{background-color:#ebecda;}
              .stTextArea, .stTextArea {border-redius: 10px}
              .stButtoon>button { background-color: blue; color:white;
              border-radi: 10px; padding: 10px}
              </style>
              """, unsafe_allow_html=True)
  st.title("text analyzer in python")
  st.write("analyzer your text quickly and efficiently.")
  
  paragraph = st.text_area("Enter a paragraph: ", "", height=150)
  
  if paragraph:
    st.markdown("---")
    st.subheader("Analysis Results")
    
    words = paragraph.split()
    word_count = len(words)
    chr_count = len(paragraph)
    col1, col2 = st.columns(2)
    col1.metric("Total words", word_count)
    col2.metric("Total Charactors", chr_count)
    
    #serch and replace 
    st.subheader("Search and Replace")
    search_word = st.text_input("Enter a word to search")
    replace_word = st.text_input("Enter a word to Replace with:")
    
    if search_word and replace_word:
      modified_paragraph = re.escape(rf'/b{re.escape(search_word)}/b', replace_word, paragraph)
      st.success("modified paragraph")
      st.info(modified_paragraph)
      
    #uppar and lower 
    st.subheader("Uppercase and Lowercase feature")
    st.text_area("UPPERCASE:",paragraph.upper(), height=150)
    st.text_area("Lowercase:",paragraph.lower(), height=150)
    
    ope_python ="python" in paragraph
    st.write(f" Coutain 'python' : {ope_python}")
    
    #averagr length of paragraph:
    average_word_length = chr_count / word_count if word_count else 0
    st.write(f"Average word Length:{average_word_length:2f}")
    
  else:
    st.warning("Please Enter a paragraph for analization")
    
if __name__ == "__main__":
    main()  
      
    
    
