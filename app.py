import streamlit as st
from input_module import get_customer_details
from intent_module import detect_intent
from retrieval_module import retrieve_similar_email
from reply_module import generate_reply
from tone_module import improve_tone
from summary_module import summarize_conversation
from save_module import save_reply


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="IntelliMail AI",
    page_icon="✉",
    layout="wide",
    initial_sidebar_state="expanded"
)


# ============================================================
# CUSTOM CSS
# ============================================================

st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

* {
    font-family: 'Inter', sans-serif;
}

.stApp {
    background:
        radial-gradient(circle at 10% 10%, rgba(99,102,241,0.13), transparent 25%),
        radial-gradient(circle at 90% 20%, rgba(139,92,246,0.10), transparent 25%),
        #f8fafc;
}

/* Remove Streamlit top padding */
.block-container {
    padding-top: 2rem;
    padding-bottom: 3rem;
    max-width: 1450px;
}

/* Sidebar */
section[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #111827 0%, #1e1b4b 100%);
}

section[data-testid="stSidebar"] * {
    color: white !important;
}

.sidebar-logo {
    font-size: 25px;
    font-weight: 800;
    padding: 10px 0 30px 5px;
}

.sidebar-item {
    padding: 12px 14px;
    border-radius: 10px;
    margin-bottom: 6px;
    background: rgba(255,255,255,0.06);
    font-size: 14px;
}

.sidebar-status {
    margin-top: 35px;
    padding: 14px;
    border-radius: 12px;
    background: rgba(34,197,94,0.12);
    border: 1px solid rgba(34,197,94,0.25);
    font-size: 13px;
}

/* Header */
.hero {
    padding: 5px 0 25px 0;
}

.hero-title {
    font-size: 42px;
    font-weight: 800;
    letter-spacing: -1.5px;
    color: #111827;
    margin-bottom: 5px;
}

.hero-title span {
    background: linear-gradient(90deg, #4f46e5, #7c3aed);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

.hero-subtitle {
    color: #64748b;
    font-size: 16px;
}

/* Status badge */
.status-badge {
    display: inline-block;
    padding: 7px 13px;
    border-radius: 30px;
    background: #ecfdf5;
    color: #047857;
    border: 1px solid #a7f3d0;
    font-size: 12px;
    font-weight: 600;
}

/* Cards */
.card {
    background: rgba(255,255,255,0.92);
    border: 1px solid #e2e8f0;
    border-radius: 18px;
    padding: 24px;
    box-shadow: 0 8px 30px rgba(15,23,42,0.06);
    margin-bottom: 18px;
}

.card-title {
    font-size: 19px;
    font-weight: 700;
    color: #111827;
    margin-bottom: 5px;
}

.card-subtitle {
    color: #64748b;
    font-size: 13px;
    margin-bottom: 18px;
}

/* Section headers */
.section-header {
    font-size: 24px;
    font-weight: 800;
    color: #111827;
    margin: 35px 0 15px 0;
}

/* Intent */
.intent-card {
    background: linear-gradient(135deg, #eef2ff, #f5f3ff);
    border: 1px solid #c7d2fe;
    border-radius: 16px;
    padding: 20px;
    text-align: center;
}

.intent-label {
    color: #6366f1;
    font-size: 12px;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 1px;
}

.intent-value {
    color: #312e81;
    font-size: 24px;
    font-weight: 800;
    margin-top: 7px;
}

/* Metric cards */
.metric-card {
    background: white;
    border: 1px solid #e2e8f0;
    border-radius: 15px;
    padding: 18px;
    text-align: center;
    box-shadow: 0 5px 20px rgba(15,23,42,0.04);
}

.metric-number {
    font-size: 26px;
    font-weight: 800;
    color: #4f46e5;
}

.metric-label {
    color: #64748b;
    font-size: 12px;
    margin-top: 3px;
}

/* AI response */
.ai-response {
    background: linear-gradient(135deg, #111827, #312e81);
    color: white;
    border-radius: 18px;
    padding: 25px;
    box-shadow: 0 12px 35px rgba(49,46,129,0.18);
}

.ai-response-title {
    font-size: 16px;
    font-weight: 700;
    margin-bottom: 15px;
}

.ai-response-text {
    font-size: 14px;
    line-height: 1.8;
    white-space: pre-wrap;
}

/* Summary */
.summary-card {
    background: #f8fafc;
    border-left: 4px solid #6366f1;
    padding: 18px;
    border-radius: 10px;
    color: #334155;
    line-height: 1.7;
}

/* Buttons */
.stButton > button {
    border-radius: 10px;
    font-weight: 700;
    min-height: 45px;
}

div[data-testid="stFormSubmitButton"] button {
    background: linear-gradient(90deg, #4f46e5, #7c3aed);
    color: white;
    border: none;
}

/* Input fields */
.stTextInput input,
.stTextArea textarea {
    border-radius: 10px !important;
    border: 1px solid #cbd5e1 !important;
    background: white !important;
}

/* Footer */
.footer {
    text-align: center;
    color: #94a3b8;
    font-size: 12px;
    margin-top: 50px;
    padding-top: 20px;
    border-top: 1px solid #e2e8f0;
}

</style>
""", unsafe_allow_html=True)


# ============================================================
# SIDEBAR
# ============================================================

with st.sidebar:

    st.markdown(
        '<div class="sidebar-logo">✦ IntelliMail AI</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="sidebar-item">▣ Email Workspace</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="sidebar-item">◉ Intent Intelligence</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="sidebar-item">✧ AI Response Studio</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="sidebar-item">▤ Conversation Insights</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="sidebar-item">◈ Saved Responses</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div class="sidebar-status">
            <b>● AI Engine Online</b><br><br>
            Ollama<br>
            Llama 3.2<br>
            Local AI Processing
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div style="margin-top:30px;font-size:12px;color:#94a3b8;">
        Intelligent Email Assistant<br>
        AI-powered customer communication
        </div>
        """,
        unsafe_allow_html=True
    )


# ============================================================
# HERO HEADER
# ============================================================

st.markdown(
    """
    <div class="hero">
        <div class="hero-title">
            Intelligent Email <span>Assistant</span>
        </div>
        <div class="hero-subtitle">
            Transform customer emails into intelligent, professional responses with AI.
        </div>
        <br>
        <span class="status-badge">● Ollama AI Engine Connected</span>
    </div>
    """,
    unsafe_allow_html=True
)


# ============================================================
# EMAIL COMPOSER
# ============================================================

st.markdown(
    '<div class="section-header">Customer Email Workspace</div>',
    unsafe_allow_html=True
)

left, right = st.columns([1, 1.45], gap="large")


with left:

    st.markdown(
        """
        <div class="card">
            <div class="card-title">Customer Information</div>
            <div class="card-subtitle">
                Enter the details received from the customer.
            </div>
        """,
        unsafe_allow_html=True
    )

    customer_name = st.text_input(
        "Customer Name",
        placeholder="e.g. Priya"
    )

    email_subject = st.text_input(
        "Email Subject",
        placeholder="e.g. Refund Request for Order"
    )

    st.markdown("</div>", unsafe_allow_html=True)


with right:

    st.markdown(
        """
        <div class="card">
            <div class="card-title">Customer Message</div>
            <div class="card-subtitle">
                Paste the customer's email message below.
            </div>
        """,
        unsafe_allow_html=True
    )

    customer_email = st.text_area(
        "Customer Email",
        placeholder="Type or paste the customer email here...",
        height=155,
        label_visibility="collapsed"
    )

    st.markdown("</div>", unsafe_allow_html=True)


process = st.button(
    "Analyze Email & Generate Response",
    type="primary",
    use_container_width=True
)


# ============================================================
# PROCESSING
# ============================================================

if process:

    if not customer_name or not email_subject or not customer_email:

        st.warning(
            "Please complete the customer name, subject and email message."
        )

    else:

        # ----------------------------------------------------
        # INTENT
        # ----------------------------------------------------

        with st.spinner("AI is analyzing customer intent..."):
            intent = detect_intent(customer_email)

        st.markdown(
            '<div class="section-header">AI Email Analysis</div>',
            unsafe_allow_html=True
        )

        intent_col, score_col, engine_col = st.columns(3)

        with intent_col:
            st.markdown(
                f"""
                <div class="intent-card">
                    <div class="intent-label">Detected Intent</div>
                    <div class="intent-value">{intent}</div>
                </div>
                """,
                unsafe_allow_html=True
            )

        # ----------------------------------------------------
        # SIMILAR EMAIL
        # ----------------------------------------------------

        with st.spinner("Searching previous customer conversations..."):
            similar_email, score = retrieve_similar_email(customer_email)

        with score_col:
            st.markdown(
                f"""
                <div class="metric-card">
                    <div class="metric-number">{round(score, 2)}</div>
                    <div class="metric-label">SIMILARITY SCORE</div>
                </div>
                """,
                unsafe_allow_html=True
            )

        with engine_col:
            st.markdown(
                """
                <div class="metric-card">
                    <div class="metric-number">AI</div>
                    <div class="metric-label">LLAMA 3.2 ENGINE</div>
                </div>
                """,
                unsafe_allow_html=True
            )


        # ----------------------------------------------------
        # SIMILAR EMAIL CARD
        # ----------------------------------------------------

        st.markdown(
            """
            <div class="card">
                <div class="card-title">Similar Customer Conversation</div>
                <div class="card-subtitle">
                    Retrieved using TF-IDF and cosine similarity.
                </div>
            """,
            unsafe_allow_html=True
        )

        sim1, sim2 = st.columns(2)

        with sim1:
            st.write("**Customer**")
            st.write(similar_email["Customer Name"])

            st.write("**Subject**")
            st.write(similar_email["Email Subject"])

        with sim2:
            st.write("**Previous Intent**")
            st.write(similar_email["Intent"])

            st.write("**Previous Email**")
            st.write(similar_email["Customer Email"])

        st.markdown("</div>", unsafe_allow_html=True)


        # ----------------------------------------------------
        # AI REPLY
        # ----------------------------------------------------

        with st.spinner("Generating intelligent customer response..."):
            reply = generate_reply(
                customer_name,
                customer_email,
                intent
            )

        st.markdown(
            '<div class="section-header">AI Response Studio</div>',
            unsafe_allow_html=True
        )

        st.markdown(
            """
            <div class="ai-response">
                <div class="ai-response-title">
                    ✦ AI Generated Response
                </div>
            """,
            unsafe_allow_html=True
        )

        st.markdown(
            f'<div class="ai-response-text">{reply}</div>',
            unsafe_allow_html=True
        )

        st.markdown("</div>", unsafe_allow_html=True)


        # ----------------------------------------------------
        # TONE IMPROVEMENT
        # ----------------------------------------------------

        with st.spinner("Improving response tone and empathy..."):
            improved_reply = improve_tone(reply)

        st.markdown(
            '<div class="section-header">Tone Improvement</div>',
            unsafe_allow_html=True
        )

        tone_left, tone_right = st.columns(2, gap="large")

        with tone_left:

            st.markdown(
                """
                <div class="card">
                    <div class="card-title">Original AI Reply</div>
                    <div class="card-subtitle">
                        Initial response generated by Llama 3.2
                    </div>
                """,
                unsafe_allow_html=True
            )

            st.write(reply)

            st.markdown("</div>", unsafe_allow_html=True)


        with tone_right:

            st.markdown(
                """
                <div class="card">
                    <div class="card-title">Refined Professional Reply</div>
                    <div class="card-subtitle">
                        Improved for clarity, empathy and professionalism
                    </div>
                """,
                unsafe_allow_html=True
            )

            st.write(improved_reply)

            st.markdown("</div>", unsafe_allow_html=True)


        # ----------------------------------------------------
        # SUMMARY
        # ----------------------------------------------------

        with st.spinner("Generating conversation summary..."):
            summary = summarize_conversation(
                customer_email,
                improved_reply
            )

        st.markdown(
            '<div class="section-header">Conversation Intelligence</div>',
            unsafe_allow_html=True
        )

        st.markdown(
            f"""
            <div class="summary-card">
                <b>Conversation Summary</b><br><br>
                {summary}
            </div>
            """,
            unsafe_allow_html=True
        )


        # ----------------------------------------------------
        # SAVE
        # ----------------------------------------------------

        st.markdown(
            '<div class="section-header">Response Management</div>',
            unsafe_allow_html=True
        )

        filename = save_reply(
            customer_name,
            customer_email,
            intent,
            improved_reply,
            summary
        )

        save_col1, save_col2 = st.columns([3, 1])

        with save_col1:
            st.success(
                f"Response successfully saved as {filename}"
            )

        with save_col2:
            st.download_button(
                label="Download Reply",
                data=improved_reply,
                file_name="customer_reply.txt",
                mime="text/plain",
                use_container_width=True
            )


# ============================================================
# FOOTER
# ============================================================

st.markdown(
    """
    <div class="footer">
        IntelliMail AI · Intelligent Email Assistant ·
        Powered by Ollama & Llama 3.2
    </div>
    """,
    unsafe_allow_html=True
)