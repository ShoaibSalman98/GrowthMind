import streamlit as st

st.set_page_config(page_title="Growth MindSet by Shoaib Salman")
st.title("Growth Mindset AI project of Q3")

st.header(" 🤾🏼‍♂️  Wellcome the Growth Mindset Setup Page  🏆")
st.write('"GrowthMind" is a powerful app designed to help you develop a growth mindset and achieve your full potential. With daily motivational insights, goal-setting tools, and progress tracking, it empowers you to embrace challenges, learn from failures, and cultivate resilience. Start your journey towards personal and professional growth today! 🚀')

# Quote Section.
st.header(" 💡 Growth Mindset Quote")
st.write( '"Success is not an accident; it’s a result of continuous learning, perseverance, and a growth mindset." — Carol S. Dweck🌱🚀 ')  


st.header("🛠️ Today how you challenge yourself ❓")
user_input= st.text_input("Explain the challenge you face in your life")

#condition

if user_input:
    st.success(f" ✍️ You Said: {user_input}. Keep continue your efforts to do your best 🚩")
else:
    st.warning("Please enter a challenge to start your growth mindset journey.")
    
    
    # Reflection Section.
    st.header("Reflect Your Learning 📖")
    reflection= st.text_area("Write your Reflection")
    
    if reflection:
        st.success(f" ���️ Reflection: {reflection}. You've been learning a lot today! ��")
    else:
        st.info("Please enter your reflection to reflect on your learning.")
        
# Acheivements. 
st.header(" 🕺 Celebrate your Acheivements 🏅") 
acheivements= st.text_input(" 📢 Share your recent Achievements")

if acheivements:
    st.success(f"�� Achievement ,🚀: {acheivements}. You're doing great! ��")
else:
    st.info(" 📝 Please enter your achievements to celebrate your progress.")
    
# Progress Tracking.

st.header("�� Track Your Progress ��")
progress= st.slider("How many days have passed?", min_value=0, max_value=30)

if progress >= 30:
    st.success("Congratulations! You've reached your goal of 30 days of growth mindset.")
    
# Footer.
st.write("- - - ")
st.write(" 🎯 Keep Beliving Yourself. Growth is a journey not a destination 🚩 ")
st.write("® **Created BY Shoaib Salman **")
    
    
    
    
