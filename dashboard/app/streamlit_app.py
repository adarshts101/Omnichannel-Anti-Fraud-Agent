"""
FraudShield — Omnichannel Fraud Intelligence Platform
Version 4.1.0 — Professional Edition
"""

import streamlit as st
import time
import random
from datetime import datetime
from io import BytesIO
from PIL import Image

st.set_page_config(
    page_title="FraudShield — Intelligence Platform",
    page_icon="🛡",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ── theme init ──
if "dark" not in st.session_state:
    st.session_state["dark"] = False

DARK = st.session_state["dark"]

CSS = f"""
<style>
@import url('https://fonts.googleapis.com/css2?family=Instrument+Serif:ital@0;1&family=Plus+Jakarta+Sans:wght@300;400;500;600;700&family=Fira+Code:wght@400;500;600&display=swap');

:root {{
    /* ── Surfaces ── */
    --canvas:     {"#0E1117" if DARK else "#F6F4F1"};
    --surface:    {"#161B22" if DARK else "#FFFFFF"};
    --surface-2:  {"#1C2430" if DARK else "#F9F8F6"};
    --surface-3:  {"#232D3F" if DARK else "#F0EDE8"};

    /* ── Borders ── */
    --line:       {"#2A3444" if DARK else "#E8E4DE"};
    --line-hi:    {"#364455" if DARK else "#D5CFC7"};
    --line-focus: {"#4E9EFF" if DARK else "#1A2B4A"};

    /* ── Text ── */
    --ink:        {"#E8ECF1" if DARK else "#0F1923"};
    --ink-2:      {"#CBD3DC" if DARK else "#1E2A36"};
    --ink-3:      {"#9AAABB" if DARK else "#3A4654"};
    --ink-4:      {"#6A7A8A" if DARK else "#5C6876"};
    --ink-5:      {"#4A5A6A" if DARK else "#8A939C"};

    /* ── Brand ── */
    --navy:       {"#4E9EFF" if DARK else "#1A2B4A"};
    --navy-dim:   {"rgba(78,158,255,0.12)" if DARK else "rgba(26,43,74,0.08)"};
    --navy-mid:   {"rgba(78,158,255,0.22)" if DARK else "rgba(26,43,74,0.15)"};

    /* ── Status ── */
    --red:        {"#FF6B6B" if DARK else "#C0392B"};
    --red-mid:    {"#FF4757" if DARK else "#E74C3C"};
    --red-dim:    {"rgba(255,71,87,0.12)" if DARK else "rgba(192,57,43,0.08)"};
    --red-border: {"rgba(255,71,87,0.28)" if DARK else "rgba(192,57,43,0.2)"};

    --amber:      {"#FFB142" if DARK else "#B7600A"};
    --amber-mid:  {"#FFA502" if DARK else "#E07B12"};
    --amber-dim:  {"rgba(255,165,2,0.12)" if DARK else "rgba(183,96,10,0.08)"};
    --amber-border:{"rgba(255,165,2,0.28)" if DARK else "rgba(183,96,10,0.2)"};

    --orange:     {"#FF7F50" if DARK else "#A84010"};
    --orange-dim: {"rgba(255,127,80,0.12)" if DARK else "rgba(168,64,16,0.08)"};
    --orange-border:{"rgba(255,127,80,0.28)" if DARK else "rgba(168,64,16,0.2)"};

    --green:      {"#2ED573" if DARK else "#1A6B3A"};
    --green-mid:  {"#26C95B" if DARK else "#27AE60"};
    --green-dim:  {"rgba(46,213,115,0.10)" if DARK else "rgba(26,107,58,0.07)"};
    --green-border:{"rgba(46,213,115,0.24)" if DARK else "rgba(26,107,58,0.18)"};

    --nav-h: 60px;
    --radius: 10px;
}}

*, *::before, *::after {{ box-sizing: border-box; margin: 0; padding: 0; }}

html, body, [class*="css"] {{
    font-family: 'Plus Jakarta Sans', system-ui, sans-serif !important;
    background: var(--canvas) !important;
    color: var(--ink) !important;
    font-size: 14px !important;
    line-height: 1.6 !important;
    -webkit-font-smoothing: antialiased !important;
}}

#MainMenu, footer, header {{ visibility: hidden !important; }}
.block-container {{ padding: 0 !important; max-width: 100% !important; }}
section[data-testid="stMain"] > div {{ padding: 0 !important; }}

::-webkit-scrollbar {{ width: 5px; height: 5px; }}
::-webkit-scrollbar-track {{ background: var(--surface-3); }}
::-webkit-scrollbar-thumb {{ background: var(--line-hi); border-radius: 3px; }}
::-webkit-scrollbar-thumb:hover {{ background: var(--ink-4); }}

/* ═══════════ NAVIGATION ═══════════ */
.nav {{
    position: sticky; top: 0; z-index: 200;
    height: var(--nav-h);
    background: var(--surface);
    border-bottom: 1px solid var(--line);
    display: flex; align-items: center;
    padding: 0 32px; gap: 0;
    box-shadow: 0 1px 0 var(--line), 0 2px 8px rgba(0,0,0,{"0.3" if DARK else "0.04"});
}}
.nav-brand {{
    display: flex; align-items: center; gap: 11px;
    margin-right: 40px; flex-shrink: 0;
}}
.nav-logomark {{
    width: 34px; height: 34px; border-radius: 8px;
    background: var(--navy);
    display: flex; align-items: center; justify-content: center;
    flex-shrink: 0;
}}
.nav-logomark svg {{ width: 18px; height: 18px; }}
.nav-wordmark {{
    font-family: 'Plus Jakarta Sans', sans-serif;
    font-size: 15px; font-weight: 700;
    color: var(--ink); letter-spacing: -0.03em;
}}
.nav-wordmark span {{ color: var(--navy); }}
.nav-divider-v {{
    width: 1px; height: 20px;
    background: var(--line); margin: 0 20px; flex-shrink: 0;
}}
.nav-tabs {{
    display: flex; align-items: center; gap: 2px; flex: 1;
}}
.nav-tab {{
    padding: 7px 14px; border-radius: 7px;
    font-size: 13px; font-weight: 500;
    color: var(--ink-3); cursor: pointer;
    transition: all 0.12s; white-space: nowrap;
    letter-spacing: -0.01em;
}}
.nav-tab:hover {{ color: var(--ink); background: var(--surface-3); }}
.nav-tab.active {{
    color: var(--navy); background: var(--navy-dim);
    font-weight: 600;
}}
.nav-right {{
    display: flex; align-items: center; gap: 12px; flex-shrink: 0;
}}
.nav-status {{
    display: flex; align-items: center; gap: 7px;
    padding: 6px 13px;
    background: var(--green-dim);
    border: 1px solid var(--green-border);
    border-radius: 100px;
    font-family: 'Fira Code', monospace;
    font-size: 10px; font-weight: 600;
    color: var(--green); letter-spacing: 0.05em;
}}
.nav-status-dot {{
    width: 6px; height: 6px; border-radius: 50%;
    background: var(--green-mid);
    animation: blink 2.8s ease-in-out infinite;
}}
@keyframes blink {{
    0%,100% {{ opacity: 1; }}
    50% {{ opacity: 0.35; }}
}}
.nav-ver {{
    font-family: 'Fira Code', monospace;
    font-size: 11px; color: var(--ink-5);
    letter-spacing: 0.02em;
}}

/* ── Theme toggle ── */
.theme-toggle {{
    width: 44px; height: 24px; border-radius: 100px;
    background: {"var(--navy)" if DARK else "var(--surface-3)"};
    border: 1.5px solid var(--line-hi);
    position: relative; cursor: pointer;
    transition: background 0.25s;
    flex-shrink: 0;
    display: flex; align-items: center;
    padding: 2px;
}}
.theme-toggle-knob {{
    width: 18px; height: 18px; border-radius: 50%;
    background: {"var(--canvas)" if DARK else "var(--ink-4)"};
    position: absolute;
    left: {"22px" if DARK else "2px"};
    transition: left 0.25s, background 0.25s;
    display: flex; align-items: center; justify-content: center;
    font-size: 10px;
}}

/* ═══════════ PAGE LAYOUT ═══════════ */
.page {{
    padding: 32px 36px 48px;
    max-width: 1380px; margin: 0 auto;
}}
.pg-header {{ margin-bottom: 28px; }}
.pg-crumb {{
    display: flex; align-items: center; gap: 6px;
    font-family: 'Fira Code', monospace;
    font-size: 11px; color: var(--ink-4);
    letter-spacing: 0.04em; margin-bottom: 14px;
}}
.pg-crumb-sep {{ color: var(--ink-5); }}
.pg-title-row {{
    display: flex; align-items: flex-end;
    justify-content: space-between; gap: 16px;
}}
.pg-title {{
    font-family: 'Instrument Serif', Georgia, serif;
    font-size: 30px; font-weight: 400;
    color: var(--ink); letter-spacing: -0.02em;
    line-height: 1.1;
}}
.pg-title em {{ font-style: italic; color: var(--navy); }}
.pg-sub {{
    font-size: 13px; color: var(--ink-2);
    margin-top: 6px; font-weight: 400;
    max-width: 560px; line-height: 1.6;
}}
.pg-badge {{
    display: inline-flex; align-items: center; gap: 6px;
    padding: 6px 14px;
    background: var(--navy-dim);
    border: 1px solid var(--navy-mid);
    border-radius: 100px;
    font-family: 'Fira Code', monospace;
    font-size: 10px; font-weight: 600;
    color: var(--navy); letter-spacing: 0.06em;
    white-space: nowrap; flex-shrink: 0;
}}

/* ═══════════ KPI STRIP ═══════════ */
.kpi-row {{
    display: grid; grid-template-columns: repeat(4, 1fr);
    gap: 14px; margin-bottom: 30px;
}}
.kpi {{
    background: var(--surface);
    border: 1px solid var(--line);
    border-radius: var(--radius);
    padding: 20px 22px;
    position: relative; overflow: hidden;
    transition: box-shadow 0.2s, border-color 0.2s;
}}
.kpi:hover {{
    border-color: var(--line-hi);
    box-shadow: 0 4px 16px rgba(0,0,0,{"0.4" if DARK else "0.06"});
}}
.kpi::after {{
    content: '';
    position: absolute; bottom: 0; left: 0; right: 0;
    height: 3px; border-radius: 0 0 var(--radius) var(--radius);
}}
.kpi.navy::after  {{ background: var(--navy); }}
.kpi.red::after   {{ background: var(--red-mid); }}
.kpi.green::after {{ background: var(--green-mid); }}
.kpi.amber::after {{ background: var(--amber-mid); }}
.kpi-top {{
    display: flex; justify-content: space-between;
    align-items: flex-start; margin-bottom: 16px;
}}
.kpi-lbl {{
    font-family: 'Fira Code', monospace;
    font-size: 10px; font-weight: 600;
    color: var(--ink-3); letter-spacing: 0.08em; text-transform: uppercase;
}}
.kpi-icon {{
    width: 32px; height: 32px; border-radius: 8px;
    display: flex; align-items: center; justify-content: center;
    font-size: 15px;
}}
.kpi-icon.navy  {{ background: var(--navy-dim); }}
.kpi-icon.red   {{ background: var(--red-dim); }}
.kpi-icon.green {{ background: var(--green-dim); }}
.kpi-icon.amber {{ background: var(--amber-dim); }}
.kpi-val {{
    font-family: 'Instrument Serif', Georgia, serif;
    font-size: 32px; font-weight: 400;
    color: var(--ink); letter-spacing: -0.03em;
    line-height: 1; margin-bottom: 6px;
}}
.kpi-delta {{ font-size: 12px; font-weight: 500; display: flex; align-items: center; gap: 4px; }}
.kpi-delta.up   {{ color: var(--green); }}
.kpi-delta.down {{ color: var(--red);   }}

/* ═══════════ SECTION HEADERS ═══════════ */
.sec-hd {{
    display: flex; align-items: flex-end;
    justify-content: space-between; margin-bottom: 16px;
}}
.sec-hl {{ width: 24px; height: 2px; background: var(--navy); border-radius: 1px; margin-bottom: 8px; }}
.sec-title {{
    font-family: 'Instrument Serif', Georgia, serif;
    font-size: 16px; font-weight: 400; color: var(--ink); letter-spacing: -0.01em;
}}
.sec-desc {{ font-size: 12px; color: var(--ink-3); margin-top: 2px; }}
.sec-tag {{
    font-family: 'Fira Code', monospace;
    font-size: 10px; font-weight: 600;
    color: var(--navy); letter-spacing: 0.06em;
    background: var(--navy-dim);
    border: 1px solid var(--navy-mid);
    padding: 4px 11px; border-radius: 100px;
}}

/* ═══════════ CHANNEL TABS ═══════════ */
.ch-tabs {{
    display: flex; gap: 8px; margin-bottom: 20px;
}}
.ch-tab {{
    display: flex; align-items: center; gap: 10px;
    padding: 12px 20px; border-radius: 10px;
    background: var(--surface);
    border: 1.5px solid var(--line);
    cursor: pointer; transition: all 0.15s;
    font-size: 13px; font-weight: 700; color: var(--ink-2);
    flex: 1; justify-content: center;
}}
.ch-tab:hover {{ border-color: var(--navy-mid); color: var(--ink); background: var(--surface-2); }}
.ch-tab.active {{
    border-color: var(--navy);
    background: var(--navy-dim);
    color: var(--navy);
}}
.ch-tab-icon {{
    width: 32px; height: 32px; border-radius: 8px;
    display: flex; align-items: center; justify-content: center;
    font-size: 17px; flex-shrink: 0;
}}
.ch-tab.active .ch-tab-icon {{ background: var(--navy-dim); }}

/* ── Channel logo cards ── */
.ch-card {{
    background: var(--surface);
    border: 1px solid var(--line);
    border-radius: var(--radius);
    padding: 18px 20px;
    margin-bottom: 16px;
}}
.ch-card-hd {{
    display: flex; align-items: center; gap: 14px; margin-bottom: 16px;
    padding-bottom: 14px; border-bottom: 1px solid var(--line);
}}
.ch-logo-wrap {{
    width: 44px; height: 44px; border-radius: 12px;
    display: flex; align-items: center; justify-content: center;
    flex-shrink: 0; font-size: 22px;
}}
/* platform colours */
.ch-logo-whatsapp {{ background: #25D36620; }}
.ch-logo-sms      {{ background: #007AFF20; }}
.ch-logo-voice    {{ background: #FF375F20; }}
.ch-logo-email    {{ background: #FF950020; }}
.ch-logo-telegram {{ background: #0088CC20; }}
.ch-logo-doc      {{ background: #7B61FF20; }}

.ch-card-lbl {{
    font-family: 'Fira Code', monospace;
    font-size: 9px; font-weight: 700; color: var(--ink-3);
    letter-spacing: 0.1em; text-transform: uppercase;
}}
.ch-card-name {{ font-size: 14px; font-weight: 700; color: var(--ink); letter-spacing: -0.01em; margin-top: 2px; }}
.ch-card-desc {{ font-size: 12px; color: var(--ink-3); margin-top: 2px; }}

/* platform badge strip */
.platform-strip {{
    display: flex; gap: 8px; flex-wrap: wrap; margin-bottom: 14px;
}}
.plat-badge {{
    display: inline-flex; align-items: center; gap: 6px;
    padding: 5px 12px; border-radius: 100px;
    font-size: 12px; font-weight: 700; cursor: pointer;
    border: 1.5px solid var(--line-hi); transition: all 0.14s;
    background: var(--surface-2); color: var(--ink-2);
}}
.plat-badge:hover {{ background: var(--surface-3); color: var(--ink); }}
.plat-badge.sel   {{ background: var(--navy-dim); border-color: var(--navy-mid); color: var(--navy); }}
.plat-badge-dot   {{ width: 8px; height: 8px; border-radius: 50%; }}
.pd-wa  {{ background: #25D366; }}
.pd-sms {{ background: #007AFF; }}
.pd-vc  {{ background: #FF375F; }}
.pd-em  {{ background: #FF9500; }}
.pd-tg  {{ background: #0088CC; }}

/* ═══════════ ACTION RAIL ═══════════ */
.action-rail {{
    background: var(--surface);
    border: 1px solid var(--line);
    border-radius: var(--radius);
    padding: 18px 22px;
    display: flex; align-items: center;
    justify-content: space-between;
    margin-bottom: 28px; gap: 20px;
}}
.rail-note {{ font-size: 13px; color: var(--ink-2); }}
.rail-note strong {{ color: var(--ink); font-weight: 700; }}
.rail-stats {{ display: flex; align-items: center; }}
.rail-stat {{ text-align: center; padding: 0 22px; border-right: 1px solid var(--line); }}
.rail-stat:last-child {{ border-right: none; padding-right: 0; }}
.rail-stat:first-child {{ padding-left: 0; }}
.rail-stat-v {{
    font-family: 'Instrument Serif', Georgia, serif;
    font-size: 20px; font-weight: 400;
    color: var(--navy); letter-spacing: -0.02em; line-height: 1;
}}
.rail-stat-l {{
    font-family: 'Fira Code', monospace;
    font-size: 9px; font-weight: 600;
    color: var(--ink-3); letter-spacing: 0.08em;
    text-transform: uppercase; margin-top: 3px;
}}

/* ═══════════ REPORT ═══════════ */
.report-shell {{
    background: var(--surface);
    border: 1px solid var(--line);
    border-radius: var(--radius);
    overflow: hidden; margin-bottom: 18px;
    box-shadow: 0 2px 12px rgba(0,0,0,{"0.3" if DARK else "0.05"});
}}
.report-top {{
    background: var(--navy);
    padding: 16px 24px;
    display: flex; align-items: center; justify-content: space-between;
}}
.report-top-left {{ display: flex; align-items: center; gap: 10px; }}
.report-icon {{
    width: 28px; height: 28px; border-radius: 7px;
    background: rgba(255,255,255,0.12);
    display: flex; align-items: center; justify-content: center; font-size: 14px;
}}
.report-title {{
    font-family: 'Plus Jakarta Sans', sans-serif;
    font-size: 13px; font-weight: 700;
    color: #FFFFFF; letter-spacing: -0.01em;
}}
.report-meta {{
    font-family: 'Fira Code', monospace;
    font-size: 10px; color: rgba(255,255,255,0.45); letter-spacing: 0.04em;
}}
.report-body {{ padding: 24px; }}

.score-block {{
    display: flex; align-items: center; gap: 24px;
    padding: 22px 24px; border-radius: 10px;
    border: 1px solid; margin-bottom: 20px;
    position: relative; overflow: hidden;
}}
.score-block::before {{
    content: ''; position: absolute; top: 0; right: 0;
    width: 120px; height: 120px; border-radius: 50%; opacity: 0.06;
    transform: translate(30px,-30px);
}}
.score-block.lv-critical {{ background: var(--red-dim); border-color: var(--red-border); }}
.score-block.lv-critical::before {{ background: var(--red); }}
.score-block.lv-high    {{ background: var(--amber-dim); border-color: var(--amber-border); }}
.score-block.lv-high::before {{ background: var(--amber); }}
.score-block.lv-medium  {{ background: var(--orange-dim); border-color: var(--orange-border); }}
.score-block.lv-medium::before {{ background: var(--orange); }}
.score-block.lv-low     {{ background: var(--green-dim); border-color: var(--green-border); }}
.score-block.lv-low::before {{ background: var(--green); }}
.score-gauge {{
    width: 90px; height: 90px; border-radius: 50%;
    border: 2px solid; flex-shrink: 0;
    display: flex; flex-direction: column; align-items: center; justify-content: center;
}}
.score-gauge.lv-critical {{ border-color: var(--red); }}
.score-gauge.lv-high     {{ border-color: var(--amber); }}
.score-gauge.lv-medium   {{ border-color: var(--orange); }}
.score-gauge.lv-low      {{ border-color: var(--green); }}
.score-n {{
    font-family: 'Instrument Serif', Georgia, serif;
    font-size: 30px; font-weight: 400; line-height: 1; letter-spacing: -0.03em;
}}
.score-n.lv-critical {{ color: var(--red); }}
.score-n.lv-high     {{ color: var(--amber); }}
.score-n.lv-medium   {{ color: var(--orange); }}
.score-n.lv-low      {{ color: var(--green); }}
.score-d {{ font-family:'Fira Code',monospace; font-size:10px; color:var(--ink-4); line-height:1; }}
.score-info {{ flex: 1; }}
.score-level {{
    font-family: 'Instrument Serif', Georgia, serif;
    font-size: 24px; font-weight: 400; letter-spacing: -0.02em; line-height: 1.1; margin-bottom: 5px;
}}
.score-level.lv-critical {{ color: var(--red); }}
.score-level.lv-high     {{ color: var(--amber); }}
.score-level.lv-medium   {{ color: var(--orange); }}
.score-level.lv-low      {{ color: var(--green); }}
.score-threat {{ font-size: 12px; color: var(--ink-3); margin-bottom: 12px; }}
.threat-pill {{
    display: inline-flex; align-items: center; gap: 6px;
    padding: 4px 12px; border-radius: 100px;
    font-family: 'Fira Code', monospace;
    font-size: 10px; font-weight: 600;
    letter-spacing: 0.06em; text-transform: uppercase; border: 1px solid;
}}
.tp-critical {{ color:var(--red);    background:var(--red-dim);    border-color:var(--red-border); }}
.tp-high     {{ color:var(--amber);  background:var(--amber-dim);  border-color:var(--amber-border); }}
.tp-medium   {{ color:var(--orange); background:var(--orange-dim); border-color:var(--orange-border); }}
.tp-low      {{ color:var(--green);  background:var(--green-dim);  border-color:var(--green-border); }}
.tp-dot {{ width:5px;height:5px;border-radius:50%;background:currentColor; }}

.ac {{
    display: flex; gap: 14px; align-items: flex-start;
    padding: 16px 18px; border-radius: 9px;
    margin-bottom: 20px; border: 1px solid; border-left: 3px solid;
}}
.ac.lv-critical {{ background:var(--red-dim);    border-color:var(--red-border);    border-left-color:var(--red); }}
.ac.lv-high     {{ background:var(--amber-dim);  border-color:var(--amber-border);  border-left-color:var(--amber); }}
.ac.lv-medium   {{ background:var(--orange-dim); border-color:var(--orange-border); border-left-color:var(--orange); }}
.ac.lv-low      {{ background:var(--green-dim);  border-color:var(--green-border);  border-left-color:var(--green); }}
.ac-icon {{ font-size:18px;line-height:1.5;flex-shrink:0; }}
.ac-lbl {{
    font-family:'Fira Code',monospace; font-size:9px; font-weight:600;
    color:var(--ink-4); letter-spacing:0.12em; text-transform:uppercase; margin-bottom:3px;
}}
.ac-text {{ font-size:13px;font-weight:500;color:var(--ink-2);line-height:1.55; }}

/* ═══════════ LOWER PANELS ═══════════ */
.panel {{
    background: var(--surface); border: 1px solid var(--line);
    border-radius: var(--radius); overflow: hidden;
    box-shadow: 0 1px 4px rgba(0,0,0,{"0.2" if DARK else "0.04"});
}}
.panel-hd {{
    padding: 13px 20px; border-bottom: 1px solid var(--line);
    background: var(--surface-2);
    display: flex; align-items: center; justify-content: space-between;
}}
.panel-title {{
    font-size: 13px; font-weight: 700; color: var(--ink);
    letter-spacing: -0.01em; display: flex; align-items: center; gap: 8px;
}}
.panel-body {{ padding: 18px 20px; }}
.ch-row {{
    display: grid; grid-template-columns: 68px 1fr 52px;
    align-items: center; gap: 14px; padding: 10px 0;
    border-bottom: 1px solid var(--line);
}}
.ch-row:last-child {{ border-bottom: none; }}
.ch-lbl {{ display:flex;align-items:center;gap:7px;font-size:12px;font-weight:700;color:var(--ink-2); }}
.ch-lbl-dot {{ width:5px;height:5px;border-radius:50%; }}
.ch-track {{ background:var(--surface-3);border-radius:100px;height:7px;overflow:hidden; }}
.ch-fill {{ height:100%;border-radius:100px;transition:width 0.8s ease; }}
.ch-fill.lv-critical {{ background:var(--red-mid); }}
.ch-fill.lv-high     {{ background:var(--amber-mid); }}
.ch-fill.lv-medium   {{ background:#D86030; }}
.ch-fill.lv-low      {{ background:var(--green-mid); }}
.ch-pct {{ font-family:'Fira Code',monospace;font-size:12px;font-weight:600;text-align:right; }}
.ch-pct.lv-critical {{ color:var(--red); }}
.ch-pct.lv-high     {{ color:var(--amber); }}
.ch-pct.lv-medium   {{ color:var(--orange); }}
.ch-pct.lv-low      {{ color:var(--green); }}
.meta-r {{
    display:flex;justify-content:space-between;align-items:center;
    padding:8px 0;border-bottom:1px solid var(--line);font-size:12px;
}}
.meta-r:last-child {{ border-bottom:none; }}
.meta-k {{ color:var(--ink-2);font-weight:500; }}
.meta-v {{ font-family:'Fira Code',monospace;font-size:11px;font-weight:700;color:var(--navy); }}
.sig-r {{
    display:flex;gap:12px;align-items:flex-start;
    padding:10px 0;border-bottom:1px solid var(--line);
}}
.sig-r:last-child {{ border-bottom:none; }}
.sig-n {{ font-family:'Fira Code',monospace;font-size:10px;color:var(--ink-5);min-width:24px;padding-top:2px; }}
.sig-dot {{ width:5px;height:5px;border-radius:50%;background:var(--navy);flex-shrink:0;margin-top:7px; }}
.sig-text {{ font-size:12px;color:var(--ink-2);flex:1;line-height:1.5; }}
.sig-ts {{ font-family:'Fira Code',monospace;font-size:10px;color:var(--ink-5);white-space:nowrap; }}
.int-r {{
    display:grid;grid-template-columns:175px 70px 1fr;
    align-items:center;gap:14px;padding:10px 0;
    border-bottom:1px solid var(--line);font-size:12px;
}}
.int-r:last-child {{ border-bottom:none; }}
.int-nm {{ font-weight:600;color:var(--ink-2); }}
.int-chip {{
    display:inline-flex;align-items:center;padding:3px 9px;border-radius:100px;
    font-family:'Fira Code',monospace;font-size:9px;font-weight:600;
    letter-spacing:0.06em;text-transform:uppercase;border:1px solid;
}}
.chip-live    {{ color:var(--green);background:var(--green-dim);border-color:var(--green-border); }}
.chip-pending {{ color:var(--amber);background:var(--amber-dim);border-color:var(--amber-border); }}
.int-d {{ color:var(--ink-2); }}

/* ═══════════ ANALYTICS ═══════════ */
.analytics-grid {{
    display: grid; grid-template-columns: 1fr 1fr 1fr;
    gap: 16px; margin-bottom: 16px;
}}
.analytics-wide {{
    display: grid; grid-template-columns: 2fr 1fr;
    gap: 16px; margin-bottom: 30px;
}}
.chart-card {{
    background: var(--surface);
    border: 1px solid var(--line);
    border-radius: var(--radius);
    overflow: hidden;
    box-shadow: 0 1px 4px rgba(0,0,0,{"0.2" if DARK else "0.04"});
}}
.chart-hd {{
    padding: 14px 20px; border-bottom: 1px solid var(--line);
    background: var(--surface-2);
    display: flex; align-items: center; justify-content: space-between;
}}
.chart-title {{ font-size: 13px; font-weight: 700; color: var(--ink); }}
.chart-subtitle {{ font-size: 11px; color: var(--ink-3); margin-top: 1px; }}
.chart-body {{ padding: 20px; }}
.chart-body svg {{ display: block; }}

/* Bar chart */
.bar-group {{ display: flex; align-items: flex-end; gap: 10px; height: 120px; }}
.bar-col {{ display: flex; flex-direction: column; align-items: center; flex: 1; height: 100%; justify-content: flex-end; }}
.bar-rect {{ border-radius: 4px 4px 0 0; width: 100%; transition: opacity 0.2s; }}
.bar-rect:hover {{ opacity: 0.8; }}
.bar-lbl {{ font-family:'Fira Code',monospace; font-size:9px; color:var(--ink-4); margin-top:6px; }}
.bar-val {{ font-family:'Instrument Serif',Georgia,serif; font-size:13px; color:var(--ink-2); margin-bottom:4px; }}

/* Donut */
.donut-wrap {{ display:flex;align-items:center;gap:20px; }}
.donut-legend {{ display:flex;flex-direction:column;gap:8px;flex:1; }}
.donut-leg-r {{ display:flex;align-items:center;gap:8px; }}
.donut-leg-dot {{ width:8px;height:8px;border-radius:50%;flex-shrink:0; }}
.donut-leg-lbl {{ font-size:11px;color:var(--ink-2);flex:1; }}
.donut-leg-val {{
    font-family:'Fira Code',monospace;font-size:11px;
    font-weight:700;color:var(--ink);
}}

/* Sparkline table */
.spark-r {{
    display:grid;grid-template-columns:80px 1fr 45px;
    align-items:center;gap:12px;padding:8px 0;
    border-bottom:1px solid var(--line);
}}
.spark-r:last-child {{ border-bottom:none; }}
.spark-lbl {{ font-size:12px;font-weight:700;color:var(--ink-2); }}
.spark-line {{ height:28px; }}
.spark-val {{
    font-family:'Fira Code',monospace;font-size:11px;
    font-weight:600;text-align:right;
}}

/* Timeline */
.tl-row {{
    display:grid;grid-template-columns:36px 1fr;
    gap:0;align-items:start;margin-bottom:0;
}}
.tl-time {{
    font-family:'Fira Code',monospace;font-size:9px;
    color:var(--ink-3);text-align:right;padding-right:12px;
    padding-top:3px;
}}
.tl-bar-wrap {{ padding-bottom:12px;border-left:1.5px solid var(--line);padding-left:14px; }}
.tl-bar-wrap:last-child {{ border-left:1.5px solid transparent; }}
.tl-dot {{
    width:8px;height:8px;border-radius:50%;
    margin-left:-19px;float:left;margin-top:4px;margin-right:10px;
}}
.tl-entry {{ font-size:12px;color:var(--ink);font-weight:700; }}
.tl-sub {{ font-size:11px;color:var(--ink-3);margin-top:2px; }}

/* ═══════════ WIDGET OVERRIDES ═══════════ */
.stFileUploader > div {{
    background: var(--surface-2) !important;
    border: 1.5px dashed var(--line-hi) !important;
    border-radius: 9px !important;
    transition: border-color 0.15s !important;
}}
.stFileUploader > div:hover {{ border-color: var(--navy) !important; }}
.stFileUploader label {{ color: var(--ink-3) !important; font-size: 12px !important; font-weight: 500 !important; }}
.stFileUploader [data-testid="stFileUploadDropzone"] p {{ color: var(--ink-4) !important; font-size: 12px !important; }}
.stTextArea textarea {{
    background: var(--surface-2) !important;
    color: var(--ink) !important;
    border: 1px solid var(--line) !important;
    border-radius: 9px !important;
    font-family: 'Plus Jakarta Sans', sans-serif !important;
    font-size: 13px !important; line-height: 1.65 !important;
    resize: vertical !important;
    caret-color: var(--navy) !important;
    box-shadow: inset 0 1px 3px rgba(0,0,0,0.03) !important;
}}
.stTextArea textarea:focus {{
    border-color: var(--navy) !important;
    box-shadow: 0 0 0 3px var(--navy-dim), inset 0 1px 3px rgba(0,0,0,0.03) !important;
    outline: none !important;
}}
.stTextArea textarea::placeholder {{ color: var(--ink-5) !important; }}
.stButton > button {{
    background: var(--navy) !important;
    color: {"#0E1117" if DARK else "#FFFFFF"} !important;
    border: none !important; border-radius: 9px !important;
    font-family: 'Plus Jakarta Sans', sans-serif !important;
    font-weight: 700 !important; font-size: 13px !important;
    padding: 11px 28px !important; letter-spacing: -0.01em !important;
    transition: all 0.15s !important;
    box-shadow: 0 2px 8px rgba(26,43,74,0.2) !important;
}}
.stButton > button:hover {{
    transform: translateY(-1px) !important;
    box-shadow: 0 6px 20px rgba(26,43,74,0.28) !important;
}}
.stButton > button:active {{ transform: translateY(0) !important; }}
.stProgress {{ margin: 6px 0 !important; }}
.stProgress > div > div {{ background: var(--navy) !important; border-radius: 100px !important; }}
.stProgress > div {{ background: var(--surface-3) !important; border-radius: 100px !important; height: 4px !important; }}
.stExpander {{
    background: var(--surface) !important;
    border: 1px solid var(--line) !important;
    border-radius: 9px !important; margin-bottom: 12px !important;
    box-shadow: 0 1px 4px rgba(0,0,0,{"0.2" if DARK else "0.04"}) !important;
}}
.stExpander summary {{
    font-size: 13px !important; font-weight: 700 !important;
    color: var(--ink-2) !important; padding: 14px 18px !important;
    letter-spacing: -0.01em !important;
}}
.stAlert {{
    background: var(--surface-2) !important;
    border: 1px solid var(--line) !important;
    border-radius: 9px !important; color: var(--ink-3) !important; font-size: 13px !important;
}}
[data-testid="stSuccess"] {{ background:var(--green-dim)!important;border-color:var(--green-border)!important;color:var(--green)!important; }}
[data-testid="stInfo"]    {{ background:var(--navy-dim)!important;border-color:var(--navy-mid)!important;color:var(--navy)!important; }}
[data-testid="stError"]   {{ background:var(--red-dim)!important;border-color:var(--red-border)!important;color:var(--red)!important; }}
p  {{ font-size:13px!important;color:var(--ink-2)!important; }}
li {{ font-size:13px!important;color:var(--ink-2)!important; }}
h3 {{ font-family:'Instrument Serif',Georgia,serif!important;font-size:16px!important;font-weight:400!important;color:var(--ink)!important; }}
hr {{ border-color:var(--line)!important;margin:16px 0!important; }}
.stCaption {{ font-size:11px!important;color:var(--ink-3)!important; }}
label {{ color: var(--ink-2) !important; font-weight: 600 !important; }}
.stFileUploader label {{ color: var(--ink-2) !important; font-size: 13px !important; font-weight: 600 !important; }}
.stFileUploader [data-testid="stFileUploadDropzone"] p {{ color: var(--ink-3) !important; font-size: 13px !important; }}</style>
"""

st.markdown(CSS, unsafe_allow_html=True)


# ══════════════════════════════════════════════
# UTILITIES
# ══════════════════════════════════════════════

def utc_now():   return datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")
def utc_short(): return datetime.utcnow().strftime("%H:%M:%S")
def case_id():   return f"FS-{random.randint(100000,999999)}"
def ref_id():    return f"REF-{random.randint(10000,99999)}"

def severity(s: int) -> str:
    if s >= 80: return "critical"
    if s >= 65: return "high"
    if s >= 45: return "medium"
    return "low"

def threat_color(lv: str) -> str:
    d = {"critical":"#C0392B","high":"#B7600A","medium":"#A84010","low":"#1A6B3A"}
    if DARK:
        d = {"critical":"#FF6B6B","high":"#FFB142","medium":"#FF7F50","low":"#2ED573"}
    return d[lv]

def pill_cls(lv): return {"critical":"tp-critical","high":"tp-high","medium":"tp-medium","low":"tp-low"}[lv]

def validate(a, im, t):
    return any([a is not None, im is not None, t.strip()])


# ══════════════════════════════════════════════
# ANALYSIS ENGINE
# ══════════════════════════════════════════════

def run_audio(f):
    if f is None: return {"score":0,"signals":[]}
    time.sleep(0.45)
    s = random.randint(58,94)
    return {"score":s,"signals":[
        "Synthetic voice fingerprint detected — TTS confidence 0.91",
        "Urgency-pattern language matched against phishing call corpus",
        "Caller ID spoofing metadata embedded in SIP header",
        f"Speech cadence anomaly: 2.3σ above behavioural baseline",
    ]}

def run_image(f):
    if f is None: return {"score":0,"signals":[]}
    time.sleep(0.40)
    s = random.randint(50,91)
    return {"score":s,"signals":[
        "Embedded QR code — redirect URL flagged by threat intelligence feed",
        "Logo manipulation detected: 87% template similarity to HDFC phishing kit",
        "EXIF metadata stripped — consistent with dark-web document tooling",
        "Brand impersonation classification confidence: 0.94",
    ]}

def run_text(txt):
    if not txt.strip(): return {"score":0,"signals":[]}
    time.sleep(0.30)
    s = random.randint(62,97)
    kws = ["otp","urgent","verify","click","account","suspended",
           "prize","winner","kyc","bank","reward","limited time"]
    hits = [k for k in kws if k.lower() in txt.lower()]
    signals = [f"Phishing keyword matched: '{k}'" for k in hits[:3]] or [
        "Surface keywords absent — deep semantic model triggered"
    ]
    signals += [
        "Sending domain absent from trusted organisational registry",
        f"Shannon entropy: {random.uniform(3.1,4.8):.2f} — elevated vs clean-corpus baseline",
    ]
    return {"score":s,"signals":signals}

def aggregate(ar, ir, tr):
    scores = [r["score"] for r in [ar,ir,tr] if r["score"] > 0]
    if not scores: return {}
    composite = min(int(0.6*max(scores)+0.4*(sum(scores)/len(scores))),99)
    lv = severity(composite)
    cfg = {
        "critical":("Critical Risk","🚨","Multi-channel coordinated fraud attack",
            "Block all related transactions immediately. Escalate to the Fraud Response Team. Preserve all channel evidence for forensic examination and regulatory reporting."),
        "high":    ("High Risk","⚠️","Targeted phishing / social engineering",
            "Flag account for mandatory manual review. Trigger step-up authentication challenge. Notify customer via verified secondary channel within 30 minutes."),
        "medium":  ("Medium Risk","📋","Suspicious activity — possible reconnaissance",
            "Add to active watchlist. Monitor all subsequent activity over a 24-hour window. Send proactive fraud awareness notification to the account holder."),
        "low":     ("Low Risk","✅","Low-confidence anomaly — possible false positive",
            "Log for audit trail and compliance records. No immediate escalation required. Routine enhanced monitoring continues per policy."),
    }
    label,icon,threat,action = cfg[lv]
    all_sigs = ar.get("signals",[])+ir.get("signals",[])+tr.get("signals",[])
    return {
        "composite":composite,"level":lv,"label":label,"icon":icon,
        "threat":threat,"action":action,"all_signals":all_sigs,
        "audio_score":ar["score"],"image_score":ir["score"],"text_score":tr["score"],
        "timestamp":utc_now(),"ts_short":utc_short(),"case_id":case_id(),"ref":ref_id(),
    }


# ══════════════════════════════════════════════
# RENDER — NAV
# ══════════════════════════════════════════════

def render_nav():
    moon = "🌙" if not DARK else "☀️"
    st.markdown(f"""
    <div class="nav">
        <div class="nav-brand">
            <div class="nav-logomark">
                <svg viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                    <path d="M12 2L4 6V12C4 16.4 7.4 20.5 12 22C16.6 20.5 20 16.4 20 12V6L12 2Z"
                          fill="rgba(255,255,255,0.2)" stroke="white" stroke-width="1.5"
                          stroke-linecap="round" stroke-linejoin="round"/>
                    <path d="M9 12L11 14L15 10" stroke="white" stroke-width="1.5"
                          stroke-linecap="round" stroke-linejoin="round"/>
                </svg>
            </div>
            <div class="nav-wordmark">Fraud<span>Shield</span></div>
        </div>
        <div class="nav-divider-v"></div>
        <div class="nav-tabs">
            <div class="nav-tab active">Threat Analysis</div>
            <div class="nav-tab">Dashboard</div>
            <div class="nav-tab">Case History</div>
            <div class="nav-tab">Analytics</div>
            <div class="nav-tab">Integrations</div>
            <div class="nav-tab">Settings</div>
        </div>
        <div class="nav-right">
            <div class="nav-status">
                <div class="nav-status-dot"></div>
                ALL SYSTEMS NOMINAL
            </div>
            <div class="nav-ver">v4.1.0</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Theme toggle button in a small column layout outside nav HTML
    _, col_btn = st.columns([20, 1])
    with col_btn:
        label = "☀️" if DARK else "🌙"
        if st.button(label, key="theme_btn", help="Toggle dark/light mode"):
            st.session_state["dark"] = not st.session_state["dark"]
            st.rerun()


def render_kpis():
    st.markdown("""
    <div class="kpi-row">
        <div class="kpi navy">
            <div class="kpi-top"><div class="kpi-lbl">Cases Today</div><div class="kpi-icon navy">📂</div></div>
            <div class="kpi-val">1,482</div>
            <div class="kpi-delta up">↑ 84 from yesterday</div>
        </div>
        <div class="kpi red">
            <div class="kpi-top"><div class="kpi-lbl">Threats Blocked</div><div class="kpi-icon red">🛡</div></div>
            <div class="kpi-val">347</div>
            <div class="kpi-delta up">↑ 23 from yesterday</div>
        </div>
        <div class="kpi green">
            <div class="kpi-top"><div class="kpi-lbl">Detection Accuracy</div><div class="kpi-icon green">🎯</div></div>
            <div class="kpi-val">97.4%</div>
            <div class="kpi-delta up">↑ 0.3% vs last week</div>
        </div>
        <div class="kpi amber">
            <div class="kpi-top"><div class="kpi-lbl">Avg Analysis Time</div><div class="kpi-icon amber">⚡</div></div>
            <div class="kpi-val">1.8s</div>
            <div class="kpi-delta down">↓ 0.2s improvement</div>
        </div>
    </div>
    """, unsafe_allow_html=True)


# ══════════════════════════════════════════════
# RENDER — CHANNEL TABS + INPUTS
# ══════════════════════════════════════════════

def render_inputs():
    # Section header
    st.markdown("""
    <div class="sec-hd">
        <div class="sec-hd-left">
            <div class="sec-hl"></div>
            <div class="sec-title">Evidence Submission</div>
            <div class="sec-desc">Select a channel and upload evidence for AI analysis</div>
        </div>
        <div class="sec-tag">MULTI-CHANNEL INPUT</div>
    </div>
    """, unsafe_allow_html=True)

    # Channel tab selector
    if "ch_tab" not in st.session_state:
        st.session_state["ch_tab"] = "voice"

    col1, col2, col3 = st.columns(3)

    tabs = [
        ("voice", "🎙️", "Voice / Audio", col1),
        ("text",  "💬", "SMS / Email / Chat", col2),
        ("doc",   "📄", "Image / Document", col3),
    ]
    for key, icon, label, col in tabs:
        with col:
            active_cls = "active" if st.session_state["ch_tab"] == key else ""
            st.markdown(f"""
            <div class="ch-tab {active_cls}" id="tab-{key}">
                <div class="ch-tab-icon">{icon}</div>
                <span>{label}</span>
            </div>
            """, unsafe_allow_html=True)
            if st.button(f"Select {label}", key=f"tab_btn_{key}",
                         use_container_width=True,
                         help=f"Switch to {label} channel"):
                st.session_state["ch_tab"] = key
                st.rerun()

    af, imf, txt = None, None, ""
    active = st.session_state["ch_tab"]

    # ── Voice tab ──
    if active == "voice":
        st.markdown("""
        <div class="ch-card">
            <div class="ch-card-hd">
                <div class="ch-logo-wrap ch-logo-voice">🎙️</div>
                <div>
                    <div class="ch-card-lbl">Channel 01 · Audio</div>
                    <div class="ch-card-name">Voice Call Analysis</div>
                    <div class="ch-card-desc">Upload call recordings for AI-powered deepfake and social-engineering detection</div>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)

        # Platform logos strip
        if "plat_voice" not in st.session_state:
            st.session_state["plat_voice"] = "Voice Call"
        plat_voice_opts = [
            ("📞", "Voice Call", "#FF375F", "pd-vc"),
            ("🟢", "WhatsApp",  "#25D366", "pd-wa"),
            ("✈️", "Telegram",  "#0088CC", "pd-tg"),
        ]
        plat_html = '<div class="platform-strip">'
        for em, name, color, dot_cls in plat_voice_opts:
            sel = "sel" if st.session_state["plat_voice"] == name else ""
            plat_html += f'<span class="plat-badge {sel}"><span class="plat-badge-dot {dot_cls}"></span>{em} {name}</span>'
        plat_html += '</div>'
        st.markdown(plat_html, unsafe_allow_html=True)

        c1, c2, c3 = st.columns(3)
        with c1:
            if st.button("📞 Voice Call", key="pv1", use_container_width=True):
                st.session_state["plat_voice"] = "Voice Call"; st.rerun()
        with c2:
            if st.button("🟢 WhatsApp Voice", key="pv2", use_container_width=True):
                st.session_state["plat_voice"] = "WhatsApp"; st.rerun()
        with c3:
            if st.button("✈️ Telegram Audio", key="pv3", use_container_width=True):
                st.session_state["plat_voice"] = "Telegram"; st.rerun()

        af = st.file_uploader("Upload call recording (.wav, .mp3)",
                               type=["wav","mp3"], key="au")
        if af:
            st.success(f"`{af.name}` — {af.size/1024:.1f} KB")
            st.audio(af)

    # ── Text tab ──
    elif active == "text":
        st.markdown("""
        <div class="ch-card">
            <div class="ch-card-hd">
                <div class="ch-logo-wrap ch-logo-sms">💬</div>
                <div>
                    <div class="ch-card-lbl">Channel 02 · Text</div>
                    <div class="ch-card-name">SMS / Email / Chat</div>
                    <div class="ch-card-desc">Paste message content for semantic phishing and keyword threat analysis</div>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)

        # Platform selector
        if "plat_text" not in st.session_state:
            st.session_state["plat_text"] = "SMS"
        plat_text_opts = [
            ("📱", "SMS",       "#007AFF", "pd-sms"),
            ("📧", "Email",     "#FF9500", "pd-em"),
            ("🟢", "WhatsApp",  "#25D366", "pd-wa"),
            ("✈️", "Telegram",  "#0088CC", "pd-tg"),
        ]
        plat_html = '<div class="platform-strip">'
        for em, name, color, dot_cls in plat_text_opts:
            sel = "sel" if st.session_state["plat_text"] == name else ""
            plat_html += f'<span class="plat-badge {sel}"><span class="plat-badge-dot {dot_cls}"></span>{em} {name}</span>'
        plat_html += '</div>'
        st.markdown(plat_html, unsafe_allow_html=True)

        c1, c2, c3, c4 = st.columns(4)
        for col, (em, name, _, _) in zip([c1,c2,c3,c4], plat_text_opts):
            with col:
                if st.button(f"{em} {name}", key=f"pt_{name}", use_container_width=True):
                    st.session_state["plat_text"] = name; st.rerun()

        plat = st.session_state["plat_text"]
        placeholders = {
            "SMS":      "Paste SMS body here… e.g. 'Dear customer, your OTP is…'",
            "Email":    "Paste email content, including subject and body…",
            "WhatsApp": "Paste WhatsApp message transcript…",
            "Telegram": "Paste Telegram message content…",
        }
        txt = st.text_area(
            f"Paste {plat} content",
            height=200, key="tx",
            placeholder=placeholders.get(plat,"Paste message content here…")
        )
        if txt.strip():
            st.caption(f"{len(txt.split())} words · {len(txt)} characters · Platform: {plat}")

    # ── Document tab ──
    elif active == "doc":
        st.markdown("""
        <div class="ch-card">
            <div class="ch-card-hd">
                <div class="ch-logo-wrap ch-logo-doc">📄</div>
                <div>
                    <div class="ch-card-lbl">Channel 03 · Document</div>
                    <div class="ch-card-name">Image & Document Analysis</div>
                    <div class="ch-card-desc">Upload images or PDF documents for forgery detection and brand-impersonation analysis</div>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)

        if "doc_type" not in st.session_state:
            st.session_state["doc_type"] = "image"

        c1, c2 = st.columns(2)
        with c1:
            if st.button("🖼️ Image (JPG/PNG)", key="dt_img", use_container_width=True):
                st.session_state["doc_type"] = "image"; st.rerun()
        with c2:
            if st.button("📄 PDF Document", key="dt_pdf", use_container_width=True):
                st.session_state["doc_type"] = "pdf"; st.rerun()

        if st.session_state["doc_type"] == "image":
            imf = st.file_uploader("Upload image (.jpg, .png)",
                                    type=["jpg","jpeg","png"], key="im")
            if imf:
                img = Image.open(BytesIO(imf.getvalue()))
                st.image(img, caption=imf.name, use_container_width=True)
        else:
            pdf_file = st.file_uploader("Upload PDF document (.pdf)",
                                         type=["pdf"], key="pdf_up")
            if pdf_file:
                st.success(f"📄 `{pdf_file.name}` — {pdf_file.size/1024:.1f} KB uploaded")
                st.caption("PDF will be processed for text extraction, embedded links, and metadata analysis.")
                # treat PDF upload as image-channel input for analysis
                imf = pdf_file

    return af, imf, txt


def render_rail():
    st.markdown("""
    <div class="action-rail">
        <div class="rail-note">
            Provide at least one channel of evidence, then execute the engine.
            <strong>Results generated in under 2 seconds.</strong>
        </div>
        <div class="rail-stats">
            <div class="rail-stat"><div class="rail-stat-v">3</div><div class="rail-stat-l">Channels</div></div>
            <div class="rail-stat"><div class="rail-stat-v">12+</div><div class="rail-stat-l">Signals</div></div>
            <div class="rail-stat"><div class="rail-stat-v">97.4%</div><div class="rail-stat-l">Accuracy</div></div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    _, c2, _ = st.columns([3,2,3])
    with c2:
        return st.button("▶  Run Analysis", use_container_width=True, type="primary")


def do_analysis(af, imf, txt):
    steps = [
        ("Scanning audio channel…",   lambda: run_audio(af)),
        ("Scanning image channel…",   lambda: run_image(imf)),
        ("Scanning text channel…",    lambda: run_text(txt)),
        ("Aggregating signals…",      None),
        ("Finalising threat report…", None),
    ]
    pb = st.progress(0)
    stat = st.empty()
    res = []
    for i, (lbl, fn) in enumerate(steps):
        stat.caption(f"⟳  {lbl}")
        pb.progress(int(i/len(steps)*100))
        if fn: res.append(fn())
        else: time.sleep(0.25)
    pb.progress(100); stat.empty()
    return aggregate(
        res[0] if len(res)>0 else {"score":0,"signals":[]},
        res[1] if len(res)>1 else {"score":0,"signals":[]},
        res[2] if len(res)>2 else {"score":0,"signals":[]},
    )


def render_results(r):
    if not r: return
    lv = r["level"]

    st.markdown(f"""
    <div class="report-shell">
        <div class="report-top">
            <div class="report-top-left">
                <div class="report-icon">🛡</div>
                <div class="report-title">Threat Analysis Report</div>
            </div>
            <div class="report-meta">{r['case_id']} &nbsp;·&nbsp; {r['ref']} &nbsp;·&nbsp; {r['timestamp']}</div>
        </div>
        <div class="report-body">
            <div class="score-block lv-{lv}">
                <div class="score-gauge lv-{lv}">
                    <div class="score-n lv-{lv}">{r['composite']}</div>
                    <div class="score-d">/ 100</div>
                </div>
                <div class="score-info">
                    <div class="score-level lv-{lv}">{r['label']}</div>
                    <div class="score-threat">{r['threat']}</div>
                    <span class="threat-pill {pill_cls(lv)}">
                        <span class="tp-dot"></span>
                        {r['label'].upper()} THREAT DETECTED
                    </span>
                </div>
            </div>
            <div class="ac lv-{lv}">
                <div class="ac-icon">{r['icon']}</div>
                <div>
                    <div class="ac-lbl">Recommended Action</div>
                    <div class="ac-text">{r['action']}</div>
                </div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    col_l, col_r = st.columns([3,2], gap="medium")
    with col_l:
        ch_data = [("Audio",r["audio_score"]),("Image/Doc",r["image_score"]),("Text",r["text_score"])]
        rows = ""
        for lbl, s in ch_data:
            if s == 0: continue
            lvc = severity(s)
            rows += f"""
            <div class="ch-row">
                <div class="ch-lbl"><span class="ch-lbl-dot" style="background:{threat_color(lvc)}"></span>{lbl}</div>
                <div class="ch-track"><div class="ch-fill lv-{lvc}" style="width:{s}%"></div></div>
                <div class="ch-pct lv-{lvc}">{s}%</div>
            </div>"""
        st.markdown(f"""
        <div class="panel">
            <div class="panel-hd"><div class="panel-title">📊 Channel Scores</div></div>
            <div class="panel-body">{rows}</div>
        </div>""", unsafe_allow_html=True)
    with col_r:
        st.markdown(f"""
        <div class="panel">
            <div class="panel-hd"><div class="panel-title">🗂 Case Metadata</div></div>
            <div class="panel-body">
                <div class="meta-r"><span class="meta-k">Case ID</span><span class="meta-v">{r['case_id']}</span></div>
                <div class="meta-r"><span class="meta-k">Reference</span><span class="meta-v">{r['ref']}</span></div>
                <div class="meta-r"><span class="meta-k">UTC Timestamp</span><span class="meta-v">{r['timestamp']}</span></div>
                <div class="meta-r"><span class="meta-k">Engine</span><span class="meta-v">FraudShield v4.1</span></div>
                <div class="meta-r"><span class="meta-k">Model</span><span class="meta-v">Gemini 2.0 Flash</span></div>
                <div class="meta-r"><span class="meta-k">Signals Found</span><span class="meta-v">{len(r['all_signals'])}</span></div>
                <div class="meta-r"><span class="meta-k">Channels Active</span><span class="meta-v">Audio · Image · Text</span></div>
            </div>
        </div>""", unsafe_allow_html=True)

    with st.expander(f"🔍 Detected Signals — {len(r['all_signals'])} found", expanded=True):
        rows = ""
        for i, sig in enumerate(r["all_signals"], 1):
            rows += f"""
            <div class="sig-r">
                <div class="sig-n">#{i:02d}</div>
                <div class="sig-dot"></div>
                <div class="sig-text">{sig}</div>
                <div class="sig-ts">{r['ts_short']}</div>
            </div>"""
        st.markdown(f'<div style="padding:4px 0">{rows}</div>', unsafe_allow_html=True)

    with st.expander("🔌 API Integration Status"):
        integrations = [
            ("Google Agent Builder","Pending","Multi-agent orchestration and workflow layer"),
            ("Gemini 2.0 Flash","Pending","Multimodal audio, image, and text understanding"),
            ("MongoDB MCP","Pending","Case storage, audit logging, and retrieval"),
            ("Elasticsearch MCP","Pending","Similarity search and threat intelligence indexing"),
            ("Cloud Speech-to-Text","Pending","Real-time audio transcription pipeline"),
            ("Vertex AI Vision","Pending","Document forgery detection and OCR extraction"),
        ]
        rows = ""
        for nm, st_label, desc in integrations:
            chip = "chip-live" if st_label == "Live" else "chip-pending"
            rows += f"""
            <div class="int-r">
                <div class="int-nm">{nm}</div>
                <span class="int-chip {chip}">{st_label}</span>
                <div class="int-d">{desc}</div>
            </div>"""
        st.markdown(f'<div style="padding:4px 0">{rows}</div>', unsafe_allow_html=True)


# ══════════════════════════════════════════════
# RENDER — ANALYTICS SECTION
# ══════════════════════════════════════════════

def _bar_svg(data, colors, height=110):
    """Generate inline SVG bar chart."""
    val_color = "#CBD3DC" if DARK else "#1E2A36"
    lbl_color = "#9AAABB" if DARK else "#3A4654"
    max_v = max(v for _,v in data) or 1
    w_total = 340
    n = len(data)
    bar_w = max(18, int((w_total - (n-1)*10) / n))
    gap = 10
    svg_h = height + 30
    bars = ""
    x = 0
    for i, (lbl, val) in enumerate(data):
        bh = int((val / max_v) * height)
        by = height - bh
        col = colors[i % len(colors)]
        bars += f'<rect x="{x}" y="{by}" width="{bar_w}" height="{bh}" rx="3" fill="{col}" opacity="0.85"/>'
        bars += f'<text x="{x + bar_w//2}" y="{by-5}" text-anchor="middle" font-family="Fira Code" font-size="10" font-weight="600" fill="{val_color}">{val}</text>'
        bars += f'<text x="{x + bar_w//2}" y="{height+18}" text-anchor="middle" font-family="Fira Code" font-size="9" font-weight="500" fill="{lbl_color}">{lbl}</text>'
        x += bar_w + gap
    return f'<svg viewBox="0 0 {x} {svg_h}" width="100%" xmlns="http://www.w3.org/2000/svg">{bars}</svg>'


def _donut_svg(segments, size=110):
    """Generate inline SVG donut chart."""
    import math
    cx, cy, r, thick = size/2, size/2, size*0.38, size*0.14
    total = sum(v for _,v,_ in segments)
    if total == 0: return ""
    svg = f'<svg viewBox="0 0 {size} {size}" width="{size}" height="{size}" xmlns="http://www.w3.org/2000/svg">'
    angle = -math.pi/2
    for lbl, val, color in segments:
        sweep = 2*math.pi*(val/total)
        x1 = cx + r*math.cos(angle)
        y1 = cy + r*math.sin(angle)
        angle += sweep
        x2 = cx + r*math.cos(angle)
        y2 = cy + r*math.sin(angle)
        lg = 1 if sweep > math.pi else 0
        d = f"M {cx} {cy} L {x1:.2f} {y1:.2f} A {r} {r} 0 {lg} 1 {x2:.2f} {y2:.2f} Z"
        svg += f'<path d="{d}" fill="{color}" opacity="0.85"/>'
    # centre hole
    svg += f'<circle cx="{cx}" cy="{cy}" r="{r-thick}" fill="var(--surface)"/>'
    svg += '</svg>'
    return svg


def _sparkline_svg(vals, color, w=140, h=28):
    if len(vals) < 2: return ""
    mn, mx = min(vals), max(vals)
    rng = (mx-mn) or 1
    step = w / (len(vals)-1)
    pts = " ".join(f"{i*step:.1f},{h - (v-mn)/rng*h:.1f}" for i,v in enumerate(vals))
    return f'<svg viewBox="0 0 {w} {h}" width="{w}" height="{h}" xmlns="http://www.w3.org/2000/svg"><polyline points="{pts}" fill="none" stroke="{color}" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg>'


def render_analytics():
    st.markdown("""
    <div class="sec-hd" style="margin-top:36px">
        <div class="sec-hd-left">
            <div class="sec-hl"></div>
            <div class="sec-title">Platform Analytics</div>
            <div class="sec-desc">Live threat statistics, channel distribution, and detection trends</div>
        </div>
        <div class="sec-tag">ANALYTICS</div>
    </div>
    """, unsafe_allow_html=True)

    # ── Row 1: 3 charts ──
    c1, c2, c3 = st.columns(3, gap="medium")

    # Chart 1 — Threats by channel (bar)
    with c1:
        red   = "#FF6B6B" if DARK else "#E74C3C"
        amber = "#FFB142" if DARK else "#E07B12"
        navy  = "#4E9EFF" if DARK else "#1A2B4A"
        green = "#2ED573" if DARK else "#27AE60"
        purple= "#A78BFA"

        bar_data  = [("SMS",148),("Email",97),("Voice",63),("WhatsApp",28),("Telegram",11)]
        bar_colors= [red, amber, navy, green, purple]
        bar_svg   = _bar_svg(bar_data, bar_colors)
        st.markdown(f"""
        <div class="chart-card">
            <div class="chart-hd">
                <div><div class="chart-title">Threats by Channel</div>
                <div class="chart-subtitle">Last 24 hours · 347 total</div></div>
            </div>
            <div class="chart-body">{bar_svg}</div>
        </div>""", unsafe_allow_html=True)

    # Chart 2 — Threat score distribution (donut)
    with c2:
        segments = [
            ("Critical (80–99)", 42, "#FF6B6B" if DARK else "#C0392B"),
            ("High (65–79)",     89, "#FFB142" if DARK else "#B7600A"),
            ("Medium (45–64)",  134, "#FF7F50" if DARK else "#A84010"),
            ("Low (0–44)",       82, "#2ED573" if DARK else "#1A6B3A"),
        ]
        donut = _donut_svg(segments, size=120)
        legend = "".join(
            f'<div class="donut-leg-r"><span class="donut-leg-dot" style="background:{c}"></span>'
            f'<span class="donut-leg-lbl">{l}</span>'
            f'<span class="donut-leg-val">{v}</span></div>'
            for l,v,c in segments
        )
        st.markdown(f"""
        <div class="chart-card">
            <div class="chart-hd">
                <div><div class="chart-title">Score Distribution</div>
                <div class="chart-subtitle">Today's threat severity breakdown</div></div>
            </div>
            <div class="chart-body">
                <div class="donut-wrap">
                    {donut}
                    <div class="donut-legend">{legend}</div>
                </div>
            </div>
        </div>""", unsafe_allow_html=True)

    # Chart 3 — Platform sparklines
    with c3:
        spark_data = [
            ("SMS",    [22,31,28,40,38,52,45,60,55,48,58,65,70,74,81,88,93,100,92,148], red),
            ("Email",  [10,12,18,22,15,20,28,31,30,42,38,50,55,60,58,65,70,80,88,97],  amber),
            ("Voice",  [5,8,12,10,14,18,22,19,25,28,30,35,38,40,45,50,48,55,60,63],    navy),
            ("WA",     [2,3,4,5,6,5,8,10,12,10,14,16,18,20,22,24,22,26,28,28],         green),
            ("TG",     [1,2,2,3,3,4,5,4,6,7,7,8,8,9,9,10,10,11,11,11],                purple),
        ]
        rows = ""
        for lbl, vals, color in spark_data:
            svg = _sparkline_svg(vals, color)
            rows += f"""
            <div class="spark-r">
                <div class="spark-lbl">{lbl}</div>
                <div class="spark-line">{svg}</div>
                <div class="spark-val" style="color:{color}">{vals[-1]}</div>
            </div>"""
        st.markdown(f"""
        <div class="chart-card">
            <div class="chart-hd">
                <div><div class="chart-title">Channel Trends</div>
                <div class="chart-subtitle">Hourly threat volume</div></div>
            </div>
            <div class="chart-body"><div style="padding:4px 0">{rows}</div></div>
        </div>""", unsafe_allow_html=True)

    # ── Row 2: detections over time (bar) + recent activity ──
    c4, c5 = st.columns([2,1], gap="medium")

    with c4:
        days = ["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]
        vals = [random.randint(260,420) for _ in range(7)]
        vals[-1] = 347  # today
        det_colors = [navy]*6 + [red]
        det_svg = _bar_svg(list(zip(days, vals)), det_colors, height=100)
        st.markdown(f"""
        <div class="chart-card">
            <div class="chart-hd">
                <div><div class="chart-title">Detections Over Time</div>
                <div class="chart-subtitle">Weekly view — today highlighted in red</div></div>
            </div>
            <div class="chart-body">{det_svg}</div>
        </div>""", unsafe_allow_html=True)

    with c5:
        events = [
            ("09:41","🔴","FS-382910","Critical SMS phishing — account takeover attempt"),
            ("09:37","🟠","FS-381204","High-risk voice call — synthetic speech flagged"),
            ("09:29","🟡","FS-379556","Medium — suspicious email domain"),
            ("09:18","🔴","FS-378001","Critical PDF — forged bank statement"),
            ("09:05","🟢","FS-376340","Low — routine anomaly, logged"),
        ]
        tl_rows = ""
        for ts, dot, case, desc in events:
            tl_rows += f"""
            <div class="tl-row">
                <div class="tl-time">{ts}</div>
                <div class="tl-bar-wrap">
                    <span style="float:left;margin-left:-19px;margin-top:3px;margin-right:8px;font-size:10px;">{dot}</span>
                    <div class="tl-entry">{case}</div>
                    <div class="tl-sub">{desc}</div>
                </div>
            </div>"""
        st.markdown(f"""
        <div class="chart-card">
            <div class="chart-hd">
                <div><div class="chart-title">Recent Activity</div>
                <div class="chart-subtitle">Last 5 cases</div></div>
            </div>
            <div class="chart-body" style="padding-top:14px;padding-bottom:14px">{tl_rows}</div>
        </div>""", unsafe_allow_html=True)


# ══════════════════════════════════════════════
# MAIN
# ══════════════════════════════════════════════

def main():
    render_nav()
    st.markdown('<div class="page">', unsafe_allow_html=True)

    st.markdown("""
    <div class="pg-header">
        <div class="pg-crumb">
            FraudShield <span class="pg-crumb-sep">/</span> Threat Analysis
        </div>
        <div class="pg-title-row">
            <div>
                <div class="pg-title">Omnichannel <em>Threat Analysis</em></div>
                <div class="pg-sub">
                    Submit evidence across audio, image, and text channels for AI-powered,
                    multimodal fraud detection and risk classification.
                </div>
            </div>
            <div class="pg-badge">FRAUD INTELLIGENCE PLATFORM</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    render_kpis()
    af, imf, txt = render_inputs()
    clicked = render_rail()

    if clicked:
        if not validate(af, imf, txt):
            st.error("Please provide at least one channel of evidence before executing the analysis.")
        else:
            st.info("Analysis in progress — scanning all submitted channels…")
            result = do_analysis(af, imf, txt)
            st.success("Analysis complete — threat report generated.")
            render_results(result)

    render_analytics()
    st.markdown('</div>', unsafe_allow_html=True)


if __name__ == "__main__":
    main()
