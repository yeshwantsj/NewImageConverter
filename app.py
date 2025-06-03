import streamlit as st
import streamlit.components.v1 as components
import base64

st.set_page_config(layout="wide")

# Load and encode resume PDF
with open("Resume.PDF", "rb") as pdf_file:
    pdf_data = base64.b64encode(pdf_file.read()).decode()

# Load and encode local profile image
with open("2.jpeg", "rb") as image_file:
    image_data = base64.b64encode(image_file.read()).decode()
    image_base64 = f"data:image/jpeg;base64,{image_data}"

# HTML content including profile and chatbot
html_code = f"""
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <title>Yeshwant S. Jadhav</title>
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <style>
    body {{
      margin: 0;
      font-family: Arial, sans-serif;
      background-color: #f4f4f4;
    }}
    .chat-icon {{
      position: fixed;
      bottom: 20px;
      right: 20px;
      background-color: white;
      border-radius: 50%;
      padding: 10px;
      box-shadow: 0 4px 12px rgba(0, 0, 0, 0.2);
      z-index: 10000;
      cursor: pointer;
      animation: pulse 2s infinite;
    }}
    .chatbot-widget {{
      position: fixed;
      bottom: 90px;
      right: 20px;
      width: 300px;
      background-color: white;
      font-family: Arial, sans-serif;
      z-index: 9999;
      display: none;
      border-radius: 10px;
      overflow: hidden;
      box-shadow: 0 0 12px rgba(0, 0, 0, 0.2);
    }}
    .chat-header {{
      background-color: #4E342E;
      color: white;
      padding: 10px;
      font-weight: bold;
    }}
    .chat-body {{
      max-height: 300px;
      overflow-y: auto;
      padding: 10px;
    }}
    .chat-controls {{
      padding: 10px;
      border-top: 1px solid #ccc;
    }}
    .chat-container {{
      display: flex;
      flex-direction: column;
    }}
    .bot-message {{
      background-color: #EEE;
      padding: 8px;
      margin: 5px 0;
      border-radius: 5px;
      align-self: flex-start;
    }}
    .user-message {{
      background-color: #DCF8C6;
      padding: 8px;
      margin: 5px 0;
      border-radius: 5px;
      align-self: flex-end;
    }}
  </style>
</head>
<body>

<div style="background-color: #FFDD44; min-height: 100vh; display: flex; flex-direction: column; justify-content: center; align-items: center; padding: 20px;">
  <div style="background: #4E342E; padding: 40px; border-radius: 15px; max-width: 800px; width: 100%; box-shadow: 0 4px 15px rgba(0, 0, 0, 0.2);">
    <div style="display: flex; flex-wrap: wrap; justify-content: center; align-items: center;">
      <img src="{image_base64}" alt="Profile Photo" style="width: 180px; height: 180px; border-radius: 50%; object-fit: cover; margin-right: 30px; box-shadow: 0 4px 10px rgba(0, 0, 0, 0.3);">
      <div style="flex: 1; max-width: 600px; padding: 10px; color: #FFF;">
        <h1 style="margin: 0; font-size: 32px;">Yeshwant Shankar Jadhav</h1>
        <h3 style="margin: 5px 0 15px; font-size: 24px;">Procurement Specialist</h3>
        <p style="margin-bottom: 15px; font-size: 18px;">
          Hello! I’m a passionate Procurement Specialist with 9+ years of experience driving cost-effective sourcing 
          and building strong supplier relationships.
        </p>
        <p style="font-size: 16px;"><strong>Email:</strong> Yeshwantsjadhav@gmail.com</p>
        <p style="font-size: 16px;"><strong>Phone:</strong> +91-7709917611</p>
        <p style="font-size: 16px;"><strong>Location:</strong> Ulhasnagar, Thane, Maharashtra</p>
        <a href="data:application/pdf;base64,{pdf_data}" download="Resume.PDF" style="display: inline-block; margin-top: 20px; padding: 12px 25px; background-color: #3E2723; color: #FFDD44; text-decoration: none; border-radius: 5px; font-size: 16px; font-weight: bold;">Download Resume</a>
      </div>
    </div>
  </div>
</div>

<!-- Floating Chat Icon -->
<div id="chatIcon" class="chat-icon" onclick="toggleChat(true)">
  <img src="https://cdn-icons-png.flaticon.com/512/4712/4712027.png" alt="Chatbot" width="50">
</div>

<!-- Chatbot Widget -->
<div class="chatbot-widget" id="chatWidget">
  <div class="chat-header">
    <span>Chat with Me</span>
    <button onclick="toggleChat(false)" style="float:right; background:none; border:none; font-size:16px; cursor:pointer;">×</button>
  </div>
  <div class="chat-body" id="chatBody">
    <div class="chat-container" id="chatContainer">
      <div class="bot-message">Hi! Ask me anything about my profile.</div>
    </div>
    <div class="chat-controls">
      <select id="question" onchange="handleUserSelection()">
        <option value="">--Select a question--</option>
        <option value="whyHire">Why should we hire you?</option>
        <option value="strengths">What are your strengths?</option>
        <option value="experience">Tell me about your experience.</option>
        <option value="projects">Describe a project you've worked on.</option>
        <option value="weakness">What is your biggest weakness?</option>
        <option value="teamwork">How do you work in a team?</option>
        <option value="challenge">Describe a challenging situation you faced.</option>
        <option value="future">Where do you see yourself in 5 years?</option>
        <option value="whyCompany">Why do you want to join our company?</option>
        <option value="skills">What technical skills do you have?</option>
        <option value="achievement">What’s your biggest professional achievement?</option>
      </select>
    </div>
  </div>
</div>

<script>
  function toggleChat(show) {{
    document.getElementById('chatWidget').style.display = show ? 'block' : 'none';
  }}

  function handleUserSelection() {{
    const question = document.getElementById('question').value;
    const container = document.getElementById('chatContainer');

    if (!question) return;

    const userMsg = document.createElement('div');
    userMsg.className = 'user-message';
    userMsg.textContent = document.querySelector(`#question option[value="${{question}}"]`).textContent;
    container.appendChild(userMsg);

    const botMsg = document.createElement('div');
    botMsg.className = 'bot-message';

    const responses = {{
      whyHire: "With 9+ years of experience in procurement, I specialize in cost optimization, strategic sourcing, and building strong supplier relationships. I’ve successfully streamlined procurement processes, reduced costs, and always look for innovative ways to add value. My experience and adaptability ensure I can help your team achieve its procurement goals efficiently.",
      strengths: "My strengths include strong negotiation skills, a keen eye for cost-saving opportunities, and building lasting supplier relationships. I’m analytical, detail-oriented, and adaptable, always looking to improve procurement processes and embrace new technologies.",
      experience: "I have 9+ years of experience in procurement, managing supplier relationships, optimizing costs, and streamlining procurement processes. I’ve successfully negotiated contracts, reduced expenses, and implemented strategies to improve efficiency and value for the organizations I’ve worked with.",
      projects: "I have worked on several high-value projects, including one at Writer Corporation, where I managed procurement for a project worth around 95 crores. Additionally, I handled a project at Wintech to build a factory, which had a budget of approximately 10 crores. In both projects, I was responsible for sourcing materials, negotiating contracts, and ensuring cost efficiency throughout the procurement process.",
      weakness: "Sometimes I overanalyze details, but I’m working on balancing perfection with speed.",
      teamwork: "I believe in clear communication, mutual respect, and leveraging each team member’s strengths. I am collaborative and always open to feedback to achieve team goals effectively.",
      challenge: "In one project, supplier delays threatened the timeline. I proactively sourced alternate vendors and renegotiated delivery schedules, ensuring the project stayed on track without compromising quality.",
      future: "In 5 years, I see myself leading a procurement team in a dynamic organization, leveraging technology and data analytics to drive strategic sourcing and cost efficiencies.",
      whyCompany: "I admire your company’s commitment to innovation and quality. I want to contribute my procurement expertise to help support your growth and efficiency goals.",
      skills: "I am skilled in supplier management, contract negotiation, procurement software like SAP Ariba, and data-driven decision-making.",
      achievement: "Successfully renegotiated a supplier contract saving 15% annually, and led procurement for a major project with a budget of over 100 crores, completing it under budget and on time."
    }};

    botMsg.textContent = responses[question] || "I am not sure about that, please ask something else.";
    container.appendChild(botMsg);

    // Scroll chat to bottom
    const chatBody = document.getElementById('chatBody');
    chatBody.scrollTop = chatBody.scrollHeight;

    // Reset select
    document.getElementById('question').value = "";
  }}
</script>

</body>
</html>
"""

# Render HTML in Streamlit
components.html(html_code, height=600, scrolling=False)
