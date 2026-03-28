import codecs

def replace_in_file(path, replacements):
    with codecs.open(path, 'r', 'utf-8') as f:
        text = f.read()
    
    for old, new in replacements:
        text = text.replace(old, new)
        
    with codecs.open(path, 'w', 'utf-8') as f:
        f.write(text)

# html
replacements_html = [
    ("BNI BEST | Kết Nối Kinh Doanh", "Cộng Đồng | Kết Nối Doanh Nhân"),
    ("của BNI BEST Chapter", "của Cộng Đồng Doanh Nhân"),
    ("""      <div class="bni-logo">
        <div class="bni-logo-badge">
          <div class="bni-text"><span>BNI</span></div>
          <div class="best-text">BEST</div>
        </div>
        <div class="meeting-badge">BUỔI HỌP ĐỊNH KỲ</div>
      </div>""", 
     """      <div class="bni-logo" style="margin-bottom: 30px;">
        <div class="meeting-badge" style="font-size: 16px; padding: 8px 24px; border: 2px solid rgba(255,255,255,0.5);">SỰ KIỆN KẾT NỐI DOANH NHÂN</div>
      </div>"""),
    ("của <strong style=\"color:#FFD700\">BEST Chapter</strong>", "của <strong style=\"color:#FFD700\">Cộng Đồng Doanh Nhân</strong>"),
    ("BNI BEST Chapter – Lần thứ 93", "Sự Kiện Kết Nối – Lần thứ 93"),
    ("Khoảnh khắc BNI", "Khoảnh khắc Sự kiện"),
    ('alt="BNI Moment"', 'alt="Khoảnh khắc"'),
    ("""      <div class="footer-logo">
        <div class="footer-bni">BNI</div>
        <div class="footer-best">BEST CHAPTER</div>
      </div>""", 
     """      <div class="footer-logo">
        <div class="footer-bni" style="font-size: 24px;">KẾT NỐI</div>
        <div class="footer-best">DOANH NHÂN</div>
      </div>"""),
    ("Business Network International – BEST Chapter", "Cộng Đồng Kết Nối Doanh Nhân"),
    ("© 2026 BNI BEST Chapter.", "© 2026 Cộng Đồng Doanh Nhân.")
]

replace_in_file(r"c:\Users\ADMIN\.gemini\antigravity\scratch\bni-invite\index.html", replacements_html)

# md
replacements_md = [
    ("Danh Sách Khách Mời BNI", "Danh Sách Khách Mời Sự Kiện"),
    ("Sự kiện Kết Nối Doanh Nhân BNI BEST", "Sự kiện Kết Nối Doanh Nhân"),
    ("BNI BEST Chapter", "Cộng Đồng Doanh Nhân"),
    ("Sự kiện Kết nối Doanh nhân của BNI BEST Chapter", "Sự kiện Kết nối Doanh nhân")
]

replace_in_file(r"C:\Users\ADMIN\.gemini\antigravity\brain\9fde42d0-cbf9-4c84-84de-c8c7f6aab132\google_apps_script_guide.md", replacements_md)

print("Done replacing.")
