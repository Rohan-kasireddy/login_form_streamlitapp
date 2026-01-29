import streamlit as st
#header of app
st.header("student records")
#title of app
st.title("student management system")
#subheader of app
st.subheader("manage student data easily")
#markdown
st.markdown("------------------------------------------------------------------------------------")
#text
st.text("this app helps you to manage student records efficiently")
#write
st.write("hii")
st.write(123)
st.write(12.34)
st.write(["apple","banana","cherry"])
st.write([1,2])
#markdown 
st.markdown("**bold text**")
st.markdown("*italic text*")
st.markdown("- item1\n- item2")
st.markdown("<h3 style='color:blue'>This is a blue heading</h3>", unsafe_allow_html=True)
#caption
st.caption("this is a caption for student management system app")
#code 
st.code("print('hello world')")
st.code("""
def hello():
    print("Hello, World!")
""", language='python')
#latex
st.latex(r"E=mc^2")
st.latex(r"""
         a^2 + b^2 = c^2""")
#divider ---to separate sections
st.divider()
if st.button("click me"):
    st.write("button clicked!")
    st.success("operation successful")
    st.balloons()
else:
    st.write("button not clicked yet")
name=st.text_input("enter your name")
if name=="":
    st.warning("name cannot be empty")
elif not name.isalpha():
    st.error("name should contain only alphabets")
else:
    st.success(f"welcome, {name}!")
#text area
feedback=st.text_area("enter your feedback")
st.write("your feedback:", feedback)
#checkbox
if st.checkbox("subscribe to newsletter"):
    st.write("subscribed!")
#radio buttons
gender=st.radio("select your gender",["male","female","other"])
st.write("you selected:", gender)
#selectbox
course=st.selectbox("select your course",["math","science","history"])
st.write("you selected:", course)
#multiselect
hobbies=st.multiselect("select your hobbies",["reading","sports","music","traveling"])
st.write("you selected:", hobbies)
#slider
age=st.slider("select your age",0,100,25)
st.write("your age is:", age)
#file uploader
uploaded_file=st.file_uploader("upload your profile picture",type=["png","jpg","jpeg"])
if uploaded_file is not None:
    st.success("file uploaded successfully")
    st.write("file name:", uploaded_file.name)
#form
with st.form("student_form"):
    student_name=st.text_input("student name")
    student_age=st.number_input("student age",min_value=0,max_value=120)
    submitted=st.form_submit_button("submit")
    if submitted:
        st.write("student name:", student_name)
        st.write("student age:", student_age)
#form submit button->method to create a submit button within a form context
with st.form("login"):
    username=st.text_input("username")
    password=st.text_input("password",type="password")
    login_submitted=st.form_submit_button("login")
    if login_submitted:
        st.success("login successful ")
st.divider()
#columns
col1, col2, col3 = st.columns(3)
with col1:
    st.header("Column 1")
    st.write("This is column 1")
with col2:
    st.header("Column 2")
    st.write("This is column 2")
with col3:
    st.header("Column 3")
    st.write("This is column 3")
st.divider()
#container
container=st.container()
container.write("this is inside a container")
container.button("click")
#table method to display data in tabular format
data = {
    'Name': ['Anurag', 'Sumit', 'Rohit'],
    'Age': [21, 22, 20],
    'Course': ['B.Tech', 'M.Tech', 'BBA']
}
st.table(data)
#sidebar
st.sidebar.title("menu")
option=st.sidebar.selectbox("select an option",["home","about","contact"])
st.sidebar.write("you selected:", option)
#cache data
@st.cache_data
def load_data():
    return  [1, 2, 3, 4, 5]
data=load_data()
st.write(data)