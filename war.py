
import streamlit as st

# Fighter Plane Class
class FighterPlane:
    def __init__(self, name, speed, altitude, attack_message, landing_message, image_url):
        self.name = name
        self.speed = speed
        self.altitude = altitude
        self.attack_message = attack_message
        self.landing_message = landing_message
        self.image_url = image_url

    def fly(self):
        return f"🛫 {self.name} is flying at {self.altitude} feet with speed {self.speed} km/h."

    def attack(self):
        return self.attack_message

    def land(self):
        return self.landing_message

# Aircraft objects
f16 = FighterPlane(
    "F-16 Falcon",
    1500,
    35000,
    "🚀 F-16 Falcon is launching a missile attack on Indian Air Base!",
    "🛬 F-16 Falcon is landing safely at Mushif Air Base.",
    "https://upload.wikimedia.org/wikipedia/commons/thumb/3/3e/F-16_June_2008.jpg/640px-F-16_June_2008.jpg"
)

jf17 = FighterPlane(
    "JF-17 Thunder",
    1200,
    30000,
    "🚀 JF-17 Thunder is targeting the Indian Radar Station and destroyed!",
    "🛬 JF-17 Thunder returned back successfully to PAF Base M.M.Alam Mianwali.",
    "https://upload.wikimedia.org/wikipedia/commons/7/72/Pakistan_Air_Force_JF-17_Thunder.jpg"
)

j10c = FighterPlane(
    "J-10C Vigorous Dragon",
    1700,
    45000,
    "🚀 J-10C is engaging in a high-speed intercept mission destruction of Rafale!",
    "🛬 J-10C Mission completed successfully landed at Minhas Air Base.",
    "https://upload.wikimedia.org/wikipedia/commons/8/8e/Chengdu_J-10B.jpg"
)

# Mapping aircraft names to objects
aircrafts = {
    "F-16 Falcon": f16,
    "JF-17 Thunder": jf17,
    "J-10C Vigorous Dragon": j10c
}

# Page title and styling
st.markdown("<h1 style='color:purple; font-size: 45px;'>🛩️ F-16 | JF-17 | J-10C Combat</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='font-size: 24px; color:green'>Welcome to the Fighter Jet War Room! Select an aircraft and command it in action.</h3>", unsafe_allow_html=True)

# Aircraft selection
selected_name = st.selectbox("Choose Your Aircraft", list(aircrafts.keys()), index=0)
selected_plane = aircrafts[selected_name]

# Show aircraft image
st.image(selected_plane.image_url, caption=selected_plane.name, use_container_width=True)

# Action buttons
col1, col2, col3 = st.columns(3)

with col1:
    if st.button("✈️ Fly", use_container_width=True):
        st.markdown(f"<h3 style='color:green;'>{selected_plane.fly()}</h3>", unsafe_allow_html=True)

with col2:
    if st.button("🚀 Attack", use_container_width=True):
        st.markdown(f"<h3 style='color:orange;'>{selected_plane.attack()}</h3>", unsafe_allow_html=True)

with col3:
    if st.button("🛬 Land", use_container_width=True):
        st.markdown(f"<h3 style='color:blue;'>{selected_plane.land()}</h3>", unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown("<h4 style='text-align:center;'>Designed with ❤️ using Streamlit | Developed by Muhammad Tariq Mahboob</h4>", unsafe_allow_html=True)