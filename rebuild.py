import os

# Read current file up to the wrapper div
with open('C:/Users/ADMIN/.gemini/antigravity/scratch/bni-invite/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Find where the CSS ends and body begins - keep only head+css portion
# Split at </style></head><body> boundary
head_end = html.find('<body>')
top_half = html[:head_end + len('<body>')]

# Remove the old CSS we no longer need (poster-card styles) by replacing sections we keep
# We'll re-inject the CSS for hero modifications

# Get all images from assets/images
images_dir = 'C:/Users/ADMIN/.gemini/antigravity/scratch/bni-invite/assets/images'
images = sorted([f for f in os.listdir(images_dir) if f.lower().endswith(('.jpg', '.jpeg', '.png', '.webp'))])
gallery_items = '\n'.join([
    f'<div class="gallery-item" onclick="openLightbox(this)"><img src="assets/images/{img}" alt="Sự kiện BNI #{i+1}" loading="lazy"></div>'
    for i, img in enumerate(images)
])

new_body = f"""

  <!-- ===== WELCOME GATE ===== -->
  <div id="welcome-gate" class="welcome-gate">
    <div class="welcome-content">
      <h1 class="welcome-title">Sự kiện Kết Nối Doanh Nhân</h1>
      <p class="welcome-subtitle">Nơi bạn đến để <strong>TĂNG DOANH THU</strong>, <strong>MỞ RỘNG QUAN HỆ</strong> và <strong>BỨT PHÁ</strong> kinh doanh ngay lập tức!</p>
      
      <form id="landing-form" class="welcome-form">
        <label class="form-label">Họ và tên *</label>
        <input type="text" id="lf-name" class="form-input" placeholder="Nguyễn Văn A" required>
        
        <label class="form-label">Số điện thoại *</label>
        <input type="tel" id="lf-phone" class="form-input" placeholder="0900 000 000" required>
        
        <label class="form-label">Email * (Điền đúng để nhận thư mời)</label>
        <input type="email" id="lf-email" class="form-input" placeholder="email@congty.com" required>
        
        <label class="form-label">Tên Công ty / Doanh nghiệp</label>
        <input type="text" id="lf-company" class="form-input" placeholder="Công ty TNHH ABC...">
        
        <label class="form-label">Hình ảnh đại diện (tùy chọn)</label>
        <input type="file" id="lf-photo" class="form-input" accept="image/*" style="padding-top:10px;">
        
        <!-- Honeypot chống Spam Bot -->
        <div style="display:none; visibility:hidden; position:absolute; left:-9999px;">
          <input type="text" id="lf-sp-trap" name="contact-qwe-123" tabindex="-1" autocomplete="off">
        </div>
        
        <button type="submit" id="lf-submit-btn" class="submit-btn">ĐĂNG KÝ THAM DỰ →</button>
      </form>
    </div>
  </div>

  <!-- Decorative border lines -->
  <div class="border-line left"></div>
  <div class="border-line right"></div>

  <!-- Floating particles -->
  <div class="particles-container" id="particles"></div>

  <style>
    /* ===== NAMECARD / INVITATION CARD STYLE ===== */
    #invitation-card {{
      display: none;
      max-width: 480px;
      margin: 30px auto 0;
      background: linear-gradient(170deg, #9B0000 0%, #CC1D1D 45%, #9B0000 100%);
      border-radius: 20px;
      padding: 36px 28px 40px;
      text-align: center;
      color: white;
      position: relative;
      overflow: hidden;
      z-index: 2;
      box-shadow: 0 20px 60px rgba(204,29,29,0.4);
    }}
    #invitation-card::before {{
      content: '';
      position: absolute; top: 0; left: 0; right: 0; bottom: 0;
      background: radial-gradient(ellipse at 50% 35%, rgba(255,255,255,0.18) 0%, transparent 65%);
      pointer-events: none;
    }}
    .ic-brand {{
      font-size: 13px;
      font-weight: 900;
      letter-spacing: 6px;
      text-transform: uppercase;
      color: rgba(255,255,255,0.85);
      margin-bottom: 2px;
    }}
    .ic-sub {{
      font-size: 11px;
      letter-spacing: 8px;
      text-transform: uppercase;
      color: rgba(255,255,255,0.6);
      margin-bottom: 18px;
    }}
    .ic-script {{
      font-family: 'Playfair Display', serif;
      font-style: italic;
      font-size: 28px;
      color: rgba(255,255,255,0.95);
      margin-bottom: 24px;
      line-height: 1.2;
      text-shadow: 0 2px 10px rgba(0,0,0,0.2);
    }}
    .ic-photo-ring {{
      width: 140px; height: 140px;
      margin: 0 auto 24px;
      border-radius: 50%;
      border: 4px solid rgba(255,255,255,0.7);
      box-shadow: 0 0 0 8px rgba(255,255,255,0.15), 0 0 40px rgba(255,255,255,0.2);
      overflow: hidden;
      background: rgba(255,255,255,0.1);
      display: flex; align-items: center; justify-content: center;
    }}
    .ic-photo-ring img {{
      width: 100%; height: 100%; object-fit: cover;
    }}
    .ic-photo-placeholder {{
      font-size: 50px; opacity: 0.5;
    }}
    .ic-greeting {{
      font-size: 14px; color: rgba(255,255,255,0.75);
      margin-bottom: 6px;
    }}
    .ic-name {{
      font-size: 22px; font-weight: 900;
      letter-spacing: 1px; text-transform: uppercase;
      color: #fff;
      margin-bottom: 8px;
      text-shadow: 0 2px 8px rgba(0,0,0,0.2);
    }}
    .ic-company {{
      font-size: 14px; color: rgba(255,255,255,0.8);
      font-weight: 500;
    }}
    .ic-motto {{
      font-size: 13px;
      line-height: 1.5;
      font-style: italic;
      color: rgba(255,255,255,0.7);
      margin-top: 24px;
      padding-top: 20px;
      border-top: 1px solid rgba(255,255,255,0.15);
    }}

    /* ===== LIGHTBOX ===== */
    #lightbox {{
      display: none;
      position: fixed; top: 0; left: 0; width: 100vw; height: 100vh;
      background: rgba(0,0,0,0.92);
      z-index: 99999;
      align-items: center; justify-content: center;
      cursor: zoom-out;
    }}
    #lightbox.open {{ display: flex; }}
    #lightbox img {{
      max-width: 92vw; max-height: 92vh;
      border-radius: 8px;
      box-shadow: 0 20px 60px rgba(0,0,0,0.6);
      animation: lbPop 0.25s cubic-bezier(0.34, 1.56, 0.64, 1);
    }}
    @keyframes lbPop {{
      from {{ transform: scale(0.85); opacity: 0; }}
      to {{ transform: scale(1); opacity: 1; }}
    }}
    #lightbox-close {{
      position: absolute; top: 20px; right: 24px;
      color: white; font-size: 32px; cursor: pointer;
      font-weight: 300; line-height: 1;
      opacity: 0.7; transition: opacity 0.2s;
    }}
    #lightbox-close:hover {{ opacity: 1; }}

    /* Toast */
    .toast {{ position: fixed; bottom: -60px; left: 50%; transform: translateX(-50%); background: #1a1a2e; color: white; padding: 16px 24px; border-radius: 8px; font-weight: 500; font-size: 14px; box-shadow: 0 10px 30px rgba(0,0,0,0.3); z-index: 99999; transition: bottom 0.4s cubic-bezier(0.18, 0.89, 0.32, 1.28); white-space: nowrap; }}
    .toast.show {{ bottom: 30px; }}
  </style>

  <!-- LIGHTBOX OVERLAY -->
  <div id="lightbox" onclick="closeLightbox()">
    <span id="lightbox-close" onclick="closeLightbox()">✕</span>
    <img id="lightbox-img" src="" alt="">
  </div>

  <div class="wrapper" style="padding-bottom: 40px;">

    <!-- ===== INVITATION NAMECARD (hiện sau khi điền form) ===== -->
    <div id="invitation-card">
      <div class="ic-brand">BEST CHAPTER</div>
      <div class="ic-sub">Cộng đồng chủ doanh nghiệp</div>
      <div class="ic-script">Trân Trọng Kính Mời</div>
      <div class="ic-photo-ring">
        <div class="ic-photo-placeholder" id="ic-photo-placeholder">👤</div>
        <img id="ic-photo-img" src="" alt="" style="display:none; width:100%; height:100%; object-fit:cover;">
      </div>
      <div class="ic-name" id="ic-name">NGUYỄN VĂN A</div>
      <div class="ic-company" id="ic-company">Công ty TNHH ABC</div>
      <div class="ic-motto">
        Nơi hội tụ những doanh nhân tạo giá trị<br>
        Kết nối để cùng nhau bứt phá
      </div>
    </div>

    <!-- HERO SECTION -->
    <section class="hero reveal">
      <div class="bni-logo reveal">
        <div class="bni-logo-badge">
          <div class="bni-text" style="font-size: 64px;">BEST <span>CHAPTER</span></div>
        </div>
        <div class="meeting-badge">CỘNG ĐỒNG CHỦ DOANH NGHIỆP TẠI HỒ CHÍ MINH</div>
      </div>
      
      <div class="hero-label">Trân trọng Kính mời Anh/Chị tham dự</div>
      <h1 class="hero-title">
        Sự kiện định kỳ 
        <span id="meeting-num" style="display:inline-block; color:#FFD700; font-family:'Playfair Display', serif; font-style:italic; margin-left:8px; font-size: 1.2em;">94</span>
      </h1>
      <p class="hero-subtitle">Mở rộng mối quan hệ và gia tăng doanh số thông qua các cơ hội học hỏi.</p>
      <div style="font-size: 14px; color: rgba(255,255,255,0.9); margin-top: -20px; margin-bottom: 30px;">
        📍 AQUA JARDIN - 307 Nơ Trang Long, Bình Lợi Trung, Tp. HCM
      </div>
      
      <div class="hero-date-pill">
        <div class="dot"></div>
        <span id="event-date-display">Đang cập nhật...</span>
      </div>
    </section>

    <!-- COUNTDOWN -->
    <section class="countdown-section reveal" id="countdown">
      <div class="countdown-label">Sự kiện sẽ bắt đầu sau</div>
      <div class="countdown-grid">
        <div class="countdown-item"><div class="countdown-value" id="cd-days">00</div><div class="countdown-unit">Ngày</div></div>
        <div class="countdown-item"><div class="countdown-value" id="cd-hours">00</div><div class="countdown-unit">Giờ</div></div>
        <div class="countdown-item"><div class="countdown-value" id="cd-mins">00</div><div class="countdown-unit">Phút</div></div>
        <div class="countdown-item"><div class="countdown-value" id="cd-secs">00</div><div class="countdown-unit">Giây</div></div>
      </div>
    </section>

    <!-- BENEFITS -->
    <section class="section reveal">
      <div class="section-inner">
        <h2 class="section-title">Giá trị nhận được</h2>
        <h3 class="section-heading">Tại sao bạn nên tham gia?</h3>
        <ul class="benefit-list">
          <li class="benefit-item"><div class="benefit-icon">🤝</div><div class="benefit-text"><strong>Mở rộng mối quan hệ:</strong> Gặp gỡ hơn 70 chủ doanh nghiệp uy tín.</div></li>
          <li class="benefit-item"><div class="benefit-icon">📢</div><div class="benefit-text"><strong>Quảng bá doanh nghiệp:</strong> Cơ hội giới thiệu sản phẩm, dịch vụ trực tiếp.</div></li>
          <li class="benefit-item"><div class="benefit-icon">📈</div><div class="benefit-text"><strong>Tăng trưởng doanh thu:</strong> Gia tăng khách hàng thông qua networking & referral.</div></li>
        </ul>
      </div>
    </section>

    <!-- LOCATION & TIME -->
    <section class="section reveal" style="padding-top: 0;">
      <div class="section-inner">
        <h2 class="section-title">Thông tin</h2>
        <h3 class="section-heading">Thời gian & Địa điểm</h3>
        <div class="info-grid">
          <div class="info-col">
            <div class="info-col-title">⏰ Thời gian</div>
            <div class="info-col-main">06:30 - 09:00</div>
            <div class="info-col-sub">Thứ Tư mỗi tuần</div>
          </div>
          <div class="info-divider"></div>
          <div class="info-col">
            <div class="info-col-title">📍 Địa điểm</div>
            <div class="info-col-main">AQUA JARDIN</div>
            <div class="info-col-sub">307 Nơ Trang Long, Bình Lợi Trung, Tp. HCM</div>
            <a href="https://maps.google.com/?q=AQUA+JARDIN+307+No+Trang+Long+Ho+Chi+Minh" target="_blank" class="map-btn">🗺️ Xem Bản Đồ</a>
          </div>
        </div>
      </div>
    </section>

    <!-- SPEAKER / CMS -->
    <section class="section reveal" style="padding-top: 0;">
      <div class="section-inner" style="background: var(--cream); border: 2px solid rgba(204,29,29,0.15);">
        <h2 class="section-title" style="text-align:center;">Tâm Điểm Sự Kiện</h2>
        <h3 class="section-heading" style="text-align:center;">Bài Chia Sẻ 10 Phút</h3>
        <div style="display:flex; align-items:center; justify-content:center; gap:20px; flex-wrap:wrap; margin-top:20px;">
          <div style="width:110px; height:110px; border-radius:50%; background:#ddd; border:4px solid var(--red); overflow:hidden; flex-shrink:0;">
            <img src="https://ui-avatars.com/api/?name=Hu%E1%BB%9Dng&background=CC1D1D&color=fff&size=150" alt="Speaker" id="speaker-img" style="width:100%; height:100%; object-fit:cover;">
          </div>
          <div style="text-align:left; max-width:280px;">
            <span style="font-size:12px; font-weight:700; color:var(--gray); text-transform:uppercase; letter-spacing:1px;">Chủ Đề</span>
            <h4 id="sp-topic" style="font-size:18px; font-weight:800; color:var(--red); line-height:1.3; margin:6px 0 10px;">Bí Mật Kinh doanh<br>Sức Khỏe Làm Đẹp thời 5.0</h4>
            <div id="sp-name" style="font-size:13px; font-weight:600; color:#333; line-height:1.6;">SPEAKER: <strong style="color:var(--red); font-size:14px;">NGUYỄN THỊ HƯỜNG</strong><br>CÔNG TY TNHH BIG EMPIRE</div>
          </div>
        </div>
      </div>
    </section>

    <!-- SCHEDULE -->
    <section class="section reveal" style="padding-top: 0;">
      <div class="section-inner">
        <h2 class="section-title">Agenda</h2>
        <h3 class="section-heading">Lịch trình chi tiết</h3>
        <ul class="schedule-list">
          <li class="schedule-item">
            <div class="schedule-time">06:30</div>
            <div class="schedule-dot"></div>
            <div class="schedule-content">
              <div class="schedule-phase">Đón khách & Giao lưu mở</div>
              <ul class="schedule-items"><li>Networking tự do, Ăn sáng & Cà phê</li></ul>
            </div>
          </li>
          <li class="schedule-item">
            <div class="schedule-time">07:00</div>
            <div class="schedule-dot"></div>
            <div class="schedule-content">
              <div class="schedule-phase">Phần chính sự kiện</div>
              <ul class="schedule-items"><li>Giới thiệu 60 giây từng doanh nghiệp</li><li>Trao đổi cơ hội kinh doanh (Referrals)</li></ul>
            </div>
          </li>
          <li class="schedule-item">
            <div class="schedule-time">08:00</div>
            <div class="schedule-dot"></div>
            <div class="schedule-content">
              <div class="schedule-phase">Bài chia sẻ 10 phút</div>
              <ul class="schedule-items"><li>Thuyết trình chính & Hỏi đáp</li></ul>
            </div>
          </li>
          <li class="schedule-item">
            <div class="schedule-time">08:45</div>
            <div class="schedule-dot"></div>
            <div class="schedule-content">
              <div class="schedule-phase">Bế mạc</div>
              <ul class="schedule-items"><li>Giao lưu sau sự kiện</li></ul>
            </div>
          </li>
        </ul>
      </div>
    </section>

    <!-- NOTES -->
    <section class="section reveal" style="padding-top: 0;">
      <div class="section-inner">
        <h2 class="section-title">Chuẩn bị</h2>
        <h3 class="section-heading">Lưu ý khi tham dự</h3>
        <div class="notes-grid">
          <div class="note-item"><div class="note-emoji">👔</div><div class="note-text"><strong>Trang phục</strong>Lịch sự, chuyên nghiệp (Business Casual / Vest).</div></div>
          <div class="note-item"><div class="note-emoji">🪪</div><div class="note-text"><strong>Nhận diện</strong>Mang theo <strong>danh thiếp (Namecard)</strong> thật nhiều để trao đổi.</div></div>
          <div class="note-item"><div class="note-emoji">☕</div><div class="note-text"><strong>Chi phí</strong>Phí tham dự (phòng họp & điểm tâm sáng) là <strong>300.000 VNĐ</strong>.</div></div>
          <div class="note-item"><div class="note-emoji">⏰</div><div class="note-text"><strong>Thời gian</strong>Vui lòng đến sớm trước 06:30 để có nhiều thời gian giao lưu.</div></div>
        </div>
      </div>
    </section>

    <!-- GALLERY (ảnh thực) -->
    <section class="section reveal" style="padding-top: 0;">
      <div class="section-inner">
        <h2 class="section-title">Khoảnh khắc</h2>
        <h3 class="section-heading">Hình ảnh sự kiện</h3>
        <div class="gallery-grid">
          {gallery_items}
        </div>
        <p style="text-align:center; font-size:12px; color:var(--gray); margin-top:14px;">Bấm vào ảnh để xem toàn màn hình</p>
      </div>
    </section>

    <!-- CONTACT -->
    <section class="section reveal" style="padding-top: 0;">
      <div class="section-inner">
        <h2 class="section-title">Hỗ trợ</h2>
        <h3 class="section-heading">Liên hệ ban tổ chức</h3>
        <div class="contact-grid">
          <div class="contact-card">
            <div class="contact-avatar">👩‍💼</div>
            <div><div class="contact-role">Khách mời</div><div class="contact-name">Hoàng Thị Thùy Linh</div><div class="contact-phone"><a href="tel:0985508979">0985.508.979</a></div></div>
          </div>
          <div class="contact-card">
            <div class="contact-avatar">👩‍💻</div>
            <div><div class="contact-role">Thư ký</div><div class="contact-name">Nguyễn Thị Hiền</div><div class="contact-phone"><a href="tel:0976900494">0976.900.494</a></div></div>
          </div>
        </div>
      </div>
    </section>

    <!-- FOOTER -->
    <footer class="footer">
      <div class="footer-logo">
        <div class="footer-bni">BEST CHAPTER</div>
        <div class="footer-best">DOANH NHÂN KẾT NỐI</div>
      </div>
      <div class="footer-divider"></div>
      <p class="footer-text">Giao lưu kết nối, vươn tầm cao mới.</p>
      <div class="footer-copy">© 2026. All rights reserved.</div>
    </footer>

  </div><!-- end .wrapper -->

  <script>
    // ===== 1. PARTICLES =====
    (function() {{
      const container = document.getElementById('particles');
      for (let i = 0; i < 15; i++) {{
        const p = document.createElement('div');
        p.className = 'particle';
        p.style.left = Math.random() * 100 + '%';
        p.style.width = p.style.height = (Math.random() * 8 + 4) + 'px';
        p.style.animationDuration = (Math.random() * 20 + 15) + 's';
        p.style.animationDelay = (Math.random() * 15) + 's';
        container.appendChild(p);
      }}
    }})();

    // ===== 2. COUNTDOWN & EVENT DATE =====
    (function() {{
      function getNextWednesday() {{
        const wednesdayVN = new Date();
        const diffDays = (3 - new Date().getDay() + 7) % 7 || (new Date().getHours() < 6 || (new Date().getHours() === 6 && new Date().getMinutes() < 30) ? 0 : 7);
        wednesdayVN.setDate(new Date().getDate() + diffDays);
        wednesdayVN.setHours(6, 30, 0, 0);
        return wednesdayVN;
      }}
      const targetDateObj = getNextWednesday();

      const dd = String(targetDateObj.getDate()).padStart(2,'0');
      const mm = String(targetDateObj.getMonth()+1).padStart(2,'0');
      const yyyy = targetDateObj.getFullYear();
      const d = document.getElementById('event-date-display');
      if(d) d.innerHTML = 'Thứ Tư, ' + dd + '/' + mm + '/' + yyyy;

      const baseDate = new Date(2026, 3, 1, 6, 30, 0, 0);
      const diffWeeks = Math.round((targetDateObj.getTime() - baseDate.getTime()) / (7*24*60*60*1000));
      const numSpan = document.getElementById('meeting-num');
      if(numSpan) numSpan.textContent = 94 + diffWeeks;

      function pad(n) {{ return String(n).padStart(2,'0'); }}
      function update() {{
        const diff = targetDateObj.getTime() - Date.now();
        if(diff <= 0 && diff > -3600000*2.5) {{
          document.getElementById('countdown').innerHTML = '<p class="countdown-expired">🎉 Sự kiện đang diễn ra!</p>';
          return;
        }}
        if(diff <= -3600000*2.5) {{ window.location.reload(); return; }}
        const days = Math.floor(diff/86400000);
        const h = Math.floor((diff%86400000)/3600000);
        const m = Math.floor((diff%3600000)/60000);
        const s = Math.floor((diff%60000)/1000);
        const el = document.getElementById('cd-days');
        if(el) {{
          el.textContent = pad(days);
          document.getElementById('cd-hours').textContent = pad(h);
          document.getElementById('cd-mins').textContent = pad(m);
          document.getElementById('cd-secs').textContent = pad(s);
        }}
      }}
      update();
      setInterval(update, 1000);
    }})();

    // ===== 3. REVEAL ON SCROLL =====
    (function() {{
      const observer = new IntersectionObserver((entries) => {{
        entries.forEach(e => {{
          if(e.isIntersecting) {{ e.target.classList.add('visible'); observer.unobserve(e.target); }}
        }});
      }}, {{ threshold: 0.1 }});
      document.querySelectorAll('.reveal').forEach(el => observer.observe(el));
    }})();

    const WEBHOOK_URL = 'https://script.google.com/macros/s/AKfycbyAxSNFdzIisxksv0fmemkYqLoAX_naV3GQkbSYuibFRidU5edRFKooTpHKSTmFQf9k/exec';

    document.getElementById('landing-form').addEventListener('submit', function(e) {{
      e.preventDefault();
      const honeypot = document.getElementById('lf-sp-trap').value;
      if(honeypot) return;

      const btn = document.getElementById('lf-submit-btn');
      btn.textContent = '⏳ ĐANG GỬI...';
      btn.disabled = true;

      const name = document.getElementById('lf-name').value.trim();
      const phone = document.getElementById('lf-phone').value.trim();
      const email = document.getElementById('lf-email').value.trim();
      const company = document.getElementById('lf-company').value.trim() || 'Khách mời';
      const fileInput = document.getElementById('lf-photo');
      const file = fileInput.files[0];

      if(typeof fbq === 'function') fbq('track', 'CompleteRegistration');

      if(file) {{
        const reader = new FileReader();
        reader.onload = function(ev) {{
          processSubmit(name, phone, email, company, ev.target.result);
        }};
        reader.readAsDataURL(file);
      }} else {{
        processSubmit(name, phone, email, company, null);
      }}
    }});

    function processSubmit(name, phone, email, company, photoBase64) {{
      // Gửi về webhook Apps Script ngay lập tức
      fetch(WEBHOOK_URL, {{
        method: 'POST',
        headers: {{ 'Content-Type': 'text/plain;charset=utf-8' }},
        body: JSON.stringify({{ name, phone, email, company, photo: photoBase64 }})
      }}).then(r => r.json())
        .then(d => console.log('Webhook OK:', d))
        .catch(err => console.log('Webhook error (non-blocking):', err));

      // Hiển thị Invitation Card cá nhân
      document.getElementById('welcome-gate').style.opacity = '0';
      setTimeout(() => {{
        document.getElementById('welcome-gate').style.display = 'none';

        // Điền thông tin vào thẻ mời
        document.getElementById('ic-name').textContent = 'Khách mời: ' + name.toUpperCase();
        document.getElementById('ic-company').textContent = 'Đại diện công ty: ' + company;

        if(photoBase64) {{
          document.getElementById('ic-photo-placeholder').style.display = 'none';
          const img = document.getElementById('ic-photo-img');
          img.src = photoBase64;
          img.style.display = 'block';
        }}

        const card = document.getElementById('invitation-card');
        card.style.display = 'block';

        window.scrollTo(0, 0);
        showToast('✅ Đã gửi đăng ký! Đang tải thư mời...');
      }}, 500);
    }}

    // ===== 5. GALLERY LIGHTBOX =====
    function openLightbox(el) {{
      const img = el.querySelector('img');
      document.getElementById('lightbox-img').src = img.src;
      document.getElementById('lightbox').classList.add('open');
      document.body.style.overflow = 'hidden';
    }}
    function closeLightbox() {{
      document.getElementById('lightbox').classList.remove('open');
      document.body.style.overflow = '';
    }}
    document.addEventListener('keydown', function(e) {{
      if(e.key === 'Escape') closeLightbox();
    }});

    // ===== 6. TOAST =====
    function showToast(msg) {{
      let t = document.getElementById('toast');
      if(!t) {{
        t = document.createElement('div');
        t.id = 'toast'; t.className = 'toast';
        document.body.appendChild(t);
      }}
      t.textContent = msg;
      t.classList.add('show');
      setTimeout(() => t.classList.remove('show'), 6000);
    }}

    // ===== 7. GOOGLE SHEETS CMS SPEAKER =====
    (function() {{
      const CMS_CSV_URL = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vTeZOZkkus3PIv-QuhZTT83J9_C3WYGC7rhzg_DyiAaBkn0nE0Ec7nqU-AGkkHz8a06aUK9AR8pliT4/pub?gid=0&single=true&output=csv';
      
      function getCSVRows(csv) {{
        const rows = [];
        let row = [];
        let cur = '';
        let inQuotes = false;
        for (let i = 0; i < csv.length; i++) {{
          const char = csv[i];
          const next = csv[i+1];
          if (inQuotes && char === '"' && next === '"') {{
            cur += '"'; i++;
          }} else if (char === '"') {{
            inQuotes = !inQuotes;
          }} else if (!inQuotes && char === ',') {{
            row.push(cur.trim()); cur = '';
          }} else if (!inQuotes && (char === '\\n' || char === '\\r')) {{
            if (cur !== '' || row.length > 0) {{
              row.push(cur.trim()); rows.push(row); row = []; cur = '';
            }}
            if (char === '\\r' && next === '\\n') i++;
          }} else {{
            cur += char;
          }}
        }}
        if (cur !== '' || row.length > 0) {{
          row.push(cur.trim()); rows.push(row);
        }}
        return rows;
      }}

      fetch(CMS_CSV_URL)
        .then(r => r.text())
        .then(csv => {{
          const rows = getCSVRows(csv);
          if(rows.length < 2) return;
          const data = rows[1]; // First data row after header
          const [imgUrl, topic, spkName, spkCompany] = data;
          if(imgUrl) document.getElementById('speaker-img').src = imgUrl;
          if(topic) document.getElementById('sp-topic').innerHTML = topic.replace(/\\n/g,'<br>');
          if(spkName || spkCompany) {{
            document.getElementById('sp-name').innerHTML =
              `SPEAKER: <strong style="color:var(--red); font-size:14px;">${{spkName}}</strong><br>${{spkCompany}}`;
          }}
        }})
        .catch(err => console.log('CMS Error:', err));
    }})();
  </script>
</body>
</html>"""

new_html = top_half + new_body
with open('C:/Users/ADMIN/.gemini/antigravity/scratch/bni-invite/index.html', 'w', encoding='utf-8') as f:
    f.write(new_html)

print(f"Done! Rebuilt with {len(images)} gallery images.")
