
import streamlit as st

# Function for collecting user information
def collect_user_info():
    st.title("فرم ثبت اطلاعات تغذیه‌ای")
    
    # Personal Information Section
    st.header("بخش 1: اطلاعات فردی")
    name = st.text_input("نام کامل")
    age = st.number_input("سن", min_value=0)
    gender = st.selectbox("جنسیت", ["مرد", "زن"])
    marital_status = st.selectbox("وضعیت تأهل", ["مجرد", "متأهل"])
    
    # Anthropometric Data Section
    st.header("بخش 2: اطلاعات آنتروپومتریک")
    weight = st.number_input("وزن (kg)", min_value=0)
    height = st.number_input("قد (cm)", min_value=0)
    waist = st.number_input("دور کمر (cm)", min_value=0)
    hip = st.number_input("دور باسن (cm)", min_value=0)
    
    # Medical History Section
    st.header("بخش 3: سابقه پزشکی و دارویی")
    medical_conditions = st.text_area("بیماری‌های فعلی یا گذشته (اگر دارید)")
    medications = st.text_area("داروهای مصرفی (اگر دارید)")
    
    # Lifestyle Section
    st.header("بخش 4: سبک زندگی")
    activity_level = st.selectbox("سطح فعالیت بدنی", ["نشسته", "فعال", "بسیار فعال"])
    sleep_hours = st.number_input("میانگین ساعت خواب شبانه", min_value=0)
    
    # Goals and Preferences Section
    st.header("بخش 5: اهداف و ترجیحات غذایی")
    diet_type = st.selectbox("نوع رژیم غذایی", ["وگان", "کم چرب", "پر پروتئین", "ویژه"])
    goal = st.text_input("هدف شما از رژیم غذایی")
    
    # Health Issues Section
    st.header("بخش 6: وضعیت گوارشی")
    digestive_issues = st.text_area("مشکلات گوارشی (اگر دارید)")
    
    # Calculation of Calories and Macronutrients
    st.header("بخش 7: محاسبه کالری و درشت مغذی‌ها")
    calories = 10 * weight + 6.25 * height - 5 * age
    if gender == "مرد":
        calories += 5
    else:
        calories -= 161
    
    st.write(f"کالری مورد نیاز شما: {calories:.2f} کیلوکالری در روز")
    
    # Saving the data
    if st.button("ارسال اطلاعات"):
        st.success(f"اطلاعات شما با موفقیت ثبت شد. نام: {name}, سن: {age}, جنسیت: {gender}, وضعیت تأهل: {marital_status}")
        # Here you can add code to send data to an email or save it in a database

# Run the app
if __name__ == "__main__":
    collect_user_info()
