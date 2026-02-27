import streamlit as st
import streamlit.components.v1 as components

# Page configuration
st.set_page_config(
    page_title="EduBright — Grammar & Math Academy",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ─────────────────────────── GLOBAL CSS ────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700;900&family=DM+Sans:wght@300;400;500;600&family=Space+Mono:wght@700&display=swap');

/* ── Reset & Base ── */
*, *::before, *::after { box-sizing: border-box; }

:root {
  --english-primary: #FF6B6B;
  --english-secondary: #FF8E53;
  --english-light: #FFF0EE;
  --english-dark: #C0392B;
  --math-primary: #4ECDC4;
  --math-secondary: #44A5E0;
  --math-light: #E8FFFE;
  --math-dark: #1A7A74;
  --gold: #F7C948;
  --dark: #1A1A2E;
  --text: #2D3748;
  --muted: #718096;
  --white: #FFFFFF;
  --radius: 18px;
  --shadow: 0 8px 40px rgba(0,0,0,0.12);
  --shadow-hover: 0 16px 60px rgba(0,0,0,0.18);
}

/* ── Hide Streamlit chrome ── */
#MainMenu, footer, header { visibility: hidden; }
.block-container { padding: 0 !important; max-width: 100% !important; }
section[data-testid="stSidebar"] > div { padding-top: 0 !important; }

/* ── Body ── */
body, .stApp {
  background: linear-gradient(135deg, #F5F7FF 0%, #EEF2FF 50%, #F0FFF4 100%);
  font-family: 'DM Sans', sans-serif;
  color: var(--text);
}

/* ── Sidebar ── */
section[data-testid="stSidebar"] {
  background: linear-gradient(180deg, var(--dark) 0%, #16213E 60%, #0F3460 100%) !important;
  border-right: none !important;
  box-shadow: 4px 0 30px rgba(0,0,0,0.25);
}
section[data-testid="stSidebar"] * { color: white !important; }
section[data-testid="stSidebar"] .stRadio label { 
  font-family: 'DM Sans', sans-serif !important;
  font-size: 15px !important;
}
section[data-testid="stSidebar"] hr { border-color: rgba(255,255,255,0.15) !important; }

/* ── Sidebar logo area ── */
.sidebar-logo {
  background: linear-gradient(135deg, var(--english-primary), var(--math-primary));
  border-radius: 16px;
  padding: 20px;
  text-align: center;
  margin-bottom: 24px;
}
.sidebar-logo h1 {
  font-family: 'Playfair Display', serif !important;
  font-size: 26px !important;
  font-weight: 900 !important;
  color: white !important;
  margin: 0 !important;
  letter-spacing: -0.5px;
}
.sidebar-logo p {
  font-size: 11px !important;
  opacity: 0.85;
  margin: 4px 0 0 0 !important;
  letter-spacing: 2px;
  text-transform: uppercase;
}

/* ── Hero Section ── */
.hero-section {
  background: linear-gradient(135deg, #1A1A2E 0%, #16213E 50%, #0F3460 100%);
  padding: 60px 48px 50px;
  position: relative;
  overflow: hidden;
}
.hero-section::before {
  content: '';
  position: absolute;
  top: -60px; right: -60px;
  width: 300px; height: 300px;
  border-radius: 50%;
  background: radial-gradient(circle, rgba(255,107,107,0.3) 0%, transparent 70%);
}
.hero-section::after {
  content: '';
  position: absolute;
  bottom: -80px; left: 30%;
  width: 400px; height: 400px;
  border-radius: 50%;
  background: radial-gradient(circle, rgba(78,205,196,0.25) 0%, transparent 70%);
}
.hero-badge {
  display: inline-block;
  background: rgba(247,201,72,0.2);
  border: 1px solid var(--gold);
  border-radius: 100px;
  padding: 6px 18px;
  font-size: 12px;
  font-weight: 600;
  letter-spacing: 1.5px;
  text-transform: uppercase;
  color: var(--gold) !important;
  margin-bottom: 20px;
}
.hero-title {
  font-family: 'Playfair Display', serif !important;
  font-size: clamp(36px, 5vw, 64px) !important;
  font-weight: 900 !important;
  color: white !important;
  line-height: 1.1 !important;
  margin: 0 0 18px 0 !important;
}
.hero-title span.en { color: var(--english-primary); }
.hero-title span.mt { color: var(--math-primary); }
.hero-subtitle {
  font-size: 17px;
  color: rgba(255,255,255,0.72) !important;
  max-width: 560px;
  line-height: 1.7;
  margin: 0 0 32px 0 !important;
}
.hero-stats {
  display: flex;
  gap: 32px;
  flex-wrap: wrap;
  position: relative;
  z-index: 1;
}
.hero-stat {
  text-align: center;
}
.hero-stat-num {
  font-family: 'Space Mono', monospace;
  font-size: 28px;
  font-weight: 700;
  color: var(--gold) !important;
  line-height: 1;
}
.hero-stat-label {
  font-size: 12px;
  color: rgba(255,255,255,0.6) !important;
  text-transform: uppercase;
  letter-spacing: 1px;
  margin-top: 4px;
}

/* ── Subject cards ── */
.subject-card {
  border-radius: var(--radius);
  padding: 28px 24px;
  margin: 8px 0;
  position: relative;
  overflow: hidden;
  transition: transform 0.25s ease, box-shadow 0.25s ease;
  cursor: pointer;
}
.subject-card:hover { transform: translateY(-4px); box-shadow: var(--shadow-hover); }
.subject-card.english {
  background: linear-gradient(135deg, #FF6B6B 0%, #FF8E53 100%);
  color: white !important;
  box-shadow: 0 8px 32px rgba(255,107,107,0.35);
}
.subject-card.math {
  background: linear-gradient(135deg, #4ECDC4 0%, #44A5E0 100%);
  color: white !important;
  box-shadow: 0 8px 32px rgba(78,205,196,0.35);
}
.subject-card-icon { font-size: 40px; margin-bottom: 12px; }
.subject-card-title {
  font-family: 'Playfair Display', serif;
  font-size: 22px;
  font-weight: 700;
  margin: 0 0 8px 0;
  color: white !important;
}
.subject-card-desc {
  font-size: 14px;
  opacity: 0.88;
  margin: 0;
  line-height: 1.6;
  color: white !important;
}
.subject-card-badge {
  position: absolute;
  top: 16px; right: 16px;
  background: rgba(255,255,255,0.25);
  border-radius: 100px;
  padding: 4px 12px;
  font-size: 11px;
  font-weight: 700;
  letter-spacing: 1px;
  color: white !important;
}

/* ── Section titles ── */
.section-title {
  font-family: 'Playfair Display', serif !important;
  font-size: 32px !important;
  font-weight: 700 !important;
  color: var(--dark) !important;
  margin: 0 0 6px 0 !important;
}
.section-subtitle {
  font-size: 15px;
  color: var(--muted) !important;
  margin: 0 0 28px 0 !important;
}

/* ── Content cards ── */
.content-card {
  background: white;
  border-radius: var(--radius);
  padding: 24px;
  box-shadow: var(--shadow);
  margin-bottom: 16px;
  border-left: 4px solid transparent;
  transition: all 0.2s ease;
}
.content-card:hover { transform: translateX(4px); box-shadow: var(--shadow-hover); }
.content-card.english-card { border-left-color: var(--english-primary); }
.content-card.math-card { border-left-color: var(--math-primary); }
.content-card h3 {
  font-family: 'Playfair Display', serif;
  font-size: 18px;
  font-weight: 700;
  margin: 0 0 10px 0;
  color: var(--dark) !important;
}
.content-card p {
  font-size: 14px;
  line-height: 1.7;
  color: var(--text) !important;
  margin: 0;
}

/* ── Grammar rule box ── */
.rule-box {
  background: linear-gradient(135deg, var(--english-light) 0%, #FFF5F5 100%);
  border: 1px solid rgba(255,107,107,0.25);
  border-radius: 14px;
  padding: 22px;
  margin: 12px 0;
}
.rule-box h4 {
  font-family: 'Space Mono', monospace;
  font-size: 13px;
  color: var(--english-dark) !important;
  text-transform: uppercase;
  letter-spacing: 1.5px;
  margin: 0 0 10px 0;
}
.rule-box p { font-size: 15px; line-height: 1.7; margin: 0; }

/* ── Math formula box ── */
.formula-box {
  background: linear-gradient(135deg, var(--math-light) 0%, #E0F9F7 100%);
  border: 1px solid rgba(78,205,196,0.35);
  border-radius: 14px;
  padding: 22px;
  margin: 12px 0;
}
.formula-box h4 {
  font-family: 'Space Mono', monospace;
  font-size: 13px;
  color: var(--math-dark) !important;
  text-transform: uppercase;
  letter-spacing: 1.5px;
  margin: 0 0 10px 0;
}
.formula-display {
  font-family: 'Space Mono', monospace;
  font-size: 20px;
  font-weight: 700;
  color: var(--math-dark) !important;
  text-align: center;
  padding: 14px;
  background: white;
  border-radius: 10px;
  margin: 10px 0;
  box-shadow: 0 2px 12px rgba(78,205,196,0.2);
}

/* ── Topic tags ── */
.topic-tag {
  display: inline-block;
  border-radius: 100px;
  padding: 5px 14px;
  font-size: 12px;
  font-weight: 600;
  margin: 3px;
}
.topic-tag.en { background: rgba(255,107,107,0.12); color: var(--english-dark) !important; }
.topic-tag.mt { background: rgba(78,205,196,0.15); color: var(--math-dark) !important; }

/* ── Quiz elements ── */
.quiz-option {
  background: white;
  border: 2px solid #E2E8F0;
  border-radius: 12px;
  padding: 14px 18px;
  margin: 8px 0;
  cursor: pointer;
  transition: all 0.2s ease;
  font-size: 15px;
}
.quiz-option:hover { border-color: var(--math-primary); background: var(--math-light); }
.quiz-option.correct { border-color: #48BB78; background: #F0FFF4; color: #276749 !important; }
.quiz-option.wrong { border-color: var(--english-primary); background: var(--english-light); }

/* ── Progress bars ── */
.progress-bar-container {
  background: #EDF2F7;
  border-radius: 100px;
  height: 8px;
  overflow: hidden;
  margin: 8px 0;
}
.progress-bar-fill {
  height: 100%;
  border-radius: 100px;
  transition: width 0.6s ease;
}
.progress-bar-fill.english { background: linear-gradient(90deg, var(--english-primary), var(--english-secondary)); }
.progress-bar-fill.math { background: linear-gradient(90deg, var(--math-primary), var(--math-secondary)); }

/* ── Tip/info boxes ── */
.tip-box {
  border-radius: 12px;
  padding: 16px 20px;
  margin: 12px 0;
  display: flex;
  align-items: flex-start;
  gap: 12px;
}
.tip-box.info { background: #EBF8FF; border-left: 4px solid #4299E1; }
.tip-box.warn { background: #FFFAF0; border-left: 4px solid #ECC94B; }
.tip-box.success { background: #F0FFF4; border-left: 4px solid #48BB78; }
.tip-box-icon { font-size: 20px; margin-top: 2px; }
.tip-box-text { font-size: 14px; line-height: 1.6; color: var(--text) !important; }

/* ── Chatbot container ── */
.chatbot-fab {
  position: fixed;
  bottom: 28px;
  right: 28px;
  z-index: 9999;
}

/* ── n8n chat overrides ── */
:root {
  --chat--color-primary: #4ECDC4;
  --chat--color-primary-shade-50: #44B5AE;
  --chat--color-primary-shade-100: #3D9E97;
  --chat--color-secondary: #FF6B6B;
  --chat--color-white: #ffffff;
  --chat--color-light: #f2f4f8;
  --chat--color-dark: #1A1A2E;
  --chat--color-typing: #404040;
  --chat--border-radius: 16px;
  --chat--transition-duration: 0.2s;
  --chat--window--width: 380px;
  --chat--window--height: 560px;
  --chat--header--background: linear-gradient(135deg, #1A1A2E 0%, #0F3460 100%);
  --chat--header--color: white;
  --chat--message--bot--background: #F0FFFE;
  --chat--message--bot--color: #1A1A2E;
  --chat--message--user--background: linear-gradient(135deg, #4ECDC4, #44A5E0);
  --chat--message--user--color: white;
  --chat--input--background: white;
  --chat--toggle--background: linear-gradient(135deg, #FF6B6B, #FF8E53);
  --chat--toggle--hover--background: linear-gradient(135deg, #FF5252, #FF7043);
  --chat--toggle--active--background: linear-gradient(135deg, #E53935, #F4511E);
}

/* ── Main content wrapper ── */
.main-content-wrapper {
  padding: 32px 40px 80px;
  max-width: 1200px;
}

/* ── Stagger animation ── */
@keyframes fadeSlideUp {
  from { opacity: 0; transform: translateY(24px); }
  to   { opacity: 1; transform: translateY(0); }
}
.animate-1 { animation: fadeSlideUp 0.5s ease 0.05s both; }
.animate-2 { animation: fadeSlideUp 0.5s ease 0.15s both; }
.animate-3 { animation: fadeSlideUp 0.5s ease 0.25s both; }
.animate-4 { animation: fadeSlideUp 0.5s ease 0.35s both; }

/* ── Streamlit radio styling ── */
div[data-testid="stRadio"] > label { display: none; }
div[data-testid="stRadio"] > div {
  display: flex;
  flex-direction: column;
  gap: 4px;
}
div[data-testid="stRadio"] label {
  display: block !important;
  padding: 10px 16px !important;
  border-radius: 10px !important;
  transition: background 0.2s ease !important;
}
div[data-testid="stRadio"] label:hover { background: rgba(255,255,255,0.1) !important; }

/* ── Dividers ── */
.fancy-divider {
  border: none;
  height: 2px;
  background: linear-gradient(90deg, var(--english-primary), var(--gold), var(--math-primary));
  border-radius: 100px;
  margin: 28px 0;
}

/* Fix stale Streamlit select/button colors */
.stButton > button {
  border-radius: 12px !important;
  font-family: 'DM Sans', sans-serif !important;
  font-weight: 600 !important;
  transition: all 0.2s ease !important;
}
</style>
""", unsafe_allow_html=True)

# ─────────────────────────── CHATBOT HTML ────────────────────────────
# KEY INSIGHT: position:fixed inside an iframe is fixed to the IFRAME box,
# not the browser viewport. So we must position the IFRAME itself as fixed.
# We do this by injecting CSS into the parent page that targets the iframe,
# and giving the iframe a tall height so the chat window can open upward.
CHATBOT_HTML = """<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<link href="https://cdn.jsdelivr.net/npm/@n8n/chat/dist/style.css" rel="stylesheet" />
<style>
  * { margin: 0; padding: 0; box-sizing: border-box; }
  html, body {
    background: transparent !important;
    overflow: visible;
    width: 100%;
    height: 100%;
  }

  :root {
    --chat--color-primary: #4ECDC4;
    --chat--color-primary-shade-50: #3ab8af;
    --chat--color-primary-shade-100: #2ea39b;
    --chat--color-secondary: #FF6B6B;
    --chat--color-white: #ffffff;
    --chat--color-light: #f4f7fa;
    --chat--color-light-shade-50: #e8eef3;
    --chat--color-light-shade-100: #dce4eb;
    --chat--color-medium: #9aacb9;
    --chat--color-dark: #1A1A2E;
    --chat--color-disabled: #c4cdd6;
    --chat--color-typing: #404040;
    --chat--border-radius: 16px;
    --chat--transition-duration: 0.2s;
    --chat--window--width: 380px;
    --chat--window--height: 520px;
    --chat--header--background: linear-gradient(135deg, #1A1A2E 0%, #0F3460 100%);
    --chat--header--color: #ffffff;
    --chat--header--padding: 18px 20px;
    --chat--message--bot--background: #f0fffe;
    --chat--message--bot--color: #1A1A2E;
    --chat--message--user--background: #1A1A2E;
    --chat--message--user--color: #F0F4FF;
    --chat--input--background: #ffffff;
    --chat--input--border-color: #e2e8f0;
    --chat--input--text-color: #1A1A2E;
    --chat--input--placeholder--color: #a0aec0;
    --chat--toggle--size: 60px;
    --chat--toggle--background: linear-gradient(135deg, #FF6B6B 0%, #FF8E53 100%);
    --chat--toggle--hover--background: linear-gradient(135deg, #FF5252 0%, #FF7043 100%);
    --chat--toggle--active--background: linear-gradient(135deg, #E53935 0%, #F4511E 100%);
    --chat--toggle--color: #ffffff;
    --chat--toggle--border-radius: 50%;
  }

  /* Position the entire chat widget at bottom-right of this iframe */
  #n8n-chat {
    position: absolute;
    bottom: 20px;
    right: 20px;
  }

  /* Force human message text to be clearly readable */
  .chat-message--user,
  .chat-message--user *,
  .chat-message--user p,
  .chat-message--user span {
    color: #F0F4FF !important;
  }
</style>
</head>
<body>
<div id="n8n-chat"></div>
<script type="module">
  import { createChat } from 'https://cdn.jsdelivr.net/npm/@n8n/chat/dist/chat.bundle.es.js';

  createChat({
    webhookUrl: 'https://apple.faziar.xyz/webhook/5cf49311-f0a3-4876-a3b6-9a8011e159cd/chat',
    target: '#n8n-chat',
    mode: 'window',
    showWelcomeScreen: false,
    defaultLanguage: 'en',
    initialMessages: [
      'Hi there! 👋 I am your EduBright AI Tutor!',
      'Ask me anything about English Grammar or Mathematics — I am here to help! 🎓'
    ],
    i18n: {
      en: {
        title: '🎓 EduBright AI Tutor',
        subtitle: 'Your personal Grammar & Math assistant',
        footer: '',
        getStarted: 'Start Learning!',
        inputPlaceholder: 'Ask a grammar or math question...',
        closeButtonTooltip: 'Close',
      }
    }
  });
</script>
</body>
</html>
"""

# ─────────────────────────── DATA ────────────────────────────
GRAMMAR_TOPICS = {
    "Tenses": {
        "icon": "⏰",
        "rules": [
            {"title": "Simple Present Tense", "rule": "Subject + V1 (add 's/es' for He/She/It)", "example": "She reads books every day.", "tip": "Used for habitual actions, general truths, and schedules."},
            {"title": "Simple Past Tense", "rule": "Subject + V2 (regular: +ed; irregular: varied)", "example": "They visited Paris last summer.", "tip": "Used for completed actions at a specific time in the past."},
            {"title": "Present Perfect", "rule": "Subject + have/has + V3", "example": "I have finished my homework.", "tip": "Used for past actions with present relevance."},
            {"title": "Future Simple", "rule": "Subject + will + V1", "example": "She will graduate next year.", "tip": "Used for predictions, promises, and spontaneous decisions."},
        ]
    },
    "Parts of Speech": {
        "icon": "📝",
        "rules": [
            {"title": "Nouns", "rule": "A noun names a person, place, thing, or idea.", "example": "The teacher gave the students a difficult assignment.", "tip": "Types: Common, Proper, Abstract, Collective, Countable, Uncountable."},
            {"title": "Adjectives", "rule": "Adjectives describe or modify nouns.", "example": "The beautiful, old castle stood on a tall hill.", "tip": "Order: Opinion → Size → Age → Shape → Color → Origin → Material → Purpose + Noun."},
            {"title": "Adverbs", "rule": "Adverbs modify verbs, adjectives, or other adverbs.", "example": "She spoke very quietly and walked away quickly.", "tip": "Many adverbs end in '-ly' but not all (fast, hard, well)."},
            {"title": "Conjunctions", "rule": "Conjunctions join words, phrases, or clauses.", "example": "I wanted to go, but it was raining.", "tip": "FANBOYS: For, And, Nor, But, Or, Yet, So (coordinating conjunctions)."},
        ]
    },
    "Punctuation": {
        "icon": "✏️",
        "rules": [
            {"title": "Comma Rules", "rule": "Use commas to separate items in a list, after introductory phrases, and before conjunctions joining independent clauses.", "example": "After dinner, we watched a movie, played games, and talked.", "tip": "The Oxford comma (before 'and' in a series) prevents ambiguity."},
            {"title": "Apostrophes", "rule": "Use apostrophes for contractions and possessives.", "example": "It's a beautiful day. The dog's bone was buried.", "tip": "Never use an apostrophe for 'its' (possessive). Only for 'it's' (it is/has)."},
            {"title": "Semicolons", "rule": "Use semicolons to join independent clauses without a conjunction.", "example": "She studied hard; she passed the exam.", "tip": "Can also separate complex list items that already contain commas."},
        ]
    },
    "Sentence Structure": {
        "icon": "🏗️",
        "rules": [
            {"title": "Simple Sentence", "rule": "One independent clause: Subject + Predicate", "example": "The dog barked loudly.", "tip": "Can have compound subjects or predicates and still be simple."},
            {"title": "Compound Sentence", "rule": "Two independent clauses joined by a coordinating conjunction or semicolon.", "example": "She loves art, and her brother loves music.", "tip": "Both clauses must be able to stand alone as complete sentences."},
            {"title": "Complex Sentence", "rule": "An independent clause + one or more dependent clauses.", "example": "Although it was raining, they continued the game.", "tip": "Dependent clause can begin with: because, although, when, if, since, etc."},
        ]
    },
}

MATH_TOPICS = {
    "Algebra": {
        "icon": "🔢",
        "formulas": [
            {"title": "Quadratic Formula", "formula": "x = (-b ± √(b²-4ac)) / 2a", "desc": "Solves any quadratic equation ax² + bx + c = 0", "example": "x²-5x+6=0 → x=3 or x=2"},
            {"title": "Linear Equation", "formula": "y = mx + b", "desc": "Slope-intercept form. m = slope, b = y-intercept", "example": "y = 2x + 3 has slope 2 and crosses y-axis at 3"},
            {"title": "Difference of Squares", "formula": "a² - b² = (a+b)(a-b)", "desc": "Special factoring pattern for perfect square differences", "example": "x² - 9 = (x+3)(x-3)"},
            {"title": "FOIL Method", "formula": "(a+b)(c+d) = ac + ad + bc + bd", "desc": "First, Outer, Inner, Last — multiply two binomials", "example": "(x+2)(x+3) = x²+5x+6"},
        ]
    },
    "Geometry": {
        "icon": "📐",
        "formulas": [
            {"title": "Circle", "formula": "Area = πr²   |   Circumference = 2πr", "desc": "r = radius, π ≈ 3.14159", "example": "r=5 → Area = 78.54 sq units"},
            {"title": "Triangle", "formula": "Area = ½ × base × height", "desc": "Pythagorean theorem: a² + b² = c² (right triangles)", "example": "base=8, height=5 → Area = 20 sq units"},
            {"title": "Rectangle", "formula": "Area = l × w   |   Perimeter = 2(l+w)", "desc": "l = length, w = width", "example": "l=10, w=4 → Area=40, Perimeter=28"},
            {"title": "Trapezoid", "formula": "Area = ½(a+b) × h", "desc": "a and b are parallel sides, h is height", "example": "a=6, b=10, h=4 → Area = 32"},
        ]
    },
    "Statistics": {
        "icon": "📊",
        "formulas": [
            {"title": "Mean (Average)", "formula": "Mean = Σx / n", "desc": "Sum of all values divided by count of values", "example": "Data: 4,8,15,16,23 → Mean = 66/5 = 13.2"},
            {"title": "Standard Deviation", "formula": "σ = √(Σ(x-μ)² / N)", "desc": "Measures spread of data around the mean", "example": "Low σ = data close to mean; High σ = spread out"},
            {"title": "Probability", "formula": "P(E) = Favorable / Total outcomes", "desc": "Must be between 0 (impossible) and 1 (certain)", "example": "Flipping heads: P = 1/2 = 0.5 = 50%"},
        ]
    },
    "Calculus": {
        "icon": "∫",
        "formulas": [
            {"title": "Power Rule (Derivative)", "formula": "d/dx[xⁿ] = n·xⁿ⁻¹", "desc": "Multiply by exponent, reduce exponent by 1", "example": "d/dx[x³] = 3x²"},
            {"title": "Chain Rule", "formula": "d/dx[f(g(x))] = f'(g(x))·g'(x)", "desc": "Derivative of composite functions", "example": "d/dx[sin(x²)] = cos(x²)·2x"},
            {"title": "Basic Integral", "formula": "∫xⁿ dx = xⁿ⁺¹/(n+1) + C", "desc": "Anti-derivative of power functions (n ≠ -1)", "example": "∫x² dx = x³/3 + C"},
        ]
    },
}

GRAMMAR_QUIZ = [
    {"q": "Which sentence uses the correct tense?", "options": ["She go to school yesterday.", "She went to school yesterday.", "She goed to school yesterday.", "She goes to school yesterday."], "answer": 1, "explanation": "'Went' is the irregular past tense of 'go'. We use simple past for completed actions."},
    {"q": "Identify the adjective in: 'The tall boy ran quickly.'", "options": ["The", "tall", "ran", "quickly"], "answer": 1, "explanation": "'Tall' is an adjective because it describes the noun 'boy'. 'Quickly' is an adverb modifying the verb 'ran'."},
    {"q": "Which is a compound sentence?", "options": ["The cat sat on the mat.", "Although it rained, she smiled.", "She sings, and he dances.", "Running fast, he won the race."], "answer": 2, "explanation": "A compound sentence has two independent clauses joined by a conjunction. 'She sings' and 'he dances' are both independent."},
    {"q": "Choose the correct punctuation:", "options": ["Its a beautiful day.", "It's a beautiful day.", "Its' a beautiful day.", "It is' a beautiful day."], "answer": 1, "explanation": "'It's' = 'it is' (contraction). 'Its' is possessive and needs no apostrophe."},
]

MATH_QUIZ = [
    {"q": "Solve: 2x + 6 = 14. What is x?", "options": ["x = 3", "x = 4", "x = 5", "x = 10"], "answer": 1, "explanation": "2x = 14 - 6 = 8, so x = 8/2 = 4. Always perform the same operation on both sides."},
    {"q": "What is the area of a circle with radius 7? (Use π ≈ 3.14)", "options": ["43.96", "153.86", "21.98", "49"], "answer": 1, "explanation": "Area = πr² = 3.14 × 7² = 3.14 × 49 = 153.86 square units."},
    {"q": "Factor: x² - 9", "options": ["(x-3)(x-3)", "(x+9)(x-1)", "(x+3)(x-3)", "Cannot be factored"], "answer": 2, "explanation": "x² - 9 is a difference of squares: a² - b² = (a+b)(a-b). Here a=x, b=3."},
    {"q": "Find the mean of: 2, 4, 6, 8, 10", "options": ["5", "6", "7", "8"], "answer": 1, "explanation": "Mean = (2+4+6+8+10) / 5 = 30 / 5 = 6."},
]

# ─────────────────────────── SESSION STATE ────────────────────────────
if "quiz_answers" not in st.session_state:
    st.session_state.quiz_answers = {}
if "quiz_submitted" not in st.session_state:
    st.session_state.quiz_submitted = {}

# ─────────────────────────── SIDEBAR ────────────────────────────
with st.sidebar:
    st.markdown("""
    <div class="sidebar-logo">
        <h1>🎓 EduBright</h1>
        <p>Grammar & Math Academy</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("### 📚 Navigate")
    page = st.radio("", ["🏠 Home", "📖 English Grammar", "🔢 Mathematics", "🧩 Quiz Zone", "📊 Progress"], label_visibility="collapsed")

    st.markdown("---")
    st.markdown("""
    <div style='padding: 16px; background: rgba(255,255,255,0.08); border-radius: 12px;'>
        <p style='font-size:13px; margin:0; opacity:0.8;'>💡 <b>Tip:</b> Click the chat button at the bottom-right to ask our AI Tutor anything!</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("---")
    st.markdown("""
    <div style='text-align:center;'>
        <p style='font-size:11px; opacity:0.5; margin:0;'>EduBright v1.0 • Made with ❤️</p>
    </div>
    """, unsafe_allow_html=True)

# ─────────────────────────── PAGES ────────────────────────────

# ══ HOME ══
if page == "🏠 Home":
    st.markdown("""
    <div class="hero-section">
        <div style="position:relative; z-index:1;">
            <div class="hero-badge">🌟 AI-Powered Learning Platform</div>
            <h1 class="hero-title">
                Master <span class="en">English</span><br>
                & <span class="mt">Mathematics</span>
            </h1>
            <p class="hero-subtitle">
                An interactive, beautifully designed learning platform for students of all levels. 
                Explore grammar rules, math formulas, and test your knowledge — powered by AI assistance.
            </p>
            <div class="hero-stats">
                <div class="hero-stat">
                    <div class="hero-stat-num">50+</div>
                    <div class="hero-stat-label">Topics</div>
                </div>
                <div class="hero-stat">
                    <div class="hero-stat-num">200+</div>
                    <div class="hero-stat-label">Examples</div>
                </div>
                <div class="hero-stat">
                    <div class="hero-stat-num">AI</div>
                    <div class="hero-stat-label">Tutor</div>
                </div>
                <div class="hero-stat">
                    <div class="hero-stat-num">24/7</div>
                    <div class="hero-stat-label">Available</div>
                </div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<div class="main-content-wrapper">', unsafe_allow_html=True)

    col1, col2 = st.columns(2, gap="large")
    with col1:
        st.markdown("""
        <div class="subject-card english animate-1">
            <div class="subject-card-badge">📖 GRAMMAR</div>
            <div class="subject-card-icon">✍️</div>
            <h2 class="subject-card-title">English Grammar</h2>
            <p class="subject-card-desc">Master tenses, parts of speech, punctuation, sentence structure, and more. Clear rules with real examples.</p>
        </div>
        """, unsafe_allow_html=True)
        st.markdown("""
        <div style='display:flex; flex-wrap:wrap; gap:6px; margin-top:12px;' class="animate-2">
            <span class="topic-tag en">Tenses</span>
            <span class="topic-tag en">Nouns & Pronouns</span>
            <span class="topic-tag en">Punctuation</span>
            <span class="topic-tag en">Sentence Types</span>
            <span class="topic-tag en">Parts of Speech</span>
            <span class="topic-tag en">Voice & Narration</span>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="subject-card math animate-1">
            <div class="subject-card-badge">🔢 MATH</div>
            <div class="subject-card-icon">📐</div>
            <h2 class="subject-card-title">Mathematics</h2>
            <p class="subject-card-desc">Explore algebra, geometry, statistics and calculus. Visual formulas and step-by-step solutions to build confidence.</p>
        </div>
        """, unsafe_allow_html=True)
        st.markdown("""
        <div style='display:flex; flex-wrap:wrap; gap:6px; margin-top:12px;' class="animate-2">
            <span class="topic-tag mt">Algebra</span>
            <span class="topic-tag mt">Geometry</span>
            <span class="topic-tag mt">Statistics</span>
            <span class="topic-tag mt">Calculus</span>
            <span class="topic-tag mt">Trigonometry</span>
            <span class="topic-tag mt">Number Theory</span>
        </div>
        """, unsafe_allow_html=True)

    st.markdown('<hr class="fancy-divider">', unsafe_allow_html=True)

    st.markdown("""
    <h2 class="section-title animate-3">🤖 Meet Your AI Tutor</h2>
    <p class="section-subtitle">Powered by advanced AI — ask questions, get explanations, solve problems instantly.</p>
    """, unsafe_allow_html=True)

    col_a, col_b, col_c = st.columns(3, gap="medium")
    for col, icon, title, desc in [
        (col_a, "💬", "Ask Anything", "Grammar rules, math solutions, or concept explanations — your AI tutor handles it all."),
        (col_b, "⚡", "Instant Answers", "Get clear, step-by-step explanations in seconds. No waiting, no textbook hunting."),
        (col_c, "🎯", "Personalized", "The AI adapts to your level and gives targeted help exactly where you need it."),
    ]:
        with col:
            st.markdown(f"""
            <div class="content-card animate-4" style="border-left-color: var(--gold); text-align:center; padding: 28px;">
                <div style="font-size:36px; margin-bottom:12px;">{icon}</div>
                <h3 style="text-align:center;">{title}</h3>
                <p style="text-align:center;">{desc}</p>
            </div>
            """, unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)

# ══ ENGLISH GRAMMAR ══
elif page == "📖 English Grammar":
    st.markdown("""
    <div class="hero-section" style="background: linear-gradient(135deg, #C0392B 0%, #FF6B6B 50%, #FF8E53 100%);">
        <div style="position:relative; z-index:1;">
            <div class="hero-badge" style="border-color:#FFF; color:#FFF !important; background:rgba(255,255,255,0.2);">📖 ENGLISH GRAMMAR</div>
            <h1 class="hero-title">Grammar <span style="color:#FFF7AA;">Rules</span><br>& Examples</h1>
            <p class="hero-subtitle">Explore comprehensive grammar topics with clear rules and practical examples.</p>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<div class="main-content-wrapper">', unsafe_allow_html=True)

    topic_names = list(GRAMMAR_TOPICS.keys())
    selected_topic = st.selectbox("📌 Choose a Grammar Topic", topic_names, label_visibility="visible")

    if selected_topic:
        topic = GRAMMAR_TOPICS[selected_topic]
        st.markdown(f"""
        <div style="display:flex; align-items:center; gap:12px; margin:20px 0 8px;">
            <span style="font-size:36px;">{topic['icon']}</span>
            <h2 class="section-title" style="margin:0 !important;">{selected_topic}</h2>
        </div>
        <hr class="fancy-divider">
        """, unsafe_allow_html=True)

        for i, rule in enumerate(topic["rules"]):
            with st.expander(f"📌 {rule['title']}", expanded=(i == 0)):
                st.markdown(f"""
                <div class="rule-box">
                    <h4>📏 Rule</h4>
                    <p>{rule['rule']}</p>
                </div>
                """, unsafe_allow_html=True)

                st.markdown(f"""
                <div class="content-card english-card">
                    <h3>✏️ Example</h3>
                    <p style="font-style:italic; font-size:16px;">"{rule['example']}"</p>
                </div>
                """, unsafe_allow_html=True)

                st.markdown(f"""
                <div class="tip-box info">
                    <div class="tip-box-icon">💡</div>
                    <div class="tip-box-text"><b>Tip:</b> {rule['tip']}</div>
                </div>
                """, unsafe_allow_html=True)

    st.markdown("""
    <div class="tip-box warn" style="margin-top:24px;">
        <div class="tip-box-icon">🤖</div>
        <div class="tip-box-text"><b>Need more help?</b> Click the chat button at bottom-right to ask the AI tutor any grammar question!</div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)

# ══ MATHEMATICS ══
elif page == "🔢 Mathematics":
    st.markdown("""
    <div class="hero-section" style="background: linear-gradient(135deg, #1A7A74 0%, #4ECDC4 50%, #44A5E0 100%);">
        <div style="position:relative; z-index:1;">
            <div class="hero-badge" style="border-color:#FFF; color:#FFF !important; background:rgba(255,255,255,0.2);">🔢 MATHEMATICS</div>
            <h1 class="hero-title">Formulas &<br><span style="color:#FFF7AA;">Concepts</span></h1>
            <p class="hero-subtitle">Master math formulas, theorems and step-by-step examples across all major topics.</p>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<div class="main-content-wrapper">', unsafe_allow_html=True)

    math_topic_names = list(MATH_TOPICS.keys())
    selected_math = st.selectbox("📌 Choose a Math Topic", math_topic_names, label_visibility="visible")

    if selected_math:
        topic = MATH_TOPICS[selected_math]
        st.markdown(f"""
        <div style="display:flex; align-items:center; gap:12px; margin:20px 0 8px;">
            <span style="font-size:36px;">{topic['icon']}</span>
            <h2 class="section-title" style="margin:0 !important;">{selected_math}</h2>
        </div>
        <hr class="fancy-divider">
        """, unsafe_allow_html=True)

        for i, formula in enumerate(topic["formulas"]):
            with st.expander(f"📐 {formula['title']}", expanded=(i == 0)):
                st.markdown(f"""
                <div class="formula-box">
                    <h4>📏 Formula</h4>
                    <div class="formula-display">{formula['formula']}</div>
                    <p>{formula['desc']}</p>
                </div>
                """, unsafe_allow_html=True)

                st.markdown(f"""
                <div class="content-card math-card">
                    <h3>🔍 Example</h3>
                    <p style="font-family: 'Space Mono', monospace; font-size:15px;">{formula['example']}</p>
                </div>
                """, unsafe_allow_html=True)

    st.markdown("""
    <div class="tip-box info" style="margin-top:24px;">
        <div class="tip-box-icon">🤖</div>
        <div class="tip-box-text"><b>Stuck on a problem?</b> Open the AI chat and paste your math problem — the tutor will walk you through it step by step!</div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)

# ══ QUIZ ZONE ══
elif page == "🧩 Quiz Zone":
    st.markdown("""
    <div class="hero-section" style="background: linear-gradient(135deg, #1A1A2E 0%, #2D1B69 50%, #11998E 100%);">
        <div style="position:relative; z-index:1;">
            <div class="hero-badge" style="border-color:var(--gold); color:var(--gold) !important;">🧩 QUIZ ZONE</div>
            <h1 class="hero-title">Test Your<br><span style="color:var(--gold);">Knowledge</span></h1>
            <p class="hero-subtitle">Challenge yourself with grammar and math quizzes. Get instant feedback and explanations.</p>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<div class="main-content-wrapper">', unsafe_allow_html=True)

    quiz_tab = st.radio("Select Quiz Type", ["📖 English Grammar Quiz", "🔢 Mathematics Quiz"], horizontal=True)

    current_quiz = GRAMMAR_QUIZ if "Grammar" in quiz_tab else MATH_QUIZ
    quiz_key = "grammar" if "Grammar" in quiz_tab else "math"
    card_class = "english-card" if "Grammar" in quiz_tab else "math-card"
    accent = "var(--english-primary)" if "Grammar" in quiz_tab else "var(--math-primary)"

    st.markdown(f"""
    <div style="margin:20px 0; padding:16px 20px; background:white; border-radius:14px; 
                box-shadow: var(--shadow); border-left: 4px solid {accent};">
        <p style="margin:0; font-size:15px;">📋 <b>{len(current_quiz)} Questions</b> | Click an answer, then submit to see explanations.</p>
    </div>
    """, unsafe_allow_html=True)

    with st.form(f"{quiz_key}_quiz_form"):
        answers = {}
        for i, q in enumerate(current_quiz):
            st.markdown(f"""
            <div class="content-card {card_class}" style="margin-bottom:4px;">
                <h3>Q{i+1}. {q['q']}</h3>
            </div>
            """, unsafe_allow_html=True)
            answers[i] = st.radio(f"q{i}", q["options"], key=f"{quiz_key}_q{i}", label_visibility="collapsed")
            st.markdown("<div style='height:8px'></div>", unsafe_allow_html=True)

        submitted = st.form_submit_button("🎯 Submit Quiz", use_container_width=True, type="primary")

    if submitted:
        score = 0
        st.markdown("<hr class='fancy-divider'>", unsafe_allow_html=True)
        st.markdown('<h2 class="section-title">📊 Results</h2>', unsafe_allow_html=True)

        for i, q in enumerate(current_quiz):
            chosen = answers[i]
            correct_text = q["options"][q["answer"]]
            is_correct = chosen == correct_text
            if is_correct:
                score += 1

            status = "✅ Correct!" if is_correct else "❌ Incorrect"
            color = "#48BB78" if is_correct else "#FF6B6B"
            bg = "#F0FFF4" if is_correct else "#FFF5F5"

            st.markdown(f"""
            <div style="background:{bg}; border-radius:14px; padding:18px; margin:10px 0; border-left: 4px solid {color};">
                <p style="margin:0 0 8px; font-weight:600;">Q{i+1}. {q['q']}</p>
                <p style="margin:0 0 6px; color:{color}; font-weight:700;">{status}</p>
                <p style="margin:0 0 6px; font-size:14px;"><b>Your answer:</b> {chosen}</p>
                {"" if is_correct else f'<p style="margin:0 0 6px; font-size:14px;"><b>Correct answer:</b> {correct_text}</p>'}
                <div class="tip-box info" style="margin-top:10px;">
                    <div class="tip-box-icon">💡</div>
                    <div class="tip-box-text"><b>Explanation:</b> {q['explanation']}</div>
                </div>
            </div>
            """, unsafe_allow_html=True)

        pct = (score / len(current_quiz)) * 100
        medal = "🥇" if pct == 100 else "🥈" if pct >= 75 else "🥉" if pct >= 50 else "📚"
        msg = "Perfect score!" if pct == 100 else "Great job!" if pct >= 75 else "Keep practicing!" if pct >= 50 else "Review the topics and try again!"

        st.markdown(f"""
        <div style="background: linear-gradient(135deg, var(--dark), #0F3460); border-radius:18px; 
                    padding:32px; text-align:center; margin-top:24px; color:white;">
            <div style="font-size:56px; margin-bottom:12px;">{medal}</div>
            <h2 style="font-family:'Playfair Display',serif; font-size:28px; color:white !important; margin:0 0 8px;">{score}/{len(current_quiz)} Correct</h2>
            <p style="font-size:18px; color:var(--gold) !important; font-weight:600; margin:0 0 12px;">{pct:.0f}% — {msg}</p>
            <div class="progress-bar-container" style="max-width:300px; margin:0 auto; height:12px;">
                <div class="progress-bar-fill {'english' if 'Grammar' in quiz_tab else 'math'}" style="width:{pct}%;"></div>
            </div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)

# ══ PROGRESS ══
elif page == "📊 Progress":
    st.markdown("""
    <div class="hero-section" style="background: linear-gradient(135deg, #2D3748 0%, #4A5568 100%);">
        <div style="position:relative; z-index:1;">
            <div class="hero-badge" style="border-color:var(--gold); color:var(--gold) !important;">📊 PROGRESS</div>
            <h1 class="hero-title">Your Learning<br><span style="color:var(--gold);">Journey</span></h1>
            <p class="hero-subtitle">Track your progress, revisit topics, and celebrate your achievements.</p>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<div class="main-content-wrapper">', unsafe_allow_html=True)

    col1, col2 = st.columns(2, gap="large")

    with col1:
        st.markdown('<h2 class="section-title">📖 English Grammar</h2>', unsafe_allow_html=True)
        grammar_progress = {"Tenses": 85, "Parts of Speech": 72, "Punctuation": 60, "Sentence Structure": 45}
        for topic, val in grammar_progress.items():
            st.markdown(f"""
            <div style="margin:12px 0;">
                <div style="display:flex; justify-content:space-between; margin-bottom:6px;">
                    <span style="font-weight:600; font-size:14px;">{topic}</span>
                    <span style="font-weight:700; color:var(--english-primary);">{val}%</span>
                </div>
                <div class="progress-bar-container">
                    <div class="progress-bar-fill english" style="width:{val}%;"></div>
                </div>
            </div>
            """, unsafe_allow_html=True)

    with col2:
        st.markdown('<h2 class="section-title">🔢 Mathematics</h2>', unsafe_allow_html=True)
        math_progress = {"Algebra": 78, "Geometry": 65, "Statistics": 55, "Calculus": 30}
        for topic, val in math_progress.items():
            st.markdown(f"""
            <div style="margin:12px 0;">
                <div style="display:flex; justify-content:space-between; margin-bottom:6px;">
                    <span style="font-weight:600; font-size:14px;">{topic}</span>
                    <span style="font-weight:700; color:var(--math-primary);">{val}%</span>
                </div>
                <div class="progress-bar-container">
                    <div class="progress-bar-fill math" style="width:{val}%;"></div>
                </div>
            </div>
            """, unsafe_allow_html=True)

    st.markdown("<hr class='fancy-divider'>", unsafe_allow_html=True)

    col_a, col_b, col_c, col_d = st.columns(4, gap="medium")
    for col, icon, num, label, color in [
        (col_a, "🎯", "8", "Topics Explored", "#FF6B6B"),
        (col_b, "✅", "28", "Quizzes Passed", "#4ECDC4"),
        (col_c, "⭐", "342", "Points Earned", "#F7C948"),
        (col_d, "🔥", "7", "Day Streak", "#FF8E53"),
    ]:
        with col:
            st.markdown(f"""
            <div class="content-card" style="text-align:center; border-left-color:{color}; padding:24px 16px;">
                <div style="font-size:32px; margin-bottom:8px;">{icon}</div>
                <div style="font-family:'Space Mono',monospace; font-size:28px; font-weight:700; color:{color};">{num}</div>
                <div style="font-size:12px; color:var(--muted); text-transform:uppercase; letter-spacing:1px; margin-top:4px;">{label}</div>
            </div>
            """, unsafe_allow_html=True)

    st.markdown("""
    <div class="tip-box success" style="margin-top:28px;">
        <div class="tip-box-icon">🎉</div>
        <div class="tip-box-text"><b>Keep it up!</b> You're on a 7-day streak. Complete today's quiz to maintain your streak and earn bonus points!</div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)

# ─────────────────────────── CHATBOT INJECTION ────────────────────────────
# The iframe must be position:fixed on the PARENT page (not inside iframe).
# We inject CSS targeting the iframe, then render it tall enough (650px)
# to contain the open chat window expanding upward from the button.
st.markdown("""
<style>
/* Target the chatbot iframe specifically and pin it to bottom-right */
div[data-testid="stCustomComponentV1"]:last-of-type > iframe,
.element-container:last-of-type iframe {
    position: fixed !important;
    bottom: 0px !important;
    right: 0px !important;
    width: 430px !important;
    height: 650px !important;
    border: none !important;
    z-index: 999999 !important;
    background: transparent !important;
    pointer-events: all !important;
}
/* Also target by a broader selector as fallback */
iframe[title="streamlit_chatbot"] {
    position: fixed !important;
    bottom: 0px !important;
    right: 0px !important;
    width: 430px !important;
    height: 650px !important;
    border: none !important;
    z-index: 999999 !important;
    background: transparent !important;
}
</style>
""", unsafe_allow_html=True)

components.html(CHATBOT_HTML, height=650, scrolling=False)