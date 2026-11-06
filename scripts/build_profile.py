"""Regenerate the concise public professional profile (requires reportlab)."""
from pathlib import Path
from reportlab.platypus import SimpleDocTemplate,Paragraph,Spacer,HRFlowable
from reportlab.lib.styles import getSampleStyleSheet,ParagraphStyle
from reportlab.lib.colors import HexColor
from reportlab.lib.enums import TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
pdfmetrics.registerFont(TTFont("ProfileSans", "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"))
pdfmetrics.registerFont(TTFont("ProfileBold", "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"))
pdfmetrics.registerFontFamily("ProfileSans", normal="ProfileSans", bold="ProfileBold", italic="ProfileSans", boldItalic="ProfileBold")
root=Path(__file__).resolve().parents[1]
styles=getSampleStyleSheet()
styles.add(ParagraphStyle(name='NameCustom',fontName='ProfileBold',fontSize=27,leading=31,textColor=HexColor('#15342f'),spaceAfter=8))
styles.add(ParagraphStyle(name='SubtitleCustom',fontName='ProfileBold',fontSize=11,leading=16,textColor=HexColor('#00776f'),spaceAfter=12))
styles.add(ParagraphStyle(name='SectionCustom',fontName='ProfileBold',fontSize=10,leading=14,textColor=HexColor('#00776f'),spaceBefore=12,spaceAfter=6))
styles.add(ParagraphStyle(name='TextCustom',fontName='ProfileSans',fontSize=9,leading=13,textColor=HexColor('#344641'),spaceAfter=7))
styles.add(ParagraphStyle(name='RoleCustom',fontName='ProfileBold',fontSize=10,leading=14,textColor=HexColor('#15342f'),spaceAfter=4))
items=[]
def p(text,style='TextCustom'):items.append(Paragraph(text,styles[style]))
p('Mauricio Ruiz','NameCustom')
p('Data analytics | Business analysis | Project delivery','SubtitleCustom')
p('Dublin, Ireland &nbsp; | &nbsp; <link href="https://www.linkedin.com/in/mauricioruizmieles/" color="#00776f">LinkedIn</link> &nbsp; | &nbsp; <link href="https://ruizmielesmauricio.github.io/mauricio-s_portfolio/" color="#00776f">Portfolio</link> &nbsp; | &nbsp; <link href="https://github.com/ruizmielesmauricio" color="#00776f">GitHub</link>')
items.append(HRFlowable(width='100%',thickness=1,color=HexColor('#c8d9cf'),spaceAfter=8))
p('PROFESSIONAL PROFILE','SectionCustom')
p('Analyst with experience in global technology operations, stakeholder requirements, KPI reporting, workflow automation and machine learning. Combines a background in social communication with a First Class Honours Higher Diploma in Data Analytics to communicate findings and support practical business decisions.')
p('CORE SKILLS','SectionCustom')
p('SQL, Python, Power BI, statistics, machine learning, XGBoost, Pandas, scikit-learn, Streamlit, Plotly, Power Apps, Dataverse, requirements gathering, root cause analysis, stakeholder collaboration and process improvement.')
p('EXPERIENCE','SectionCustom')
p('TikTok | Business analysis and project management','RoleCustom')
p('Dublin | March 2024 - Present')
p('Gather stakeholder requirements and translate them into reporting and automation solutions. Build operational KPI dashboards, investigate emerging risks and coordinate improvements across EMEA teams. Developed Python reporting workflows saving approximately eight hours of manual work each week and machine learning workflows to anticipate moderation risks.')
items.append(Spacer(1,6))
p('Accenture | Quality Analyst','RoleCustom')
p('Dublin | September 2021 - March 2024')
p('Conducted quality audits and root cause analysis, gathered stakeholder feedback, and built Power BI dashboards integrating Dataverse data. Designed and deployed a Power Apps workflow that reduced appeals processing time by 50% and improved reporting consistency.')
p('SELECTED PROJECTS','SectionCustom')
p('<b>NASDAQ-100 forecasting:</b> Combined market and macroeconomic data, engineered time-series features and evaluated XGBoost models using chronological splits. Published direction-classification experiment reported 74% accuracy.')
p('<b>Music analytics dashboards:</b> Integrated multiple APIs, resolved metadata inconsistencies and built interactive Streamlit and Plotly dashboards for the Big Four of thrash metal and Death\'s studio discography.')
p('<b>AI portfolio assistant:</b> Built a deployed conversational interface using structured Markdown knowledge, embeddings, vector retrieval and Gemini to answer questions about professional experience and projects.')
p('EDUCATION','SectionCustom')
p('<b>Higher Diploma in Data Analytics - First Class Honours</b><br/>National College of Ireland')
p('<b>Bachelor\'s degree in Social Communication</b>')
items.append(Spacer(1,8))
p('<font size="8" color="#697c73">Concise professional profile | November 2026 | Project reports and demonstrations are available through the portfolio.</font>')
out=root/'assets/mauricio-ruiz-profile.pdf'
SimpleDocTemplate(str(out),pagesize=A4,rightMargin=43,leftMargin=43,topMargin=35,bottomMargin=32,title='Mauricio Ruiz - Professional Profile',author='Mauricio Ruiz').build(items)
print(out)
