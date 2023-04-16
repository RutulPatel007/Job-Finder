import streamlit as st
from PIL import Image, ImageDraw
from HOME import info


# Define a function to create job box
def create_job_box(job_name, company_name, salary, resume_match_percentage, skills_required):
    box_style = 'border:1px solid #ccc; border-radius:5px; padding:10px; margin-bottom:10px; position:relative; background-color:#f8f9fa;'
    box_html = f'''
        <div style="{box_style}">
            <h3 style="margin:0">{job_name}</h3>
            <p style="margin:0">{company_name}</p>
            <p style="margin:0">Salary: {salary} </p>
            <p style="margin:0">Skills Required: {', '.join(skills_required)}</p>
            <div style="display:flex; justify-content:space-between;">
                <button style="border:none; background-color:#007bff; color:white; padding:5px 10px; cursor:pointer;">Apply Now</button>
                <button style="border:none; background-color:#28a745; color:white; padding:5px 10px; cursor:pointer;">Prepare</button>
            </div>
            <div style="position:absolute; top:0; right:0; transform:translate(50%,-50%); width:30px; height:30px; display:flex; justify-content:center; align-items:center; font-size:14px;">
                <div style="background-color:#28a745; border-radius:50%; width:100%; height:100%; display:flex; justify-content:center; align-items:center; color:white;">
                    {resume_match_percentage}%
                </div>
                <div style="position:absolute; top:80%; left:200%; transform:translate(-50%,-50%); text-align:center;">
                    Resume Match
                </div>
            </div>
        </div>
    '''
    return box_html

# Create a Streamlit app
u=info()
st.title("results")

def app():
    st.title('Results')

    # Display job boxes
    for x in range(0, len(u[2])):
        st.markdown(create_job_box(u[0][x].text.strip(), u[1][x].text.strip(), u[2][x], 100, ['Python', 'Data Analysis', 'Machine Learning']), unsafe_allow_html=True)

# Run the Streamlit app
if __name__ == '__main__':
    app()
