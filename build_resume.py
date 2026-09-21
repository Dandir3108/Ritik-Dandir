from pathlib import Path
from PIL import Image, ImageDraw
from docx import Document
from docx.shared import Mm, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_LINE_SPACING
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_CELL_VERTICAL_ALIGNMENT
from docx.oxml import OxmlElement
from docx.oxml.ns import qn

ROOT = Path(__file__).resolve().parent
PHOTO = ROOT / 'Ritik Resume Image.png'
OUT = ROOT / 'Ritik_Dandir_Resume.docx'
ASSET = ROOT / '_resume_work'
ASSET.mkdir(exist_ok=True)
HEX = ASSET / 'profile_hex.png'

NAVY = '062A4D'; DARK = '031D36'; BLUE = '0B4F8A'; ACCENT = '2F80C9'
LIGHT = 'EAF3FB'; TEXT = '102A43'; GREY = '5B6770'; WHITE = 'FFFFFF'

def shade(cell, fill):
    tcPr = cell._tc.get_or_add_tcPr(); shd = tcPr.find(qn('w:shd'))
    if shd is None: shd = OxmlElement('w:shd'); tcPr.append(shd)
    shd.set(qn('w:fill'), fill)

def borders(cell, **kwargs):
    tcPr = cell._tc.get_or_add_tcPr(); b = tcPr.first_child_found_in('w:tcBorders')
    if b is None: b = OxmlElement('w:tcBorders'); tcPr.append(b)
    for edge in ('top','left','bottom','right','insideH','insideV'):
        if edge in kwargs:
            tag = 'w:' + edge; el = b.find(qn(tag))
            if el is None: el = OxmlElement(tag); b.append(el)
            val, color, sz = kwargs[edge]
            el.set(qn('w:val'), val); el.set(qn('w:color'), color); el.set(qn('w:sz'), str(sz))

def cell_margin(cell, top=80, start=100, bottom=80, end=100):
    tc = cell._tc; tcPr = tc.get_or_add_tcPr(); mar = tcPr.first_child_found_in('w:tcMar')
    if mar is None: mar = OxmlElement('w:tcMar'); tcPr.append(mar)
    for side, val in [('top',top),('start',start),('bottom',bottom),('end',end)]:
        el = mar.find(qn('w:' + side))
        if el is None: el = OxmlElement('w:' + side); mar.append(el)
        el.set(qn('w:w'), str(val)); el.set(qn('w:type'), 'dxa')

def set_width(cell, mm):
    cell.width = Mm(mm); tcPr = cell._tc.get_or_add_tcPr(); w = tcPr.find(qn('w:tcW'))
    if w is None: w = OxmlElement('w:tcW'); tcPr.append(w)
    w.set(qn('w:w'), str(int(mm * 56.7))); w.set(qn('w:type'), 'dxa')

def set_repeat_table_header(row):
    trPr = row._tr.get_or_add_trPr(); el = OxmlElement('w:tblHeader'); el.set(qn('w:val'), 'true'); trPr.append(el)

def no_borders(table):
    for row in table.rows:
        for cell in row.cells: borders(cell, top=('nil','FFFFFF',0), left=('nil','FFFFFF',0), bottom=('nil','FFFFFF',0), right=('nil','FFFFFF',0))

def font(run, size=9, color=TEXT, bold=False, italic=False, name='Arial'):
    run.font.name = name; run._element.rPr.rFonts.set(qn('w:eastAsia'), name)
    run.font.size = Pt(size); run.font.bold = bold; run.font.italic = italic; run.font.color.rgb = RGBColor.from_string(color)

def para(cell, text='', size=9, color=TEXT, bold=False, italic=False, align=None, before=0, after=0, line=1.0):
    p = cell.add_paragraph() if len(cell.paragraphs) > 0 and cell.paragraphs[0].text else cell.paragraphs[0]
    p.paragraph_format.space_before = Pt(before); p.paragraph_format.space_after = Pt(after); p.paragraph_format.line_spacing = line
    if align is not None: p.alignment = align
    r = p.add_run(text); font(r, size, color, bold, italic)
    return p

def clear_cell(cell):
    cell.text = ''
    p = cell.paragraphs[0]; p.paragraph_format.space_after = Pt(0); p.paragraph_format.space_before = Pt(0)

def sidebar_heading(cell, title, symbol='●'):
    p = cell.add_paragraph(); p.paragraph_format.space_before = Pt(6); p.paragraph_format.space_after = Pt(1)
    r = p.add_run(symbol + '  '); font(r, 10, 'B9E0FF', True)
    r = p.add_run(title); font(r, 9.5, WHITE, True)
    p2 = cell.add_paragraph(); p2.paragraph_format.space_after = Pt(3)
    r = p2.add_run('━━━━━━━━━━━━━━━━'); font(r, 5.8, '8CB6D9')

def sidebar_bullet(cell, text, size=8.2):
    p = cell.add_paragraph(style=None); p.paragraph_format.left_indent = Mm(3.8); p.paragraph_format.first_line_indent = Mm(-3.2); p.paragraph_format.space_after = Pt(1.2); p.paragraph_format.line_spacing = 1.0
    r=p.add_run('•  '); font(r,size,'DDEEFF'); r=p.add_run(text); font(r,size,WHITE)

def section_header(cell, title, icon='●'):
    t = cell.add_table(rows=1, cols=2); t.alignment = WD_TABLE_ALIGNMENT.LEFT; t.autofit = False
    t.columns[0].width = Mm(10); t.columns[1].width = Mm(105)
    a,b=t.rows[0].cells; set_width(a,10); set_width(b,105); shade(a,BLUE); shade(b,BLUE); cell_margin(a,30,60,30,60); cell_margin(b,55,120,55,120)
    borders(a, top=('nil',WHITE,0), left=('nil',WHITE,0), bottom=('nil',WHITE,0), right=('nil',WHITE,0)); borders(b, top=('nil',WHITE,0), left=('nil',WHITE,0), bottom=('nil',WHITE,0), right=('nil',WHITE,0))
    p=a.paragraphs[0]; p.alignment=WD_ALIGN_PARAGRAPH.CENTER; r=p.add_run(icon); font(r,9,WHITE,True)
    p=b.paragraphs[0]; r=p.add_run(title); font(r,9.5,WHITE,True)
    # thin extension line
    p3=cell.add_paragraph(); p3.paragraph_format.space_after=Pt(2); p3.paragraph_format.line_spacing=0.2; r=p3.add_run('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━'); font(r,4.5,'8CB6D9')

def add_body(cell,text,size=8.5,bold=False,after=2,italic=False):
    p=cell.add_paragraph(); p.paragraph_format.space_after=Pt(after); p.paragraph_format.line_spacing=1.0
    r=p.add_run(text); font(r,size,TEXT,bold,italic); return p

def bullet(cell, text, size=8.0, after=0.7):
    p=cell.add_paragraph(); p.paragraph_format.left_indent=Mm(4.2); p.paragraph_format.first_line_indent=Mm(-3.6); p.paragraph_format.space_after=Pt(after); p.paragraph_format.line_spacing=1.0
    r=p.add_run('•  '); font(r,size,BLUE,True); r=p.add_run(text); font(r,size,TEXT)

def make_hex():
    im=Image.open(PHOTO).convert('RGB'); w,h=im.size
    crop_w=int(h*0.78); left=(w-crop_w)//2; crop=im.crop((left,0,left+crop_w,h))
    crop=crop.resize((700,760),Image.Resampling.LANCZOS)
    out=Image.new('RGBA',(760,820),(0,0,0,0)); out.paste(crop,(30,30))
    mask=Image.new('L',(700,760),0); d=ImageDraw.Draw(mask); d.polygon([(350,0),(680,165),(680,560),(350,760),(20,560),(20,165)],fill=255)
    alpha=Image.new('L',out.size,0); alpha.paste(mask,(30,30)); out.putalpha(alpha)
    dr=ImageDraw.Draw(out); pts=[(380,15),(725,180),(725,575),(380,805),(35,575),(35,180)]
    dr.line(pts+[pts[0]],fill=(205,235,255,255),width=7,joint='curve')
    out.save(HEX)

def build():
    make_hex(); d=Document(); sec=d.sections[0]; sec.page_width=Mm(210); sec.page_height=Mm(297); sec.top_margin=Mm(0); sec.bottom_margin=Mm(0); sec.left_margin=Mm(0); sec.right_margin=Mm(0); sec.header_distance=Mm(0); sec.footer_distance=Mm(0)
    styles=d.styles; styles['Normal'].font.name='Arial'; styles['Normal']._element.rPr.rFonts.set(qn('w:eastAsia'),'Arial'); styles['Normal'].font.size=Pt(9)
    outer=d.add_table(rows=1,cols=2); outer.alignment=WD_TABLE_ALIGNMENT.CENTER; outer.autofit=False; no_borders(outer)
    left,right=outer.rows[0].cells; set_width(left,65); set_width(right,145); left.vertical_alignment=WD_CELL_VERTICAL_ALIGNMENT.TOP; right.vertical_alignment=WD_CELL_VERTICAL_ALIGNMENT.TOP; shade(left,NAVY); shade(right,'FFFFFF'); cell_margin(left,250,600,180,520); cell_margin(right,650,600,200,650)
    # sidebar
    p=left.paragraphs[0]; p.alignment=WD_ALIGN_PARAGRAPH.CENTER; p.paragraph_format.space_after=Pt(2); r=p.add_run(); r.add_picture(str(HEX),width=Mm(50))
    for txt, sym in [('+91 797-426-8544','☎'),('ritikdandir@gmail.com','✉'),('Khargone, Madhya Pradesh, India','●'),('linkedin.com/in/ritikdandir','in')]:
        p=left.add_paragraph(); p.paragraph_format.left_indent=Mm(1.5); p.paragraph_format.space_after=Pt(2); r=p.add_run(sym+'  '); font(r,9,'DDEEFF',True); r=p.add_run(txt); font(r,8.2,WHITE)
    p=left.add_paragraph(); p.paragraph_format.space_before=Pt(5); r=p.add_run('━━━━━━━━━━━━━━━━━━━━'); font(r,5.5,'8CB6D9')
    sidebar_heading(left,'TECHNICAL SKILLS','⚙')
    for x in ['BIW Welding Process','Fixture Costing & Estimation','Techno-Commercial Estimation','Manufacturing Process Analysis','Process Optimization','Cycle-Time Optimization','Engineering Cost Analysis','Engineering Documentation','Technical Proposal Preparation','Business & Engineering Reporting']: sidebar_bullet(left,x)
    sidebar_heading(left,'SOFTWARE & TOOLS','▣')
    for x in ['MS Excel (Advanced)','Pivot Tables | XLOOKUP | Power Query','MS PowerPoint','Power BI (Basic/Intermediate)','AutoCAD (Basic)','ERP / SAP (Basic)']: sidebar_bullet(left,x)
    sidebar_heading(left,'PROFESSIONAL SKILLS','●')
    for x in ['Analytical Thinking','Problem Solving','Technical Communication','Team Collaboration','Documentation Management','Time Management','Engineering Coordination','Business Communication']: sidebar_bullet(left,x)
    sidebar_heading(left,'LANGUAGES','文')
    for x in ['English','Hindi']: sidebar_bullet(left,x)
    # main header
    p=right.paragraphs[0]; p.paragraph_format.space_after=Pt(1); r=p.add_run('RITIK DANDIR'); font(r,27,NAVY,True)
    p=right.add_paragraph(); p.paragraph_format.space_after=Pt(2); p.paragraph_format.line_spacing=0.95; r=p.add_run('Mechanical Engineer | Manufacturing Engineering |\nBIW | Fixture Costing & Techno-Commercial Estimation'); font(r,10.2,NAVY,True)
    p=right.add_paragraph(); p.alignment=WD_ALIGN_PARAGRAPH.RIGHT; p.paragraph_format.space_after=Pt(3); r=p.add_run('Building Efficient Manufacturing Solutions\nThrough Engineering, Analysis & Innovation'); font(r,8.3,BLUE,False,True)
    section_header(right,'PROFESSIONAL SUMMARY','●')
    add_body(right,'Mechanical Engineering professional with experience in automotive manufacturing engineering, BIW welding processes, fixture costing, techno-commercial estimation, process analysis, cycle-time optimization, and engineering documentation.',8.25,False,1)
    add_body(right,'Currently working as an Executive Engineer at JBM Group, with progression from Graduate Engineer Trainee to Executive Engineer within one year. Experienced in preparing engineering cost estimates and techno-commercial offers, supporting fixture costing activities, analysing manufacturing processes, developing business dashboards, and coordinating technical information for engineering and commercial proposals.',8.25,False,1)
    add_body(right,'Strong interest in manufacturing engineering, fixture/tooling, process optimization, engineering costing, and project engineering within the automotive industry.',8.25,False,2)
    section_header(right,'PROFESSIONAL EXPERIENCE','▣')
    p=right.add_paragraph(); p.paragraph_format.space_after=Pt(0); r=p.add_run('JBM GROUP    |    '); font(r,9.1,NAVY,True); r=p.add_run('Gurugram'); font(r,9.1,TEXT)
    p=right.add_paragraph(); p.paragraph_format.space_after=Pt(0); r=p.add_run('Executive Engineer – Engineering'); font(r,9.2,NAVY,True); r=p.add_run('                                      2023 – Present'); font(r,8.3,TEXT)
    exp=['Prepare techno-commercial offers and engineering cost estimates based on project requirements, technical specifications, and defined scope.','Support BIW welding process-related engineering activities and evaluation of manufacturing requirements.','Perform engineering and manufacturing process analysis to identify opportunities for process optimization and improved manufacturing efficiency.','Support cycle-time analysis and optimization activities for manufacturing processes.','Perform fixture costing and estimation activities, including evaluation of engineering requirements and associated costs.','Prepare and maintain engineering and business documentation for project and management requirements.','Develop business dashboards and analytical reports using MS Excel and available tools.','Coordinate technical information from relevant stakeholders for preparation of commercial and engineering proposals.','Analyse engineering requirements and associated cost elements to support commercial decision-making and project estimation.','Prepare technical information and presentations for communication of engineering and commercial requirements.']
    for x in exp: bullet(right,x,7.65,0.25)
    # career box
    box=right.add_table(rows=1,cols=1); box.alignment=WD_TABLE_ALIGNMENT.CENTER; no_borders(box); c=box.cell(0,0); shade(c,LIGHT); cell_margin(c,90,150,80,150)
    p=c.paragraphs[0]; p.paragraph_format.space_after=Pt(1); r=p.add_run('CAREER PROGRESSION'); font(r,8.7,BLUE,True)
    p=c.add_paragraph(); p.paragraph_format.space_after=Pt(1); r=p.add_run('Graduate Engineer Trainee  →  Executive Engineer'); font(r,8.5,NAVY,True); r=p.add_run('   (within 1 year)'); font(r,7.8,TEXT)
    p=c.add_paragraph(); p.paragraph_format.space_after=Pt(0); r=p.add_run('Progressed to the position of Executive Engineer, reflecting increased responsibility in engineering, costing, process analysis, documentation and commercial estimation.'); font(r,7.55,TEXT)
    section_header(right,'CORE ENGINEERING EXPERTISE','⚙')
    t=right.add_table(rows=1,cols=2); t.alignment=WD_TABLE_ALIGNMENT.LEFT; t.autofit=False; t.columns[0].width=Mm(65); t.columns[1].width=Mm(65); no_borders(t)
    a,b=t.rows[0].cells; set_width(a,65); set_width(b,65); cell_margin(a,0,0,0,100); cell_margin(b,0,100,0,0)
    for x in ['BIW Welding Process','Fixture Costing & Estimation','Techno-Commercial Estimation','Manufacturing Process Analysis','Process Optimization','Cycle-Time Optimization']: bullet(a,x,7.8,0.2)
    for x in ['Engineering Cost Analysis','Engineering Documentation','Technical Proposal Preparation','Business & Engineering Reporting','Excel-Based Analysis','Dashboard Development']: bullet(b,x,7.8,0.2)
    section_header(right,'EDUCATION','◆')
    edu=[('2024','Precision Engineering Certificate Course','SSR Global Skill Park, Bhopal'),('2023','Bachelor of Technology (B.Tech) – Mechanical Engineering','Chameli Devi Group of Institutions'),('2019','Class XII – PCM','Shree Vaishnav Vidya Mandir, Khargone'),('2016','Class X','Shree Vaishnav Vidya Mandir, Khargone')]
    for yr,title,school in edu:
        p=right.add_paragraph(); p.paragraph_format.left_indent=Mm(4); p.paragraph_format.first_line_indent=Mm(-4); p.paragraph_format.space_after=Pt(0); p.paragraph_format.line_spacing=0.95; r=p.add_run('●  '); font(r,8,BLUE,True); r=p.add_run(title); font(r,8.1,NAVY,True); r=p.add_run('                                      '+yr); font(r,7.8,BLUE,True)
        p=right.add_paragraph(); p.paragraph_format.left_indent=Mm(7); p.paragraph_format.space_after=Pt(1); p.paragraph_format.line_spacing=0.95; r=p.add_run(school); font(r,7.5,TEXT)
    # table row exact page height
    trPr=outer.rows[0]._tr.get_or_add_trPr(); h=OxmlElement('w:trHeight'); h.set(qn('w:val'),str(int(297*56.7))); h.set(qn('w:hRule'),'atLeast'); trPr.append(h)
    d.save(OUT)
    print(OUT)

if __name__=='__main__': build()
